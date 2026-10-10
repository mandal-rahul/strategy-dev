# Global equities on a 2–3 year horizon (hold to ~late 2029)

**Prepared:** Sat 2026-10-10 (last US session Fri Oct 9). **Role:** global equity analyst. A red team will fact-check this.
**Builds on:** `FINAL_RECOMMENDATIONS.md`, `REPORT.md`, `working/global_stocks.md`, `working/contrarian_final.md`, `working/missed_opportunities.md`, `working/redteam_round1.md`. Facts already settled there are reused and cited to their original URL, not searched again.
**Method limits:** WebFetch and finance sites are blocked, so every new figure comes from a WebSearch result summary. I opened no page. I ran 46 searches. Tags: **[H]** = filing or 2+ sources agree; **[M]** = one credible source; **[L]** = aggregator, undated, conflicting, single broker, or memory; **(calc)** = my arithmetic; **(mem)** = my background knowledge, not verified. EPS is labelled GAAP, adjusted or "clean" (one-offs removed). Not investment advice.

---

## 0. Summary table (sorted by risk-adjusted score)

Returns are **USD, pre-tax and before FX**, over 3 years with dividends reinvested. "Score" is the risk-adjusted rank metric (defined in §1). The **★** names form the shortlist.

| # | Name | Price / date [conf] | Clean fwd P/E (basis) vs ~10y median → anchor | EPS CAGR used (FY27→FY30) | Div % / buyback % | Base / Bear / Bull, 3-yr total (per yr) | E[r]/yr | Score | Conv. |
|---|---|---|---|---|---|---|---|---|---|
| 1 ★ | **Intuit (INTU)** | $291.08 Oct 6 [M]; an undated $321.69 also seen [L] | **12.6x** FY27 non-GAAP incl. SBC (14.4x GAAP) vs ~33x (old basis, mem L) → **regime anchor 20x** | 13% | 1.9 / 6.8 | **+98% (25.5%) / −3% (−0.9%) / +162% (37.9%)** | 22.0% | 21.5 | **4** |
| 2 | Mastercard (MA) | not verified; fwd P/E 24.6 Oct 6 [M] | 24.6x vs ~33x (mem L) → anchor 30x | 13% | 0.6 / ~2.5 (mem) | +63% (17.7%) / +4% (1.4%) / +89% (23.6%) | 15.1% | 15.1 | (alt. to V) |
| 3 ★ | **Netflix (NFLX)** | $71.57 Oct 8 [M] | **18.7x** clean CY27 ($3.83) vs 10y median not meaningful → **regime anchor 22x** | 15% | 0 / ~4 (calc L) | **+66% (18.3%) / −8% (−2.8%) / +125% (31.1%)** | 16.2% | 14.8 | **3** |
| 4 ★ | **Uber (UBER)** | $70.24 Oct 8 [M] | **15.9x** fwd adj. (basis unclear, L); ~17.5x FCF after SBC (calc) → **anchor 20x** (no usable history) | 17% (L) | 0 / n.v. | **+81% (21.8%) / −20% (−7.1%) / +145% (34.8%)** | 17.8% | 14.3 | **3** |
| 5 ★ | **Amazon (AMZN)** | $259.92 Oct 7 [M] | **25.2x** clean CY27 ($10.3) vs median not meaningful (reinvestment era) → **anchor 25x** | 17% | 0 / 0 | **+60% (16.8%) / −5% (−1.7%) / +111% (28.2%)** | 15.1% | 14.2 | **3.5** |
| 6 ★ | **Microsoft (MSFT)** | $535.07 Oct 9 [M] | **26.4x** fwd (FY27 ~$19.6) vs ~27x (from 31.5x trailing median, M) | 15% | 0.7 / ~0.5 (mem) | **+57% (16.2%) / 0% (0.1%) / +91% (24.0%)** | 14.1% | 14.1 | **4** |
| 7 | Adobe (ADBE) | $242.25 Oct 9 [M] | 9.2x FY27 non-GAAP excl. SBC (~11x incl. SBC; 13.5x trailing GAAP) vs ~30x (mem L) → regime anchor 15x | 8% | 0 / ~10 (calc) | +66% (18.3%) / −13% (−4.7%) / +123% (30.6%) | 15.6% | 13.3 | 2.5 |
| 8 ★ | **Visa (V)** (or MA) | ~$376 Oct 8 [M] | **25.2x** FY27 ($14.94) vs ~28x (from 5y avg trailing 32x, L) | 12% | 0.7 / ~2.5 (L) | **+51% (14.8%) / +2% (0.7%) / +74% (20.3%)** | 12.7% | 12.7 | **4** |
| 9 | Booking (BKNG) | $180.30 Sep 9 (stale) [M] | ~16.5x NTM vs ~20x 5y fwd avg [M] | 12% (L) | 0.8 / ~4 (mem) | +59% (16.8%) / −14% (−4.8%) / +98% (25.6%) | 13.6% | 11.2 | 3 |
| 10 ★ | **Medtronic (MDT)** | $93.29 Sep 2 (stale; ~−3.6% over the 30 days to Oct 9) [L] | **15.6x** FY27 non-GAAP ($5.97) vs ~17x (mem L) | 7.5% | 3.0 / ~1 | **+42% (12.4%) / 0% (−0.2%) / +63% (17.8%)** | 10.6% | 10.5 | **3.5** |
| 11 ★ | **Elevance (ELV)** | $400.09 Oct 6 [M] | **13.6x** CY27 adj. (~$29.4) vs ~14x (mem L) | 11% | 1.7 / ~3 (mem) | **+46% (13.4%) / −9% (−3.0%) / +73% (20.0%)** | 11.0% | 9.5 | **3** |
| 12 | Salesforce (CRM) | $229.13 Oct 9 [H] | 16.1x FY27 clean (~$14.2, ex-Anthropic gains) vs ~39x 5y fwd avg [M] → regime anchor 20x | 9% | 0.7 / ~4 (mem) | +48% (14.0%) / −17% (−6.0%) / +96% (25.2%) | 11.8% | 8.8 | 2.5 |
| 13 ★ (opt.) | **Alphabet (GOOGL)** | $348.29 Oct 8 [M] | **23.4x** clean CY27 (~$14.9) vs ~23x (26.2–27.6x trailing median, M) | 13% | 0.3 / ~1.5 (mem) | **+44% (13.0%) / −13% (−4.4%) / +80% (21.5%)** | 10.8% | 8.6 | **3.5** |
| 14 | UnitedHealth (UNH) | ~$378–382 Oct 9 intraday [M] | 17.1x CY27 adj. (~$22.2, Zacks) vs ~18x (5y NTM median 19.1x, L) | 12% | 2.3 / 1.4 | +54% (15.6%) / −18% (−6.4%) / +81% (21.9%) | 11.7% | 8.5 | 3 |
| 15 | Novo Nordisk (NVO ADR) | $38.18 Oct 8 [M] | ~9.7x vs ~22x (mem) → regime anchor 13x | 2% (L) | ~4.5 (mem L) / small | +42% (12.3%) / −19% (−6.9%) / +116% (29.3%) | 11.8% | 8.3 | 2 |
| 16 | Meta (META) | ~$741.90 Oct 5/6 [M] | 21.8x clean CY27 (~$34) vs ~21x (mem L) | 13% | 0.3 / ~1 (mem) | +43% (12.6%) / −14% (−5.0%) / +85% (22.8%) | 10.8% | 8.3 | 3 |
| 17 | TSMC (TSM ADR) | $453.31 Oct 9 [H] | ~21x NTM ADR (local ~18–19x; ADR premium ~15%) vs ~20x (5y avg fwd 21.8x, L) | 14% | ~1.0 (mem) / 0 | +49% (14.2%) / −22% (−7.9%) / +103% (26.7%) | 11.8% | 7.9 | 3 |
| 18 | Nvidia (NVDA) | ~$220 (calc from "+19% YTD", **L**) | ~14.5x FY28 ($15.6–15.7) vs median not meaningful → anchor 20x | 5% (post-peak) | 0 / ~2 | +38% (11.3%) / −24% (−8.6%) / +143% (34.4%) | 12.1% | 7.8 | 2.5 |
| 19 | Berkshire (BRK.B) | ~$505 Aug 28 (stale) [L] | 1.45x P/B (Aug 17) vs ~1.45x (mem) | 8.5% (BVPS) | 0 / ~0.8 | +28% (8.5%) / 0% (−0.1%) / +47% (13.7%) | 7.7% | 7.6 | 3 |
| 20 | TotalEnergies (TTE ADR) | €78.43 Oct 9 [M] | ~12x **normalised** ($72.5 Brent; calc) / 11x trailing vs ~11.5x (mem) | 5% (norm.) | 4.6 / ~4 | +30% (9.1%) / −10% (−3.5%) / +41% (12.1%) | 6.7% | 4.9 | 2.5 (as a compounder) |
| 21 | ASML (ASML) | ~$1,770 Oct 8 [L; a €1,421 quote also seen] | ~31x CY27 vs ~30x (mem L) | 11% | 0.5 / ~0.7 | +37% (11.0%) / −28% (−10.4%) / +74% (20.2%) | 7.9% | 2.8 | 3 |
| 22 | Samsung Electronics | ₩262,000 Oct 8 [M] | ~3.7x 2027E peak; ~12.6x **normalised** (calc L) | n/m (cyclical) | ~1.5 (mem) | +21% (6.6%) / −27% (−10.0%) / +69% (19.2%), in KRW | 5.6% | 0.6 | 2 |
| — | S&P Global (SPGI) | price not found | ~20–22x vs ~27x "normal" [L] | ~10% (L) | — | not modelled (no price) | — | — | watch |

**Shortlist (ranked by score):** Intuit → Netflix → Uber → Amazon → Microsoft → Visa (or Mastercard) → Medtronic → Elevance → Alphabet (optional 9th).
**Drop for the long horizon:** TotalEnergies (a tactical war hedge, not a compounder), Adobe (AI-factor overlap with Intuit plus a leadership vacuum), and TSMC (peak margins, ADR premium, 2028 digestion risk; first alternate). UnitedHealth stays out, since its bear case once the DOJ tail is included puts it below Elevance.
**Add:** Microsoft, Amazon, Visa/Mastercard, Medtronic and Alphabet.

---

## 1. The model (so the red team can rerun it)

**Formula.** 3-yr total return = (1+g)³ × (PE_exit / PE_now) × (1+d)³ − 1.
- **g:** expected per-share EPS CAGR over the three years *after* the forward-P/E year (≈ FY27→FY30). I use consensus where it exists (usually FY27, sometimes FY28) and my own stated fade beyond that. Using the year after the P/E year avoids double-counting front-loaded growth (AMZN, NFLX, TSM, UNH).
- **Buybacks are already inside per-share g.** I show the buyback yield for information only and do **not** add it again. The brief's "EPS growth + buyback yield" would double-count it.
- **d:** dividend yield.
- **Base PE_exit:** P/E moves **halfway** from today's level to an anchor. The anchor is the ~10-year median forward P/E. Where the business's growth or risk profile has clearly changed, I use an explicit **regime anchor** (flagged "R" in the model; reasons are in each section). Using an AI-victim's 2016–2021 multiple (30–40x) would be indefensible.
- **Bear / bull:** an explicit g and exit P/E for each name (see sections).
- **Expected return:** E[r] = 0.5 × base + 0.25 × bear + 0.25 × bull (annualised).
- **Score:** E[r] − 0.5 × max(0, −bear annual return). This penalises deep bear cases.
- The script is at `scratchpad/scripts/model.py` (rerun with `python3 -I model.py`).

**Robustness.**
1. **Bear-heavy weights (40/35/25).** Every score falls 1.5–3pp. The top-8 order barely changes: Microsoft and Amazon move above Uber, and Visa moves above Adobe.
2. **Rate-regime overlay.** If the US 10-year stays above 5% (5.24% Oct 9) and every anchor is 15% lower, every base return falls ~2–3pp a year. Scores fall 1–2pp, and the ranking holds (Intuit 19.5, MA 13.4, NFLX 13.1, AMZN 12.7, MSFT 12.6, UBER 12.5).
3. **Intuit.** At $322 instead of $291, E[r] falls ~3pp and Intuit is still first. With g = 8% instead of 13%, the base is still ~20% a year.

**What the model does not include (for the India-based investor):**
- **Tax.** LTCG is 12.5% after 24 months. Example: a 16%/yr pre-tax base gives +56% over 3 years, about +49% after tax, or ~14.2%/yr. US dividends carry 25% withholding, creditable via Form 67.
- **FX.** A drift from INR 96.7 to 99 (BMI, Mar-2028) adds about 1%/yr. A peace-deal rally to ~92 costs 4–6% one-off.
- **US estate tax.** It applies to US-situs holdings above ~$60k. **Medtronic is an Irish plc**. Shares of a foreign company are generally not US-situs, but ADR treatment is debated (mem; check with an adviser).

---

## 2. Shortlist: one section per name

### ★1. Intuit (INTU). Conviction 4. Score 21.5
- **Data.**
  - Price $291.08 (Oct 6 intraday) [M] ([ad-hoc-news](https://www.ad-hoc-news.de/boerse/news/corporate-news/intuit-stock-gains-2-25-percent-while-growth-guidance-cools/70243920)). An undated $321.69 appears on TrendSpider and Barchart gives a ~$87.5B market cap [L] ([TrendSpider](https://trendspider.com/markets/symbols/INTU/); [Barchart](https://www.barchart.com/story/news/437217/how-is-intuit-s-stock-performance-compared-to-other-software-application-stocks)). FQ1 results are due **Nov 19** [L].
  - FY27 non-GAAP EPS guide (new basis: **includes** $5.81 of SBC) is $22.88–23.12; consensus $23.07 [H]. GAAP guide $20.12–20.36 [H] ([SEC 8-K](https://www.sec.gov/Archives/edgar/data/0000896878/000089687826000029/fy26q4earningspressrelease.htm)). FY28: KeyCorp $26.84 (+16%; one broker) [L] ([dailypolitical/MarketBeat](https://www.dailypolitical.com/?p=10490006)).
  - FY26: **$5.5B of buybacks** (+96%), $7.9B authorisation left, dividend raised 15% to **$1.38/quarter** ($5.52/yr), cash $7.2B vs debt $7.7B [H] ([10-K FY26](https://www.sec.gov/Archives/edgar/data/0000896878/000089687826000037/intu-20260731.htm)).
- **Valuation.** 12.6x FY27 non-GAAP (incl. SBC), 14.4x GAAP. Shareholder yield ~8.7% (1.9% dividend + 6.8% buyback, calc on ~$81B).
- **Inputs.**
  - Base: g 13%. P/E 12.6x → 16.3x (halfway to a **regime anchor of 20x**, roughly the market multiple for a ~13% grower). The old ~33x median is not used.
  - Bear: g 5% (net income roughly flat, buybacks only), P/E 10x.
  - Bull: g 16%, P/E 20x.
- **Thesis.** A ~13% EPS compounder priced as if in structural decline. Even at flat net income, the 6–7% buyback yield and ~2% dividend give about 8%/yr, which is why the bear case is only ~−1%/yr. QuickBooks/GBS is guided +13–14% [H].
- **Moat versus 2027–29 threats.**
  - AI tax agents threaten DIY TurboTax at the low end: units fell 2% and Intuit "lost on price" under $50k [H, prior work]. TurboTax is guided at only +2–3% for FY27 [H].
  - The core of the moat (SMB ledger, payroll and payments data, plus filing liability) is stickier than a seat licence.
  - Durability: **medium**.
- **Monitor yearly:**
  1. GBS/QuickBooks Online ecosystem revenue growth (≥12%).
  2. TurboTax units and revenue at the May tax-season report.
- **Sell if** GBS growth falls below 10% for two quarters, or TurboTax revenue declines while buybacks are cut.

### ★2. Netflix (NFLX). Conviction 3. Score 14.8
- **Data.**
  - $71.57 (Oct 8) [M]. Consensus EPS: **2026 $3.59, which includes the ~$0.5 WBD fee → clean ~$3.08 (calc)**; 2027 $3.83 (range $3.58–4.40, 35 analysts); 2028 $4.56 (28 analysts) [L] ([Tickflow](https://tickflow.io/stock/NFLX/forecast); [MarketBeat/Erste $3.82](https://www.marketbeat.com/instant-alerts/erste-group-bank-decreases-earnings-estimates-for-netflix-2026-07-29/)).
  - The fee and the $12.5B FCF guide are in the Q1 letter [H] ([SEC](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000137/ex991_q126.htm)). Q3 results Oct 20 [H].
- **Valuation.** 18.7x clean 2027; 15.7x 2028 (calc). About 28x underlying FCF (red team).
- **Inputs.**
  - Base: g 15% (2028 +19% per consensus, then 15% and 13%). P/E 18.7x → 20.4x (**regime anchor 22x**; the 10-year median of ~40–90x comes from the pre-profit era and is not used).
  - Bear: g 7%, P/E 14x.
  - Bull: g 19%, P/E 25x.
- **Thesis.** Margin expansion (31.5% in 2026), ads doubling to ~$3B, and buybacks (~$4.7B in Q2) produce high-teens EPS growth at a market multiple.
- **Threats.** Engagement erosion to YouTube, short-form and AI video. Wells sees hours per member −4% in H2 [M]. Engagement data will be disclosed only once a year from 2027. Durability: **medium**.
- **Monitor yearly:**
  1. Revenue growth and the operating-margin guide each January.
  2. Ad revenue, plus the annual "What We Watched" view hours.
- **Sell if** revenue growth falls below 8% or the margin guide stops expanding, or if Netflix attempts another large acquisition.

### ★3. Uber (UBER). Conviction 3. Score 14.3 (lowest data confidence on the list)
- **Data.**
  - $70.24 (Oct 8) [M]. Adjusted EPS consensus is muddled: FY26 $2.97 → **FY27 $4.43 (+49%)** per Barchart; Tickflow uses a different basis [L] ([Barchart](https://www.barchart.com/story/news/3334045/earnings-preview-what-to-expect-from-uber-technologies-report); [Tickflow](https://tickflow.io/stock/UBER/forecast)).
  - TTM FCF is above $10B. SBC is ~$1.9B (mem), so P/FCF after SBC is ~17.5x (calc).
  - The Delivery Hero tender (~$14.8B, €14B bridge, close H2-2027) is confirmed [M] ([The Star](https://www.thestar.com.my/business/business-news/2026/07/16/uber-launches-us148bil-offer-for-delivery-hero-to-create-global-platform)). So is Waymo's own app in Austin and Atlanta from Jan-2028 [M] ([TNW](https://thenextweb.com/news/waymo-uber-exclusivity-ends-austin-atlanta-robotaxi)).
- **Inputs.**
  - Base: g 17% (cross-checked against FCF/share growth of ~15%). P/E 15.9x → 17.9x (anchor 20x).
  - Bear: g 5% (AV operators go direct in top cities; leverage from Delivery Hero), P/E 11x.
  - Bull: g 21%, P/E 22x.
- **Thesis.** Uber is the demand aggregator across 15+ AV partners, and bookings grow ~18–22%. The 2028 Waymo date falls **inside** the holding period, so this is a sizing and conviction issue.
- **Threats.** AV disintermediation (**high**, 2028–29), plus driver-classification rules. Durability: **medium-low**.
- **Monitor yearly:**
  1. Gross-bookings growth (≥15%) and FCF after SBC.
  2. Trip trends in the Waymo- and Tesla-direct cities.
- **Sell if** bookings growth stays below 12% for two quarters, gross leverage stays above ~2.5x after the Delivery Hero close, or trip share falls in AV-direct cities.

### ★4. Amazon (AMZN). Conviction 3.5. Score 14.2
- **Data.**
  - $259.92 (Oct 7) [M]. **Q2-26 GAAP EPS of $5.75 includes a ~$53.4B pre-tax Anthropic revaluation gain; clean ~$1.88** [M] ([FourWeekMBA](https://fourweekmba.com/ai-amazon-aws-q2-2026-anthropic-gain-ai-infrastructure/); [TheWrap](https://www.thewrap.com/industry-news/business/amazon-earnings-q2-2026/)). Operating income $27.5B (+43%).
  - Consensus (ex-gains) 2026 ~$7.76; **2027 $10.09–10.47** (52 analysts; 8 upward revisions in 30 days) [M] ([24/7 Wall St, 2026-09-24](https://247wallst.com/investing/2026/09/24/amazon-stock-could-have-another-big-run-ahead-heres-my-2027-price-prediction/); [Tickflow](https://tickflow.io/stock/AMZN/forecast)). 2028 consensus not found.
  - AWS +37%. Capex ~$220B. TTM FCF −$7.6B [M] (team macro brief).
- **Inputs.**
  - Base: g 17% (2028 +20%, then 17% and 15%; my fade). P/E flat at ~25x (regime anchor 25x; the 10-year median is distorted by the reinvestment era).
  - Bear: g 8%, P/E 19x.
  - Bull: g 21%, P/E 30x.
- **Thesis.** AWS has re-accelerated with a $496B backlog. Ads and retail margins are rising, and capex digestion would turn FCF positive.
- **Threats.** AI capex not earning its cost of capital (FCF negative); an FTC antitrust trial (mem, date not verified). Durability: **high**.
- **Monitor yearly:**
  1. AWS growth (≥25%).
  2. FCF turning positive by 2028.
- **Sell if** AWS growth falls below 15% while capex keeps rising, or FCF is still negative through 2028.

### ★5. Microsoft (MSFT). Conviction 4. Score 14.1
- **Data.**
  - $535.07 (Oct 9) [M] (StockAnalysis via team). FY26 revenue $331.8B (+17.8%); Q4 non-GAAP EPS $4.74 vs $4.24 [M] ([S&P Global MI](https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/08/microsoft-postq-azure-usd100b-milestone-as-ai-demand-lifts-earnings-and-outlook); [beancount](https://beancount.io/blog/2026/07/29/microsoft-fy2026-earnings-analysis)).
  - Azure +43% cc; above $100B for the year; FQ1 guide ~+45% [M].
  - **FY27 EPS consensus ~$19.5–19.7; FY28 ~$23.0–23.25** (29 analysts) [M] ([Trefis 08-21](https://www.trefis.com/articles/612403/microsoft-stock-gets-cheaper-only-if-the-forecast-arrives/2026-08-21); [Trefis 09-23](https://www.trefis.com/articles/616304/what-microsofts-trailing-multiple-leaves-out/2026-09-23); [FutureSearch](https://futuresearch.ai/app/p/a/msft-2027-08-04)).
  - 10-year median trailing P/E 31.5 (Wisesheets) [M] ([Wisesheets](https://wisesheets.io/pe-ratio/MSFT)).
- **Inputs.**
  - Base: g 15% (FY28 +18% per consensus, then 14% and 13%). P/E 26.4x → 26.7x (anchor ~27x forward-equivalent).
  - Bear: g 9%, P/E 20x.
  - Bull: g 18%, P/E 30x.
- **Thesis.** Microsoft owns both the AI infrastructure layer and the agent layer that threatens seat software. Its return is roughly its earnings growth, with a bear case near zero.
- **Threats.**
  - Capex digestion (~$175B in CY26 [M]).
  - Copilot seat pricing.
  - OpenAI dependence.
  - Durability: **high**.
- **Monitor yearly:**
  1. Azure growth (≥25%).
  2. Capex intensity versus commercial RPO growth.
- **Sell if** Azure growth falls below 20% while capex/revenue keeps rising, or the P/E goes above ~35x.

### ★6. Visa (V), or Mastercard. Conviction 4. Score 12.7 (MA 15.1, on weaker inputs)
- **Data.**
  - ~$376 (Oct 8) [M]. FQ3 FY26: net revenue $11.6B (+14%); non-GAAP EPS $3.32; payments volume +10% (passed $4T); cross-border +13% [H] ([SEC 8-K](https://www.sec.gov/Archives/edgar/data/0001403161/000140316126000103/q32026earningsrelease.htm); [Quartz](https://qz.com/visa-fiscal-q3-2026-earnings-revenue-growth-072826)).
  - FY26 guide: EPS growth at the low end of mid-teens [H]. **FY27 consensus $14.94 (+13.7%)** [M] ([Eastern Progress/Zacks](https://www.easternprogress.com/wall-street-raises-visa-outlook-after-strong-q3-buy-hold-or-sell/article_bf7007ff-bc8b-5f31-bbe3-0eb413b46ec1.html)).
  - Forward P/E 25.6 (Aug 25) [M] ([GuruFocus](https://www.gurufocus.com/term/forward-pe-ratio/V)). 5-year average trailing P/E ~32x [L] ([VCP Scanner](https://www.vcpscanner.com/stock/v/pe-history)).
  - $20B buyback [M] ([TIKR](https://www.tikr.com/de/blog/why-visa-stock-looks-undervalued-after-a-17-revenue-beat-and-a-20-billion-buyback)).
- **Inputs.**
  - Base: g 12%. P/E 25.2x → 26.6x (anchor 28x).
  - Bear: g 8%, P/E 20x.
  - Bull: g 14%, P/E 29x.
- **Thesis.** A toll road on nominal spending. Its 2026 de-rating (~25x vs ~28x history) is an entry point, and the bear case is still positive (+0.7%/yr).
- **Threats.**
  - The DOJ debit suit continues; the shareholder suit was dismissed Jun 30, 2026 [M] ([Bloomberg Law](https://news.bloomberglaw.com/litigation/visa-escapes-shareholder-class-suit-over-doj-antitrust-complaint)).
  - Credit Card Competition Act (status not verified).
  - Stablecoin / account-to-account rails. Agentic commerce still runs on card credentials (judgment).
  - Durability: **high**.
- **Mastercard** has slightly faster growth and no DOJ debit suit. Its price and consensus were not verified here (forward P/E 24.6, Oct 6 [M]). **Hold one of the two.**
- **Monitor yearly:**
  1. Net revenue growth (≥9%).
  2. Cross-border volume growth.
- **Sell if** interchange-cap or routing legislation passes, or net revenue growth falls below 7%.

### ★7. Medtronic (MDT). Conviction 3.5. Score 10.5 (the most defensive bear case on the list)
- **Data.**
  - $93.29 (Sep 2) [M]. A German report says the stock fell 3.6% in the 30 days to Oct 9, so the price is likely ~$90 (calc, L) ([boerse-global](https://www.boerse-global.de/medtronic-aktie-fda-gibt-ligasure-fuer-hugo-frei/830399)).
  - Q1 FY27: revenue $9.76B (+13.7%, inflated by an extra week). **FY27 organic growth guide raised to 7.25–7.75%; non-GAAP EPS $5.94–6.00**; cardiac ablation +88% [H] ([Medtronic PR, 2026-09-01](https://news.medtronic.com/2026-09-01-Medtronic-reports-first-quarter-fiscal-2027-results-delivers-broad-based-portfolio-performance-and-raises-fiscal-2027-guidance)).
  - The MiniMed split-off exchange offer was scheduled to end Oct 9; the outcome is not verified [M]. If completed, it retires Medtronic shares (calc: accretive).
- **Inputs.**
  - Base: g 7.5%, dividend 3.0%. P/E 15.6x → 16.3x (anchor ~17x, mem L).
  - Bear: g 3%, P/E 13x.
  - Bull: g 9%, P/E 18x.
- **Thesis.** Pulsed-field ablation (Affera) and renal denervation lift growth from ~4% to ~6–7%, at a below-history multiple, with a 48-year dividend-growth record. No AI, oil or managed-care exposure, and possibly not US-situs for estate tax.
- **Threats.** Medtech tariffs, China volume-based procurement, PFA competition from BSX and J&J. Durability: **high**.
- **Monitor yearly:**
  1. Organic growth (≥5%).
  2. Cardiac-ablation revenue (on track for ~$1B).
- **Sell if** organic growth falls below 4% and EPS growth below 5%.

### ★8. Elevance (ELV). Conviction 3. Score 9.5
- **Data.**
  - $400.09 (Oct 6) [M]. 2026 adjusted EPS guide **≥$27.00** [H] (team SEC). Management is "confident" of **≥12% adjusted EPS growth in 2027** [M] ([Newsquawk](https://www.newsquawk.com/headlines/elevance-elv-notes-that-it-remains-confident-in-returning-to-at-least-12-adjusted-eps-growth-in-2027-citing-progress-across-the-portfolio)).
  - Zacks FY27 $28.83 / FY28 $32.49 [L] ([MarketBeat](https://www.marketbeat.com/instant-alerts/zacks-research-forecasts-lower-earnings-for-elevance-health-2026-07-30/)). Q3 results Oct 21 [H].
- **Inputs.**
  - Base: g 11%, dividend 1.7%. P/E 13.6x → 13.8x.
  - Bear: g 4%, P/E 10.5x.
  - Bull: g 13%, P/E 15.5x.
- **Thesis.** Margin recovery from a Medicaid trough (−1.75%) and Medicare Advantage repair, at ~13.6x.
- **Threats.**
  - The enhanced ACA subsidies **have lapsed**. Exchange enrollment fell from ~22M to ~19M, and insurers are seeking a **+14–15% median 2027 rate rise** [M] ([KFF Health News](https://kffhealthnews.org/insurance/priced-out-obamacare-affordable-care-act-aca-premium-increases-peterson-kff/)).
  - Medicaid acuity and eligibility changes from 2027 (mem).
  - Durability: **medium**.
- **Why Elevance rather than UNH.** On base inputs UNH scores higher (11.1). Once a DOJ settlement and the 2028 PBM-delinking hit are put in UNH's bear case (g 3%, 12x), its score drops to **8.5**, and Elevance is cheaper (13.6x vs 17.1x). Hold **one** managed-care name.
- **Monitor yearly:**
  1. Adjusted EPS against the ≥12% 2027 target.
  2. Medicaid operating margin.
- **Sell if** 2027 EPS growth is below 8% or the benefit-expense ratio stays above ~91.5%.

### ★9 (optional). Alphabet (GOOGL). Conviction 3.5. Score 8.6
- **Data.**
  - $348.29 (Oct 8) [M]. **Clean 2027 EPS ~$14.7–15.4** (Erste $14.74; S&P Global's ~24x consensus 2027 P/E) [M/L] ([S&P Global MI](https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/07/alphabet-earnings-preview-q2-2026); [MarketBeat](https://www.marketbeat.com/instant-alerts/alphabet-fy2027-eps-estimate-boosted-by-erste-group-bank-2026-07-29/)). The headline $19.79 includes the ~$98B equity gain.
  - Q2-26: revenue $119.8B (+24%); Search +17%; Cloud **+82%** to $24.8B; Gemini 950M MAU [M] ([MarketBeat](https://www.marketbeat.com/instant-alerts/alphabet-q2-earnings-call-highlights-2026-07-22/); [the-decoder](https://the-decoder.com/google-ceo-pichai-says-geminis-next-leap-depends-on-building-much-larger-base-models/)).
  - Capex $195–205B. 10-year median trailing P/E 26.2 (Wisesheets) / 27.55 (GuruFocus) [M] ([Wisesheets](https://www.wisesheets.io/pe-ratio/GOOGL); [GuruFocus](https://www.gurufocus.com/term/pettm/GOOG)).
- **Inputs.**
  - Base: g 13%. P/E flat at ~23x.
  - Bear: g 6%, P/E 17x.
  - Bull: g 17%, P/E 26x.
- **Thesis.** The "AI kills search" fear is not showing in the numbers (Search +17%). Cloud is a second engine, and **Waymo hedges the Uber position**.
- **Threats.**
  - Ad-tech remedy (Sep 2, 2026): **no divestiture**; a 6-year behavioural decree [M] ([The Star](https://www.thestar.com.my/tech/tech-news/2026/09/17/google-should-relax-ad-tech-rules-appoint-antitrust-monitor-us-judge-finds)). The search case is under cross-appeal.
  - Depreciation from capex.
  - Durability: **high**.
- Optional only: at ~23x it is fair, not cheap.
- **Monitor yearly:**
  1. Search revenue growth (≥8%).
  2. FCF turning positive again.
- **Sell if** Search growth falls below 5% for two quarters, or FCF is still negative through 2028.

**Indicative weights within the global sleeve:** INTU 15, MSFT 15, V 13, AMZN 12, NFLX 10, MDT 10, ELV 9, GOOGL 8, UBER 8.
- AI-seat-victim exposure is INTU only: 15% of the sleeve, ~3.75% of total at a 25% sleeve. With TCS and Infosys that is still under the 15–18% cap.
- AI-capex spenders (MSFT, AMZN, GOOGL): 35%.
- Non-AI (V, MDT, ELV): 32%.

---

## 3. Names not shortlisted (with reasons)

- **Adobe (score 13.3, conviction 2.5): drop for the long horizon.**
  - The numbers screen well: 9.2x non-GAAP, ~10% buyback yield [M] ([Seeking Alpha FY27 $26.39](https://seekingalpha.com/article/4909004-adobe-stock-free-cash-flow-machine-in-full-gear); [TIKR $25B buyback](https://www.tikr.com/blog/adobe-stock-is-down-24-in-2026-does-the-25-billion-buyback-change-the-math)).
  - But generative AI is the most direct substitute threat on the list. CEO, CFO and creative head all change within a year. And it is the same factor as Intuit.
  - Consensus EPS growth of only ~8%/yr (FY26 ~$24 → FY30 ~$33 [L]) comes mostly from buybacks.
- **TSMC (7.9): demote to first alternate.**
  - Consensus EPS NT$99.5 (2026) → NT$116.6 (2027); Citi/GS NT$125–131 (2027) and ~NT$165 (2028) [M] ([UDN](https://money.udn.com/money/story/5607/9412563); [LTN](https://ec.ltn.com.tw/article/breakingnews/5594511)). JPM sees 2027 USD revenue growth above 20% [M].
  - The bear case is −22% over 3 years: a 2028 digestion after ~$1T of hyperscaler capex in 2027, peak 66–69% gross margins, and an ADR premium (~15%) that Indian investors cannot avoid. Buy only below ~$360 (~16–17x).
- **TotalEnergies (4.9): drop as a 2–3 year holding.**
  - On normalised ($72.5 Brent) earnings it returns ~9%/yr in the base case, mostly from dividends and buybacks.
  - Its value as a war hedge decays, and a peace deal is a double loss for an INR investor (oil plus rupee). It is a tactical hedge only. If already bought, hold to a ceasefire or to the 24-month mark.
- **UnitedHealth (8.5 after the DOJ tail).** Zacks puts FY27 at $22.16 and FY28 at $25.69 [L] ([MarketBeat](https://www.marketbeat.com/instant-alerts/zacks-research-issues-positive-forecast-for-unh-earnings-2026-07-31/)). It is the managed-care alternate. Switch only if Q3 (Oct 13) and the 2027 commentary show the cost trend bending.
- **Mastercard (15.1).** A substitute for Visa (see ★6).
- **Booking (11.2).**
  - ~16x NTM vs ~20x 5-year average after the Sep-8 AI-agent scare [M] ([TIKR, 2026-09-09](https://www.tikr.com/blog/booking-holdings-ceo-says-the-ai-fear-is-wrong-heres-where-the-stock-could-go-from-16x-earnings)). The price is stale.
  - It is another AI-intermediation victim. Alternate to Intuit, not in addition.
- **Salesforce (8.8).**
  - FY27 consensus jumped from $14.13 to $16.76 on Anthropic gains [M] ([24/7 Wall St, 2026-09-29](https://247wallst.com/investing/2026/09/29/salesforce-is-down-double-digits-this-year-our-model-sees-48-upside/)). On clean EPS it is ~16x for ~7% organic growth.
  - Same AI-seat factor as Intuit.
- **Meta (8.3).**
  - ~$742 [M] ([ChartMill via Money365](https://www.money365.market/news/latest/meta-platforms-shares-rise-1-90-as-quality-screen-highlights-1b790540)). Q2 EPS of $6.18 included ~$1.17 of legal and severance charges [M] ([INDmoney](https://www.indmoney.com/blog/us-stocks/why-meta-stock-fell-q2-earnings-analysis)).
  - ~22x clean 2027 is fair, with capex of $135–145B rising toward ~$205B (Citi) in 2027.
- **Novo Nordisk (8.3).**
  - The 2026 guide is a **decline** of 0% to −6% at CER [M] ([Inderes](https://www.inderes.dk/en/analyst-comments/hca-redflag-novo-nordisk-ai-1)). This settles the open question in the team's earlier work.
  - Medicare's negotiated Ozempic price is **$274/month vs a $959 list** from 2027, and Novo is cutting list prices by up to 50% on Jan 1, 2027 [M] ([Fierce Healthcare](https://www.fiercehealthcare.com/pharma/medicare-unveils-price-reductions-15-drugs-including-novos-semaglutide); [KTVU](https://www.ktvu.com/news/novo-nordisk-slash-list-prices-ozempic-wegovy-up-50)). Citi's 2027 EPS is 7% below consensus [M].
  - A value trap until 2027 pricing is visible.
- **Nvidia (7.8).**
  - FY28 consensus $15.5–15.7, ~14.5–17x [M] ([24/7 Wall St, 2026-09-29](https://247wallst.com/investing/2026/09/29/nvidia-stock-is-at-its-cheapest-valuation-since-2015/)). Price not verified.
  - It is peak-cycle AI hardware and overlaps with TSMC. The bear case is −24%.
- **Berkshire (7.6).**
  - 1.45x book (Aug 17) [L] ([Pluang](https://pluang.com/en/news-feed/berkshire-hathaway-sinyal-beli-dari-buffett-pembaruan-rating)). Q2 operating earnings $12.98B (+16%); $4.5B Q2 buyback [M] ([Morningstar](https://www.morningstar.com/stocks/berkshire-hathaway-earnings-cash-balances-retreat-increased-investments-share-buybacks-q2)).
  - About 8% a year with ~0% bear downside. Use it as a cash alternative, not a compounder.
- **ASML (2.8).**
  - The 2026 sales guide was raised to €43–45B; consensus sees ~28% 2027 sales growth; the 2027 EUV book is "full" (JPM) [M] ([Börse Express](https://www.boerse-express.com/news/articles/asml-43-bis-45-milliarden-umsatz-2026-angepeilt-934961); [Proactive](https://www.proactiveinvestors.co.uk/a/45352134/jp-morgan-expects-asml-to-signal-strong-2027-demand-as-stock-trades-at-u)).
  - At ~31x 2027 after +66% YTD, a digestion bear case gives −28%. Q3 results (~Oct 14–15) should bring the first 2027 guide.
- **Samsung (0.6).**
  - On normalised operating profit of ₩150–200T it trades at ~12–13x, plus a ₩400T+ cash build (calc L).
  - The pattern of memory stocks peaking before earnings, plus difficult LRS access (London GDR), keep it out.

---

## 4. Moat durability against the main 2027–2029 threats

| Name | AI disruption of seats/intermediation | AI capex digestion | Regulation / antitrust | Drug / healthcare pricing | Overall |
|---|---|---|---|---|---|
| Intuit | **High** (DIY tax agents) / medium (QuickBooks) | — | IRS Direct File (mem) | — | Medium |
| Netflix | Medium (AI video, YouTube) | — | Low | — | Medium |
| Uber | **High** (AV direct apps from 2028) | — | Medium (labour, AV rules) | — | Medium-low |
| Amazon | Low | Medium (FCF −) | Medium (FTC, mem) | — | High |
| Microsoft | Medium (M365 seats) but owns the agent layer | Medium | Low-medium | — | High |
| Visa / MA | Low (agentic commerce uses card rails, judgment) | — | **Medium** (DOJ debit suit, CCCA) | — | High |
| Medtronic | — | — | Low (tariffs, China VBP) | Low-medium | High |
| Elevance | — | — | **High** (Medicaid, ACA) | Medium (MA rates) | Medium |
| Alphabet | Medium (answer engines) | Medium | Medium → lower (behavioural remedies) | — | High |
| Adobe | **Very high** | — | Low | — | Low-medium |
| TSMC / ASML / NVDA / Samsung | — | **High** | Medium (Taiwan, tariffs, export controls) | — | High moat, cyclical earnings |
| UNH | — | — | **High** (DOJ, PBM delinking 2028) | Medium | Medium |
| Novo | — | — | — | **Very high** (2027 Medicare price; 50% list cut) | Low-medium |

---

## 5. Drop / add versus the near-term plan (`FINAL_RECOMMENDATIONS.md`)

| Near-term name | 2–3 year verdict | Why |
|---|---|---|
| Intuit | **Keep; largest position** | Highest score; ~8.7% shareholder yield caps the downside |
| Netflix | **Keep; upgrade to full size after Q3** | High-teens EPS growth at ~19x; the 3-year bear case is only −8% |
| Uber | **Keep, small** | Good math, but the AV date sits inside the window |
| Elevance | **Keep** (the single managed-care slot) | Cheapest managed-care name; UNH is the alternate |
| TSMC | **Drop to alternate** | Bear −22%; peak margins; ADR premium |
| Adobe | **Drop** | AI substitution, leadership vacuum, duplicates the Intuit factor |
| TotalEnergies | **Drop as a compounder** (tactical hedge only) | Hedge value decays; double loss on peace |
| UnitedHealth | **Stays dropped** (alternate) | DOJ/PBM tail puts it below Elevance |
| — | **Add Microsoft, Amazon, Visa (or MA), Medtronic; Alphabet optional** | Durable compounders where a flat multiple still gives ~14–17%/yr |

**Tax interaction.** Any name already bought under the near-term plan should, where possible, be held to the 24-month LTCG date unless a sell condition triggers. Selling earlier is taxed at slab rates (up to ~39%).

---

## 6. Open data issues for the red team

1. **Stale or unverified prices:**
   - MDT (Sep 2), BKNG (Sep 9), BRK.B (Aug 28), NVDA (no direct quote), MA (none).
   - INTU: $291 (Oct 6) vs an undated $322.
   - ASML: $1,770 vs an undated €1,421.
2. **10-year medians verified via search:** GOOGL, MSFT (trailing), V (5-year), CRM (5-year forward), BKNG (5-year forward), UNH (5-year NTM), TSM (5-year forward). **All others are from memory [L].**
3. **Consensus beyond FY27/FY28 is my fade assumption for every name.** Single-broker inputs: INTU FY28 (KeyCorp), ELV and UNH 2027–28 (Zacks).
4. **Uber's EPS basis is inconsistent across providers**; the FCF cross-check is used.
5. **TTE is modelled on normalised earnings** (team calc, [L]); the ADR price in USD is not verified.

---

## Sources (all seen only as WebSearch summaries; none opened)

**Model inputs: new this round**
- MSFT: https://www.trefis.com/articles/612403/microsoft-stock-gets-cheaper-only-if-the-forecast-arrives/2026-08-21 · https://www.trefis.com/articles/616304/what-microsofts-trailing-multiple-leaves-out/2026-09-23 · https://futuresearch.ai/app/p/a/msft-2027-08-04 · https://simplywall.st/stocks/us/software/nasdaq-msft/microsoft/news/microsoft-corporation-just-beat-analyst-forecasts-and-analys/amp · https://wisesheets.io/pe-ratio/MSFT · https://www.gurufocus.com/term/forward-pe-ratio/MSFT · https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/08/microsoft-postq-azure-usd100b-milestone-as-ai-demand-lifts-earnings-and-outlook · https://beancount.io/blog/2026/07/29/microsoft-fy2026-earnings-analysis · https://www.tradingpedia.com/2026/07/30/microsoft-climbs-as-cloud-business-powers-earnings/
- GOOGL: https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/07/alphabet-earnings-preview-q2-2026 · https://www.marketbeat.com/instant-alerts/alphabet-fy2027-eps-estimate-boosted-by-erste-group-bank-2026-07-29/ · https://www.vcpscanner.com/valuation/googl/estimates · https://www.wisesheets.io/pe-ratio/GOOGL · https://www.gurufocus.com/term/pettm/GOOG · https://www.marketbeat.com/instant-alerts/alphabet-q2-earnings-call-highlights-2026-07-22/ · https://the-decoder.com/google-ceo-pichai-says-geminis-next-leap-depends-on-building-much-larger-base-models/ · https://blog.google/company-news/inside-google/message-ceo/alphabet-earnings-q2-2026/ · https://www.thestar.com.my/tech/tech-news/2026/09/17/google-should-relax-ad-tech-rules-appoint-antitrust-monitor-us-judge-finds · https://ppc.land/google-faces-six-year-worldwide-ad-tech-decree-instead-of-adx-sale/
- AMZN: https://247wallst.com/investing/2026/09/24/amazon-stock-could-have-another-big-run-ahead-heres-my-2027-price-prediction/ · https://www.barchart.com/story/news/3205360/here-s-what-to-expect-from-amazon-com-s-next-earnings-report · https://tickflow.io/stock/AMZN/forecast · https://fourweekmba.com/ai-amazon-aws-q2-2026-anthropic-gain-ai-infrastructure/ · https://www.thewrap.com/industry-news/business/amazon-earnings-q2-2026/ · https://beancount.io/blog/2026/07/31/amazon-fy2026-q2-earnings-analysis
- META: https://www.money365.market/news/latest/meta-platforms-shares-rise-1-90-as-quality-screen-highlights-1b790540 · https://www.google.com/finance/quote/META:NASDAQ?fstype=ii · https://beta.earningswhispers.com/go/x/META · https://www.marketbeat.com/stocks/NASDAQ/FB/earnings/ · https://www.indmoney.com/blog/us-stocks/why-meta-stock-fell-q2-earnings-analysis · https://kalkine.com/news/technology/why-is-meta-platforms-nasdaqmeta-stock-falling-9-pre-market-today · https://www.xtb.com/en/market-analysis/meta-drops-8-despite-strong-revenue-growth · https://gurufocus.com/term/pettm/META
- V / MA: https://www.sec.gov/Archives/edgar/data/0001403161/000140316126000103/q32026earningsrelease.htm · https://qz.com/visa-fiscal-q3-2026-earnings-revenue-growth-072826 · https://www.easternprogress.com/wall-street-raises-visa-outlook-after-strong-q3-buy-hold-or-sell/article_bf7007ff-bc8b-5f31-bbe3-0eb413b46ec1.html · https://www.tikr.com/de/blog/why-visa-stock-looks-undervalued-after-a-17-revenue-beat-and-a-20-billion-buyback · https://www.gurufocus.com/term/forward-pe-ratio/V · https://www.vcpscanner.com/stock/v/pe-history · https://news.bloomberglaw.com/litigation/visa-escapes-shareholder-class-suit-over-doj-antitrust-complaint · https://www.gurufocus.com/term/forward-pe-ratio/MA
- ASML: https://www.boerse-express.com/news/articles/asml-43-bis-45-milliarden-umsatz-2026-angepeilt-934961 · https://www.proactiveinvestors.co.uk/a/45352134/jp-morgan-expects-asml-to-signal-strong-2027-demand-as-stock-trades-at-u · https://ioplus.nl/en/posts/asml-beats-forecasts-lifts-outlook-as-ai-demand-surges- · https://global.morningstar.com/en-nd/stocks/asml-earnings-long-term-prospects-vastly-improved · https://www.marketbeat.com/instant-alerts/fy2026-earnings-estimate-for-asml-issued-by-erste-group-bank-2026-07-31/
- MDT: https://news.medtronic.com/2026-09-01-Medtronic-reports-first-quarter-fiscal-2027-results-delivers-broad-based-portfolio-performance-and-raises-fiscal-2027-guidance · https://pulse2.com/medtronic-revenue-rises-13-7-to-9-76-billion-as-broad-based-growth-drives-higher-fiscal-2027-outlook/ · https://www.boerse-global.de/medtronic-aktie-fda-gibt-ligasure-fuer-hugo-frei/830399 · https://www.quiverquant.com/news/Medtronic+Rises+as+MiniMed+Split-Off+Exchange+Ratio+Nears+Completion · https://www.mexc.com/stocks/mdt · https://equibles.com/stocks/MDT · https://upstox.com/us-stocks/mdt-share-price/
- NVO: https://www.inderes.dk/en/analyst-comments/hca-redflag-novo-nordisk-ai-1 · https://www.boerse-express.com/news/articles/novo-nordisk-aktie-citi-hebt-kursziel-auf-330-kronen-930366 · https://www.fiercehealthcare.com/pharma/medicare-unveils-price-reductions-15-drugs-including-novos-semaglutide · https://www.ktvu.com/news/novo-nordisk-slash-list-prices-ozempic-wegovy-up-50
- BRK: https://www.morningstar.com/stocks/berkshire-hathaway-earnings-cash-balances-retreat-increased-investments-share-buybacks-q2 · https://www.vermoegenszentrum.ch/en/stock-exchange-and-markets/news/berkshire-q2-fy26-net-earnings-more-doubled-usd-2567-billion · https://pluang.com/en/news-feed/berkshire-hathaway-sinyal-beli-dari-buffett-pembaruan-rating · https://www.syfe.com/stocks/us/BRK.B
- TSMC: https://money.udn.com/money/story/5607/9412563 · https://ec.ltn.com.tw/article/breakingnews/5594511 · https://newtalk.tw/news/view/2026-06-23/1042759 · https://nz.finance.yahoo.com/news/tsmc-tsm-gets-price-target-210710185.html · https://www.itiger.com/news/1164473817
- UBER: https://www.barchart.com/story/news/3334045/earnings-preview-what-to-expect-from-uber-technologies-report · https://tickflow.io/stock/UBER/forecast · https://vcpscanner.com/valuation/uber/estimates
- NFLX: https://tickflow.io/stock/NFLX/forecast · https://www.marketbeat.com/instant-alerts/erste-group-bank-decreases-earnings-estimates-for-netflix-2026-07-29/
- INTU: https://www.sec.gov/Archives/edgar/data/0000896878/000089687826000037/intu-20260731.htm · https://www.dailypolitical.com/?p=10490006 · https://www.itiger.com/news/1125135160 · https://beancount.io/blog/2026/09/13/intuit-fy2026-earnings-analysis · https://trendspider.com/markets/symbols/INTU/ · https://www.barchart.com/story/news/437217/how-is-intuit-s-stock-performance-compared-to-other-software-application-stocks
- ADBE: https://seekingalpha.com/article/4909004-adobe-stock-free-cash-flow-machine-in-full-gear · https://www.tikr.com/blog/adobe-stock-is-down-24-in-2026-does-the-25-billion-buyback-change-the-math · https://www.tikr.com/blog/adobe-stock-2026-outlook-q2-earnings-on-june-11-and-a-25-billion-buyback-in-place
- CRM: https://247wallst.com/investing/2026/09/29/salesforce-is-down-double-digits-this-year-our-model-sees-48-upside/ · https://www.tikr.com/blog/salesforce-stock-prediction-where-analysts-see-the-stock-going-by-2028 · https://valueinvesting.io/CRM/metric/forward-pe
- ELV / UNH / ACA: https://www.marketbeat.com/instant-alerts/zacks-research-forecasts-lower-earnings-for-elevance-health-2026-07-30/ · https://www.newsquawk.com/headlines/elevance-elv-notes-that-it-remains-confident-in-returning-to-at-least-12-adjusted-eps-growth-in-2027-citing-progress-across-the-portfolio · https://www.tikr.com/blog/elevance-health-stock-analysis-guidance-raised-to-27-street-high-at-498-tikr-target-at-534 · https://www.marketbeat.com/instant-alerts/zacks-research-issues-positive-forecast-for-unh-earnings-2026-07-31/ · https://www.marketbeat.com/instant-alerts/what-is-zacks-researchs-estimate-for-unh-q3-earnings-2026-08-20/ · https://kffhealthnews.org/insurance/priced-out-obamacare-affordable-care-act-aca-premium-increases-peterson-kff/ · https://modernaction.io/briefing/aca-insurers-seek-2027-premium-hikes-as-subsidy-pressure-ret-636eb280
- Other: https://247wallst.com/investing/2026/09/29/nvidia-stock-is-at-its-cheapest-valuation-since-2015/ · https://parameter.io/nvidia-nvda-stock-approaches-all-time-peak-following-historic-150b-share-repurchase/ · https://www.tikr.com/blog/nvidia-stock-is-up-19-in-2026-time-to-sell-or-load-up · https://www.tikr.com/blog/booking-holdings-ceo-says-the-ai-fear-is-wrong-heres-where-the-stock-could-go-from-16x-earnings · https://www.simplywall.st/narratives/wkaxahhl-the-algorithm-vs-the-agent-bookings-post-disintermediation-defense · https://www.investing.com/news/economy-news/sp-global-forecasts-2026-profit-below-estimates-shares-plunge-4496477 · https://stockchase.com/SPGI-N/page/1

**Reused from team files (original URLs)**
- Prices: MSFT, TSM, CRM https://stockanalysis.com/stocks/msft/ · https://stockanalysis.com/stocks/tsm/ · https://stockanalysis.com/stocks/crm/ ; NFLX https://stockinvest.us/stock/NFLX ; UBER https://seekingalpha.com/symbol/UBER ; ADBE https://robinhood.com/us/en/stocks/ADBE/ ; ELV https://www.heygotrade.com/en/us-stock/elv/ ; GOOGL https://fullratio.com/stocks/nasdaq-googl/pe-ratio ; AMZN https://www.tradingkey.com/analysis/stocks/us-stocks/262205651-amazon-amzn-stock-forecast-october-8-2026-tradingkey ; UNH https://www.investing.com/news/stock-market-news/why-is-unitedhealth-stock-rallying-today-93CH-4941328 ; NVO https://www.heygotrade.com/en/us-stock/nvo/ ; TTE https://www.ad-hoc-news.de/boerse/news/corporate-news/totalenergies-stock-at-eur-78-43-up-38-3-percent-year-to-date/70280082 ; ASML https://www.macrotrends.net/stocks/charts/ASML/asml-holding/stock-price-history ; Samsung https://www.digitaltoday.co.kr/en/view/112552/kospi-slides-on-foreign-institution-selling-samsung-electronics-falls-despite-record-results
- Clean-EPS adjustments: Alphabet ~$98B gain https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000066/googexhibit991q22026.htm ; Salesforce Anthropic gains https://investor.salesforce.com/news/news-details/2026/Salesforce-Delivers-Record-Second-Quarter-Fiscal-2027-Results/ ; Netflix WBD fee https://www.sec.gov/Archives/edgar/data/1065280/000106528026000137/ex991_q126.htm ; Intuit SBC basis https://www.sec.gov/Archives/edgar/data/0000896878/000089687826000029/fy26q4earningspressrelease.htm ; UNH reserve release https://healthcarefinancenews.com/news/unitedhealth-raises-outlook-q2-profit-jumps-55b
- Uber / Waymo: https://www.thestar.com.my/business/business-news/2026/07/16/uber-launches-us148bil-offer-for-delivery-hero-to-create-global-platform · https://thenextweb.com/news/waymo-uber-exclusivity-ends-austin-atlanta-robotaxi · https://www.gurufocus.com/term/price-to-free-cash-flow/UBER
- TTE: https://www.sec.gov/Archives/edgar/data/0000879764/000110465926086078/tot-20260630xex99d1.htm · https://www.morningstar.com/stocks/xpar/tte/quote
- India-investor rules (TCS, LTCG, estate tax): see `working/contrarian_final.md` §7 item 24.
