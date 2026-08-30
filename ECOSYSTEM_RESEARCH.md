# Ecosystem Research — Marktplaats-/koppelingskansen voor 3 WoonIoT-producten

_Beslis-klaar rapport. Opgesteld 25 aug 2026. Alle marktplaatsen zijn geverifieerd via WebSearch; onzekerheden staan expliciet gemarkeerd._

Doel: per product bepalen waar we een koppeling/module kunnen **listen** voor (a) exposure en (b) aanvullende omzet. Verdict-legenda:

- **ONTWIKKELEN** = echte connector/module bouwen + listen (het loont de bouw-effort).
- **ADVERTEREN** = geen/lichte build; alleen listen/present zijn voor exposure.
- **SKIP** = niet doen (mismatch doelgroep, te duur, te zwaar, of geen echte etalage).

---

## Spoor 1 — CRA-Portal (compliance-connector voor hardware-fabrikanten)

Doelgroep: fabrikanten/importeurs/distributeurs van elektronica met digitale componenten. Model: gratis connector + CRA-Portal-abo (49-149/mnd). Odoo-connector (CRA + NIS2) is al gebouwd. Relevante timing: CRA-rapportageplicht (Art. 14) vanaf **11 sep 2026**, volledige toepassing 11 dec 2027 — de urgentie bij fabrikanten piekt nu, dus exposure heeft momentum.

### Ranglijst

| # | Platform | Marktplaats + toelating | Doelgroep-fit (hardware-fab.) | Effort | Verdien-/exposure-model | Verdict + waarom |
|---|----------|------------------------|-------------------------------|--------|-------------------------|------------------|
| 1 | **Odoo Apps** | JA — self-serve upload via GitHub, lichte review. Al gedaan. | Hoog — veel EU-MKB-fabrikanten draaien Odoo MRP | Laag (klaar) | Gratis connector = gratis listing, funnel naar abo | **ONTWIKKELEN (klaar)** — thuisbasis, houd 'm actueel en zichtbaar |
| 2 | **MS Dynamics 365 Business Central (AppSource)** | JA — Partner Center, 2 validaties (technisch + marketing), data-classificatie/GDPR verplicht, object-range/prefix reserveren | Hoog — BC is dé mid-market ERP voor fabrikanten in DACH/NL/EU | Hoog | Gratis listing; enorme B2B-exposure, MS co-sell mogelijk | **ONTWIKKELEN** — grootste exposure-waarde voor exact onze doelgroep; zwaar maar strategisch |
| 3 | **SAP Store (Business One / App Center)** | JA — Publishing Cockpit + Partner Cockpit, formele certificering, revenue-share-optie | Hoog qua fit, maar SAP-B1-klant = grotere fabrikant | Hoog | SAP Store-listing + revenue-share, prestige | **ADVERTEREN** — listing/partner-profiel zonder diepe build eerst; volledige connector alleen bij vraag |
| 4 | **Zoho Marketplace** | JA — publish via checkbox, review 24-48u, 30% commissie op betaald | Matig — Zoho-fabrikanten bestaan, minder EU-hardware | Laag/Middel | 30% bij betaald; gratis bij eigen billing; snelle toelating | **ADVERTEREN** — lage drempel + snelle review maken een lichte listing goedkoop de moeite |
| 5 | **Katana MRP** | JA — Integration Marketplace (in-app nav) + partner-programma, open REST API | Hoog — Katana = MRP voor kleine e-manufacturers, precies CRA-scope | Middel | Partner-listing + demo-account/consult; exposure bij groeiende maker-basis | **ONTWIKKELEN (fase 2)** — sterke niche-fit; bouwen zodra Odoo/BC staan |
| 6 | **Sage Marketplace** | JA — ISV/Tech-Partner listing, wereldwijde store | Matig — Sage sterker in finance/boekhouding dan MRP | Middel | ISV-listing (resale/referral) | **ADVERTEREN** — listen kan, maar minder pure fabrikant-fit dan BC/Katana |
| 7 | **Weclapp** | JA — weclapp Store + REST API/partner-solutions | Matig/Hoog — DACH-cloud-ERP met productie-module | Middel | Store-listing | **ADVERTEREN** — DACH-exposure; connector alleen bij concrete lead |
| 8 | **ERPNext / Frappe Cloud Marketplace** | JA — maar **alleen open source** (MIT/GPL), app op GitHub, team-approval | Matig — technische/open-source-fabrikanten | Middel | Gratis listing; onze connector is niet OS → licentie-conflict | **SKIP** — open-source-eis botst met ons closed abo-model |
| 9 | **AFAS Profit** | JA — App Connector + certified partner (gesloten certificering) | Matig (NL) — AFAS sterker in HR/finance dan discrete productie | Middel/Hoog | Certified connector, NL-markt | **SKIP (voorlopig)** — zware certificering, geen kern-fabrikant-fit |
| 10 | **Exact Online App Centre** | JA — "Get published", demo met partner-manager verplicht (op kantoor/online) | Matig (NL/BE) — Exact = boekhouding, niet MRP | Middel | App Centre-listing, NL-bereik | **SKIP (voorlopig)** — boekhoud-publiek ≠ CRA-beslisser; herweeg bij NL-tractie |
| 11 | **MRPeasy** | NEE (geen eigen store) — alleen REST API (Unlimited-plan), koppelen via Make/airSlate | Hoog qua doelgroep (kleine fab.), maar geen etalage | Middel | Geen listing-etalage → geen exposure-winst | **SKIP** — geen marktplaats om in te staan |
| 12 | **Fishbowl** | Deels — Partner Directory (geen self-serve store), API's | Matig — QuickBooks-gericht, VS-markt | Middel | Partner-directory-vermelding | **SKIP** — VS/QuickBooks-focus, geen EU-CRA-relevantie |
| 13 | **Shopify / WooCommerce** | JA (grote app stores) | Laag — verkopers ≠ fabrikanten/CRA-plichtigen | Middel | App-store-listing | **SKIP** — verkeerde doelgroep; CRA raakt de maker, niet de webshop |

### Top-3 aanbeveling — CRA-Portal

1. **ONTWIKKELEN — Business Central (AppSource).** Na Odoo de grootste hefboom: BC is dé mid-market-ERP voor precies onze fabrikant-doelgroep in NL/DACH, met MS co-sell-exposure. Zwaar toelatingstraject, maar strategisch de moeite.
2. **ONTWIKKELEN (fase 2) — Katana MRP.** Beste niche-fit: MRP voor kleine e-manufacturers = kern-CRA-scope, open API, in-app marketplace. Middel-effort, hoge relevantie.
3. **ADVERTEREN — SAP Store + Zoho + Sage/Weclapp.** Lichte listings/partner-profielen zonder diepe build; goedkope extra vindbaarheid. **SKIP**: ERPNext (OS-eis), MRPeasy/Fishbowl (geen EU-etalage), Shopify/WooCommerce (verkeerde doelgroep).

---

## Spoor 2 — RingAI (AI-telefoniste, Odoo-belmodule)

Doelgroep: NL ZZP'ers + klein MKB. Model: gratis module/connector + RingAI-abo. Odoo-module (gesprekken + AI-samenvatting + terugbel-taak) is in aanbouw.

### Ranglijst

| # | Platform | Marktplaats + toelating | Doelgroep-fit (NL ZZP/MKB) | Effort | Verdien-/exposure-model | Verdict + waarom |
|---|----------|------------------------|----------------------------|--------|-------------------------|------------------|
| 1 | **Odoo Apps Store** | JA — `apps@odoo.com`, vendor-guidelines review | Hoog — module al in aanbouw, Odoo groeit in NL-MKB | Laag (bezig) | Gratis module = gratis listing (30% geldt alleen bij betaald) | **ONTWIKKELEN** — thuisbasis, nul kosten, directe vindbaarheid |
| 2 | **Teamleader Focus** | JA — Marketplace + Dev Portal, review (testaccount + demo naar marketplace@teamleader.eu) | Zeer hoog — Benelux-CRM #1 voor ZZP/klein MKB | Laag/Middel | Gratis listing; verkoop eigen abo | **ONTWIKKELEN** — beste NL/BE-fit buiten Odoo, lichte review, hoogste ROI/uur |
| 3 | **Pipedrive Marketplace** | JA — Developer Hub, review tot ~21 werkdagen, eigen ToS/Privacy | Hoog — populair bij NL sales-ZZP/MKB | Middel | Gratis listing; billing via ons; levendige telefonie-categorie | **ONTWIKKELEN (fase 2)** — brede reach, goede API/OAuth, na Odoo+Teamleader |
| 4 | **HubSpot App Marketplace** | JA — Ecosystem-review ~10 wd (max 60), **0% revenue-share** | Middel/Hoog — NL scale-ups, minder pure ZZP | Middel/Hoog | Gratis listing, 0% fee, sterke SEO/exposure | **ADVERTEREN / ONTWIKKELEN fase 2** — grote exposure + 0% fee, maar zwaardere eisen, minder ZZP |
| 5 | **3CX CRM-integratie** | Functioneel JA — CRM Integration Wizard + JSON-template (geen klassieke store) | Middel — veel NL-MKB draait 3CX; call-log past | Laag/Middel | Geen fee; template in 3CX-clientlijst | **ADVERTEREN (lichte build)** — goedkope template (2-3 dgn), maar 3CX is deels concurrent van onze telefonie-laag |
| 6 | **Voys / VoIPGRID** | GEEN publieke store — integraties via Zapier + open API/GitHub | Zeer hoog — maar RingAI gebruikt Voys al als SIP-trunk | Laag (Zapier) | Geen etalage → geen exposure-winst uit "listing" | **ADVERTEREN (navragen)** — technisch koppelen ja; besloten partner-directory onzeker → direct bij Voys navragen (eigen leverancier = natuurlijke NL-kans) |
| 7 | **Zoho Marketplace** | JA — review 24-48u, 30% op betaald | Laag/Middel — dunne NL-ZZP-penetratie | Middel | 30% bij betaald; gratis bij eigen billing | **SKIP (tenzij internationaal)** — snelle toelating, maar te weinig NL-doelgroep |
| 8 | **Freshworks/Freshsales** | JA — dev-portal, review ~1 week | Laag — beperkt NL-marktaandeel | Middel | Gratis listing + "Verified"-badge | **SKIP** — degelijk maar te weinig NL-relevantie voor de effort |
| 9 | **Lightspeed** | JA — partner-programma (geen self-serve), aanvraag + certificering | Laag — retail/horeca POS, niet call-centric | Hoog | Co-marketing, partner manager | **SKIP** — verkeerde use-case (geen inbound-telefonie-behoefte) |
| 10 | **Salesforce AppExchange** | JA — Security Review $999/poging (gratis voor free apps), ~$150/jr, 15-25% share, 5-9 mnd | Laag — enterprise, niet ZZP/MKB | Zeer hoog | Duur, traag, revenue-share | **SKIP** — kosten/doorlooptijd haaks op ZZP-product |
| 11 | **Moneybird / Simplicate / Gripp / e-Boekhouden** | Integratiepagina's JA, **echte self-serve marketplace NEE** | Hoog qua NL-ZZP, maar boekhouden ≠ telefonie | Middel | Geen etalage/revenue-model | **SKIP** — geen marktplaats + geen telefonie-context |

### Top-3 aanbeveling — RingAI

1. **ONTWIKKELEN — Odoo Apps Store.** Module is er al; publiceer gratis. Kern, nul kosten, directe vindbaarheid.
2. **ONTWIKKELEN — Teamleader Focus.** Beste Benelux-ZZP/MKB-fit buiten Odoo. Bouw de tweede connector (call-log + AI-samenvatting + terugbel-taak). Lichte review, gratis listing, hoogste ROI per uur.
3. **ONTWIKKELEN (fase 2) — Pipedrive**, daarna **HubSpot** (0% fee, veel SEO-exposure). Kies Pipedrive eerst bij één keuze. **ADVERTEREN**: 3CX-template + Voys navragen. **SKIP**: Salesforce (te duur/traag), Zoho/Freshworks (te weinig NL), Lightspeed (POS), boekhoudpakketten (geen etalage).

---

## Spoor 3 — Situara (safety/incident-communicatie) als HR-/personeelsmodule

**Kernbevinding vooraf (belangrijk):** de vraag verwart twee producten. Situara is vandaag een **consumentgerichte omgevingsrisico-/gevarenkaart** (lagen: drinkwater-incidenten, stralingskaart, risico-score). Wat HR-klanten in deze hoek willen is **emergency mass notification** — alert naar medewerkers, contactenlijst, "ben je veilig"-roll-call (categorie Everbridge/AlertMedia). Een HR-veiligheidsmodule is daarom **geen Situara-koppeling, maar een nieuw product bouwen.** De marktplaatsen bestáán allemaal (geverifieerd); de blokkade is product-fit, niet infrastructuur.

### Ranglijst

| # | Platform | Marktplaats + toelating | Doelgroep-fit | Effort | Verdien-/exposure-model | Verdict + waarom |
|---|----------|------------------------|---------------|--------|-------------------------|------------------|
| 1 | **Odoo Apps** | JA — self-serve upload, lichte review | Laag/Matig — Odoo HR = admin/proces, niet crisis | Laag | Gratis listing als funnel | **ADVERTEREN (light)** — enige echt self-serve; alleen als er al een lichte koppeling ligt |
| 2 | **BambooHR Marketplace** | JA — "Apply Now", API-check, Marketplace Agreement | Matig — 30k SMB-klanten (vooral VS), veiligheid past thematisch | Middel | Exposure bij 30k klanten, geen verplichte rev-share | **ADVERTEREN-kandidaat / SKIP** — mooie exposure, maar VS-gericht + product-mismatch |
| 3 | **Factorial** | JA — partnerprogramma, REST API, ~80 integraties | Matig — EU-SMB, dicht bij Situara-markt | Middel | Listing + newsletter/social-push | **SKIP** — markt past, maar geen product om te koppelen |
| 4 | **Personio Marketplace** | JA — via integration-partner@personio.com, joint QA | Matig — EU-SMB, eist "echte meerwaarde" + gedeelde klanten | Middel | Listing marketplace + in-app | **SKIP** — toelating vereist bestaande gedeelde klanten (niet aanwezig) |
| 5 | **Nmbrs (Visma)** | JA — App Store + partnerformulier, API | Laag/Matig — payroll/NL, nauwelijks veiligheid | Middel | App Store-listing | **SKIP** — payroll-publiek, verkeerde thematiek |
| 6 | **AFAS Profit** | JA — App Connector + certified partner | Matig (NL) — HR/tijdregistratie, gesloten certificering | Middel/Hoog | Certified connector | **SKIP** — zware certificering, geen kern-fit |
| 7 | **MS Teams / AppSource** | JA — maar niche **al gevuld** (RedFlag, Sparrow, Crises Control, AlertMedia) | Hoog thematisch, maar **verzadigd** | Hoog | AppSource-listing | **SKIP** — juiste plek, maar incumbents zitten er al met echte notificatie-producten |
| 8 | **SAP SuccessFactors (SAP Store)** | JA — formele certificering (3 niveaus) | Enterprise, niet Situara's markt | Hoog | SAP Store-listing | **SKIP** — enterprise-schaal, verkeerd |
| 9 | **Workday Marketplace** | JA — "Built on Workday", betaalde certificering ($1.5-2.5k persoon) | Enterprise, niet Situara's markt | Hoog | Marketplace + certificering | **SKIP** — enterprise, kostbaar, geen fit |

**Concurrentielandschap:** de emergency/mass-notification-niche is **druk en goed gefinancierd** (Everbridge, AlertMedia, OnSolve/Crisis24, Regroup, RedFlag, Hyper-Reach, InformaCast, DeskAlerts, Crises Control — Gartner heeft er een eigen marktcategorie voor). Geen open gat; volwassen markt met sterke incumbents.

### Top-3 + eindoordeel — Situara

**Overall verdict: NIET nastreven als serieuze track — dit is een distractie.** Drie harde redenen:
1. **Product-mismatch.** Situara = publieke gevarenkaart, geen werknemer-notificatiesysteem. Een HR-listing vereist eerst een nieuw product (contactenlijsten, roll-call, targeting per afdeling). De marktplaats is het makkelijke deel; het product is het echte werk.
2. **Verzadigde niche.** Waar het thematisch wél past (Teams/AppSource) zitten Everbridge, AlertMedia, RedFlag er al met volwassen producten. Situara komt als laatkomer zonder onderscheid.
3. **Geen gedeelde klanten.** Personio/Factorial/BambooHR verwachten bestaande gedeelde klanten + "echte meerwaarde" — die basis is er niet.

**Als je tóch een low-effort experiment wilt:**
1. **ADVERTEREN — Odoo Apps** (enige self-serve, gratis) — alleen als er al een lichte koppeling ligt.
2. **ADVERTEREN — BambooHR** (30k klanten, lichte toelating) — puur exposure-gok.
3. **SKIP al het overige.** Geen certificeringstrajecten (SAP/Workday/AFAS). Energie beter besteed aan Situara's eigen consumenten-/pilot-kanaal.

---

## Onzekerheden (expliciet gemarkeerd)

- **Listing-fees** voor Personio/Factorial/Nmbrs/AFAS/Teamleader/Pipedrive niet publiek bevestigd — waarschijnlijk gratis listing bij eigen billing, maar niet 100% geverifieerd. Behandel als "gratis exposure tot bevestigd".
- **Revenue-share Pipedrive/Teamleader**: niet publiek gevonden; billing loopt via ons (vermoedelijk 0% op eigen abo).
- **Voys/VoIPGRID besloten partner-directory** (VoIPGRID→Voys Partners-transitie 2025): mogelijk niet-publiek → direct bij Voys navragen; het is onze eigen SIP-leverancier en de meest natuurlijke NL-exposure-kans.
- **Odoo "gratis listing"**: klopt voor gratis modules; 30% geldt alleen bij betaalde modules.
- **Business Central / SAP-connector-effort** is hoog ingeschat op basis van gepubliceerde validatie-eisen; exacte doorlooptijd hangt af van onze AL/integratie-ervaring.
- **Situara product-fit-oordeel** steunt op wat Situara volgens de projectcontext ís (consumenten-gevarenkaart). Bestaat er intern al een B2B-werknemersnotificatie-variant, dan verschuift de fit richting Teams/BambooHR "matig-ONTWIKKELEN" — niet live te verifiëren.
