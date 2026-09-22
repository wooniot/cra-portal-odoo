# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class HrEmployee(models.Model):
    """Toont de AI-geletterdheidsstand op de medewerkerkaart.

    De velden zijn READ-ONLY en worden opgehaald bij CRAIA. Odoo blijft het
    personeelssysteem; CRAIA bewaart het bewijs. Zo staat dezelfde stand niet op
    twee plekken half bij te zijn.
    """

    _inherit = "hr.employee"

    craia_status = fields.Selection(
        [("onbekend", "Not sent"), ("nieuw", "Sent"), ("uitgenodigd", "Invited"),
         ("bezig", "In progress"), ("afgerond", "Completed"), ("verlopen", "Expired")],
        string="AI literacy", default="onbekend", readonly=True, copy=False,
        help="Status in CRAIA. Refresh with the button to fetch the current state.")
    craia_geldig_tot = fields.Date(string="Valid until", readonly=True, copy=False)
    craia_laatste_sync = fields.Datetime(string="Last synced", readonly=True, copy=False)

    def _craia_payload(self):
        """Alleen wat artikel 4 nodig heeft: wie, welke rol, welke afdeling."""
        personen = []
        for w in self:
            email = w.work_email or ""
            if not email:
                continue
            personen.append({
                "naam": w.name or "",
                "email": email,
                "functie": w.job_title or (w.job_id.name if w.job_id else ""),
                "afdeling": w.department_id.name if w.department_id else "",
            })
        return personen

    def action_craia_send(self):
        """Stuurt de geselecteerde medewerkers naar CRAIA."""
        personen = self._craia_payload()
        if not personen:
            return self._craia_melding(
                _("No employees sent"),
                _("None of the selected employees has a work email address. CRAIA "
                  "invites people by email, so that field is required."), "warning")
        uitkomst = self.env["craia.client"]._craia_post(
            "/api/partner-api/craia/personen", {"personen": personen})
        self.write({"craia_status": "nieuw", "craia_laatste_sync": fields.Datetime.now()})

        regels = [_("New: %s") % uitkomst.get("nieuw", 0),
                  _("Updated: %s") % uitkomst.get("bijgewerkt", 0)]
        overgeslagen = uitkomst.get("overgeslagen") or []
        soort = "success"
        if overgeslagen:
            soort = "warning"
            regels.append(_("Skipped: %s") % len(overgeslagen))
            for o in overgeslagen[:3]:
                regels.append("- %s: %s" % (o.get("naam"), o.get("reden")))
        return self._craia_melding(_("Sent to CRAIA"), "\n".join(regels), soort)

    def action_craia_refresh(self):
        """Haalt de stand van de organisatie op en toont die."""
        stand = self.env["craia.client"]._craia_get("/api/partner-api/craia/stand")
        if not stand.get("actief"):
            return self._craia_melding(
                _("CRAIA is not active"),
                stand.get("reden") or _("No active CRAIA subscription was found."),
                "warning")
        regels = [
            _("AI systems: %s (high risk: %s)") % (stand.get("aantal_systemen", 0),
                                                   stand.get("aantal_hoog_risico", 0)),
            _("People: %s, completed: %s, expired: %s") % (
                stand.get("aantal_personen", 0), stand.get("aantal_afgerond", 0),
                stand.get("aantal_verlopen", 0)),
        ]
        if stand.get("craia_verloopt_op"):
            regels.append(_("Subscription valid until: %s") % stand["craia_verloopt_op"])
        return self._craia_melding(_("CRAIA status"), "\n".join(regels), "info")

    @api.model
    def _craia_melding(self, titel, bericht, soort="info"):
        return {
            "type": "ir.actions.client",
            "tag": "display_notification",
            "params": {"title": titel, "message": bericht, "type": soort,
                       "sticky": soort != "success"},
        }
