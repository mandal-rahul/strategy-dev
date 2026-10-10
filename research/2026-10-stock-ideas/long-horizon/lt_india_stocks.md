# India equities for a 2–3 year hold (to about late 2029)

**As of:** Saturday 10-Oct-2026 (last session Fri 9-Oct-2026). **Investor:** India-resident; INR returns; Indian listed-equity tax (LTCG 12.5% above ₹1.25 lakh after 12 months; dividends at slab).
**Builds on:** `FINAL_RECOMMENDATIONS.md`, `REPORT.md`, `working/india_stocks.md`, `working/india_macro.md`, `working/contrarian_final.md` and `working/missed_opportunities.md` (all in `/home/user/strategy-dev/research/2026-10-stock-ideas/`). Figures already established there are reused with their original source and confidence. They were not searched again.
**Method caveats (for the red team):**
- 46 new WebSearch queries. WebFetch and finance sites are blocked, so **every figure is taken from a search-result summary of the cited URL. No page was opened.**
- Tags: **H** = several sources agree, or a filing. **M** = one credible source, or minor conflicts. **L** = stale, conflicting, undated, my own arithmetic (**calc**), or background knowledge not re-verified (**mem**).
- Several prices are 1–7 weeks old. They are flagged; check live quotes.
- No consensus database (Bloomberg/Visible Alpha) was reachable. "Consensus" means the best available broker or aggregator figure, named in each row. **Not investment advice.**

---

## 0. Bottom line

- **The shortlist has 11 names. In rank order: ICICI Bank, SBI Life, Bajaj Finance, HDFC Bank, NTPC, Apollo Hospitals, L&T, Reliance, Bharti Airtel, Maruti Suzuki and TCS.** Using the indicative weights in §3, the shortlist's base case is **~+59% over 3 years (~16.7%/yr)**. The bear case is +4% (1.4%/yr) and the bull case +97% (25.3%/yr). The probability-weighted outcome is ~15.7%/yr pre-tax.
- **Hurdle:** a Nifty 50 index fund on the same method gives a base of **~14.3%/yr**: EPS haircut to 11%/yr, P/E 18.3x→19.4x, 1.3% yield. Bear is 1.6%/yr and bull 19.5%/yr. **The shortlist's edge is only ~2–2.5 pp/yr, and most of it comes from four financials re-rating halfway back to their 5-year medians.** With multiples held flat, the shortlist base drops to ~14.4%/yr, which is the same as the index. Anyone who will not review the names yearly is close to as well served by an index fund.
- **Drop for the longer horizon:**
  - **SBI.** It trades at its own 5-year median P/E (~11x) with ROE drifting to ~15.5%, and ECL provisioning starts Apr-2027. Base ~10%/yr, below the index.
  - **Infosys.** It is the same AI-deflation factor as TCS, with weaker guidance. Base ~9%/yr.
- **Keep but resize:**
  - **TCS:** cut to a small diversifier. It is the only USD earner and the INR hedge, not a return engine.
  - **HDFC Bank:** add rather than trim. Three years gives the governance and CEO noise time to clear.
- **Add:**
  - **SBI Life:** P/EV ~2.0x on current EV versus ~2.5–3x history; EV +15%.
  - **Bajaj Finance:** ~29.5x trailing / ~19x FY28E for ~20%+ growth.
  - **Bharti Airtel:** ~22x FY28E; tariff-led ARPU path to ₹325 by FY29.
  - **Apollo Hospitals:** ~24% PAT CAGR forecast; promoter pledge cut to ~2.5% of equity.
- **Alternates (ranked high but not taken, to limit correlation):** HDFC Life (correlated with HDFC Bank and SBI Life), HDFC AMC (geared to market level), Eicher (data weak).
- **Still rejected on price for 3 years:** Titan, Trent, Polycab, BEL, Hitachi Energy, Siemens, Dixon, Divi's, Max Healthcare. For each, a reasonable de-rating cancels most of the ~15–25% earnings growth.

---

## 1. Summary table: all 26 candidates, ranked by risk-adjusted expected return

Returns are **3-year totals, pre-tax, in INR**, with the annualised figure in brackets. "Base g" is the EPS (or EV/book) CAGR I use after a consensus haircut (§2.2). **Ratio** = probability-weighted annual return ÷ half the bull–bear annual spread (a crude Sharpe proxy). ✅ = shortlisted.

| # | Name | Price (date, conf.) | Multiple now vs 5y median (basis) | EPS CAGR: consensus → base g | Yield | Base / Bear / Bull 3-yr TR (%/yr) | Ratio | Conv. |
|---|---|---|---|---|---|---|---|---|
| 1 ✅ | ICICI Bank | ₹1,354 (9-Oct, M) | 2.30x fwd P/B vs 2.95x 5y avg (−22%) | 16% → 14% | 0.8% | **+72% (19.9)** / +18% (5.8) / +108% (27.7) | 1.72 | 4 |
| 2 ✅ | SBI Life | ₹1,685 (**11-Sep, stale**, M) | 1.98x P/EV (Jun-26 EV) vs ~2.6x (L) (−24%) | EV +15% → 15% | 0.2% | **+77% (21.0)** / +18% (5.7) / +116% (29.4) | 1.68 | 3.5 |
| 3 ✅ | Bajaj Finance | ~₹960 (9-Oct, M) | 29.5x TTM vs 34.5x 5y median (−14%) | 23–24% → 19% | 0.6% | **+85% (22.8)** / +7% (2.2) / +120% (30.0) | 1.46 | 3.5 |
| 4 | HDFC Life (alternate) | ₹548 (7-Oct, M) | ~1.8x P/EV vs ~2.4x growth-adj. (raw ~3x) (L) | EV +13% → 12% | 0.4% | +65% (18.2) / +9% (3.0) / +115% (29.1) | 1.37 | 3 |
| 5 ✅ | HDFC Bank | ₹707.25 (9-Oct, H) | 1.70x fwd P/B vs 2.7–2.8x 5y avg; 2.4x growth-adj. (−29%) | 14–15% → 11% | 1.6% | **+70% (19.4)** / +7% (2.2) / +115% (29.0) | 1.36 | 3.5 |
| 6 ✅ | NTPC | ₹312.00 (9-Oct, H) | 10.9x TTM vs ~13.5x (−19%) | 7–10% → 8% | 2.9% | **+50% (14.6)** / +2% (0.6) / +74% (20.4) | 1.32 | 3 |
| 7 ✅ | Apollo Hospitals | ₹7,895 (7-Oct, M) | ~43x FY27E (calc) / ~53x TTM vs ~75x (L; distorted) | 24% → 20% | 0.25% | **+54% (15.4)** / +5% (1.6) / +92% (24.2) | 1.30 | 3 |
| 8 ✅ | Larsen & Toubro | ~₹3,703 (9-Oct, M) | 30.7x TTM vs 34.4x 5y / 27.0x 10y median | ~15–18% → 13% | 1.0% | **+48% (13.9)** / 0% (0.1) / +81% (21.9) | 1.19 | 3 |
| 9 ✅ | Reliance | ₹1,170.30 (9-Oct, H) | 21.2x TTM vs ~25x (L) (−15%) | ~11% PAT → 11% | 0.5% | **+50% (14.5)** / −6% (−1.9) / +76% (20.8) | 1.11 | 3 |
| 10 | HDFC AMC (alternate) | ₹2,252 (9-Oct, M) | ~30x TTM (calc) vs ~35–40x (L) | +12% → 12% | 2.3% (L) | +60% (17.0) / −4% (−1.4) / +111% (28.3) | 1.09 | 3 |
| 11 ✅ | Bharti Airtel | ₹1,779.90 (5-Oct, M) | 27.9x FY27E / 21.8x FY28E; 5y median not meaningful | ~28% FY27–28 → 18% | 0.9% (L) | **+45% (13.1)** / −2% (−0.5) / +86% (22.9) | 1.09 | 3.5 |
| 12 | Eicher Motors | ~₹7,513 (17-Sep, M) | ~35x TTM (calc, L) vs ~33x (L) | ~15% → 13% | 1.2% (L) | +44% (13.0) / −8% (−2.6) / +69% (19.1) | 1.03 | 3 |
| 13 ✅ | Maruti Suzuki | ~₹11,228 (9-Oct, M) | 25x TTM vs ~29x 5y (L) / 34x 10y (M) | ~13–20% → 11% | 1.2% | **+52% (14.9)** / −9% (−3.0) / +87% (23.1) | 1.01 | 3 |
| 14 | Bajaj Auto | ~₹11,720 (**5-Aug, stale**, M) | ~25x fwd vs ~19x (L) (+30%) | ~15% → 14% | 1.8% | +37% (10.9) / −6% (−2.0) / +67% (18.5) | 0.98 | 2.5 |
| 15 | Mahindra & Mahindra | ~₹3,095 (**17-Sep**, M) | 22.2x FY27E vs ~20x (L) | 14.5% → 13% | 0.8% | +40% (11.8) / −6% (−2.1) / +79% (21.3) | 0.97 | 3 |
| 16 | ITC | ~₹255–265 (8-Oct, L) | ~17x TTM (L) vs ~24x (L) | 5% → 4% | ~5.6% | +30% (9.1) / −6% (−2.0) / +66% (18.3) | 0.89 | 2.5 |
| 17 ✅ | TCS (diversifier) | ~₹2,156 (9-Oct, M) | ~14.2x fwd vs 28.4x 5y avg (−50%) | ~6–8% → 6% | 4.5% | **+33% (10.1)** / −3% (−1.0) / +106% (27.3) | 0.89 | 2.5 |
| 18 | Power Grid | ₹249.50 (9-Oct, M) | ~15x TTM vs ~12.5x (L) (+20%) | ~15% (stale) → 7% | 3.6% | +24% (7.4) / −6% (−2.1) / +45% (13.2) | 0.88 | 2 |
| 19 | SBI (drop) | ₹959.10 (9-Oct, H) | 11.1x FY26 vs 11.0x 5y median (in line) | 8–11% → 9% | 1.7% (L) | +34% (10.2) / −9% (−2.9) / +70% (19.4) | 0.88 | 2.5 |
| 20 | Infosys (drop) | ₹1,025.10 (9-Oct, H) | ~13.3x FY27E vs ~25x (L); 10y mean 22.4x (M) | ~6–8% → 5% | 4.7% | +31% (9.3) / −3% (−1.1) / +95% (25.0) | 0.88 | 2.5 |
| 21 | Max Healthcare | ~₹1,019 (**17-Aug**, M) | ~66x TTM / ~52x FY27E (L) | ~25% → 20% | 0.15% | +40% (11.9) / −13% (−4.5) / +88% (23.5) | 0.83 | 2.5 |
| 22 | Trent | ₹2,867 (6-Oct, M) | ~70x FY27E (calc) vs >100x (L) | ~22–25% → 22% | 0.1% | +43% (12.7) / −15% (−5.3) / +91% (24.0) | 0.82 | 2.5 |
| 23 | Polycab | ₹8,255 (9-Oct, M) | ~43x TTM vs ~38x (L) | 18% → 17% | 0.45% | +32% (9.7) / −15% (−5.2) / +74% (20.4) | 0.73 | 2 |
| 24 | Titan | ₹4,365 (7-Oct, M) | ~62x FY27E (calc) vs ~85x (L) | ~20%+ → 17% | 0.3% | +30% (9.2) / −15% (−5.4) / +77% (20.9) | 0.70 | 2.5 |
| 25 | Sun Pharma | ₹1,760 (9-Oct, M) | 34.7x TTM vs ~33x (L) | 11% + Organon → 13% | 1.0% | +28% (8.6) / −17% (−5.9) / +69% (19.2) | 0.66 | 2 |
| 26 | Bharat Electronics | ~₹386 (17-Sep, M) | ~40x FY27E (calc) vs ~33x (L) | ~15% → 14% | 0.7% | +21% (6.5) / −17% (−5.9) / +67% (18.6) | 0.58 | 2 |
| — | **Nifty 50 (hurdle)** | 22,520 (9-Oct, M) | 18.3x FY27E vs ~20.5x long-run fwd avg | ~15–16% → 11% | 1.3% | **+49% (14.3)** / +5% (1.6) / +70% (19.5) | — | — |

Quick rejects (no full model; reasons in §7): Hitachi Energy India, Siemens, Dixon, KEI, Divi's, Tata Power, Coal India, HUL, Kotak Bank, CDSL/BSE, Kalpataru Projects.

---

## 2. Method

### 2.1 Formula
For each name and each scenario:

`3-yr total return = (1 + g)^3 × (M_exit / M_now) − 1 + y × [1 + (1+g) + (1+g)^2]`

- **g:** EPS CAGR. For banks it is the book-value CAGR; for life insurers, the embedded-value (EV) CAGR.
- **M:** the valuation multiple. Banks use forward P/B, insurers P/EV on the latest EV, everyone else P/E, on the stated basis.
- **y:** the current dividend yield, assumed to grow with EPS and not reinvested.
- **Scenario weights:** bear 25%, base 50%, bull 25%.
- **Multiple rule, stated per name:**
  - **Base:** the multiple reverts halfway to its 5-year median.
  - **Exceptions, explained where used:**
    - The 5-year median is a 2021–24 liquidity-era anchor I do not believe will return (Titan, Trent, Apollo, Max, BEL, Polycab, Bajaj Auto). Here the base is a **de-rating**.
    - Growth has structurally halved versus the median period (TCS, Infosys). Here the base is **flat**.
    - No meaningful median exists (Bharti, which had depressed earnings). Here the base is a modest de-rating.
  - **Bear:** roughly −15% to −35% versus today. **Bull:** full reversion to the median, or flat for de-rating names.
- **Post-tax:** for the shortlist I also show the base annualised after 12.5% LTCG on the price gain and ~31.2% slab tax (30% + cess) on dividends. This ignores the ₹1.25 lakh exemption and surcharge. High-yield names (TCS, ITC, Infosys) lose the most.
- The calculation scripts are in the scratchpad, at `scripts/lt_returns.py` and `scripts/lt_extra.py`.

### 2.2 Why base g sits below consensus (forecast-cut evidence)
- **Indian consensus has a persistent optimism bias.**
  - Since 2014, 6–12-month-forward consensus for the Sensex/BSE 500 **overestimated actual earnings by at least 10%**, and the gap reached 25% in some years. Consensus under-predicted only three times in 40 quarters ([Bloomberg Quint opinion, undated, M](https://www.bloombergquint.com/opinion/why-are-consensus-earnings-estimates-often-off-the-mark-)).
  - FY14–17 saw 10–27% downgrades, and FY18 began with a ~40% cut for Nifty companies ([Business Standard 2017, M](https://www.business-standard.com/amp/article/markets/fy18-starts-with-big-earnings-cut-117032600716_1.html)).
  - MSCI India forward EPS was cut for a sixth straight year to 2019 ([BS 2019, M](https://www.business-standard.com/amp/article/markets/from-maruti-to-asian-paints-india-inc-earnings-see-further-downgrades-119072800723_1.html)).
- **It is happening now.** FY27 Nifty EPS has been cut ~9% over the past year, from ~₹1,357 to ₹1,232 (JM via [5paisa](https://www.5paisa.com/news/nifty-fy27-earnings-estimates-trimmed-9-despite-persistent-downgrade-trend), M; carried from india_macro.md).
- **Rule I applied.** I cut 2–5 pp a year off consensus growth for cyclicals and high-expectation names (Maruti, L&T, Bajaj Finance, Bharti, Apollo, HDFC Bank). I cut 0–2 pp for regulated or steady names (NTPC, SBI, TCS, SBI Life). Every row shows both numbers.

### 2.3 The 2027–29 risk set used throughout
- **RBI tightening.** Repo is 5.50% after the 7-Oct hike, with guidance of "only a hike or a pause" (H). The 10-year G-sec is 7.28% (M).
- **Fiscal capex cuts.** ICRA expects the FY27 deficit to overshoot by ₹0.9–1.4 trn (M).
- **Oil and war.** Brent is ~$102–106 and the Iran war is active (M).
- **AI deflation** of IT services.
- **Monsoon.** It ended 12.6% deficient, the worst since 2015, with El Niño persisting (M).
- **Bank ECL accounting from 1-Apr-2027.** CRISIL estimates a CET1 hit of up to 120 bp, phased (H).
- **2029 general election.** The Lok Sabha term ends mid-2029, so voting falls ~Apr–May 2029, inside the holding window (mem, H). The likely effects:
  - pre-election fuel-price and tariff restraint;
  - a soft quarter or two of ordering under the model code of conduct;
  - a policy-continuity risk for PSUs.
- **CERC's next tariff regulations (FY2029–34)** fall inside the window. In the 2024 draft, generation ROE stayed at 15.5% and transmission ROE was trimmed to 15% ([Powerline Feb-24, M](https://powerline.net.in/2024/02/05/roe-adjustments-key-highlights-of-cercs-draft-tariff-regulations/)). I found no 2029–34 consultation yet (L).

---

## 3. Ranked shortlist (hold 2–3 years)

| Rank | Name | Thesis (one line) | 3-yr base / bear / bull (%/yr) | Base after tax | Monitor yearly | Sell if | Conv. | Indicative wt |
|---|---|---|---|---|---|---|---|---|
| 1 | **ICICI Bank** | Best-run large bank. ~17% ROE and ~14% book growth at 2.3x fwd book vs 2.95x 5y avg. | +72 / +18 / +108 (19.9 / 5.8 / 27.7) | 17.6%/yr | ROE ≥16%; NIM ≥4.1%; unsecured-retail slippages | ROE <15% for 2 years, or fwd P/B >3.3x (take profit) | 4 | 12% |
| 2 | **SBI Life** | ~15% EV compounder with SBI's branch reach, at ~2.0x current EV (1.8x FY27E) vs 3.0x in Jan-26 | +77 / +18 / +116 (21.0 / 5.7 / 29.4) | 18.8%/yr | EV growth; VNB margin (guide 26–28%) | VNB margin <24% (commission caps) or EV growth <11% for 2 years | 3.5 | 8% |
| 3 | **Bajaj Finance** | India's best consumer-credit franchise. AUM +26.5%, ROE ~20%, at ~19x FY28E | +85 / +7 / +120 (22.8 / 2.2 / 30.0) | 20.3%/yr | AUM growth; credit cost; final RBI revolving-credit rule | Credit cost >2.5%, or an RBI embargo, or ROE <17% | 3.5 | 7% |
| 4 | **HDFC Bank** | Largest private bank at ~1.7x fwd book. Deposits now outgrow loans; CEO change done | +70 / +7 / +115 (19.4 / 2.2 / 29.0) | 17.1%/yr | Deposit vs loan growth; CASA; ROA path to ≥1.9% | RBI enforcement on MSRDC/governance, or FY28 ROA <1.7% | 3.5 | 10% |
| 5 | **NTPC** | Regulated-equity compounder (35.7 GW under construction) at 10.9x vs ~13.5x, 2.9% yield | +50 / +2 / +74 (14.6 / 0.6 / 20.4) | 12.5%/yr | GW commissioned a year; regulated equity; CERC 2029–34 draft | CERC cuts generation ROE below ~14.5%, or PAT growth <5% for 2 years | 3 | 8% |
| 6 | **Apollo Hospitals** | Integrated hospitals + pharmacy; ~24% PAT CAGR forecast; HealthCo breakeven is near | +54 / +5 / +92 (15.4 / 1.6 / 24.2) | 13.6%/yr | Hospital occupancy and ARPOB; HealthCo EBITDA; promoter pledge | HealthCo still loss-making in FY28, or pledge >10% of the promoter holding | 3 | 6% |
| 7 | **L&T** | India's capex proxy with a ₹7.79 lakh cr order book, at 30.7x, between its 5y (34.4x) and 10y (27x) medians | +48 / 0 / +81 (13.9 / 0.1 / 21.9) | 12.2%/yr | Order inflow; core margin (guide ~8.3%); Gulf receivables | Gulf write-offs or cancellations; core margin <7.5% in FY28 | 3 | 8% |
| 8 | **Reliance** | Jio + Retail + O2C at 21x vs ~25x; the Jio listing gives a mark-to-market | +50 / −6 / +76 (14.5 / −1.9 / 20.8) | 12.8%/yr | Jio ARPU and listed value; O2C levies; new-energy capex returns | Holdco discount persists and capex flows to new energy without returns; EPS growth <6% | 3 | 9% |
| 9 | **Bharti Airtel** | Duopoly-ish telecom; ARPU ₹264→₹325 (FY29, HSBC) drives ~20%+ EPS growth; ~22x FY28E | +45 / −2 / +86 (13.1 / −0.5 / 22.9) | 11.4%/yr | India mobile ARPU; FCF; net debt/EBITDA | No headline tariff hike by end-2027, or FY28 ARPU <₹290 | 3.5 | 8% |
| 10 | **Maruti Suzuki** | Volume recovery (+28% H1 FY27) at trough margins (8.2%); 25x vs 34x 10y median | +52 / −9 / +87 (14.9 / −3.0 / 23.1) | 13.1%/yr | EBITDA margin back ≥10%; domestic PV share ≥40% | FY28 margin <9%, or share <38% | 3 | 8% |
| 11 | **TCS** | Diversifier: USD earner and INR hedge; ~14x fwd; ~4.5% yield; AI-fear optionality | +33 / −3 / +106 (10.1 / −1.0 / 27.3) | 8.2%/yr | CC revenue growth; TCV ≥$8 bn/qtr; EBIT margin ≥24% | CC revenue down y/y for 2 years, or margin <22% | 2.5 | 6% |
| — | **Reserve** | Indian T-bills / liquid fund (~5.6–6.3%) to stage entries around Q2 results | — | — | — | — | — | 10% |

- **Portfolio math** (weights above, renormalised to the 90% invested):
  - Base +59% (16.7%/yr), bear +4% (1.4%/yr), bull +97% (25.3%/yr), probability-weighted ~15.7%/yr.
  - With all multiples flat, the base is +50% (14.4%/yr).
- **Concentration:** financials (ICICI, HDFC Bank, SBI Life, Bajaj Finance) are ~41% of invested money, about the Nifty's own financials weight. The four share one factor: RBI rates and liquidity.
- **Ordering rule:** ranks follow the ratio column, with two exceptions:
  - HDFC Life and HDFC AMC are skipped as correlated alternates.
  - TCS is kept below its rank as the only hedge for INR and domestic slowdown.

---

## 4. Drop and add versus the near-term list (FINAL_RECOMMENDATIONS.md)

| Near-term name | 3-year verdict | Why |
|---|---|---|
| ICICI Bank | **Keep, #1** | Highest risk-adjusted return. Even with multiples flat it compounds ~14.7%/yr. |
| HDFC Bank | **Keep, raise weight** | 3 years outlasts the Jan-2027 kitchen-sink risk. Base 19.4%/yr, but 28 pp of the 3-year base comes from re-rating; flat multiple gives 12.4%/yr. |
| SBI | **Drop** | Already at its 5y median P/E (11.0x vs 11.1x). ROE guided toward ~15.5% (MOSL). Deposits +9.7% vs loans +18.6%. ECL from Apr-27. Pre-election PSU directed-lending risk. Base 10.2%/yr is below the index. |
| TCS | **Keep, small (diversifier)** | Base only ~10%/yr (8.2% post-tax: the dividends are slab-taxed). Kept for its low correlation with the domestic rate and oil risks. |
| Infosys | **Drop** | Same factor as TCS, with a guidance cut expected 23-Oct and lower margins. Base 9.3%/yr. |
| NTPC | **Keep** | A credible 8% compounder at ~19% below its 5y P/E. The new 3-year risk is the CERC FY29–34 tariff reset. |
| Reliance | **Keep** | Jio/Retail growth and holdco-discount narrowing. Event-heavy near term, irrelevant at 3 years. |
| Maruti | **Keep** | Trough margins and strong volumes. Eicher (ratio 1.03) and M&M (0.97) are alternates. |
| L&T | **Keep** | Only fairly priced capex play. Base 13.9%/yr, roughly index-like. Its role is diversification into private capex. |
| — | **Add SBI Life** | Financialisation and the protection gap. The multiple collapsed (3.0x→~2.0x P/EV) while EV grew 15%. Must confirm the live price is ≤ ~₹1,850. |
| — | **Add Bajaj Finance** | Rejected near-term over the RBI revolving-credit draft. Over 3 years, ~20% growth at ~19x FY28E outweighs a rule that hits ~15% of AUM. |
| — | **Add Bharti Airtel** | Rejected near-term on a ~70x trailing P/E, which is the wrong lens. On FY28E it is ~22x with visible ARPU growth. |
| — | **Add Apollo Hospitals** | Not screened before. A healthcare compounder whose pledge overhang was cleared in 2025. |

---

## 5. Sensitivity to the 2027–29 risks (shortlist)

Key: **H** = high, **M** = medium, **L** = low; "+" = beneficiary. The 2029 election can delay telecom tariff hikes and fuel-price pass-through.

| Name | RBI tightening | Fiscal capex cut | Oil/war >$100 | AI deflation | Weak monsoon | 2029 election |
|---|---|---|---|---|---|---|
| ICICI Bank | M (NIM flat; asset quality) | L | M | L | L–M (rural retail) | L |
| SBI Life | **H** (bond yields hit EV; new-business yields +) | L | M | L | L | M (tax/GST policy) |
| Bajaj Finance | **H** (funding cost, regulation) | L | M | L | M (rural B2C) | M (loan-waiver culture) |
| HDFC Bank | M | L | M | L | L–M | L |
| NTPC | M (bond-proxy multiple) | L (funded internally) | L / + (power demand) | + (data-centre load) | + (hot, dry = demand) | M (discom dues, CERC) |
| Apollo | L | L | L | L | L | L–M (price caps) |
| L&T | M | **H** (domestic govt orders) | **H** (Gulf ~37–40% of book) | M (LTIMindtree) | L | M (ordering lull) |
| Reliance | L | L | **H** (export duty/windfall) | L | L–M (retail) | **H** (fuel-price populism) |
| Bharti | L–M (debt) | L | L | L | L | M (hikes avoided pre-poll) |
| Maruti | M (auto loans) | L | **H** (fuel, commodities) | L | **H** (rural/small cars) | L–M |
| TCS | L | L | + (weaker INR) | **H** | L | L |

---

## 6. One section per candidate

### 6.1 ICICI Bank (NSE: ICICIBANK). ✅ Rank 1, conviction 4

**Price and valuation**
- **Price:** ~₹1,354 (9-Oct, M; [Screener snippet](https://www.screener.in/company/ICICIBANK/consolidated/) via india_stocks.md). The 52-week high is ₹1,480 or ₹1,547; sources conflict (M).
- **BVPS:** ₹530.53 (Jun-26) ([GuruFocus](https://www.gurufocus.com/term/book-value-per-share/NSE:ICICIBANK), M), so trailing P/B is 2.55x (calc).
- **Forward P/B:** 2.30x on Mar-27E BVPS of ~₹588 (calc, L).
- **History:** 5-year average forward P/B is **2.95x** ([Seeking Alpha via search, Mar-26](https://seekingalpha.com/symbol/IBN/valuation/metrics), M). The 13-year median is 2.89x ([GuruFocus](https://www.gurufocus.com/term/book-value-per-share/NSE:ICICIBANK), M).

**Growth**
- **Q1 FY27:** PAT +15.9%, NIM 4.36%, GNPA 1.38%, CET1 16.19% (H, [DSIJ](https://insights.dsij.in/dsijarticledetail/icici-bank-q1-fy27-results-net-profit-rises-16-yoy-to-rs-14805-crore-asset-quality-improves)).
- **Consensus proxy:** MOSL expects 16% PAT CAGR and ~16% loan CAGR over FY26–28 ([Business Today 5-Jun-26](https://www.businesstoday.in/amp/markets/stocks/story/icici-bank-is-mofsls-top-banking-pick-with-39-upside-potential-heres-why-535038-2026-06-05); [Multibagg](https://www.multibagg.ai/market-pulse/articles/icici-bank-motilal-target-price-cmpyv9k4fis5qnz0j9ral6vv0); M). Anand Rathi's target is ₹1,746, at 2.5x FY28E core adjusted book ([DSIJ](https://insights.dsij.in/markets/reports/report-details/icici-bank-ltd/44570), M).

**Inputs by scenario**

| | g (book) | Exit fwd P/B | 3-yr total (a year) |
|---|---|---|---|
| Base | 14% | 2.63x (halfway to 2.95x) | +72% (19.9%) |
| Bear | 10% | 2.0x | +18% (5.8%) |
| Bull | 17% | 2.95x | +108% (27.7%) |

- **Yield:** 0.8% (L).
- **With a flat multiple:** 14.7%/yr. Only ~21 pp of the 3-year base comes from re-rating.

**Durability**
- **Moat:** low-cost liabilities, risk culture and technology.
- **Governance:** no promoter.
- **Succession:** the RBI reportedly approved a two-year extension for CEO Sandeep Bakhshi ([search result on mirrored sites, 22-May-26](https://www.mycpd2.moh.gov.my/first-dry/RBI-Approves-ICICI-Bank-CEO-Sandeep-Bakhshis-Reappointment-for-Two-More-Years-21-1104), **L**). **CEO succession therefore falls around late 2028, inside the window.** The bench is deep, but HDFC Bank just hired Anup Bagchi from the ICICI group.
- **Balance sheet:** strongest capital ratios among large banks.
- **Risks:** ECL from Apr-27 (low impact given provisions; mem L); unsecured-retail cycle; deposit repricing after the hike.

### 6.2 SBI Life Insurance (NSE: SBILIFE). ✅ Rank 2, conviction 3.5

**Price and valuation**
- **Price:** ₹1,684.70 on **11-Sep-26 (stale)**, at its 52-week low of ~₹1,671. The 52-week high is ₹2,132 ([5paisa](https://www.5paisa.com/blog/sbi-life-insurance-stock-update-11-sep-26), M). Another aggregator shows ₹1,761 (undated) ([Fyers](https://fyers.in/stocks/sbi-life-insurance-company-ltd?tabs=news), L). **Verify before buying.**
- **EV:** ₹85,290 cr (Jun-26, +15%). On ~100.2 cr shares (L), P/EV is **1.98x on current EV** (calc). Nuvama has **1.8x FY27E / 1.5x FY28E** and a target of ₹2,600 ([BT 8-Sep-26](https://www.businesstoday.in/markets/stocks/story/sbi-life-hdfc-life-max-financial-ipru-shares-check-target-prices-outlook-553837-2026-09-08), M).
- **History:** 3.0x FY25A EV in Jan-26 and 2.3x in Apr-26 ([BOBCAPS](https://www.barodaetrade.com/Reports/Insurance-Q3FY26Preview8Jan26-Research.pdf), M). I use a 5-year median of **~2.6x (L)**; no decade series was found.

**Growth**
- **Q1 FY27:** APE ₹5,380 cr (+36%), VNB ₹1,410 cr (+29%), VNB margin 26.2%. FY27 guide: individual APE +14–15%, margin 26–28% (M, [DSIJ/MOSL](https://insights.dsij.in/markets/reports/report-details/sbi-life-insurance-company-ltd/44654)).
- **Broker targets:** PL ₹2,200, MOSL ₹2,240, GS ₹2,235 (early Sep-26, M) ([Fyers news](https://fyers.in/stocks/sbi-life-insurance-company-ltd?tabs=news)).

**Inputs by scenario**

| | EV growth | Exit P/EV | 3-yr total (a year) |
|---|---|---|---|
| Base | 15% | 2.30x | +77% (21.0%) |
| Bear | 11% | 1.70x | +18% (5.7%) |
| Bull | 18% | 2.60x | +116% (29.4%) |

- **Yield:** ~0.2%.
- **With a flat multiple:** 15.2%/yr.

**Durability**
- **Moat:** captive SBI bancassurance (~22,000 branches; mem L) and the lowest cost ratio among listed private insurers (mem L).
- **Governance:** SBI owns ~55% (L). Related-party dependence on SBI for distribution is both the moat and a risk.
- **Regulation:** commission caps, surrender-value rules, and the loss of input tax credit after the GST exemption (~100 bp margin drag, M).
- **Rates:** rising yields hit EV through mark-to-market. New-business yields gain.
- **Concentration:** overlaps the bank factor. HDFC Life is the fallback.

### 6.3 Bajaj Finance (NSE: BAJFINANCE). ✅ Rank 3, conviction 3.5

**Price and valuation**
- **Price:** ~₹960 (9-Oct, M, india_stocks.md). The 52-week range is ₹1,178 / ₹788. The stock was ~₹1,086–1,094 in early August ([Angel One](https://www.angelone.in/news/stocks/why-did-bajaj-finance-share-price-fall-nearly-6-percent-today-aug-7-2026), M).
- **EPS:** TTM ₹32.57 ([GuruFocus, Aug-26](https://www.gurufocus.com/term/pe-ratio/NSE:BAJFINANCE), M), so **29.5x TTM** (calc). FY26 EPS ₹30.58 ([Fyers](https://fyers.in/stocks/bajaj-finance-ltd/profit-loss), M).
- **History:** 5-year median P/E **34.5x** and P/B 5.87x ([MoneyWorks4Me, undated](https://www.moneyworks4me.com/check-before-you-invest/bajfinance), M/L). The 10-year median is 42.5x (GuruFocus, M).
- **Forward:** FY28E P/E is 19.9x at ₹999 ([MarketScreener](https://in.marketscreener.com/quote/stock/BAJAJ-FINANCE-LIMITED-33647061/valuation/), L), which implies FY28E EPS of ~₹50.

**Growth**
- **Q2 FY27 provisional AUM:** ₹5.85 lakh cr, **+26.5%** ([Indmoney](https://www.indmoney.com/blog/stocks/why-bajaj-finance-share-price-is-rising-q2-update), M).
- **Guidance:** AUM +23–25%, PAT +23–24%, ROE 19–21% (india_stocks.md, M).

**Inputs by scenario**

| | g | Exit P/E (TTM) | 3-yr total (a year) |
|---|---|---|---|
| Base | 19% | 32x (halfway) | +85% (22.8%) |
| Bear | 12% | 22x | +7% (2.2%) |
| Bull | 23% | 34.5x | +120% (30.0%) |

- **Yield:** 0.6%.

**Durability**
- **Moat:** data, distribution (97.7 mn EMI cards) and cost of funds (AAA).
- **Regulatory risk is the main risk.**
  - The RBI's draft (7-Aug-26) would bar NBFCs from revolving credit, which is ~15% of AUM. It is still only a draft ([Indmoney](https://www.indmoney.com/blog/stocks/why-bajaj-finance-share-fell-rbi-proposal); [IIFL via search](https://www.kotakneo.com/news/regulations/bajaj-finance-shares-falls-after-rbi-nbfc-proposal/), M).
  - There is history of an RBI embargo (Nov-2023, lifted 2024; mem L).
- **Governance:** Bajaj group; clean, but key-person risk (mem L).
- **Rates:** RBI tightening raises funding costs.

### 6.4 HDFC Bank (NSE: HDFCBANK). ✅ Rank 4, conviction 3.5

**Price and valuation**
- **Price:** ₹707.25 (9-Oct, H; [5paisa](https://www.5paisa.com/stocks/hdfcbank-share-price)).
- **P/B:** standalone BV is ₹367–378 (Mar-26) ([BOBCAPS](https://www.barodaetrade.com/Reports/HDFCBank-Q4FY26ResultReview19Apr26-Research.pdf); [Fyers](https://fyers.in/stocks/hdfc-bank-ltd/profit-loss); M), so trailing P/B is ~1.87–1.93x and **forward P/B ~1.70x** on Mar-27E BV of ~₹417 (calc, L).
- **History:** 5-year average P/B 2.7–2.8x ([AlphaSpread](https://www.alphaspread.com/security/nse/hdfcbank/relative-valuation/ratio/price-to-book-value); [Finbox](https://finbox.com/NSEI:HDFCBANK/explorer/price_to_book/); M). I use **2.4x "growth-adjusted"**, because post-merger ROE is ~14% against the higher pre-merger level (L).

**Growth**
- **Consensus:**
  - MOSL: 14.2% earnings CAGR FY26–28.
  - Emkay: +15% FY27 and +20% FY28 ([BS Dec-25](https://www.business-standard.com/markets/news/hdfc-bank-share-price-to-re-rate-outperform-icici-bank-stock-by-fy28-emkay-lists-4-reasons-125121100321_1.html), M).
  - Aggregator FY27E EPS ₹54.47, +12.5% ([sharpely](https://sharpely.in/stocks/hdfcbank/forecast), L).
- **But Q1 FY27 PAT grew only +5%** and NIM is 3.26% (H). My base is therefore 11%.
- **Q2 business update:** deposits +18.8% vs advances +16.3% (M).

**Inputs by scenario**

| | g | Exit fwd P/B | 3-yr total (a year) |
|---|---|---|---|
| Base | 11% | 2.05x | +70% (19.4%) |
| Bear (kitchen sink or RBI action) | 6% | 1.45x | +7% (2.2%) |
| Bull | 14% | 2.4x | +115% (29.0%) |

- **Yield:** ~1.6% (L).
- **With a flat multiple:** 12.4%/yr. This is the most re-rating-dependent name.

**Governance (unresolved)**
- **MSRDC case:** the board fined and warned the CEO, CFO and retail head, and the RBI sought an explanation.
- **SDNY class action:** *Soneji v. HDFC Bank*, 26-cv-06943.
- **Leadership:** the chairman resigned in Mar-26. The new CEO, Anup Bagchi, starts 27-Oct-26 on a term to 26-Oct-2029 (H, via redteam_round1.md and contrarian_final.md).
- **The 3-year horizon is the point:** the new CEO's first full-year numbers (FY28) arrive mid-window.

### 6.5 NTPC (NSE: NTPC). ✅ Rank 5, conviction 3

**Price and valuation**
- **Price:** ₹312.00 (9-Oct, H; [ad-hoc-news](https://www.ad-hoc-news.de/boerse/news/corporate-news/ntpc-stock-stands-at-inr-312-00-with-inr-3-0-trillion-market-value/70280018)).
- **P/E:** 10.9x TTM vs a 5-year average of 13.3–13.7x ([Trendlyne](https://trendlyne.com/tools/buy-sell-zone/959/NTPC/ntpc-ltd/); [Eulerpool](https://eulerpool.com/stock/NTPC-Stock-INE733E01010/pe); M).
- **Yield:** 2.9% on ₹9 DPS.

**Growth**
- **Consensus:** EPS CAGR FY26–28 of 7% (PL, standalone), 9.4% (Nuvama, consolidated) and 10.2% PAT (HDFC Sec) ([PL Jul-26](https://www.plindia.com/pl-research/ntpc-ntpc-in-q1fy27-result-update-healthy-q1-plan-laid-out-until-fy37-buy/); [DSIJ](https://insights.dsij.in/markets/reports/report-details/ntpc-ltd/45163); [HDFC Sky](https://hdfcsky.com/news/ntpc-ltd-selected-as-hdfc-securities-pick-of-the-week-on-strategic-growth-and-renewable-expansion); M).
- **Targets:** ₹370–450 (I-Sec ₹405 at 14x FY28E base; Geojit ₹419; MOSL Neutral ₹381; M).
- **Pipeline:** 35.7 GW under construction (H).

**Inputs by scenario**

| | g | Exit P/E | 3-yr total (a year) |
|---|---|---|---|
| Base | 8% | 12.2x (halfway) | +50% (14.6%) |
| Bear (CERC ROE trim, slower commissioning, higher rates) | 4% | 9x | +2% (0.6%) |
| Bull | 10% | 13.5x | +74% (20.4%) |

**Durability**
- **Moat:** regulated ROE on a large base. Capex is funded internally, so fiscal-cut risk is low.
- **Governance:** state-owned; dividend policy is set by government needs; directed renewable and nuclear capex.
- **Risks within the window:** the **CERC FY2029–34 tariff regulations**, thermal ESG de-rating, discom payment delays.

### 6.6 Apollo Hospitals (NSE: APOLLOHOSP). ✅ Rank 6, conviction 3

**Price and valuation**
- **Price:** ₹7,895 (7-Oct-26) on a 52-week range of ₹6,680–9,326.80 ([Anand Rathi](https://anandrathi.com/stocks/apollo-hospitals-enterprise-ltd/share-price-today), M).
- **P/E:** 59.08x at ₹8,805.5 on 28-Aug, which scales to **~53x TTM** at today's price (calc, L). That implies TTM EPS of ~₹149 and **~43x FY27E** (calc, L).
- **History:** the 5-year median P/E is ~75x (mem, L). It is distorted by HealthCo losses, so I do not use reversion.

**Growth**
- **Forecasts:** Antique expects revenue, EBITDA and PAT CAGRs of 16%, 20% and **24%** over FY26–28E (target ₹9,790). Choice expects 24.4% PAT CAGR over FY26–29E ([BT 29-Jun-26](https://www.businesstoday.in/markets/stocks/story/apollo-hospitals-medanta-healthcare-global-max-healthcare-artemis-medicare-check-target-prices-outlook-539782-2026-06-29); [Investment Guru/Choice](https://investmentguruindia.com/newsdetail/buy-apollo-hospitals-ltd-for-the-target-rs-9-600-by-choice-institutional-equities110271); M).
- **Other targets:** PL ₹10,000 (25% EBITDA CAGR; 14-Aug-26) and I-Sec ₹10,170 ([DSIJ](https://insights.dsij.in/markets/reports/report-details/apollo-hospitals-enterprise-ltd/45228), M).
- **HealthCo:** breakeven guided for Q2 FY27 (M).

**Inputs by scenario**

| | g | Exit fwd P/E | 3-yr total (a year) |
|---|---|---|---|
| Base | 20% | 38x (a de-rating) | +54% (15.4%) |
| Bear | 13% | 31x | +5% (1.6%) |
| Bull | 24% | 43x | +92% (24.2%) |

- **With a flat multiple:** 20.2%/yr. The base already assumes a −12% de-rating.

**Governance**
- **Pledge:** the promoter group sold 1.3% in Aug-25 to cut debt. Pledged shares fell from 8.57% of equity (Sep-25) to **2.49% (Dec-25 and Mar-26)** ([Outlook Business](https://www.outlookbusiness.com/corporate/apollo-hospitals-promoter-group-offloads-13-stake-for-1489-cr); [Emkay EOD](https://www.emkayglobal.com/news-details/eod/4735456); M).
- **Promoter holding:** ~28%.
- **Complexity:** HealthCo/Keimed restructuring and Advent's stake.

**Risks:** price controls on procedures and consumables; doctor-cost inflation; execution on bed additions.

### 6.7 Larsen & Toubro (NSE: LT). ✅ Rank 7, conviction 3

**Price and valuation**
- **Price:** ~₹3,703 (9-Oct, M).
- **EPS:** TTM ~₹120.7 (calc), so **30.7x**. FY26 EPS ₹116.88 ([Craytheon](https://craytheon.com/stocks/larsen-and-toubro/growth/), M).
- **History:** 5-year median 34.4x ([Craytheon](https://craytheon.com/stocks/larsen-and-toubro/), M); 10-year median 27.0x ([GuruFocus](https://www.gurufocus.com/term/pe-ratio/NSE:LT), M). Today sits between the two, so the **base multiple is flat**.

**Growth**
- **Guidance:** order inflow and revenue +10–12%.
- **Order book:** ₹7.79 lakh cr (+27%). The Middle East is **~37–40% of the book** (M).
- **Broker views:**
  - May-26 broker: 25x 2-year-forward core, target ₹4,550, FY27 cut and a stronger FY28 ([BS PDF](https://bsmedia.business-standard.com/_media/bs/data/market-reports/equity-brokertips/2026-05/17780470020.93697100.pdf), M).
  - MOSL (Nov-25, pre-war): 22% PAT CAGR FY25–28 ([BS](https://www.business-standard.com/amp/markets/news/l-t-gains-2-hits-new-high-brokerages-see-more-upside-in-stock-price-125112600384_1.html), L, stale).

**Inputs by scenario**

| | g | Exit P/E | 3-yr total (a year) |
|---|---|---|---|
| Base | 13% | 30.7x (flat) | +48% (13.9%) |
| Bear | 6% | 25x | 0% (0.1%) |
| Bull | 17% | 34x | +81% (21.9%) |

- **Yield:** 1.0%.

**Durability**
- **Moat:** execution franchise.
- **Governance:** no promoter; clean.
- **Look-through:** LTIMindtree (AI factor) and L&T Tech.
- **Balance sheet:** fine.
- **Risks:** Gulf receivables; pre-2029-election ordering lull.

### 6.8 Reliance Industries (NSE: RELIANCE). ✅ Rank 8, conviction 3

**Price and valuation**
- **Price:** ₹1,170.30 (9-Oct, H). TTM EPS ₹55.2 gives **21.2x** (M). Kotak Neo's forward P/E is 19.6x, against 31.4x two years ago (M).
- **History:** I use a 5-year median of ~25x (mem, L).

**Growth**
- **Forecasts:** MOSL expects consolidated EBITDA and PAT CAGR of ~11% over FY25–28, and 18% EBITDA CAGR over FY26–28. Jefferies expects Jio revenue and EBITDA CAGRs of 16% and 20% (FY26–28), with a target of ₹1,750 cut "over the Jio IPO delay" ([FPJ](https://www.freepressjournal.in/business/jefferies-cuts-reliance-target-price-by-38-to-rs-1750-over-jio-ipo-delay); [BT 19-Jun-26](https://www.businesstoday.in/amp/markets/stocks/story/reliance-jio-to-power-stellar-growth-in-reliance-industries-over-fy26-28-heres-how-538085-2026-06-19); M).
- **Jio IPO:** the RHP and price band were **still pending** as of early October. The reported band of ₹1,065–1,119 is unofficial ([YourStory Oct-26](https://yourstory.com/2026/10/jio-ipo-nears-launch-drhp-filed-sebi-clears-path); [NiftyTrader](https://www.niftytrader.in/markets/?p=31917); M).

**Inputs by scenario**

| | g | Exit P/E | 3-yr total (a year) |
|---|---|---|---|
| Base | 11% | 23x | +50% (14.5%) |
| Bear (O2C normalises after peace, levies, weak retail) | 5% | 17x | −6% (−1.9%) |
| Bull | 14% | 25x | +76% (20.8%) |

- **Yield:** 0.5%.

**Governance and balance sheet**
- Promoter group ~50% (mem, L).
- Related-party and minority-leakage questions around listed Jio and Retail.
- Large new-energy capex with unproven returns.
- **Election risk is high:** fuel-price populism and fortnightly export-levy reviews.

### 6.9 Bharti Airtel (NSE: BHARTIARTL). ✅ Rank 9, conviction 3.5

**Price and valuation**
- **Price:** ₹1,779.90 (5-Oct, M; Kotak Neo via india_stocks.md). An undated aggregator shows ₹1,842 (L).
- **EPS consensus:** FY27E ₹63.87 and FY28E ₹81.70 ([stockanalysis](https://stockanalysis.com/quote/nse/BHARTIARTL/forecast/); [sharpely](https://sharpely.in/stocks/bhartiartl/forecast); M/L, undated). That gives **27.9x FY27E and 21.8x FY28E** (calc).
- **History:** the trailing ~70x is distorted by past losses, so there is no usable 5-year median.

**Growth**
- **Q1 FY27:** PAT ₹8,167 cr (+37.3%); India ARPU ₹263.9 ([BS 6-Aug-26](https://www.business-standard.com/markets/news/premiumisation-tariff-hikes-expected-to-sustain-airtel-s-earnings-momentum-126080601588_1.html), M).
- **HSBC ARPU path:** ₹277 (FY27), ₹310 (FY28), ₹325 (FY29). HSBC expects a tariff hike in Q1 CY27; Morgan Stanley sees 16–20% and a target of ₹2,435 ([TelecomTalk](https://telecomtalk.info/airtel-arpu-could-hit-rs-325-by-fy29/1011523/); [TelecomTalk MS](https://telecomtalk.info/?p=1002663); M).
- **Jio IPO:** telcos are reportedly weighing hikes before Jio's IPO ([Sahi](https://www.sahi.com/news/bharti-airtel-telcos-consider-price-increases-before-jio-s-ipo-3074-PE1_COR), M).

**Inputs by scenario**

| | g | Exit fwd P/E | 3-yr total (a year) |
|---|---|---|---|
| Base | 18% | 24x (de-rating as growth normalises) | +45% (13.1%) |
| Bear (no hike until after the 2029 election) | 10% | 20x | −2% (−0.5%) |
| Bull | 22% | 28x (flat) | +86% (22.9%) |

- **Yield:** ~0.9% (L).

**Durability:** a structural duopoly with a weak third player (mem, L). Risks:
- Africa FX;
- spectrum and AGR liabilities;
- Singtel and other stake-sale overhang (mem, L);
- telcos historically avoid tariff hikes just before national elections (the 2024 hike came right after the vote; mem, M).

### 6.10 Maruti Suzuki (NSE: MARUTI). ✅ Rank 10, conviction 3

**Price and valuation**
- **Price:** ~₹11,228 (9-Oct, M; a Citi-linked article says ₹11,420).
- **P/E:** ~25x TTM vs a 10-year median of **34.0x** ([GuruFocus](https://www.gurufocus.com/term/pettm/NSE:MARUTI), M). I use a 5-year median of ~29x (L).

**Forecasts**

| Source | FY28E EPS (₹) | Note | Confidence |
|---|---|---|---|
| ICICI Securities | 548.4 | FY28E EBITDA margin 11.0% | M ([I-Sec Q1](https://mailcontent.icicidirect.com/mailcontent/idirect_marutisuzuki_q1fy27.pdf)) |
| MOSL | ~656 (implied) | Target ₹17,064 at 26x FY28E; FY28 PAT cut 4.8% | M ([DSIJ](https://insights.dsij.in/markets/reports/report-details/maruti-suzuki-india-ltd/44875)) |
| Anand Rathi | 458 (core) | Cut FY28E EPS 11.2% | M |

- **Revision trend:** estimates have been revised **down** after Q1 FY27.

**Inputs by scenario**

| | g | Exit P/E | 3-yr total (a year) |
|---|---|---|---|
| Base | 11% | 27x | +52% (14.9%) |
| Bear (monsoon, share <40%, margin stuck ~8%) | 3% | 20x | −9% (−3.0%) |
| Bull | 15% | 30x | +87% (23.1%) |

- **Yield:** 1.2%.

**Durability:** distribution and service network; Suzuki parent. Risks:
- related-party royalty to Suzuki (mem, L);
- EV lag;
- share loss.

### 6.11 TCS (NSE: TCS). ✅ Rank 11 (diversifier), conviction 2.5

**Price and valuation**
- **Price:** ~₹2,156 (9-Oct, M).
- **P/E:** **~14.2x forward** vs a **5-year average of 28.4x** ([Trendlyne 24-Jul-26](https://trendlyne.com/tools/buy-sell-zone/1372/TCS/tata-consultancy-services-ltd/), M).
- **Forward EPS:** FY28E ₹164 (a broker valuing TCS at 17x, Apr-26, [BT](https://www.businesstoday.in/amp/markets/stocks/story/tcs-share-price-target-at-rs-3350-15-brokerages-share-views-post-q4-results-524986-2026-04-10), M). An aggregator shows ~6% a year EPS growth for FY27–28 (L).
- **Dividends:** FY26 dividend **₹110** (including a ₹46 special), a ~5.1% yield ([BT](https://www.businesstoday.in/amp/markets/stocks/story/tcs-dividend-announcement-record-date-q1-payout-history-and-results-preview-541609-2026-07-08), M). I use 4.5%.

**Inputs by scenario**

| | g | Exit P/E | 3-yr total (a year) |
|---|---|---|---|
| Base (AI fear persists) | 6% | 14.2x (flat) | +33% (10.1%) |
| Bear (AI deflation) | 1% | 11.5x | −3% (−1.0%) |
| Bull (halfway re-rating) | 9% | 21x | +106% (27.3%) |

- **After tax the base is only 8.2%/yr**, because the dividend is slab-taxed.
- **Why it is kept:** it diversifies the shortlist away from domestic rates, oil and monsoon risk. If you hold a global/USD sleeve already, **replace it with HDFC AMC.**

### 6.12 HDFC Life (alternate). Conviction 3

**Price and valuation**
- **Price:** ₹547.95 (7-Oct), −30.5% from its 52-week high ([Anand Rathi](https://anandrathi.com/stocks/hdfc-life-insurance-company-ltd/share-price-today), M).
- **P/EV:** ~1.8x current EV and ~1.6x FY27E (Nuvama, M).

**Growth:** Q1 VNB +9%, EV +13%, solvency 185% ([HDFC Life PR](https://www.hdfclife.com/content/dam/hdfclifeinsurancecompany/about-us/pdf/investor-relations/financial-information/Quarterly-financial-results/HDFC-Life-Q1-FY2027-Press-Release.pdf), H).

**Model:** base 12% EV growth, exit 2.1x → **+65% (18.2%/yr)**. Bear +9%, bull +115%.

**Why only an alternate:** growth is half of SBI Life's, and its bancassurance depends on HDFC Bank, so it is the same factor twice.

### 6.13 HDFC AMC (alternate). Conviction 3

**Price and valuation**
- **Price:** ₹2,251.85 (9-Oct, M).
- **P/E:** ~30x TTM (calc, L; one source says 37.9x on an unclear EPS basis).

**Growth:** Q1 PAT ₹838 cr (+12%); market share 11.2%, down 20 bp ([HDFC AMC PR](https://files.hdfcfund.com/s3fs-public/2026-07/Press%20Release%20-%20Q1%20FY27.pdf), H). SIPs are at a record ₹32,297 cr (H).

**Model:** base 12% growth, exit 32.5x → **+60% (17.0%/yr)**. Bear −4%, bull +111%.

**Why only an alternate:** the high base partly reflects my L-confidence multiple inputs. The business is a geared bet on the market level, and SEBI expense-ratio rules are an ongoing risk. It replaces TCS if the investor already holds a USD sleeve.

### 6.14 Eicher Motors. Watch, conviction 3

**Price:** ~₹7,513 (17-Sep, M; [Anand Rathi](https://anandrathi.com/stocks/eicher-motors-ltd/share-price-today)). The 52-week range is ₹6,411–8,230 (M).

**Growth**
- **Q1 FY27:** PAT ₹1,463 cr (+21%); revenue +31.5%; record Royal Enfield volumes ([Kotak Neo](https://www.kotakneo.com/news/stocks/eicher-motors-q1-results-fy27-net-profit-rises-21-to-rs-1463-crore-royal-enfield-posts-highest-ever-quarterly-sales/), H).
- **September:** 133,958 units, its best month ever. H1 volumes +20% ([Sahi](https://www.sahi.com/news/eicher-motors-reports-september-motorcycle-sales-of-133-958-units-versus-124-328-units-yoy), M).

**Valuation:** TTM P/E ~35x (calc from FY26 PAT estimate; **L**).

**Model:** base +44% (13.0%/yr), bear −8%, bull +69%.

**Verdict:** a quality, net-cash franchise. Its ratio (1.03) edges Maruti, but its price and EPS inputs are weak. **Swap in for Maruti if a live check confirms ≤ ~33x TTM.**

### 6.15 Bajaj Auto. Reject for now, conviction 2.5

**Price:** ~₹11,720 (5-Aug, stale, M; [MoneyWorks4Me](https://www.moneyworks4me.com/company/news/index/id/357624)).

**Growth**
- **Q1 FY27:** PAT ₹2,983 cr (+42%); EBITDA margin 20.9%; exports above 700k units ([Kotak Neo](https://www.kotakneo.com/news/stocks/bajaj-auto-q1-results-fy27-profit-revenue-share-price/), H).
- **September:** volumes +5% ([NewKerala](https://www.newkerala.com/news/a/eicher-motors-sales-rise-bajaj-auto-september-export-576.htm), M).

**Valuation:** forward P/E re-rated from 15.6x to **25.1x** over two years (Kotak Neo, M).

**Model:** base +37% (10.9%/yr). The base assumes a de-rating to 22x. Bear −6%, bull +67%.

**Verdict:** already re-rated; a good business, a mediocre entry point.

### 6.16 Mahindra & Mahindra. Alternate in autos, conviction 3

**Price:** ~₹3,074–3,117 (17-Sep, M).

**EPS consensus:** FY27E ₹139.21, FY28E ₹159.40 (median of 34 analysts; [sharpely](https://sharpely.in/stocks/m&m/forecast), M/L). That gives 22.2x / 19.4x.

**Results:** Q1 auto PBIT margin 8.3% (−170 bp) (H). September SUVs +14% vs Maruti's domestic PV +36.9% (M).

**Model:** base +40% (11.8%/yr), bear −6%, bull +79%.

**Risks:** monsoon (tractors at 44.9% share); Tech Mahindra look-through (AI factor).

### 6.17 ITC. Reject (yield trap risk), conviction 2.5

**Price:** ~₹255–265. The stock touched a 52-week low of ₹254.65 on 8-Oct ([Univest](https://univest.in/blogs/itc-share-price-dips-4-percent-will-it-bounce-back-experts-view-target-price-stop-loss), L).

**Valuation and dividend:** FY26 DPS ₹14.50, so the yield is ~5.6% (calc). P/E ~17x (undated, L).

**Earnings:** the Feb-26 tax overhaul (40% GST plus excise of ₹2,100–8,500 per 1,000 sticks) cut volumes ~8–10% in H1 FY27. Q1 consolidated PAT −16% (M). Emkay expects a 5% earnings CAGR over 3 years ([BT Jun-26](https://www.businesstoday.in/amp/markets/stocks/story/itc-share-price-target-cut-as-cigarette-volumes-may-decline-8-10-in-h1-says-systematix-536039-2026-06-10), M).

**Model:** base +30% (9.1%/yr), but only **7.1%/yr after tax**. Bear −6%, bull +66%.

**Verdict:** policy risk recurs; there is a BAT stake-sale overhang (mem, L); returns are below the hurdle.

### 6.18 Power Grid. Reject, conviction 2

**Price and valuation:** ₹249.50 (9-Oct, M); ~15x TTM; yield 3.6%. FY28E EPS ₹21.9 (I-Sec Feb-26, [DSIJ](https://insights.dsij.in/markets/reports/report-details/power-grid-corporation-of-india-ltd/44014), L/stale).

**Results:** Q1 PAT −1% (M). FY27 capex ₹37,000 cr and capitalisation ₹30,000 cr (M).

**Model:** base +24% (7.4%/yr). It sits above its own median multiple, and transmission ROE was already trimmed in the last CERC cycle.

### 6.19 SBI. **Drop for 3 years**, conviction 2.5

**Price and valuation:** ₹959.10 (H). FY26 EPS ₹86.7, so 11.1x, against a **5-year median of 11.0x** ([SBI IR](https://sbi.bank.in/en/web/investor-relations/sbi-financial-highlights-past-5), M).

**Forecasts**

| Source | Forecast | Confidence |
|---|---|---|
| Anand Rathi (9-Aug-26) | FY28E EPS ₹104.5 | M ([BS PDF](https://bsmedia.business-standard.com/_media/bs/data/market-reports/equity-brokertips/2026-08/17863423890.40975100.pdf)) |
| MOSL | **8% earnings CAGR FY26–28; ROE 15.5% by FY28** | M ([BT 2-Jun-26](https://www.businesstoday.in/amp/markets/stocks/story/sbi-shares-fall-for-fifth-straight-session-should-you-buy-534434-2026-06-02)) |

**Model:** base +34% (10.2%/yr), bear −9%, bull +70%.

**Why drop:**
- No valuation cushion.
- The deposit gap (+9.7% vs +18.6% loans).
- ECL from Apr-27 (CET1 hit up to 120 bp, H).
- PSU directed lending and wage risk into the 2029 election.
- The base is below the Nifty hurdle.

**The hidden value** (subsidiaries worth ~₹300/share, L) is real but needs a listing catalyst.

### 6.20 Infosys. **Drop for 3 years**, conviction 2.5

**Price and valuation:** ₹1,025.10 (H); ~13.3x FY27E EPS of ₹77.10 ([sharpely](https://sharpely.in/stocks/infy/forecast), L/M). The 10-year mean P/E is 22.4x ([Wisesheets](https://www.wisesheets.io/pe-ratio/INFY), M).

**Shareholder returns:** FY26 DPS **₹48** (yield 4.7%) ([ZeeBiz](https://www.zeebiz.com/companies/news-500-dividend-alert-infosys-declares-rs-25-final-dividend-fy26-payout-jumps-to-rs-48-per-share-check-record-date-394185), M). An ₹18,000 cr buyback at ₹1,800 was completed in Dec-25 (SEC 6-K, H).

**Model:** base +31% (9.3%/yr), 7.4% after tax.

**Why drop:** the same factor as TCS; a guidance cut to ~0.5–2% CC is expected on 23-Oct; lower margins.

### 6.21 Max Healthcare. Reject, conviction 2.5

**Price and valuation:** ~₹1,009–1,019 (mid-Aug, M; [DSIJ/PL](https://insights.dsij.in/markets/reports/report-details/max-healthcare-institute-ltd/45289)). P/E 65.8x (4-Sep, M).

**Growth:** Q1 EBITDA margin 24.9%. It plans 3,000+ beds over FY26–28 (HDFC Sec, M).

**Model:** base +40% (11.9%/yr) after de-rating to 42x forward. Bear −13%.

**Verdict:** Apollo offers similar growth at a lower multiple.

### 6.22 Trent. Reject (watch), conviction 2.5

**Price:** ₹2,867.20 (6-Oct, intraday +11% on its Q2 update) ([Angel One](https://www.angelone.in/news/stocks/trent-share-price-gains-over-11-as-q2-fy27-revenue-jumps-23-to-5-788-crore), M). That is down from a 52-week high of ~₹6,261 (L).

**Results:** Q2 revenue +23%; Zudio has 1,000+ stores (M).

**Valuation:** MOSL said **62x FY28E** at ₹3,107 (Aug-26; [DSIJ](https://insights.dsij.in/markets/reports/report-details/trent-ltd/44989), M). That implies FY28E EPS of ~₹50 and ~70x FY27E (calc, L). MOSL notes fashion like-for-like growth is in the low single digits.

**Model:** base +43% (12.7%/yr) after a de-rating to 55x. Bear −15%.

**Verdict:** a great business at a price that still needs ~22% compounding just to tread water. Revisit below ~45x FY28E.

### 6.23 Polycab. Reject, conviction 2

**Price and valuation:** ₹8,255 (9-Oct, M); P/E 42–45x ([Dhan](https://dhan.co/stocks/polycab-india-ltd-share-price/), M).

**Growth:** FY26–29 earnings CAGR of 18%. A broker values it at 40x two-year-forward earnings, which it says is **1.5 SD above the historical average** ([Swastika/BT](https://www.businesstoday.in/amp/markets/stocks/story/polycab-rr-kabel-kei-industries-share-price-targets-as-industry-reaps-infra-benefits-537714-2026-06-18), M).

**Model:** base +32% (9.7%/yr). Bear −15%.

**Risks:** new entrants (UltraTech/Aditya Birla, Adani; mem, M); copper.

### 6.24 Titan. Reject (watch), conviction 2.5

**Price:** ₹4,364.80 (7-Oct), after a 4% fall on its Q2 update. The 52-week high was ₹5,186.70 (Aug-26) ([Angel One](https://www.angelone.in/news/stocks/titan-company-share-price-falls-over-4-after-q2-fy27-performance-update), M).

**Valuation:** a foreign broker puts it at **53x FY28E EPS of ₹86.1** (target ₹5,425) (M). That implies ~51x at today's price and ~62x FY27E (calc, L).

**Growth:** jewellery growth slowed from 39% (Q1) to ~21% (Q2). Buyer growth is in the mid-single digits; ticket sizes are doing the work (M).

**Model:** base +30% (9.2%/yr). Bear −15%.

**Verdict:** growth leans on gold prices, which are ~25% below their record.

### 6.25 Sun Pharma. Reject, conviction 2

**Price and valuation:** ₹1,760 (9-Oct, M); 34.7x TTM.

**Organon deal:** an $11.75 bn all-cash acquisition. Sun assumes ~$8.6 bn of Organon debt, takes on ~$9–9.8 bn of new bank debt, and pro-forma net debt/EBITDA is ~2.3x. Closing is expected in early 2027. Brokers' FY28 EPS-accretion estimates conflict: 17% to 40% ([MarketScreener/Reuters](https://www.marketscreener.com/news/india-s-sun-pharma-to-buy-us-listed-organon-in-11-75-billion-deal-ce7f59dcda81f02d); [Outlook Business](https://www.outlookbusiness.com/corporate/sun-pharmas-mega-buyout-plan-inside-13-bn-organon-cash-deal-structure); M).

**Organic growth:** MOSL expects an 11% EPS CAGR over FY26–28 ([DSIJ](https://insights.dsij.in/markets/reports/report-details/sun-pharmaceutical-industries-ltd/44885), M).

**Tariffs:** US Section 232 puts 100% on patented drugs, which hits Sun's specialty brands. India gets 0% on select specialty drugs (M).

**Model:** base +28% (8.6%/yr). Bear −17%.

**Verdict:** the integration and leverage risk is not paid for at ~35x.

### 6.26 Bharat Electronics. Reject, conviction 2

**Price:** ~₹386 (17-Sep, M), near its 52-week low. The high was ₹473 ([Anand Rathi](https://anandrathi.com/stocks/bharat-electronics-ltd/share-price-today); [LatestLY](https://www.latestly.com/business/bharat-electronics-stock-update-share-price-slips-further-on-q1-margin-woes-7536577.html), M).

**Earnings:** FY26 EPS ₹8.29. A broker values it at **44x FY28E EPS of ₹11** (target ₹485) ([elitewealth](https://elitewealth.in/fundamental-report-bharat-electronics-limited-bel/), M).

**Results:** Q1 PAT only +8–9% on revenue +25%; gross margin 45.5% vs 53.2% (M).

**Model:** base +21% (6.5%/yr). Bear −17%.

**Verdict:** an excellent order book (₹73,882 cr), but a ~40x forward multiple for ~15% growth.

---

## 7. Rejected without a full model

| Name | Reason (source, date, confidence) |
|---|---|
| Hitachi Energy India | ₹33,880 (28-Aug); **~144x TTM** ([Anand Rathi](https://anandrathi.com/stocks/hitachi-energy-india-ltd); [MOSL peer page](https://www.motilaloswal.com/share-market/peer-comparison/hitachi-energy-india-ltd), M). Even 30% EPS growth with a de-rating to 45x yields only ~5–6%/yr (calc). |
| Siemens Ltd | ₹3,990 (6-Aug, M); P/E 45–64x depending on source (L). Not reasonably priced. |
| Dixon Technologies | ~₹14,096 (31-Jul, M). P/E 46–97x across sources. Q1 profit spike was from other income; EBITDA margin 2.98% ([MarketsMojo](https://www.marketsmojo.com/news/result-analysis/dixon-technologies-q1-fy27-stellar-195-profit-surge-masks-margin-pressure-concerns-4130885), M). Thin-margin assembler with PLI dependence. |
| KEI Industries | Price conflicting (₹4,636–5,539, undated, L); P/E ~40–44x; 20% earnings CAGR (M). Same verdict as Polycab; no dated price. |
| Divi's Labs | At its 52-week high (₹9,570, 8-Sep), P/E 67–87x (missed_opportunities.md, M). |
| Tata Power | No 2026 price after February (~₹365, M); P/E ~32x (undated, L). Unassessable. |
| Coal India | ₹420 (8-Sep, L); 8–9x; 6.3% yield; flat profit, volume decline, government offer-for-sale overhang. ~6%/yr base, mostly slab-taxed dividends. |
| HUL | ₹1,851 (9-Oct, H); ~44x forward; ~6–7%/yr base (calc). |
| Kotak Mahindra Bank | ~₹435 (8-Oct, M), only ~4% off its high, P/B ~3.2x (conflicting). Not de-rated; ICICI is the better quality-at-a-price bank. |
| CDSL / BSE | CDSL Q1 PAT +15% to ₹118 cr ([Sahi](https://www.sahi.com/blogs/cdsl-q1-results-fy27), M), but no reliable 2026 price; BSE carries recurring SEBI F&O-expiry risk. Unassessable. |
| Kalpataru Projects | 24.55% of promoter shares pledged (M). Fails the governance screen for a 3-year hold. |

---

## 8. Gaps the red team should check

1. **Stale prices:**
   - SBI Life (11-Sep), Bajaj Auto (5-Aug), M&M and Eicher (17-Sep), Max (Aug), BEL (17-Sep).
   - SBI Life's verdict holds only if the live price is ≤ ~₹1,850, which is ~2.2x current EV.
2. **5-year medians** tagged L come from background knowledge, not a series: Reliance ~25x, Maruti 5y ~29x, SBI Life ~2.6x P/EV, HDFC Life, HDFC AMC, Apollo, Bajaj Auto, BEL, Polycab, ITC and Power Grid. The ICICI, HDFC Bank, NTPC, L&T, TCS, Bajaj Finance and SBI medians are sourced (M).
3. **Forward EPS for Titan, Trent, Apollo and BEL** is backed out from broker multiples (calc, L).
4. **ICICI CEO extension:** the source is low quality (mirrored spam domains). Confirm against an exchange filing.
5. **Re-rating dependence:** the four financials get 14–28 pp of their 3-year base from re-rating. With flat multiples, the shortlist base is 14.4%/yr, the same as the Nifty base.
6. **The scenario probabilities (25/50/25) are judgment.** The 2026 consensus-cut evidence argues for skewing toward the bear case if the RBI hikes again in December.

---

## 9. Sources (new searches this round; earlier sources are cited inline from the working files)

All were seen only as search-result summaries; no page was opened.

**Banks and NBFCs**
- https://www.businesstoday.in/amp/markets/stocks/story/icici-bank-is-mofsls-top-banking-pick-with-39-upside-potential-heres-why-535038-2026-06-05
- https://www.multibagg.ai/market-pulse/articles/icici-bank-motilal-target-price-cmpyv9k4fis5qnz0j9ral6vv0
- https://insights.dsij.in/markets/reports/report-details/icici-bank-ltd/44570
- https://www.goodreturns.in/news/sbi-hdfc-icici-to-au-sfb-these-5-bank-stocks-can-deliver-strong-returns-in-long-term-check-targ-1516167.html
- https://seekingalpha.com/symbol/IBN/valuation/metrics
- https://www.gurufocus.com/term/book-value-per-share/NSE:ICICIBANK
- https://www.mycpd2.moh.gov.my/first-dry/RBI-Approves-ICICI-Bank-CEO-Sandeep-Bakhshis-Reappointment-for-Two-More-Years-21-1104 (low quality)
- https://www.business-standard.com/markets/news/hdfc-bank-share-price-to-re-rate-outperform-icici-bank-stock-by-fy28-emkay-lists-4-reasons-125121100321_1.html
- https://askfuzz.ai/discover/news/investment-ideas/motilal-oswal-sets-hdfc-bank-target-at-1100
- https://sharpely.in/stocks/hdfcbank/forecast
- https://bsmedia.business-standard.com/_media/bs/data/market-reports/equity-brokertips/2026-08/17863423890.40975100.pdf
- https://www.businesstoday.in/amp/markets/stocks/story/sbi-shares-fall-for-fifth-straight-session-should-you-buy-534434-2026-06-02
- https://www.businesstoday.in/markets/stocks/story/bajaj-finance-share-price-nomura-raises-target-sees-18-upside-heres-why-550521-2026-08-21
- https://www.indmoney.com/blog/stocks/why-bajaj-finance-share-fell-rbi-proposal
- https://www.indmoney.com/blog/stocks/why-bajaj-finance-share-price-is-rising-q2-update
- https://www.angelone.in/news/stocks/why-did-bajaj-finance-share-price-fall-nearly-6-percent-today-aug-7-2026
- https://www.kotakneo.com/news/regulations/bajaj-finance-shares-falls-after-rbi-nbfc-proposal/
- https://www.gurufocus.com/term/pe-ratio/NSE:BAJFINANCE
- https://www.moneyworks4me.com/check-before-you-invest/bajfinance
- https://in.marketscreener.com/quote/stock/BAJAJ-FINANCE-LIMITED-33647061/valuation/
- https://fyers.in/stocks/bajaj-finance-ltd/profit-loss

**Insurers, AMC, market infrastructure**
- https://www.5paisa.com/blog/sbi-life-insurance-stock-update-11-sep-26
- https://fyers.in/stocks/sbi-life-insurance-company-ltd?tabs=news
- https://insights.dsij.in/markets/reports/report-details/sbi-life-insurance-company-ltd/44653
- https://insights.dsij.in/markets/reports/report-details/sbi-life-insurance-company-ltd/44654
- https://www.sahi.com/blogs/cdsl-q1-results-fy27
- https://pro.edgex.exchange/en-US/news/article/cdsl-q1-fy27-results-net-profit-118-crore
- https://www.multibagg.ai/market-pulse/articles/cdsl-q1fy27-97036

**IT**
- https://trendlyne.com/tools/buy-sell-zone/1372/TCS/tata-consultancy-services-ltd/
- https://www.tijorifinance.com/company/tata-consultancy-services-limited/financials/
- https://www.wisesheets.io/pe-ratio/INFY
- https://ycharts.com/companies/INFY/pe_ratio
- https://www.businesstoday.in/amp/markets/stocks/story/tcs-share-price-target-at-rs-3350-15-brokerages-share-views-post-q4-results-524986-2026-04-10
- https://pro.stockalarm.io/quote/TCS.NS/analysts
- https://sharpely.in/stocks/infy/forecast
- https://www.businesstoday.in/amp/markets/stocks/story/tcs-dividend-announcement-record-date-q1-payout-history-and-results-preview-541609-2026-07-08
- https://www.outlookbusiness.com/markets/the-dividend-catch-tcs-pays-more-but-wipro-gives-better-returns
- https://www.zeebiz.com/companies/news-500-dividend-alert-infosys-declares-rs-25-final-dividend-fy26-payout-jumps-to-rs-48-per-share-check-record-date-394185
- https://www.sec.gov/Archives/edgar/data/0001067491/000106749126000018/exv99w09.htm

**Telecom**
- https://stockanalysis.com/quote/nse/BHARTIARTL/forecast/
- https://sharpely.in/stocks/bhartiartl/forecast
- https://tradersunion.com/currencies/price/bhartiartl-inr/
- https://www.business-standard.com/markets/news/premiumisation-tariff-hikes-expected-to-sustain-airtel-s-earnings-momentum-126080601588_1.html
- https://telecomtalk.info/airtel-arpu-could-hit-rs-325-by-fy29/1011523/
- https://telecomtalk.info/?p=1002663
- https://www.sahi.com/news/bharti-airtel-telcos-consider-price-increases-before-jio-s-ipo-3074-PE1_COR

**Consumption and autos**
- https://www.angelone.in/news/stocks/titan-company-share-price-falls-over-4-after-q2-fy27-performance-update
- https://upstox.com/news/market-news/stocks/titan-shares-slide-over-3-after-q2-update-festive-shift-high-gold-prices-weigh-on-jewellery-growth/article-201416/
- https://insights.dsij.in/dsijarticledetail/titan-shares-fall-4-jewellery-growth-and-festive-demand-in-focus-id022-59875
- https://www.angelone.in/news/stocks/trent-share-price-gains-over-11-as-q2-fy27-revenue-jumps-23-to-5-788-crore
- https://upstox.com/news/market-news/stocks/trent-shares-in-focus-after-q2-revenue-jumps-23-yo-y-zudio-crosses-1-000-store-milestone/article-201309/
- https://insights.dsij.in/markets/reports/report-details/trent-ltd/44989
- https://hdfcsky.com/news/trent-favorable-risk-reward-ratio-upgrade-to-buy
- https://sharpely.in/stocks/m&m/forecast
- https://tradebrains.in/stock-to-buy-auto-stock-in-which-jefferies-hsbc-nomura-and-clsa-see-up-to-37-upside/
- https://www.moneyworks4me.com/company/news/index/id/357624
- https://anandrathi.com/stocks/eicher-motors-ltd/share-price-today
- https://www.kotakneo.com/stocks/eicher-motors-share-price/
- https://www.kotakneo.com/news/stocks/eicher-motors-q1-results-fy27-net-profit-rises-21-to-rs-1463-crore-royal-enfield-posts-highest-ever-quarterly-sales/
- https://www.kotakneo.com/news/stocks/bajaj-auto-q1-results-fy27-profit-revenue-share-price/
- https://www.sahi.com/news/eicher-motors-reports-september-motorcycle-sales-of-133-958-units-versus-124-328-units-yoy
- https://www.newkerala.com/news/a/eicher-motors-sales-rise-bajaj-auto-september-export-576.htm
- https://mailcontent.icicidirect.com/mailcontent/idirect_marutisuzuki_q1fy27.pdf
- https://insights.dsij.in/markets/reports/report-details/maruti-suzuki-india-ltd/44875
- https://insights.dsij.in/markets/reports/report-details/maruti-suzuki-india-ltd/44876
- https://bsmedia.business-standard.com/_media/bs/data/market-reports/equity-brokertips/2026-08/17857316670.77044800.pdf
- https://univest.in/blogs/itc-share-price-dips-4-percent-will-it-bounce-back-experts-view-target-price-stop-loss
- https://www.businesstoday.in/amp/markets/stocks/story/itc-share-price-target-cut-as-cigarette-volumes-may-decline-8-10-in-h1-says-systematix-536039-2026-06-10
- https://www.businesstoday.in/amp/markets/stocks/story/itc-shares-to-turn-ex-dividend-today-dividend-history-payment-date-what-to-watch-targets-533469-2026-05-27
- https://oga-prod.angelone.in/news/stocks/itc-share-price-in-focus-as-new-cigarette-tax-kicks-in-stock-sees-worst-january-ever

**Healthcare**
- https://anandrathi.com/stocks/apollo-hospitals-enterprise-ltd/share-price-today
- https://www.stockezee.com/compare/apollohosp-vs-maxhealth
- https://www.valueresearchonline.com/stocks/270996/max-healthcare-institute-ltd/peer-comparison/
- https://insights.dsij.in/markets/reports/report-details/apollo-hospitals-enterprise-ltd/45228
- https://insights.dsij.in/markets/reports/report-details/apollo-hospitals-enterprise-ltd/45221
- https://www.businesstoday.in/markets/stocks/story/apollo-hospitals-medanta-healthcare-global-max-healthcare-artemis-medicare-check-target-prices-outlook-539782-2026-06-29
- https://investmentguruindia.com/newsdetail/buy-apollo-hospitals-ltd-for-the-target-rs-9-600-by-choice-institutional-equities110271
- https://www.outlookbusiness.com/corporate/apollo-hospitals-promoter-group-offloads-13-stake-for-1489-cr
- https://www.emkayglobal.com/news-details/eod/4735456
- https://insights.dsij.in/markets/reports/report-details/max-healthcare-institute-ltd/45289
- https://www.business-standard.com/markets/news/hdfc-sec-upgrades-max-healthcare-on-strong-expansion-led-growth-outlook-125123000289_1.html
- https://insights.dsij.in/markets/reports/report-details/sun-pharmaceutical-industries-ltd/44885
- https://www.businesstoday.in/amp/markets/stocks/story/buy-sun-pharma-shares-up-to-34-upside-what-experts-say-on-indias-biggest-ever-pharma-deal-organon-527710-2026-04-28
- https://www.marketscreener.com/news/india-s-sun-pharma-to-buy-us-listed-organon-in-11-75-billion-deal-ce7f59dcda81f02d
- https://www.outlookbusiness.com/corporate/sun-pharmas-mega-buyout-plan-inside-13-bn-organon-cash-deal-structure

**Capex, power, defence**
- https://www.plindia.com/pl-research/ntpc-ntpc-in-q1fy27-result-update-healthy-q1-plan-laid-out-until-fy37-buy/
- https://insights.dsij.in/markets/reports/report-details/ntpc-ltd/45163
- https://hdfcsky.com/news/ntpc-ltd-selected-as-hdfc-securities-pick-of-the-week-on-strategic-growth-and-renewable-expansion
- https://insights.dsij.in/markets/reports/report-details/power-grid-corporation-of-india-ltd/44014
- https://www.plindia.com/pl-research/power-grid-corporation-of-india-pwgr-in-analyst-meet-update-guidance-upgraded-buy/
- https://trendlyne.com/posts/5782394/a-steady-start-to-fy27
- https://powerline.net.in/2024/02/05/roe-adjustments-key-highlights-of-cercs-draft-tariff-regulations/
- https://bsmedia.business-standard.com/_media/bs/data/market-reports/equity-brokertips/2026-05/17780470020.93697100.pdf
- https://www.business-standard.com/amp/markets/news/l-t-gains-2-hits-new-high-brokerages-see-more-upside-in-stock-price-125112600384_1.html
- https://craytheon.com/stocks/larsen-and-toubro/growth/
- https://elitewealth.in/fundamental-report-bharat-electronics-limited-bel/
- https://www.bajajbroking.in/share-market-news/bel-share-price-2026-growth-valuation-and-order-book
- https://www.latestly.com/business/bharat-electronics-stock-update-share-price-slips-further-on-q1-margin-woes-7536577.html
- https://anandrathi.com/stocks/bharat-electronics-ltd/share-price-today
- https://anandrathi.com/stocks/hitachi-energy-india-ltd
- https://www.motilaloswal.com/share-market/peer-comparison/hitachi-energy-india-ltd
- https://www.motilaloswal.com/share-market/peer-comparison/siemens-ltd
- https://www.businesstoday.in/amp/markets/stocks/story/polycab-rr-kabel-kei-industries-share-price-targets-as-industry-reaps-infra-benefits-537714-2026-06-18
- https://www.swastika.co.in/blog/polycab-share-price-outlook-bofa-targets-11000-and-kei-growth-in-wires-and-cable
- https://www.marketsmojo.com/news/result-analysis/dixon-technologies-q1-fy27-stellar-195-profit-surge-masks-margin-pressure-concerns-4130885
- https://www.businesstoday.in/amp/markets/stocks/story/adani-power-vs-tata-power-fresh-share-price-targets-key-financials-post-q3-earnings-514984-2026-02-06

**Reliance / Jio**
- https://www.freepressjournal.in/business/jefferies-cuts-reliance-target-price-by-38-to-rs-1750-over-jio-ipo-delay
- https://www.businesstoday.in/amp/markets/stocks/story/reliance-jio-to-power-stellar-growth-in-reliance-industries-over-fy26-28-heres-how-538085-2026-06-19
- https://www.niftytrader.in/markets/?p=31917
- https://yourstory.com/2026/10/jio-ipo-nears-launch-drhp-filed-sebi-clears-path

**Forecast-error history**
- https://www.bloombergquint.com/opinion/why-are-consensus-earnings-estimates-often-off-the-mark-
- https://www.business-standard.com/amp/article/markets/fy18-starts-with-big-earnings-cut-117032600716_1.html
- https://www.business-standard.com/amp/article/markets/from-maruti-to-asian-paints-india-inc-earnings-see-further-downgrades-119072800723_1.html
- https://www.bloomberg.com/news/articles/2023-05-04/a-40-earnings-downgrade-awaits-indian-stocks-bofa-says
- https://www.5paisa.com/news/nifty-fy27-earnings-estimates-trimmed-9-despite-persistent-downgrade-trend (via india_macro.md)
