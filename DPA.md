# Data Processing Addendum (DPA) — CRA-Portal & NIS2-Portal Odoo connectors

This addendum accompanies the Odoo App Store listings and the CRA-Portal subscription
terms. It documents the GDPR (Regulation (EU) 2016/679) roles and the data the
connectors exchange, so an installing customer can complete their own records of
processing.

## Roles
- **Customer** (the Odoo user / manufacturer) = **controller**.
- **Woon IoT BV** (trading as CRA-Portal, KvK 76066843) = **processor**, for the data
  the connector sends to the CRA-Portal SaaS.
- **Odoo S.A.** = distributor of the module only; it does not receive connector data.

## What the connector sends to CRA-Portal
Only what is needed to look up compliance status:
- **Product identifiers** — the Internal Reference (SKU) and name of products you
  choose to sync (`cra_portal_connector`).
- **Organisation identifier** — your CRA-Portal tenant, resolved from the Partner-API
  key (`nis2_portal_connector` and `cra_portal_connector`).
- **The Partner-API key** (client id + secret) as the authentication credential.

No personal data of end-customers, no financial data, and no product content beyond
SKU + name leave Odoo. The connector is **read-mostly**: it pulls status and writes it
back onto the Odoo product record.

## What CRA-Portal returns
Keurmerk status (traffic-light), authorisation code, public verify URL, badge URL,
NIS2 Article 21 score. This is compliance metadata about the customer's own products
and organisation.

## Hosting & sub-processors
- CRA-Portal SaaS runs on EU infrastructure (Hetzner, Germany / TransIP, Netherlands).
- No data is transferred outside the EU/EEA by the connector.
- Sub-processors: the hosting provider(s) above. A current list is available on request
  at info@cra-portal.eu.

## Security
- Transport is HTTPS; the Partner-API key authenticates every call.
- The key is stored in Odoo `ir.config_parameter` (server-side); the connector never
  logs the key or secret values (exception details are logged by type only).
- Access is scoped: keys carry only the scopes needed (`products:read`, `keurmerk:read`,
  `nis2:read`).

## Retention & deletion
- Product/organisation identifiers are processed to serve live look-ups and are retained
  for the life of the subscription.
- On termination, the customer removes the module / key; CRA-Portal deletes the
  associated tenant look-up data on request (info@cra-portal.eu).

## Data subject requests & contact
Route any GDPR request or question to **info@cra-portal.eu**. Woon IoT BV will assist
the controller within statutory timelines.

*This addendum is provided for transparency and does not replace the signed CRA-Portal
subscription agreement, which prevails where terms differ.*
