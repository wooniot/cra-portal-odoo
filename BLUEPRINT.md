# CRA-Portal Connector for Odoo — Blueprint (MVP)

**Goal:** Odoo is the base ERP; this module is the paid *add-on* that brings CRA
(Cyber Resilience Act) compliance into Odoo by connecting to the CRA-Portal SaaS.
Recurring revenue stays with us (CRA-Portal subscription), not the one-off Odoo
App Store licence — so the connector is a thin, well-behaved bridge.

## What it does (MVP)
1. **Settings** — configure the CRA-Portal base URL + a Partner-API key
   (client id + secret) per company, with a *Test connection* button.
2. **Products** — a **CRA Compliance** tab on `product.template` showing the live
   keurmerk status (green/amber/red), the public verify link, the badge, and an
   auth code — pulled from CRA-Portal and matched on the product SKU (`default_code`).
3. **CRA Compliance menu** — a product view scoped to CRA columns + a header
   action **Sync CRA status** that refreshes all matching products in one call,
   plus quick links to the CRA-Portal dashboard and the self-service
   **incident-response tool** (24h/72h process + tabletop drill).
4. **NIS2** — read the organisation's NIS2 readiness status in Settings (optional).

## How it connects
- CRA-Portal exposes a **Partner-API** (`/api/partner-api/...`, HTTP Basic
  `client_id:client_secret`, scope-gated + billing-gated):
  - `GET /api/partner-api/me` — identity, scopes, billing (used by *Test connection*).
  - `GET /api/partner-api/products` — the tenant's products.
  - `GET /api/partner-api/keurmerk` — per-product status + verify/badge/QR URLs.
  - `GET /api/partner-api/nis2/status` — org NIS2 readiness.
- The Odoo module stores the credentials in `ir.config_parameter` and calls the
  API with `requests` (Basic auth). No secrets in code.

## Module layout
```
cra_portal_connector/
  __manifest__.py            # metadata, deps, data, license, listing images
  __init__.py
  models/
    __init__.py
    cra_portal_client.py     # thin API client (AbstractModel: _cra_call)
    res_config_settings.py   # base URL + client id/secret + Test connection
    product_template.py      # CRA fields + fetch/sync + matching by SKU
  views/
    res_config_settings_views.xml
    product_template_views.xml
    cra_menus.xml
  security/ir.model.access.csv
  static/description/{index.html, icon.png}
  data/ir_config_parameter.xml   # default base URL
  README.md  LICENSE
```

## Targets & licence
- Odoo **17.0** (also intended for 18.0). Manifest version `17.0.1.0.0`.
- Licence **LGPL-3** (free connector; monetise via the CRA-Portal subscription).
  Switch to **OPL-1** if the module itself is to be sold on the App Store.
- External dependency: `requests`.

## Out of scope for MVP (phase 2)
Native incident storage in Odoo, webhook push from CRA-Portal, automatic SKU↔product
provisioning, multi-company credential sets, per-user CRA roles.

## Build → review → list
1. Build the module (this repo).
2. OpenAI code review pass; apply fixes.
3. Prepare Odoo App Store listing (name, category *Industries/Manufacturing*,
   description = `static/description/index.html`, icon, price/licence, support
   e-mail, screenshots) — see `LISTING.md`.

## Second, standalone module: `nis2_portal_connector`
A separate, independently installable Odoo module for **NIS2** (Directive (EU)
2022/2555) organisation readiness — for customers who want NIS2 only, without the
CRA product module. Same connector pattern (own settings + API client, no
dependency on the CRA module):
- **Settings** — CRA-Portal base URL + Partner-API key (scope `nis2:read`) + Test.
- **NIS2 dashboard** — pulls `GET /api/partner-api/nis2/status`: readiness
  traffic-light (green/amber/red), Art. 21 measure score, the org keurmerk
  (auth code + verify/badge URLs), plus a link to the self-assessment in the portal.
Listed as its own App Store entry (category *Industries*), same licence/price model.
Both modules live in this one repo (multi-addon).
