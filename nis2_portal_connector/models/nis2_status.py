# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Nis2PortalStatus(models.TransientModel):
    _name = "nis2.portal.status"
    _description = "NIS2 readiness (CRA-Portal)"

    entity = fields.Char(string="Organisation", readonly=True)
    status = fields.Selection(
        selection=[
            ("green", "Compliant"),
            ("amber", "In progress"),
            ("red", "Not compliant"),
            ("unknown", "Unknown / not configured"),
        ],
        string="NIS2 status", default="unknown", readonly=True,
    )
    label = fields.Char(string="Status label", readonly=True)
    score = fields.Char(string="Article 21 score", readonly=True)
    auth_code = fields.Char(string="Auth code", readonly=True)
    verify_url = fields.Char(string="Verify link", readonly=True)
    badge_url = fields.Char(string="Badge (SVG)", readonly=True)
    checked_at = fields.Datetime(string="Checked at", readonly=True)

    @api.model
    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        res.update(self._fetch(soft=True))
        return res

    @api.model
    def _fetch(self, soft=False):
        """Pull /nis2/status. When soft=True, swallow errors and show 'unknown'
        (used on dashboard open); when soft=False, surface the error to the user."""
        try:
            data = self.env["nis2.portal.client"]._cra_get("/api/partner-api/nis2/status")
        except Exception:
            if soft:
                return {"status": "unknown", "checked_at": fields.Datetime.now()}
            raise
        sc = data.get("score") or {}
        return {
            "entity": data.get("entity"),
            "status": data.get("status") or "unknown",
            "label": data.get("label"),
            "score": "%s / %s" % (sc.get("passed", "?"), sc.get("total", "?")),
            "auth_code": data.get("auth_code"),
            "verify_url": data.get("verify_url"),
            "badge_url": data.get("badge_svg"),
            "checked_at": fields.Datetime.now(),
        }

    def action_refresh(self):
        self.ensure_one()
        self.write(self._fetch(soft=False))
        return {
            "type": "ir.actions.act_window",
            "res_model": self._name,
            "res_id": self.id,
            "view_mode": "form",
            "target": "current",
        }

    def action_open_verify(self):
        self.ensure_one()
        if not self.verify_url:
            return self.action_refresh()
        return {"type": "ir.actions.act_url", "url": self.verify_url, "target": "new"}
