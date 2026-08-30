# -*- coding: utf-8 -*-
from odoo import fields, models, _
class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"
    cra_portal_base_url = fields.Char(
        string="CRA-Portal base URL",
        config_parameter="cra_portal_connector.base_url",
        default="https://dev.cra-portal.eu",
    )
    cra_portal_client_id = fields.Char(
        string="Partner-API client id",
        config_parameter="cra_portal_connector.client_id",
    )
    cra_portal_client_secret = fields.Char(
        string="Partner-API secret",
        config_parameter="cra_portal_connector.client_secret",
    )
    def action_cra_test_connection(self):
        self.ensure_one()
        self.set_values()
        data = self.env["cra.portal.client"]._cra_get("/api/partner-api/me")
        tenant = (data or {}).get("tenant", {}).get("name") or "?"
        scopes = ", ".join((data or {}).get("scopes", [])) or "-"
        billing = (data or {}).get("billing", {}).get("status") or "-"
        return {
            "type": "ir.actions.client",
            "tag": "display_notification",
            "params": {
                "title": _("CRA-Portal connected"),
                "message": _("Tenant: %(t)s · plan: %(b)s · scopes: %(s)s") % {
                    "t": tenant, "b": billing, "s": scopes,
                },
                "type": "success",
                "sticky": False,
            },
        }
