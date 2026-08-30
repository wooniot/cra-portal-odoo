# -*- coding: utf-8 -*-
import logging
from odoo import models, _
from odoo.exceptions import UserError
try:
    import requests
except ImportError:
    requests = None
_logger = logging.getLogger(__name__)
DEFAULT_BASE_URL = "https://dev.cra-portal.eu"
class CraPortalClient(models.AbstractModel):
    """API client"""
    _name = "cra.portal.client"
    _description = "CRA-Portal API client"
    def _cra_config(self):
        icp = self.env["ir.config_parameter"].sudo()
        base = (icp.get_param("cra_portal_connector.base_url") or DEFAULT_BASE_URL).rstrip("/")
        client_id = icp.get_param("cra_portal_connector.client_id") or ""
        secret = icp.get_param("cra_portal_connector.client_secret") or ""
        return base, client_id, secret
    def _cra_get(self, path, timeout=20):
        """GET endpoint and return JSON or raise UserError."""
        if requests is None:
            raise UserError(_("The Python library 'requests' is required for the CRA-Portal connector. "
                              "Install it on the Odoo server (pip install requests)."))
        base, client_id, secret = self._cra_config()
        if not client_id or not secret:
            raise UserError(_("Configure your CRA-Portal Partner-API key under "
                              "Settings → CRA-Portal first."))
        url = "%s%s" % (base, path)
        try:
            resp = requests.get(
                url, auth=(client_id, secret), timeout=timeout,
                headers={"Accept": "application/json"},
            )
        except Exception as exc:
            _logger.warning("CRA-Portal request failed: %s", type(exc).__name__)
            raise UserError(_("Could not reach CRA-Portal (%s).") % exc)
        if resp.status_code == 401:
            raise UserError(_("CRA-Portal rejected the API key (401). Check the client id and secret."))
        if resp.status_code == 402:
            raise UserError(_("Your CRA-Portal subscription is not active (402). Check your plan/billing."))
        if resp.status_code == 403:
            raise UserError(_("The API key is missing the required scope (403)."))
        if resp.status_code == 429:
            raise UserError(_("CRA-Portal rate limit reached (429). Try again shortly."))
        if resp.status_code != 200:
            raise UserError(_("CRA-Portal returned an unexpected response (HTTP %s).") % resp.status_code)
        try:
            return resp.json()
        except ValueError:
            raise UserError(_("CRA-Portal returned a non-JSON response."))

    def _cra_post(self, path, payload, timeout=20):
        """POST JSON to an endpoint and return JSON or raise UserError."""
        if requests is None:
            raise UserError(_("The Python library 'requests' is required for the CRA-Portal connector. "
                              "Install it on the Odoo server (pip install requests)."))
        base, client_id, secret = self._cra_config()
        if not client_id or not secret:
            raise UserError(_("Configure your CRA-Portal Partner-API key under "
                              "Settings → CRA-Portal first."))
        try:
            resp = requests.post(
                "%s%s" % (base, path), auth=(client_id, secret), timeout=timeout,
                json=payload, headers={"Accept": "application/json"},
            )
        except Exception as exc:
            _logger.warning("CRA-Portal request failed: %s", type(exc).__name__)
            raise UserError(_("Could not reach CRA-Portal (%s).") % exc)
        if resp.status_code == 401:
            raise UserError(_("CRA-Portal rejected the API key (401). Check the client id and secret."))
        if resp.status_code == 402:
            raise UserError(_("Your CRA-Portal subscription is not active (402). Check your plan/billing."))
        if resp.status_code == 403:
            raise UserError(_("The API key is missing the required scope (403)."))
        if resp.status_code not in (200, 201):
            raise UserError(_("CRA-Portal returned an unexpected response (HTTP %s).") % resp.status_code)
        try:
            return resp.json()
        except ValueError:
            raise UserError(_("CRA-Portal returned a non-JSON response."))
