# 2–3 Year Horizon Report (hold to ~late 2029) — DRAFT v2 for red-team round 2

As of Saturday 2026-10-10. Sources: lt_macro_themes.md, lt_global_stocks.md, lt_india_stocks.md, lt_redteam_round1.md (same folder); model re-runs from scratchpad/redteam/rt_proposed.py (30/50/20 bear/base/bull weights, red-team AI-bust bears, corrected inputs). Every figure is from web-search summaries; several prices are 1–7 weeks old. Not investment advice.

## Response to red-team round 1 (open objections O1–O20)

| ID | Objection | v2 response |
|---|---|---|
| O1 | 25/50/25 weights | **Accepted.** All headline expected returns now use the macro brief's 30/50/20 (bear/base/bull). |
| O2 | Asymmetric haircuts flatter the India edge | **Accepted.** Edge restated on equal footing: India sleeve 12.9%/yr expected vs 11.3% for an all-index sleeve (+1.6 pp); with a further 3 pp growth haircut on picks only, ~0 pp. Stated as "a small, uncertain edge". |
| O3 | Global edge compared different methods | **Accepted.** S&P 500 run through the same model: 10.4%/yr expected (base 13.7%). Picks 13.3% expected → edge ~2.9 pp before, ~0–2 pp after a 3 pp haircut. The "S&P 5–6%" comparison is removed. |
| O4 | 55% of India sleeve at/below hurdle | **Accepted.** L&T and TCS dropped; Reliance, Bharti, Maruti, Apollo cut to 5–6% of the sleeve and event-gated; NTPC kept as the low-bear rate-reset play (bear +0.6%/yr) — justified as ballast, not alpha. |
| O5 | TCS vs analyst's own rule; HDFC AMC invalid | **Accepted.** TCS dropped; replaced by the Nifty index fund, not HDFC AMC (~33–34x, base ~12.6%). The USD sleeve is the rupee hedge. |
| O6 | L&T below hurdle + Gulf exposure | **Accepted.** Dropped; held at index weight via the Nifty fund. |
| O7 | AI-capex spender bears too mild; MSFT capex stale | **Accepted.** MSFT FY27 capex ~$255–260B; MSFT/AMZN bears ~−22% over 3 years; spenders capped at ~23% of the global sleeve (Microsoft + a small Amazon). |
| O8 | Alphabet add contradicts macro | **Accepted.** Dropped; Alphabet held at index weight via an Irish-domiciled S&P 500 UCITS ETF. |
| O9 | Amazon clean EPS unverified | **Accepted.** Priced at ~26–27x; weight cut to 8% of the global sleeve. |
| O10 | Intuit headline is 45 pp re-rating | **Accepted.** Headline is now the flat-multiple base (~15%/yr); re-rating shown as upside; 12% of the sleeve; conviction 3.5; buy after FQ1 (Nov 19). Second FY28 source not found (Tickflow FY27 $26.40 vs $23.07 basis conflict noted). |
| O11 | SBI Life price/growth/regulation | **Accepted.** Price ₹1,769.55 (Sep 21) → P/EV ~2.08x; EV growth 13.5% (base 17.5%/yr); buy only ≤₹1,850; RBI/IRDAI bancassurance rule added to sell triggers. |
| O12 | HDFC Bank staging and exit | **Accepted.** 6% of the sleeve; one-third now, rest only after Q3 FY27 (Jan 2027) if NIM ≥3.3% and no RBI MSRDC action; base exit 1.9x (base 16.5%/yr). |
| O13 | Bharti below hurdle; no prepaid hike | **Accepted.** 5% of the sleeve; top-up only after a headline prepaid tariff hike. |
| O14 | Maruti growth is a GST one-off | **Accepted.** 5%; buy only after Q2 (Oct 27) and only if EBITDA margin ≥9%; Eicher is the swap if not. |
| O15 | Apollo demerger | **Accepted.** 5%; re-underwrite when HealthCo/Apollo Healthtech terms are published (listing Q4 FY27). |
| O16 | Nothing wins in the bear | **Accepted.** ~3% of total in an Indian gold ETF. |
| O17 | Reserve inconsistent, no trigger | **Accepted.** One number: 12% of the India sleeve (9% of total) = gold 4% of sleeve (3% of total) + cash 8% of sleeve (6% of total). Trigger: deploy half if the Nifty closes ≤19,140 (−15% from 22,520) and the rest at ≤17,000, or into any holding −15% from cost whose thesis is intact. |
| O18 | LRS TCS timing; no trims <24 months | **Accepted.** If the global sleeve exceeds ₹10 lakh, global tranche 3 moves to after Apr 1, 2027 (second TCS-free limit). No discretionary trims of foreign names before 24 months; exits only on a sell trigger. |
| O19 | Medtronic estate-tax claim | **Accepted.** Medtronic shares are Irish-situs for Irish capital acquisitions tax; not a clean shelter. The UCITS ETF is the main estate-tax mitigant (adviser check). |
| O20 | Index core not considered | **Accepted.** Core-satellite adopted: Nifty 50 fund = 30% of the India sleeve; S&P 500 UCITS ETF = 19% of the global sleeve. Look-through Indian financials ~30% of total, set against an explicit cap of "index-neutral +3 pp" (75% × ~36% Nifty financials ≈ 27% + 3 = 30%). |

## 1. Bottom line
- **Structure:** 75% India / 25% global; each sleeve = index-fund core + 7–8 high-conviction satellites + (India) a reserve with gold.
- **Expected returns (30/50/20, pre-tax):** India sleeve ~12.9%/yr in INR (bear 2.2 / base 15.1 / bull 21.4) vs 11.3% for all-index; global sleeve ~13.3%/yr in USD (bear −3.1 / base 16.6 / bull 24.7) vs 10.4% for an all-S&P ETF, plus ~1–2%/yr expected INR drift for an Indian investor. **The stock-picking edge is small (~0–3 pp/yr) and uncertain; most of the expected return is market return.** Anyone who will not review annually should hold the index funds plus ICICI Bank and Microsoft and stop there.
- **Entry:** three tranches (Oct 2026 / Dec 2026 / Feb 2027 — global tranche 3 after Apr 1, 2027 if the sleeve > ₹10 lakh), with event gates per name (table below). Index funds and ungated names follow the calendar tranches.

## 2. India sleeve (75% of total)

| Name | Role | % of sleeve | % of total | Base / bear (%/yr) | Entry gate | Sell if |
|---|---|---|---|---|---|---|
| Nifty 50 index fund | Core (holds L&T, TCS, Infosys, SBI etc. at index weight) | 30 | 22.5 | 13.4 / 2.2 (all-index model) | Calendar tranches | — (core) |
| ICICI Bank | Best-run bank; beats index even on a flat multiple (14.7%) | 11 | 8.25 | 17.1 / 5.8 (anchor 2.6x) | Calendar tranches | ROE < 15% or NIM < 4% for 2 quarters |
| NTPC | Low-bear power ballast at 10.9x, 2.9% yield | 8 | 6 | 14.6 / 0.6 | Calendar | CERC FY29–34 draft (~mid-2028) cuts generation ROE |
| SBI Life | Financialisation at ~2.08x EV | 7 | 5.25 | 17.5 / 3.1 (EV +13.5%) | Only at ≤ ₹1,850 | VNB margin < 24%; adverse bancassurance rule |
| HDFC Bank | Crisis-level P/B; turnaround under new CEO | 6 | 4.5 | 16.5 / 2.2 (exit 1.9x) | 1/3 now; rest after Jan-2027 results if NIM ≥ 3.3% and no RBI MSRDC action | NIM < 3.2%; book-value hit from provisions |
| Reliance | Jio listing; conglomerate discount | 6 | 4.5 | 14.5 / −1.9 | After Jio listing (~Oct 28) and RIL Q2 | New export/windfall levies; Retail EBITDA keeps falling |
| Bajaj Finance | 20%+ grower, underwritten on a flat 29.5x | 5 | 3.75 | 19.5 (flat) / 2.2 | Half now; half after the final RBI revolving-credit rule | ROE < 18%; credit cost > 2.5% |
| Bharti Airtel | Tariff-led ARPU growth | 5 | 3.75 | 13.1 / −0.5 | Half now; top up only after a headline prepaid hike | No prepaid hike by end-2027 |
| Maruti Suzuki | Margin recovery in market leader | 5 | 3.75 | 14.9 / −3.0 | Only after Q2 (Oct 27) and only if EBITDA margin ≥ 9% (else Eicher) | Share < 38%; margin < 9% for 2 quarters |
| Apollo Hospitals | Hospital + pharmacy growth (~20%) | 5 | 3.75 | 15.4 / 1.6 | Calendar; re-underwrite on demerger terms | 24/7 losses widen; demerger terms dilutive |
| Indian gold ETF | Bear-scenario hedge | 4 | 3 | — | Calendar | — (hedge) |
| Cash reserve (T-bills/liquid fund, ~5.6–6.3%) | Drawdown ammunition | 8 | 6 | — | Deploy half at Nifty ≤ 19,140, rest at ≤ 17,000 | — |

Dropped vs v1: L&T and TCS (below hurdle; held via the index). Dropped vs the near-term list: SBI, Infosys (held via the index), L&T, TCS, Maruti kept but gated. Rejected on 3-yr valuation: Titan, Trent, Polycab, BEL, Hitachi Energy, Siemens, Dixon, Divi's, Max, Sun Pharma, HDFC AMC (~33–34x), Kalpataru (pledge). Alternates: HDFC Life, Eicher.
Look-through Indian financials: ~30% of total (direct 21.75% + ~8% via the Nifty fund) — cap "index-neutral +3 pp".

## 3. Global sleeve (25% of total) — all US-listed except the UCITS ETF

| Name | Role | % of sleeve | % of total | Base / bear (%/yr, USD) | Entry gate | Sell if |
|---|---|---|---|---|---|---|
| S&P 500 UCITS ETF (Irish-domiciled, CSPX/VUAA type) | Core; not US-situs for estate tax | 19 | 4.75 | 13.7 / −2.0 (same model) | Calendar | — (core) |
| Microsoft | The single AI-capex spender at its median multiple | 15 | 3.75 | 16.2 / ~−8 (3-yr −22%) | Calendar | Azure growth < 20% while capex rises; FCF negative 2 years |
| Visa + Mastercard (split 50/50) | Payments toll road | 14 | 3.5 | 14.8 / 0.7 | Calendar | Card-routing bill (CCCA) passes with debit/credit routing mandate |
| Intuit | AI-victim with ~14x GAAP earnings | 12 | 3 | ~15 flat-multiple (25.5 with re-rating) / −0.9 | After FQ1 (Nov 19) | Business-segment growth < 10% for 2 quarters; TurboTax revenue falls while buybacks are cut |
| Medtronic | Defensive ballast, 3% yield | 10 | 2.5 | 12.4 / −0.2 | Calendar | Organic growth < 5%; split-off outcome dilutive |
| Elevance | Managed-care recovery at ~13.6x 2027 | 9 | 2.25 | 13.4 / −3.0 | Only after Q3 (Oct 21) and a 2027 guide of ≥12% EPS growth | 2027 EPS growth < 8% |
| Amazon | AWS + retail; small because clean EPS unverified | 8 | 2 | ~14 at 26–27x / ~−8 (3-yr −22%) | Calendar | AWS growth < 15% while capex rises; FCF negative through 2028 |
| Netflix | Moderate value; ads + pricing | 8 | 2 | 18.3 / −2.8 | Only after Q3 (Oct 20) | Revenue growth < 8%; margin guide stalls |
| Uber | Show-me value vs robotaxi risk | 5 | 1.25 | 21.8 / −7.1 (conviction 2.5) | Calendar | Trip share falls in AV-direct cities; bookings growth < 12%; leverage > 2.5x |

AI-capex spenders (Microsoft + Amazon): 23% of the global sleeve; AI-disruption "victims" (Intuit): 12%.
Dropped vs v1: Alphabet (held via the ETF). Dropped vs near-term: TotalEnergies (tactical hedge only; gold now covers the bear), Adobe, TSMC (alternate below ~$360), UnitedHealth (alternate to Elevance).

## 4. Portfolio rules
- Position cap: no stock > 9% of total. Look-through Indian financials ≤ index-neutral +3 pp (~30%). AI-capex spenders ≤ ~23% of the global sleeve.
- Annual review (October): re-run the model; exit only on a sell trigger or if a name's base case falls below its index core for two consecutive reviews. No discretionary trims of foreign names before 24 months or Indian names before 12 months.
- Tax/LRS: keep each financial year's remittance near ₹10 lakh where possible (20% TCS above it, refundable); report foreign assets in Schedule FA; claim US dividend withholding credit on Form 67; US-situs total under ~$60k or take advice (the UCITS ETF and Medtronic are not US-situs, but Medtronic is Irish-situs for Irish CAT).
- Dated checkpoints: hyperscaler 2027 capex guides (Oct 2026–Feb 2027), Jan 10 2027 US–China truce, Feb 1 2027 Budget, RBI final revolving-credit rule, Bharti prepaid hike, HDFC Bank Q3 FY27 (Jan 2027), Apollo demerger terms, CERC FY29–34 approach paper (~mid-2028), US election Nov 7 2028, India election Apr–May 2029.

## 5. Corrections applied (from red-team §5)
SBI Life ₹1,769.55 (Sep 21), P/EV ~2.08x, Q1 APE boosted by group protection, SBI-channel individual APE +10%, VNB margin 26.3%; Microsoft FY27 capex ~$255–260B; Amazon 2027 consensus mean $10.47 (high $15.04) — clean EPS unverified; Medtronic ~$89–93, Irish-situs, split-off ratio 4.5939 (outcome pending); Intuit possibly $275.72 (Sep 26); Bharti — only a postpaid revision (Oct 8); Apollo demerger listing Q4 FY27, 24/7 not yet at breakeven; HDFC AMC ~33–34x; SBI Funds Management already listed (Jul 2026); HDFC Bank Q1 NIM 3.26% (post-merger low); Maruti growth = GST 2.0 step-change; Elevance MA 2027 rate +2.48%, Medicaid work requirements from 2027.
