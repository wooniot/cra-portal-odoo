# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

INCIDENT_TOOL_URL = "https://cra-portal.eu/cra-incident-response/"


class ProductTemplate(models.Model):
    _inherit = "product.template"

    cra_status = fields.Selection(
        selection=[
            ("green", "Compliant"),
            ("amber", "In progress"),
            ("red", "Not compliant"),
            ("unknown", "Unknown / not synced"),
        ],
        string="CRA status",
        default="unknown",
        readonly=True,
        copy=False,
        help="Live conformity status pulled from CRA-Portal, matched on the product SKU.",
    )
    cra_auth_code = fields.Char(string="CRA auth code", readonly=True, copy=False)
    cra_verify_url = fields.Char(string="CRA verify link", readonly=True, copy=False)
    cra_badge_url = fields.Char(string="CRA badge (SVG)", readonly=True, copy=False)
    cra_last_sync = fields.Datetime(string="CRA last synced", readonly=True, copy=False)

    def action_cra_open_incident_tool(self):
        return {"type": "ir.actions.act_url", "url": INCIDENT_TOOL_URL, "target": "new"}

    def action_cra_open_verify(self):
        self.ensure_one()
        if not self.cra_verify_url:
            return self._cra_sync(self)
        return {"type": "ir.actions.act_url", "url": self.cra_verify_url, "target": "new"}

    def action_cra_fetch_status(self):
        """Sync only the selected product(s)."""
        return self._cra_sync(self)

    @api.model
    def action_cra_sync_all(self):
        """Header action: sync every product that has a SKU."""
        return self._cra_sync(self.search([("default_code", "!=", False)]))

    @api.model
    def _cra_sync(self, products):
        data = self.env["cra.portal.client"]._cra_get("/api/partner-api/keurmerk")
        by_sku = {}
        for item in (data or {}).get("products", []):
            sku = item.get("sku")
            if sku:
                by_sku[str(sku).strip().lower()] = item
        now = fields.Datetime.now()
        matched = 0
        for product in products:
            sku = (product.default_code or "").strip().lower()
            hit = by_sku.get(sku)
            if not hit:
                continue
            product.write({
                "cra_status": hit.get("status") or "unknown",
                "cra_auth_code": hit.get("auth_code") or False,
                "cra_verify_url": hit.get("verify_url") or False,
                "cra_badge_url": hit.get("badge_svg") or False,
                "cra_last_sync": now,
            })
            matched += 1
        return {
            "type": "ir.actions.client",
            "tag": "display_notification",
            "params": {
                "title": _("CRA sync"),
                "message": _("%s product(s) matched on SKU and updated.") % matched,
                "type": "success" if matched else "warning",
                "sticky": False,
            },
        }
