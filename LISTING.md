# Odoo App Store — submission checklist

Two listings (one per module). Both live in this repo (multi-addon).

## Modules
| Module | App Store name | Category | Licence | Price model |
|--------|----------------|----------|---------|-------------|
| `cra_portal_connector` | CRA-Portal Connector | Industries | LGPL-3 | Free connector · revenue = CRA-Portal subscription (recommended). Or OPL-1 paid per version. |
| `nis2_portal_connector` | NIS2-Portal Connector | Industries | LGPL-3 | idem |

## Ready ✅
- Manifests complete (name, version `17.0.1.0.0`, category, summary, description, author, website, licence, images, external_dependencies `requests`).
- `static/description/index.html` (listing page) + `icon.png` (140×140) + `banner.png` per module.
- Code: connectors, settings + Test connection, CRA product tab + SKU sync, NIS2 readiness dashboard, security (NIS2 transient access), default base-URL config param.
- Python + XML + CSV validated; OpenAI code review pass applied (secrets-in-logs tightened).

## Remaining gate before submission ⛔ (needs a running Odoo 17)
1. **Install-test on an Odoo 17 instance** — the one thing not verifiable here:
   - `-u` install both modules without errors.
   - Settings → CRA-Portal / NIS2-Portal render (the `<app>` settings block); *Test connection* works against a real Partner-API key.
   - Product **CRA Compliance** tab shows; *Refresh/Sync CRA status* matches on SKU.
   - **NIS2 → Readiness** dashboard populates and *Refresh* works.
   - Confirm the settings-view XPath (`//form` inside) renders on this exact Odoo build; adjust if the app block does not appear.
2. Take **screenshots** from that instance for each listing (settings, product tab, dashboard).
3. Optional: replace the generated `icon.png`/`banner.png` with polished brand art.

## Publisher / commercial to arrange
- Odoo **publisher account** on apps.odoo.com (entity: Woon IoT / NLFtech).
- Choose licence/price per module (LGPL-3 free vs OPL-1 paid).
- **Partner-API key issuance** for customers: document how a customer gets a
  `client_id` / `secret` (CRA-Portal admin → generate) and required scopes
  (`products:read`, `keurmerk:read`, `nis2:read`).
- **DPA / GDPR** + terms (the connectors send product/org identifiers to the
  CRA-Portal SaaS; a data-processing addendum is needed).
- Support e-mail: **info@cra-portal.eu**.
- Submit each module folder via apps.odoo.com (git or zip upload), select the
  target Odoo version(s), attach description + screenshots + price/licence.

## Target versions
17.0 now; port to 18.0 by bumping the manifest version and re-testing.
