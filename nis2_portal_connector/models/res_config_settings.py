# -*- coding: utf-8 -*-
from odoo import fields, models, _


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    nis2_portal_base_url = fields.Char(
        string="NIS2-Portal base URL",
        config_parameter="nis2_portal_connector.base_url",
        default="https://dev.cra-portal.eu",
    )
    nis2_portal_client_id = fields.Char(
        string="NIS2 Partner-API client id",
        config_parameter="nis2_portal_connector.client_id",
    )
    nis2_portal_client_secret = fields.Char(
        string="NIS2 Partner-API secret",
        config_parameter="nis2_portal_connector.client_secret",
    )

    def action_nis2_test_connection(self):
        self.ensure_one()
        self.set_values()
        data = self.env["nis2.portal.client"]._cra_get("/api/partner-api/me")
        tenant = (data or {}).get("tenant", {}).get("name") or "?"
        scopes = ", ".join((data or {}).get("scopes", [])) or "-"
        return {
            "type": "ir.actions.client",
            "tag": "display_notification",
            "params": {
                "title": _("CRA-Portal connected"),
                "message": _("Tenant: %(t)s · scopes: %(s)s") % {"t": tenant, "s": scopes},
                "type": "success",
                "sticky": False,
            },
        }
