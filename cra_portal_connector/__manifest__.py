# -*- coding: utf-8 -*-
{
    "name": "CRA-Portal Connector",
    "version": "19.0.1.0.0",
    "category": "Industries",
    "summary": "Cybersecurity compliance for the EU Cyber Resilience Act (CRA): product security status, CE-marking conformity, verify links and the 24h/72h incident process in Odoo.",
    "description": """
CRA-Portal Connector - Cyber Resilience Act (CRA) cybersecurity compliance
==========================================================================
Connects Odoo to the CRA-Portal service for the EU Cyber Resilience Act
(CRA, Regulation (EU) 2024/2847). Built for manufacturers, importers and
distributors of products with digital elements who must meet the CRA's
cybersecurity, vulnerability-handling and CE-marking obligations.

* A **CRA Compliance** tab on products showing the live conformity status
  (compliant / in progress / not compliant), the public verify link and badge.
* One-click **Sync CRA status** - matches Odoo products to CRA-Portal on SKU.
* Quick links to the CRA-Portal dashboard and the self-service incident-response
  tool (24h/72h reporting process + tabletop drill).

Keywords: cybersecurity, cyber resilience act, CRA, product security, CE marking,
conformity, vulnerability, SBOM, EU 2024/2847, compliance, NIS2.

Odoo is the base ERP; CRA-Portal delivers the compliance engine. Configure your
Partner-API key under Settings -> CRA-Portal.

External service and data: this module requires an active CRA-Portal account and
Partner-API key. It sends only the product Internal Reference (SKU) and name of the
products you sync, plus your organisation identifier, over HTTPS, authenticated by
your Partner-API key. No end-customer, financial or personal data is transmitted;
you keep ownership of your data at all times.
""",
    "author": "Woon IoT BV (CRA-Portal)",
    "website": "https://cra-portal.eu/odoo",
    "license": "LGPL-3",
    "depends": ["product"],
    "external_dependencies": {"python": ["requests"]},
    "data": [
        "data/ir_config_parameter.xml",
        "views/res_config_settings_views.xml",
        "views/product_template_views.xml",
        "views/cra_menus.xml",
    ],
    "images": ["static/description/banner.png"],
    "installable": True,
    "application": False,
}
