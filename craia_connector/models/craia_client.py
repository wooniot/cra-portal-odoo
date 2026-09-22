# -*- coding: utf-8 -*-
import logging

from odoo import models, _
from odoo.exceptions import UserError

try:
    import requests
except ImportError:
    requests = None

_logger = logging.getLogger(__name__)
STANDAARD_BASIS = "https://dev.cra-portal.eu"


class CraiaClient(models.AbstractModel):
    """Praat met de CRAIA-kant van CRA-Portal.

    Bewust dezelfde opzet als cra.portal.client: één plek waar de sleutel en de
    foutmeldingen staan, zodat een beheerder aan de melding genoeg heeft en niet
    in het logboek hoeft te kijken.
    """

    _name = "craia.client"
    _description = "CRAIA API client"

    def _craia_config(self):
        icp = self.env["ir.config_parameter"].sudo()
        basis = (icp.get_param("craia_connector.base_url") or STANDAARD_BASIS).rstrip("/")
        client_id = icp.get_param("craia_connector.client_id") or ""
        secret = icp.get_param("craia_connector.client_secret") or ""
        return basis, client_id, secret

    def _craia_check(self):
        if requests is None:
            raise UserError(_("The Python library 'requests' is required. Install it on "
                              "the Odoo server (pip install requests)."))
        basis, client_id, secret = self._craia_config()
        if not client_id or not secret:
            raise UserError(_("Configure your CRAIA Partner-API key under "
                              "Settings -> CRAIA first."))
        return basis, client_id, secret

    def _craia_fout(self, resp):
        if resp.status_code == 401:
            raise UserError(_("CRAIA rejected the API key (401). Check the client id "
                              "and secret."))
        if resp.status_code == 402:
            raise UserError(_("Your CRAIA subscription is not active (402)."))
        if resp.status_code == 403:
            raise UserError(_("The API key is missing the 'craia' scope (403)."))
        if resp.status_code == 429:
            raise UserError(_("Too many requests to CRAIA (429). Try again shortly."))
        if resp.status_code >= 400:
            raise UserError(_("CRAIA returned an error (%s).") % resp.status_code)

    def _craia_get(self, pad, timeout=20):
        basis, client_id, secret = self._craia_check()
        try:
            resp = requests.get(basis + pad, auth=(client_id, secret), timeout=timeout,
                                headers={"Accept": "application/json"})
        except Exception as exc:
            _logger.warning("CRAIA request failed: %s", type(exc).__name__)
            raise UserError(_("Could not reach CRAIA (%s).") % exc)
        self._craia_fout(resp)
        return resp.json()

    def _craia_post(self, pad, lading, timeout=60):
        basis, client_id, secret = self._craia_check()
        try:
            resp = requests.post(basis + pad, auth=(client_id, secret), json=lading,
                                 timeout=timeout, headers={"Accept": "application/json"})
        except Exception as exc:
            _logger.warning("CRAIA request failed: %s", type(exc).__name__)
            raise UserError(_("Could not reach CRAIA (%s).") % exc)
        self._craia_fout(resp)
        return resp.json()
