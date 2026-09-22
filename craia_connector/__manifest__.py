# -*- coding: utf-8 -*-
{
    "name": "CRAIA Connector - AI literacy (EU AI Act Article 4)",
    "version": "19.0.1.0.0",
    "category": "Human Resources",
    "summary": "Prove AI literacy for your staff under Article 4 of the EU AI Act: "
               "send employees to CRAIA from Odoo and see their status on the employee form.",
    "description": """
CRAIA Connector - AI literacy under the EU AI Act
==================================================
Article 4 of the EU AI Act (Regulation (EU) 2024/1689) requires providers and
deployers to ensure a sufficient level of AI literacy among staff and other persons
operating AI systems on their behalf. It applies since 2 February 2025, to every
risk class, and the obligation is continuous.

This connector removes the tedious part: your people are already in Odoo.

* **Send employees to CRAIA** from the employee list - name, job title and
  department only.
* An **AI literacy** tab on the employee form showing the live status: invited,
  in progress, completed, and the date it expires.
* An organisation-wide status view: how many AI systems, how many high-risk,
  how many people finished, how many expired.

Keywords: AI Act, artificial intelligence, AI literacy, Article 4, compliance,
governance, training records, EU 2024/1689.

Odoo stays your HR system; CRAIA keeps the evidence. Configure your Partner-API key
under Settings -> CRAIA.

External service and data: this module requires an active CRAIA subscription on
CRA-Portal and a Partner-API key. It transmits only the employee name, work email,
job title and department of the employees you choose to send, over HTTPS,
authenticated by your Partner-API key. No salary, identification, leave or appraisal
data is transmitted. You keep ownership of your data at all times.
""",
    "author": "Woon IoT BV (CRA-Portal)",
    "website": "https://cra-portal.eu/craia",
    "license": "LGPL-3",
    "depends": ["hr"],
    "external_dependencies": {"python": ["requests"]},
    "data": [
        "security/ir.model.access.csv",
        "data/ir_config_parameter.xml",
        "views/res_config_settings_views.xml",
        "views/hr_employee_views.xml",
        "views/craia_menus.xml",
    ],
    "images": ["static/description/banner.png"],
    "installable": True,
    "application": False,
}
