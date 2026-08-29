# -*- coding: utf-8 -*-
import logging

from odoo import models, _
from odoo.exceptions import UserError

try:
    import requests
except ImportError:  # pragma: no cover
    requests = None

_logger = logging.getLogger(__name__)

DEFAULT_BASE_URL = "https://dev.cra-portal.eu"


class Nis2PortalClient(models.AbstractModel):
    """Thin client for the CRA-Portal Partner-API (NIS2 scope)."""

    _name = "nis2.portal.client"
    _description = "NIS2-Portal API client"

    def _cra_config(self):
        icp = self.env["ir.config_parameter"].sudo()
        base = (icp.get_param("nis2_portal_connector.base_url") or DEFAULT_BASE_URL).rstrip("/")
        client_id = icp.get_param("nis2_portal_connector.client_id") or ""
        secret = icp.get_param("nis2_portal_connector.client_secret") or ""
        return base, client_id, secret

    def _cra_get(self, path, timeout=20):
        if requests is None:
            raise UserError(_("The Python library 'requests' is required. Install it on the Odoo server."))
        base, client_id, secret = self._cra_config()
        if not client_id or not secret:
            raise UserError(_("Configure your CRA-Portal Partner-API key under Settings -> NIS2-Portal first."))
        url = "%s%s" % (base, path)
        try:
            resp = requests.get(url, auth=(client_id, secret), timeout=timeout,
                                headers={"Accept": "application/json"})
        except Exception as exc:  # noqa: BLE001
            _logger.warning("NIS2-Portal request failed: %s", type(exc).__name__)
            raise UserError(_("Could not reach CRA-Portal (%s).") % exc)
        if resp.status_code == 401:
            raise UserError(_("CRA-Portal rejected the API key (401). Check client id/secret."))
        if resp.status_code == 402:
            raise UserError(_("Your CRA-Portal subscription is not active (402)."))
        if resp.status_code == 403:
            raise UserError(_("The API key is missing the 'nis2:read' scope (403)."))
        if resp.status_code != 200:
            raise UserError(_("CRA-Portal returned an unexpected response (HTTP %s).") % resp.status_code)
        try:
            return resp.json()
        except ValueError:
            raise UserError(_("CRA-Portal returned a non-JSON response."))
