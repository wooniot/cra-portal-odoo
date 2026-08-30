# -*- coding: utf-8 -*-
from odoo import fields, models, _


class Nis2IncidentReport(models.TransientModel):
    _name = "nis2.incident.report"
    _description = "Report a NIS2 significant incident to CRA-Portal"

    title = fields.Char(required=True)
    severity = fields.Selection(
        [("low", "Low"), ("medium", "Medium"), ("high", "High"), ("critical", "Critical")],
        string="Severity")
    description = fields.Text()

    def action_submit(self):
        self.ensure_one()
        payload = {
            "title": self.title,
            "description": self.description or "",
            "cra_report_stream": "incident",
            "incident_type": "nis2",
            "severity": self.severity or None,
        }
        res = self.env["nis2.portal.client"]._cra_post("/api/partner-api/incidents", payload)
        return {
            "type": "ir.actions.client",
            "tag": "display_notification",
            "params": {
                "title": _("NIS2 incident reported"),
                "message": _("Incident #%(id)s created in CRA-Portal (early warning due %(due)s).") % {
                    "id": res.get("id"), "due": res.get("early_warning_due_at") or "-"},
                "type": "success", "sticky": False,
            },
        }
