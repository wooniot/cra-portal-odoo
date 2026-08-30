# -*- coding: utf-8 -*-
{
    "name": "NIS2-Portal Connector",
    "version": "19.0.1.0.0",
    "category": "Industries",
    "summary": "Show your organisation's NIS2 (Directive (EU) 2022/2555) readiness inside Odoo - traffic-light status, Article 21 score and conformity mark.",
    "description": """
NIS2-Portal Connector
=====================
A standalone connector that brings NIS2 organisation readiness from the CRA-Portal
SaaS into Odoo. Independently installable - no dependency on the CRA product module.

* **NIS2 readiness dashboard** - traffic-light status (compliant / in progress /
  not compliant), the Article 21 measure score and your organisation conformity mark
  (auth code + public verify link and badge).
* Configure your Partner-API key (scope ``nis2:read``) under Settings -> NIS2-Portal.

Odoo is the base ERP; CRA-Portal delivers the NIS2 assessment engine.

External service and data: this module requires an active CRA-Portal account and
Partner-API key. It sends only your organisation identifier over HTTPS, authenticated
by your Partner-API key, and reads back your NIS2 status. No end-customer, financial
or personal data is transmitted; you keep ownership of your data at all times.
""",
    "author": "Woon IoT BV (CRA-Portal)",
    "website": "https://cra-portal.eu/odoo",
    "license": "LGPL-3",
    "depends": ["base"],
    "external_dependencies": {"python": ["requests"]},
    "data": [
        "security/ir.model.access.csv",
        "data/ir_config_parameter.xml",
        "views/res_config_settings_views.xml",
        "views/nis2_views.xml",
        "views/nis2_menus.xml",
    ],
    "images": ["static/description/banner.png"],
    "installable": True,
    "application": False,
}
