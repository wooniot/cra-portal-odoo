# -*- coding: utf-8 -*-
from odoo import fields, models, _


class CraIncidentReport(models.TransientModel):
    _name = "cra.incident.report"
    _description = "Report a CRA incident to CRA-Portal"

    title = fields.Char(required=True)
    cra_report_stream = fields.Selection(
        [("incident", "Incident"), ("vulnerability", "Vulnerability")],
        string="Type", default="incident", required=True)
    severity = fields.Selection(
        [("low", "Low"), ("medium", "Medium"), ("high", "High"), ("critical", "Critical")],
        string="Severity")
    description = fields.Text()

    def action_submit(self):
        self.ensure_one()
        payload = {
            "title": self.title,
            "description": self.description or "",
            "cra_report_stream": self.cra_report_stream,
            "incident_type": self.cra_report_stream,
            "severity": self.severity or None,
        }
        res = self.env["cra.portal.client"]._cra_post("/api/partner-api/incidents", payload)
        return {
            "type": "ir.actions.client",
            "tag": "display_notification",
            "params": {
                "title": _("CRA incident reported"),
                "message": _("Incident #%(id)s created in CRA-Portal (early warning due %(due)s).") % {
                    "id": res.get("id"), "due": res.get("early_warning_due_at") or "-"},
                "type": "success", "sticky": False,
            },
        }
