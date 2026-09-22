# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    craia_base_url = fields.Char(
        string="CRAIA base URL",
        config_parameter="craia_connector.base_url",
        default="https://dev.cra-portal.eu",
        help="Leave as is unless you run CRA-Portal on your own domain.")
    craia_client_id = fields.Char(
        string="Client id", config_parameter="craia_connector.client_id")
    craia_client_secret = fields.Char(
        string="Client secret", config_parameter="craia_connector.client_secret")

    def action_craia_test(self):
        """Test de verbinding voordat iemand gaat versturen.

        Een knop die meteen zegt of het werkt scheelt de helft van de vragen; zonder
        deze knop ontdekt een beheerder de fout pas bij de eerste echte verzending.
        """
        self.ensure_one()
        stand = self.env["craia.client"]._craia_get("/api/partner-api/craia/stand")
        if not stand.get("actief"):
            raise UserError(_("Connected, but CRAIA is not active for this account: %s")
                            % (stand.get("reden") or ""))
        return {
            "type": "ir.actions.client",
            "tag": "display_notification",
            "params": {
                "title": _("Connection works"),
                "message": _("Connected to CRAIA for %s.") % (stand.get("organisatie") or "-"),
                "type": "success", "sticky": False},
        }
