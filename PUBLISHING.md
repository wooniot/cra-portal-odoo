# Publishing, pricing & install — how customers get and pay for our Odoo modules

## Where we list (channels)
1. **Odoo App Store — apps.odoo.com** (primary). One listing per module.
   - **Who can install what:**
     - *Odoo.sh* and *on-premise/Community* customers: install any App Store module directly. **This is our core reachable market.**
     - *Odoo Online (SaaS)* customers **cannot install custom code themselves**; they can only add App Store apps that **Odoo has approved for Online**. So getting each module reviewed *and* Online-approved widens reach to the large Online base (our own Viertron Odoo is Online 19.0 — proof this market matters).
   - Odoo runs the storefront and, for **paid** apps, the billing (per Odoo version) and takes a commission; the publisher sets the price.
2. **Own channel — cra-portal.eu + GitHub.** An "Odoo integration" page on cra-portal.eu; the connector is downloadable from our private repo for Odoo.sh/on-prem customers. We sell the **CRA-Portal subscription** directly here (no Odoo cut).
3. **Odoo Partner directory** (optional, separate track): only if we also want implementation leads — requires becoming an Odoo partner; not needed to publish a module.

## Pricing — two layers (keep them separate)
- **Layer 1 — the module** (on the App Store):
  - **Recommended: FREE (LGPL-3).** Maximises installs; the connector is just the bridge.
  - Alternative: **paid per version (OPL-1)**, e.g. a one-off fee per Odoo version — Odoo takes a cut, and it is **not recurring**.
- **Layer 2 — the CRA-Portal subscription** (recurring, billed by **us**, no Odoo cut). This is where the money is. The connector is **billing-gated** by the Partner-API: no active subscription → API returns HTTP 402 → Pro features stop. Suggested Odoo-channel tiers (per company):
  | Tier | Price | Includes |
  |------|-------|----------|
  | Starter | €49 / month | up to 5 products · CRA keurmerk + verify |
  | Business | €149 / month | up to 25 products · + NIS2 readiness · + incident-response tool |
  | Enterprise | custom | unlimited products · multi-site · AR service |
  (Or align to the existing CRA-Portal web tiers — Starter/Plus.)

**Key rule:** App Store paid apps are **per-version licences, not SaaS**. Recurring revenue must run through our subscription — which the connector already enforces via the Partner-API key + billing-gate.

## Install systematics (customer journey)
1. **Get CRA-Portal** — sign up at cra-portal.eu, choose a plan, and in the CRA-Portal admin **generate a Partner-API key** (client id + secret; scopes `products:read`, `keurmerk:read`, `nis2:read`).
2. **Install the module** in Odoo:
   - *Odoo.sh*: add via the App Store or the repo on a branch.
   - *On-premise*: drop the folder in the addons path (or install the App Store zip), Update Apps List, Install.
   - *Odoo Online*: install from the App Store (once Odoo-approved for Online).
3. **Connect** — Settings → CRA-Portal (and NIS2-Portal): base URL + key → **Test connection**.
4. **Use** — give products an Internal Reference (SKU) that matches CRA-Portal, then **Action → Sync CRA status**. NIS2 → Readiness shows the org status.
5. **Lifecycle** — if the subscription lapses the Partner-API returns 402 and the connector stops surfacing Pro data; renewing restores it. No re-install needed.

## To publish (do-list)
- Create an **Odoo publisher account** on apps.odoo.com (entity: Woon IoT / NLFtech).
- Per module: name, category *Industries*, `static/description/index.html`, `icon.png`, `banner.png`, **screenshots from a running instance**, price + licence, support e-mail (info@cra-portal.eu).
- Add a **DPA / GDPR** addendum (connector sends product/org identifiers to our SaaS) + terms.
- Submit each module (git or zip), pick target Odoo version(s) (now 19.0; also 17/18 branches), pass Odoo's technical review, and request **Online compatibility** review.
- Runtime install-test on Odoo 19 already passed (see LISTING.md). Screenshots are the remaining asset.
