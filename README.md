# CRA-Portal — Odoo connectors

Two standalone Odoo add-ons that bring EU compliance status into Odoo by connecting
to the **CRA-Portal** SaaS. Odoo is the base ERP; CRA-Portal delivers the compliance
engine. Recurring value is the CRA-Portal subscription — the connectors are thin,
well-behaved bridges over the Partner-API.

| Module | What it adds |
|--------|--------------|
| **`cra_portal_connector`** | Cyber Resilience Act (Reg. (EU) 2024/2847): a CRA Compliance tab on products with live keurmerk status, verify links, one-click sync (SKU match), and a link to the self-service incident-response tool. |
| **`nis2_portal_connector`** | NIS2 (Dir. (EU) 2022/2555): an organisation readiness dashboard — traffic-light status, Article 21 measure score and the org keurmerk. Independently installable. |

Target: **Odoo 17.0** (18.0 intended). Licence: **LGPL-3** (free connectors; monetise
via the CRA-Portal subscription). External dependency: `requests`.

## Install
1. Copy the module folder(s) into your Odoo `addons` path (or install from the App Store).
2. Update the apps list and install **CRA-Portal Connector** and/or **NIS2-Portal Connector**.
3. Go to **Settings → CRA-Portal** (and **Settings → NIS2-Portal**), enter your base URL
   and Partner-API key, and press **Test connection**.

## Partner-API
The connectors call the CRA-Portal Partner-API (HTTP Basic, scope- and billing-gated):
`/api/partner-api/me`, `/products`, `/keurmerk`, `/nis2/status`. Get a key from your
CRA-Portal account. See `BLUEPRINT.md` for the design and `LISTING.md` for the Odoo
App Store checklist.

— Woon IoT BV · https://cra-portal.eu · info@cra-portal.eu
