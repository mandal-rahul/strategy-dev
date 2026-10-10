# Red team, round 1: lt_report_v1.md (2–3 year portfolio, hold to ~late 2029)

**Reviewer:** sceptical senior PM (red team). **Date:** Sat 2026-10-10.
**Read:** lt_report_v1.md, lt_macro_themes.md, lt_global_stocks.md, lt_india_stocks.md, the scripts (lt_returns.py, lt_extra.py, model.py, model_rate.py), FINAL_RECOMMENDATIONS.md and working/contrarian_final.md.
**Work done:** I re-ran all the scripts. I wrote two test scripts, `scratchpad/redteam/rt_sens.py` and `scratchpad/redteam/rt_proposed.py`; run each with `python3 -I`. I ran 57 WebSearch queries. WebFetch is blocked, so every new fact below comes from a search-result summary. No page was opened.
**Tags:** [H] filing, or two or more sources agree. [M] one credible source. [L] weak, single, undated or aggregator. (calc) my arithmetic. (mem) my background knowledge, not re-verified.
**Scenario weights:** written as bear/base/bull. "30/50/20" means the macro brief's own probabilities (30% bear, 50% base, 20% bull).
Not investment advice.

---

## 1. Verdict table

### 1a. Names (11 India, 9 global including the optional Alphabet, plus the reserve)

| # | Name | Report weight (% of total) | Verdict | Exact minimal change | Decisive reason |
|---|---|---|---|---|---|
| I1 | ICICI Bank | 8.25 | **AGREE** | None to the weight. Footnote that the 2.95x anchor is a Seeking Alpha / ADR series [L]. With a 2.6x anchor the base is still **17.1%/yr** (calc). | Growth carries the return even with a flat multiple (14.7%/yr). Best risk/return in the sleeve. The CEO term runs to ~Oct 2028 (weak sources), so succession falls inside the window. |
| I2 | HDFC Bank | 6.75 | **CONDITIONAL** | Cut to **~4.5% of total** (6% of the sleeve). Buy one-third now; buy the rest only after the **Q3 FY27 results (Jan 2027)** under the new CEO, and only if NIM is ≥3.3% and the RBI has taken no MSRDC action. Base exit P/B **1.9x** (not 2.05x) until ROE recovers. | Q1 FY27 PAT rose only +5%, NII +6.7%, and NIM was 3.26%, the lowest since the merger. The chairman resigned citing ethics, and there is a US class action. It is the most re-rating-dependent name: 28pp of its base comes from re-rating. |
| I3 | SBI Life | 5.25 | **CONDITIONAL** | Buy only at or below ₹1,850 (last seen ₹1,769.55 on Sep 21, which gives P/EV ~2.08x). Base EV growth **13.5%, not 15%**. Add RBI/IRDAI bancassurance rules to the sell triggers. | Q1 APE +36% came from lumpy group protection (3x y/y). SBI-channel individual APE grew only +10%. VNB margin fell 120bp. Even so, the base is still ~**17.5%/yr** (calc). |
| I4 | Bajaj Finance | 4.5 | **CONDITIONAL** | Buy half now. Buy the other half only after the RBI finalises the revolving-credit rule. Underwrite on a **flat 29.5x** (19.5%/yr), not on a re-rating to 32x. | Q1 FY27 was strong: ROE 20.4%, credit cost 1.54%, AUM +24%. The RBI draft is still a draft and covers ~15% of consolidated AUM and ~20% of the standalone book. |
| I5 | Reliance | 6.75 | **CONDITIONAL** | Cut to **~4.5% of total** (6% of the sleeve). Do not buy before the Jio listing (~Oct 28, unofficial) and RIL's Q2. Replace the remembered "~25x 5-year median" with a sourced series. | The base (14.5%) is at the model's own Nifty hurdle (14.3%). Holding it with Bharti doubles the telecom-tariff factor. 2029 fuel-price populism is a risk. |
| I6 | Bharti Airtel | 6.75 | **CONDITIONAL** | Cut to **~3.75% of total** (5% of the sleeve) until a headline **prepaid** tariff hike is announced; add after it. | The base (13.1%) is **below** the model's own hurdle. The FY28E consensus (+28%) assumes a hike that has not happened: only a postpaid revision on Oct 8, 2026. Vi survives (AGR dues frozen to FY32), so the market stays three-player. |
| I7 | NTPC | 6 | **AGREE** | Add the CERC timetable as a dated checkpoint. The 2024–29 approach paper came ~10 months before its period, so the FY29–34 paper lands around mid-2028 and the final rules around early 2029, next to the election. | Cheapest way into power demand (10.9x, 2.9% yield). A 7%+ G-sec makes a cut to generation ROE less likely. |
| I8 | L&T | 6 | **REJECT** | Move the 8% of the sleeve into a **Nifty 50 index fund**. | The base (13.9%) is below the model's own hurdle. About 40% of the order book is in the Middle East during an active Iran war: Q1 execution was hit and new awards deferred. The 2029 pre-election ordering lull and the LTIMindtree AI look-through add to it. Nothing in the report argues it beats the index. |
| I9 | Maruti Suzuki | 6 | **CONDITIONAL** | Buy only after Q2 (Oct 27), and only if EBITDA margin is ≥9%. Cut to **~3.75% of total** (5% of the sleeve). Eicher is the swap candidate. | The "volume recovery" (PV +36%, entry-level +96%, Apr–Aug 2026) is the one-off GST 2.0 cut of Sep 2025, which starts lapping in Oct 2026. FY28E EPS is being cut. The base is at the hurdle (14.9%) and the bear is −3%/yr. |
| I10 | Apollo Hospitals | 5.25 | **CONDITIONAL** | Cut to **~3.75% of total** (5% of the sleeve). Re-underwrite once the terms of the HealthCo → Apollo Healthtech demerger are known (listing Q4 FY27). | The listed security changes inside the window. 24/7 had not reached EBITDA breakeven by Q1 (PL, Aug 14). The P/E inputs are back-calculated [L]. The base is only ~1pp above the hurdle. |
| I11 | TCS | 4.5 | **REJECT** | Move the 6% of the sleeve into the Nifty index fund. **Do not use HDFC AMC**: it is ~33–34x TTM at ₹2,252, which gives a base of ~12.6%/yr, below the hurdle. | The base is 10.1% (8.2% after tax), below the hurdle. **The analyst's own rule says to replace TCS if the investor holds a USD sleeve, and this investor holds 25%.** That sleeve is already the INR hedge. The AI-deflation crossover (~FY29–30) arrives at the end of the window. |
| R | Rupee reserve | 9 (text says 10) | **CONDITIONAL** | Reconcile 9% vs 10%. Define the trigger exactly: for example, Nifty ≤ ~19,140 (−15% from 22,520), or −15% from cost. Carve **~3% of total into an Indian gold ETF** as the only asset in the portfolio that wins in the 30% bear. | The macro bear's list of winners is USD cash, gold, energy, Indian IT and pharma, staples and healthcare. After the TTE and TCS drops, the portfolio owns none of them except the USD sleeve and this cash. |
| G1 | Intuit | 3.75 | **CONDITIONAL** | Cut to **12% of the sleeve (3% of total)**; conviction 3.5. Headline the flat-multiple base (~15%/yr pre-haircut), not 25.5%. Buy after FQ1 (Nov 19). | **45pp of the 3-year base comes from re-rating to a "regime" 20x the analyst chose.** The FY28 input is still one broker (KeyCorp $26.84). The price may be ~$276 (Sep 26), which helps. Three 2026 shocks. |
| G2 | Microsoft | 3.75 | **CONDITIONAL** | Correct the capex input: **the FY27 guide is ~$255–260B (+~35%)**, not "~$175B in CY26". Restate the bear as **~−22% (g 4%, 18x)**. Keep 15% only if Microsoft is the **single** AI-capex spender held. | Its 0%/yr bear is inconsistent with the macro bear (an AI bust plus a US recession, with the index at −5 to −7%/yr). FY27 FCF positivity is now in doubt (unverified). |
| G3 | Visa (or Mastercard) | 3.25 | **AGREE** | Settle the "or MA" choice: split 50/50 or take Mastercard (~24.5x 2027 on Aug 17, no DOJ debit suit). Add the CCCA to the bear case. | The toll-road thesis survives. The CCCA was endorsed by Trump in Jan 2026; Stifel puts passage below 50/50. Visa is near its 52-week high ($294–386), so the "de-rating" came from EPS growth, not a price fall. |
| G4 | Amazon | 3 | **CONDITIONAL** | Cut to **8% of the sleeve (2% of total)**. Price it at **~26–27x** until the clean 2027 EPS is verified. Bear **~−22%**. | The **$10.3 "clean" 2027 EPS is not verified.** The mean of $10.47 (52 analysts) has a high of $15.04, and 2026 at $12.88 includes the gains. TTM FCF is −$7.6B and 2026 capex $220B. The macro brief says avoid megacap AI builders at ~23x+. |
| G5 | Netflix | 2.5 | **CONDITIONAL** | Buy only after Q3 (Oct 20), as the near-term plan already says. Cut to **8% of the sleeve**. | Engagement is falling: Wells puts per-member hours ~8% below 2023, and Nielsen has YouTube at 13.4% of US TV vs Netflix 7.8%. The 22x anchor is self-chosen; 13pp of the base comes from re-rating. |
| G6 | Medtronic | 2.5 | **AGREE** | Update the price (~$89–93). Note that the split-off outcome is pending. **Correct the estate-tax claim:** MDT shares are Irish-situs, so Irish CAT applies on inheritance whatever the holder's domicile. | It is the ballast: low bear, 3% yield, no AI or oil exposure. The returns are modest (~7.6%/yr after a haircut and flat P/E), so it is sized as a defensive, which is correct. |
| G7 | Elevance | 2.25 | **CONDITIONAL** | Buy only after Q3 (Oct 21), and only if the 2027 guide is ≥12% EPS growth. Keep 9% of the sleeve. | The final MA 2027 rate is +2.48% net (CMS: "the days of unlimited increases in rate must end"). Medicaid work requirements start Jan 2027. The FY27–28 inputs are one firm's (Zacks). |
| G8 | Uber | 2 | **CONDITIONAL** | Cut to **5% of the sleeve (1.25% of total)**; conviction 2.5. Pre-commit to selling if trip share falls in AV-direct cities. | It has the worst bear on the list (−20% over 3 years). Waymo is going direct (its Feb expansion did not mention Uber, and the Phoenix arrangement ended). The Delivery Hero tender adds leverage. The EPS basis is inconsistent [L]. |
| G9 | Alphabet (optional) | 2 | **REJECT** | Put the 8% of the sleeve into an **Irish-domiciled S&P 500 UCITS ETF** (CSPX/VUAA type). That holds Alphabet at index weight and is not US-situs. | It has the lowest score on the shortlist (8.6). The analyst calls it "fair, not cheap". It adds a third AI-capex spender: 2027 capex is projected at ~$308B, and Q1–Q2 2026 EPS were dominated by equity gains. It contradicts the macro brief's "avoid ~23x megacap AI". |

### 1b. Main hypotheses

| Hypothesis | Verdict | Why |
|---|---|---|
| (a) Indian financials re-rate | **UNPROVEN: treat as upside, not the base case** | ICICI, SBI Life and Bajaj Finance beat the index even on flat multiples (14.7 / 15.2 / 19.5%/yr). HDFC Bank does not (12.4%). Its 5-year de-rating is partly structural (ROE ~14%, NIM 3.26%). The macro base has RBI cuts only in 2028, ECL from Apr-2027 and a decade-high LDR, so the re-rating catalyst sits late in the window. |
| (b) Global quality compounders beat the index | **NOT DEMONSTRATED as written** | The picks (consensus growth plus re-rating) are compared with a macro index base built on haircut EPS plus de-rating. Measured the same way, the S&P 500 gives a ~13–14%/yr base. The edge is ~3pp before haircuts, ~1–3pp after a 3pp growth haircut and flat P/Es, and it then pays 1–2% FX and brokerage friction. Much of it is Intuit's self-chosen re-rating. |
| (c) Staged entry Oct–Feb | **AGREE with changes** | Gate names to their events (§4.3). Move the global February tranche to **after Apr 1, 2027**, so it uses a second ₹10 lakh TCS-free LRS limit. |
| (d) Drop/add decisions vs the near-term list | **Mostly AGREE** | I agree with dropping SBI, Infosys, Adobe and UNH, and with demoting TSMC to alternate. Dropping TTE as a compounder is right, but it removes the only bear hedge, so add gold. **Reject** adding Alphabet. **Shrink** Amazon. The report should also have dropped **TCS** (by its analyst's own rule) and **L&T** (below the hurdle). |

---

## 2. Method critique (with re-runs)

All figures are from `scratchpad/redteam/rt_sens.py` and `rt_proposed.py` (calc).

### 2.1 Double counting: mostly clean
- **Global model.** Buybacks sit inside per-share growth and are not added again. Dividends are compounded. **No double count.**
- **India model.** For banks, growth is book-value growth, which is already net of payout, and dividends are added on top. **No double count.**
- **Intuit text.** The text's "~8.7% shareholder yield" is **gross of SBC dilution**. SBC is ~$1.6B, about 2% of market cap, so the net buyback yield is ~4.8%. The bear case's g of 5% is consistent with that; the prose overstates it.

### 2.2 The edge depends on asymmetric haircuts (India)
- **The Nifty is haircut 4.5pp** (consensus ~15.5% to 11%). **The picks are haircut ~2.4pp on average** (weighted, excluding Bharti), or ~3.2pp including it. SBI Life and Reliance get **0pp**.
- The index's consensus is the sum of its constituents' consensus, so the picks deserve at least the same haircut.

| Test (30/50/20 weights) | Picks, expected %/yr | Nifty, expected %/yr | Edge |
|---|---|---|---|
| Report inputs (25/50/25) | 15.4 | 12.8 | 2.6pp |
| Macro weights 30/50/20 | 14.3 | 11.9 | 2.3pp |
| Plus flat base multiples for both | 13.2 | 10.8 | 2.4pp |
| **Equal haircut** (picks −1.5pp more) | **12.8** | 11.9 | **0.9pp** |
| Picks −3pp more ("≥10% too high" evidence) | 11.3 | 11.9 | **−0.6pp** |

- **The report's own caveat is mis-stated.** "With multiples flat it is ~0" compares **flat** picks (14.4%) with a **re-rated** Nifty (14.3%, 18.3x to 19.4x). Flat against flat, the edge is ~2.4pp.
- **The real fragility is the haircut asymmetry, not the re-rating.** Either way the conclusion is the same: the expected edge is about 0–2.5pp/yr, inside model error.

### 2.3 More than half the India sleeve does not beat the model's own hurdle
- With the Nifty at 14.3%, six of eleven names have a base at or below the hurdle +1pp: Reliance 14.5, Bharti 13.1, NTPC 14.6, L&T 13.9, Maruti 14.9 and TCS 10.1.
- Together they are **48 of 88 invested points (55%) of the India sleeve.**
- The report's own sell rule ("sell if base < hurdle for two reviews") would flag several of them on day one.
- All eleven names are Nifty 50 constituents. The sleeve is a concentrated subset of the index whose edge comes from about four names.

### 2.4 The global edge comes from a method mismatch
- The macro S&P base of ~5–6% uses EPS haircut to ~$400 (CY27), +8–9%/yr growth, and a **de-rating** to 17.5x.
- The stock models use consensus-like growth of 12–17% and move **halfway to the 10-year median, or to a self-chosen "regime" anchor**.
- On the stock method, the S&P (18.65x CY27 vs FactSet's 10-year average of ~18.8–19.0x; g 12%) gives a **base of 13.2–13.7%/yr** and an expected **10.2–10.4%** (30/50/20).

| Test (30/50/20) | Picks, expected | S&P (same method), expected | Edge |
|---|---|---|---|
| Report inputs | 14.5 | 10.2 | 4.4pp |
| −3pp growth haircut (long-term-growth bias) | 11.5 | 7.2 | 4.3pp |
| −3pp haircut and flat base P/E | 10.0 | 7.2 | 2.8pp |
| Same, base case only | 11.5 | 10.3 | **1.2pp** |

- **Evidence that consensus long-term growth is too high:**
  - Woolridge & Cusatis: analyst 3–5-year forecasts averaged **14.7% vs 9.1% realised** (1984–2006) ([Penn State](https://harrisburg.psu.edu/node/4910)).
  - McKinsey: **22% forecast vs 11% realised** (1985–2000) ([McKinsey](https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/prophets-and-profits)).
  - The highest-growth quintile realised **more than 50% less** than forecast ([hedgefundalpha](https://hedgefundalpha.com/strategies/are-earnings-forecasts-of-sell-side-analysts-biased)).
  - India: "since FY11 the consensus estimates have always overshot" ([Business Standard, Jan 2021](https://www.business-standard.com/article/markets/lofty-earnings-growth-estimates-liquidity-boom-keep-stocks-afloat-121012001368_1.html), M).
- **The report states but never applies its own 3–5pp optimism caveat.**

### 2.5 Re-rating dependence (global)
Share of each base 3-year total return that comes from re-rating, and the base after a 3pp growth haircut with a flat P/E:

| Name | Re-rating share of base TR | Base after haircut, flat P/E |
|---|---|---|
| Intuit | **45pp** | 12.1% |
| Uber | 21pp | 14.0% |
| Netflix | 13pp | 12.0% |
| Visa | 8pp | 9.8% |
| Medtronic | 6pp | 7.6% |
| MSFT, AMZN, ELV, GOOGL | ~0 | 12.8 / 14.0 / 9.8 / 10.3% |
| S&P 500 (same method) | — | 10.3% |

Under that haircut and a flat P/E, **Visa, Medtronic, Elevance and Alphabet are at or below the S&P on the same method.** Their role is defensive diversification, not edge, and the report should say so.

### 2.6 Scenario weights are inconsistent
- The stock models use 25/50/25. The macro brief says 30/50/20 and calls the bear "elevated".
- Using the macro's own weights cuts expected returns by **~1.1pp (India) and ~1.4pp (global)**. Every expected-return figure in the report should use 30/50/20.

### 2.7 The bears are idiosyncratic, but the 30% bear is systemic
- The macro bear is a 2010–13-style Indian stagflation plus a 2028 AI bust and a US recession, with the S&P at −5 to −7%/yr.
- Yet the bears for the AI-capex spenders are **+0.1% (MSFT), −1.7% (AMZN) and −4.4% (GOOGL) a year.** The names at the centre of the AI bust have milder bears than the index.
- My AI-bust bears give **MSFT −22%, AMZN −22%, GOOGL −27% over 3 years (−8 to −10%/yr).** For example, MSFT at g 4% and 18x reflects depreciation from FY27 capex of $255–260B.
- That drops the global sleeve's bear from −1.7 to **−4.1%/yr** and its expected return by ~0.6pp.

### 2.8 Anchors that flatter
- **ICICI's 2.95x.** It comes from a Seeking Alpha ADR series. Valueresearch lists a trailing P/B of 2.8 (basis unclear), and the macro brief says "~2.8–2.9x". If ICICI is really at ~2.8x trailing, the re-rating room is nearly gone. Confirm the basis before relying on it.
- **Bajaj Finance's 34.5x 5-year median.** The window includes FY22 COVID-depressed EPS.
- **Reliance, Maruti, SBI Life and others.** Their medians are from memory [L].
- **Global "regime" anchors.** Intuit 20x, Netflix 22x and Uber 20x are the analyst's choices. Seven of nine global anchors are memory or chosen.

### 2.9 The model mixes bases (Intuit)
- FY27 consensus is $23.07 on the **new** basis, which includes SBC. Tickflow shows an FY27 average of **$26.40** (19 analysts), most likely on the **old** basis. KeyCorp's FY28 $26.84 is assumed to be on the new basis.
- If any FY28 input is on the old basis, the 13% growth is overstated. FY28 is still single-sourced ([Tickflow](https://www.tickflow.io/stock/INTU/forecast); [dailypolitical/KeyCorp 2026-08-26](https://www.dailypolitical.com/?p=10490006)).

---

## 3. Per-name evidence (new facts, with URL and date)

### India

**ICICI Bank.**
- RBI approval of a further 2-year term for Sandeep Bakhshi, reportedly from **Oct 4, 2026** (so to ~Oct 2028). Every source is a weak syndicated or mirror site; there is no exchange filing [L] ([boardstewardship](https://boardstewardship.com/rbi-approves-reappointment-of-sandeep-bakhshi-as-ceo-md-of-icici-bank/), May 2026).
- Price ~₹1,401 on Jul 10; 52-week high ₹1,500 [M] ([MOSL F&O page](https://www.motilaloswal.com/futures-and-options/icici-bank-ltd)). Valueresearch shows trailing P/B 2.8 [L] ([VRO](https://valueresearchonline.com/stocks/42508/icici-bank-ltd/)).
- **The thesis survives.**

**HDFC Bank.**
- Q1 FY27: PAT ₹19,060 cr (**+4.98%**; ~9.8% underlying); NII +6.7%; **NIM 3.26%, the lowest since the merger** [M] ([INDmoney](https://www.indmoney.com/blog/stocks/why-hdfc-bank-shares-fell-after-q1-fy27-results); [Bigul](https://bigul.co/blog/market-update/hdfc-bank-stock-falls-55-after-q1-results-profit-grows-but-margins-tell-a-different-story)).
- Q2 results on **Oct 17** [M] ([PSU Connect](https://www.psuconnect.in/bank-news/hdfc-bank-fixes-date-for-q2-results-board-meeting-on-17-october)).
- The board fined the MD, CFO and group head in the MSRDC case (Jul 28) [M] ([Business Today 2026-07-28](https://www.businesstoday.in/markets/stocks/story/hdfc-bank-shares-in-focus-md-cfo-group-head-fined-in-msrdc-case-warning-letters-issued-545558-2026-07-28)). The chairman resigned on Mar 18, 2026, citing practices that did not fit his ethics; there is a US class action [M] ([Outlook Business](https://www.outlookbusiness.com/corporate/chairman-exit-ceo-departure-us-lawsuit-whats-going-on-at-hdfc-bank)).
- **The governance issue is unresolved, so staging behind the January quarter is the minimum.**

**SBI Life.**
- **₹1,769.55 on Sep 21**; 52-week range ₹1,653–2,132.90 [M] ([Anand Rathi](https://anandrathi.com/stocks/sbi-life-insurance-company-ltd/share-price-today)). The report's ₹1,685 (Sep 11) is stale. On Jun-26 EV that is ~2.08x (calc).
- Q1 FY27:
  - Group protection was 3x y/y and is "lumpy, not expected to recur" [M] ([PL 2026-07-25](https://plindia.com/ResReport/SBILIFE-25-7-26-PL.pdf)).
  - SBI/RRB bancassurance is ~47% of APE; SBI-channel individual APE grew **+10%** [M] ([DSIJ](https://insights.dsij.in/markets/reports/report-details/sbi-life-insurance-company-ltd/44727)).
  - VNB margin 26.3% (−120bp) [M].
- Regulation:
  - RBI directions on mis-selling of third-party products (issued Feb 11, 2026; effective Jul 1) require explicit per-product consent and ban bundling with loans; one summary says they bar third-party sales incentives. Sources conflict on whether these are final or draft [L/M] ([Basis Point Insight](https://basispointinsight.com/Story/rbi-tightens-grip-on-banks--non-core-sales-practices_b770515f793c.html)).
  - IRDAI has floated a 50% cap on the parent bank's share of bancassurance (background) [M] ([Business Standard](https://www.business-standard.com/industry/banking/restrictions-on-bancassurance-may-not-be-a-great-step-hdfc-life-s-padalkar-125012301578_1.html)).
- **The thesis survives at 13.5% EV growth (base ~17.5%/yr). The channel regulation is the 3-year risk the report omits.**

**Bajaj Finance.**
- The RBI revolving-credit rule is **still a draft** (Aug 6, 2026). Flexi products are ~15% of consolidated AUM and ~20% of the standalone book. NBFCs are lobbying through the FIDC [M] ([Vinod Kothari](https://vinodkothari.com/2026/08/rbi-proposes-bar-on-demand-loans-and-revolving-facilities-by-nbfcs/); [Outlook Business](https://www.outlookbusiness.com/economy-and-policy/nbfcs-seek-rbi-review-of-proposed-curbs-on-revolving-credit)).
- Q1 FY27: PAT +28%, **ROE 20.4%**, credit cost 1.54% (1.31% excluding the overlay), AUM ~+24%, MSME +2% (being pruned) [M] ([ICICI Direct Q1 note](https://mailcontent.icicidirect.com/mailcontent/idirect_bajajfinance_q1fy27.pdf); [Sahi](https://www.sahi.com/blogs/bajaj-finance-q1-results-2027-pat-rises-28-yo-y-aum-crosses-5-47-lakh-crore)).
- **The thesis survives. The risk is concentrated in one rule with a pending final date.**

**Reliance.**
- The Jio IPO is **still unofficial**: DRHP Jun 19, SEBI observations Aug 28. The reported issue dates are Oct 21–23 with listing on Oct 28. The band is not final (₹1,066–1,118 vs ₹1,150–1,220 in different reports) [M] ([The Week 2026-10-01](https://www.theweek.in/konnect/economy/2026/10/01/jio-ipo-what-investors-should-know-before-the-public-issue.html); [DSIJ](https://insights.dsij.in/dsijarticledetail/jio-platforms-ipo-key-dates-issue-size-valuation-and-other-details-id022-59902)).
- **The thesis survives only as index-like. It carries the telecom-tariff factor that Bharti also carries.**

**Bharti Airtel.**
- **There has been no headline prepaid hike.** Airtel made a **postpaid** revision (~3–11%, about ₹50 across plans) effective **Oct 8, 2026**. A prepaid hike in Q3 FY27 is a brokerage forecast, not an announcement [L/M] ([Ventura](https://www.venturasecurities.com/?p=64948); [DesiDime](https://www.desidime.com/news/airtel-recharge-hike-jio-recharge-price-hike-soon-complete-details-2026)).
- Vi's ₹87,695 cr AGR dues are frozen to FY32 and the government owns ~49%, so the third player survives through the window [M] ([Outlook Business](https://www.outlookbusiness.com/corporate/vodafone-idea-gets-new-agr-relief-as-cabinet-freezes-87695-cr-dues-till-fy32)).
- Price ₹1,871 on Jul 1; 52-week high ₹2,174.50 [M] ([Business Today](https://www.businesstoday.in/stocks/bharti-airtel-ltd-bhartiartl-share-price-364830)). Singtel sold ~0.8% in Nov 2025 and is monetising steadily, a supply overhang [M] ([Business Standard](https://www.business-standard.com/amp/industry/news/singtel-unit-to-sell-bharti-airtel-stake-worth-rs-10300-cr-125110601792_1.html)).
- **The quality is fine, but the base is below the hurdle until the hike lands. Telcos avoid hikes in the ~6 months before a general election**, so after one hike in 2027 the next window is mid-2029.

**NTPC.**
- No CERC FY29–34 consultation exists yet. The 2024–29 approach paper was issued in **May 2023**, ~10 months before its period [M] ([Powerline 2023-05-30](https://powerline.net.in/2023/05/30/cerc-issues-an-approach-paper-on-terms-and-conditions-of-tariff-regulations/)). So the FY29–34 paper lands around mid-2028 and the final rules around early 2029.
- The Forum of Regulators has recommended linking ROE to the 5-year average G-sec plus a premium. With a 7%+ G-sec, a deep cut is unlikely [M] ([CERC comments file](https://cercind.gov.in/2024/Discussion-paper/Comments&Suggestions-JAN2024/ASSOCHAM.pdf)).
- **The thesis survives.**

**L&T.**
- Q1 FY27 order inflow was ₹1.08 trn (+14%), but the Middle East was only 11% of inflow (47% the quarter before). Execution was "adversely impacted by West Asia disruptions", with a softer H1. There were no cancellations as of May, but **new awards are being deferred** [M] ([Business Recorder](https://www.brecorder.com/news/40432212); [Business Today 2026-05-06](https://businesstoday.in/markets/stocks/story/lt-share-price-targets-q4-miss-lakshya-31-announced-buy-sell-or-hold-529970-2026-05-06)).
- **Reject. The base is below the hurdle and the main exposure is to the war.**

**Maruti.**
- PV volumes rose ~36% y/y in Apr–Aug 2026, with the entry level up >96%, after the GST 2.0 cut on small cars (28% → 18%) [M] ([UNI 2026-09-22](https://www.uniindia.com/business-economy/car-sales-maruti-capex/188333)).
- Two new 250k-unit plants are being added (capex, then depreciation) [M] ([Daily Pioneer](https://dailypioneer.com/news/slug-lite/maruti-suzuki-accelerates-capex-gst-2-0-one-year?year=2026)).
- **The growth is a one-off step that laps from Oct 2026, not a cyclical recovery from a trough.**

**Apollo Hospitals.**
- 24/7 is "on track for EBITDA breakeven in coming quarters", so **it was not at breakeven in Q1** [M] ([PL 2026-08-14](https://www.plindia.com/pl-research/apollo-hospitals-enterprise-aphs-in-q1fy27-result-update-strong-show-in-hospital-segment-buy/)).
- The HealthCo → **Apollo Healthtech** demerger (Keimed merging in) has a listing pegged to **Q4 FY27** after the NCLT order of May 5, 2026 [M] ([Multibagg](https://www.multibagg.ai/market-pulse/articles/apollo-healthco-demerger-q4fy27-listing-cmpxutgq51tfwnz0jr37xo69b)).
- The consensus target is ~₹9,421 from 31 analysts, set when the price was ~₹8,957 (mid-2026) [L/M] ([Investing.com](https://uk.investing.com/equities/apollo-hospitals-consensus-estimates)).

**TCS.**
- No new search was needed: the analyst's own §6.11 says "If you hold a global/USD sleeve already, replace it with HDFC AMC".
- But HDFC AMC is **₹2,251.85 on Oct 9**, with P/E **37.09 at ₹2,517 on Jul 28**, so ~33–34x now (calc) rather than ~30x [M] ([Anand Rathi](https://anandrathi.com/stocks/hdfc-asset-management-company-ltd/share-price-today); [Equentis](https://www.equentis.com/stocks-screener/hdfcamc-share-price)). That gives a base of ~12.6%/yr, below the hurdle. **Use the index instead.**
- **Counter-argument, recorded:** in 2010–13, IT (USD earners) was the best Indian hedge. Here the 25% USD sleeve already provides that, and AI deflation removes IT's earnings floor.

**SBI (drop check).**
- SBI Funds Management listed in **July 2026** (IPO Jul 14–16; band ₹545–574) [M] ([Groww](https://groww.in/blog/sbi-funds-management-ipo-to-launch-on-july-13-2026); [Amundi disclosure](https://int.media.amundi.com/article/disclosure-regarding-proposed-initial-public-offering-sbi-funds-management-ltd)).
- The analyst's "hidden value needs a listing catalyst" is out of date: the catalyst has already happened. **The drop still stands** on the deposit gap and ECL.

### Global

**Intuit.**
- **$275.72 close on Sep 26** (one source); 52-week range $252.93–786.28 [L/M] ([InvestSmart](https://www.investsmart.com.au/security/nasdaq/intu/intuit/share-price)).
- FY28 is still single-broker (KeyCorp $26.84, Aug 26) [L].
- AI exposure: Intuit pays OpenAI >$100M a year to run TurboTax agents inside ChatGPT [M] ([eWeek](https://www.eweek.com/news/intuit-100m-chatgpt-deal/)). About a quarter of US workers planned to use AI for their taxes in 2026, up from 11% [M] ([PYMNTS 2026](https://www.pymnts.com/artificial-intelligence-2/2026/can-ai-do-your-taxes-we-found-out/)). The distribution channel is now partly someone else's interface.

**Microsoft.**
- **The FY27 capex guide is ~$255–260B, ~35% above FY26** (~$175–190B) [M] ([SentiSense 2026-07-31](https://app.sentisense.ai/stories/microsofts-ai-investments-pay-off-boosting-the-stock-market-and-tech-sector-07312026)).
- The stock was "near a one-year low" before Q4 [M] ([GeekWire](https://geekwire.com/2026/microsoft-earnings-preview-record-ai-spending-and-a-stock-near-a-one-year-low)).
- The OpenAI stake is marked to market each quarter: +$0.07/share in FQ4 vs −$0.21 a year earlier [L/M].
- The report's "~$175B in CY26" is **stale**.

**Visa / Mastercard.**
- Visa closed at **$367.39 on Sep 10**; 52-week range $293.9–385.56; Q4 results Oct 27 [L/M] ([InvestSmart](https://www.investsmart.com.au/security/nyse/v/visa/share-price)).
- Mastercard was **~$562 on Aug 17**, 24.5x 2027 [M] ([MarketScreener](https://uk.marketscreener.com/quote/stock/MASTERCARD-INC-17163/valuation/)).
- The **CCCA was reintroduced on Jan 13, 2026 and endorsed by Trump.** An attempt to attach it to a housing bill failed in March, and Stifel puts passage below 50/50 [M] ([Payments Dive](https://www.paymentsdive.com/news/ccca-seeks-new-path-to-passage/813789/); [PYMNTS](https://www.pymnts.com/credit-cards/2026/president-donald-trump-endorses-legislation-lower-credit-card-swipe-fees/); [Stifel](https://www.stifel.com/Newsletters/AdGraphics/InSight/Potomac-Perspectives/2026/PP_011626.pdf)).

**Amazon.**
- Consensus 2027 EPS is a **mean of $10.47 from 52 analysts, with a high of $15.04**. 2026 at $12.88 includes the gain [M] ([24/7 Wall St 2026-09-24](https://247wallst.com/investing/2026/09/24/amazon-stock-could-have-another-big-run-ahead-heres-my-2027-price-prediction/)). No source gives a clean ex-gain 2027 figure ([24/7 Wall St 2026-09-27](https://247wallst.com/investing/2026/09/27/is-amazon-stock-a-buy-hold-or-sell-below-250/)).
- TTM FCF is **−$7.6B**; 2026 capex is **~$220B**; capacity stays short of demand into 2027 [M] ([Kavout](https://www.kavout.com/market-lens/amazon-s-amzn-ai-bet-drives-record-growth-but-deepens-cash-flow-burn); [LetsDataScience](https://letsdatascience.com/news/aws-revenue-growth-outruns-available-ai-capacity-b0361d90)).

**Alphabet.**
- Q1-26 EPS was $5.11 against $2.63 consensus, on a **$37.7B equity gain**; Q2 included ~$98B (team) [M] ([Sherwood](https://www.sherwood.news/tech/google-earnings-q1-2026/)).
- Analysts' 2027 capex is ~**$308B** (+21% in revisions) [L/M] ([Pepperstone](https://pepperstone.com/en-gb/insights/market-analysis/equities/alphabet-q2-earnings-preview-cloud-and-capex-take-center-stage)).
- The "clean" EPS is two layers of adjustment deep, and FCF goes negative in 2027.

**Netflix.**
- Erste's 2027 estimate is $3.82, consistent with the report's $3.83 [M] ([MarketBeat 2026-07-29](https://www.marketbeat.com/instant-alerts/erste-group-bank-decreases-earnings-estimates-for-netflix-2026-07-29/)).
- Engagement:
  - Wells (Cahall): **1.6 hours a day per member in H1, ~8% below 2023** on a like-for-like basis; viewing of the top-100 originals could fall 21% in H2. Wells and HSBC both downgraded [M] ([TheWrap](https://www.thewrap.com/industry-news/business/netflix-stock-wells-fargo-hsbc-downgrade-engagement-trends-youtube-competition/)).
  - Nielsen: YouTube **13.4%** of US TV in 2026 vs Netflix **7.8%** [M] ([Luminate](https://luminatedata.com/blog/netflixs-youtube-strategy-isnt-likely-to-solve-its-problems/)).
  - The stock hit a 52-week low in July [M] ([News Tribune 2026-07-19](https://www.newstribune.com/news/2026/jul/19/netflix-stock-plunges-to-52-week-low-following/)).

**Medtronic.**
- $88.82 on Aug 11; 52-week range $73.32–106.30 [L/M] ([Upstox](https://upstox.com/us-stocks/mdt-share-price/)). It rose ~2.5% to over $93.30 on Sep 14 [M].
- The **final exchange ratio was set at the 4.5939 cap on Oct 7**. The offer expired at midnight on Oct 9, the outcome is not yet published, and proration is possible [H] ([Medtronic 2026-10-07](https://news.medtronic.com/2026-10-07-Medtronic-Announces-Final-Exchange-Ratio-of-4-5939-in-Split-Off-of-MiniMed-Group,-Inc)).
- Barron's (Oct 2) said the offer is "losing its allure"; diabetes is still consolidated in the FY27 guide [L/M] ([Trefis 2026-10-06](https://www.trefis.com/articles/617683/if-the-minimed-split-off-stalls-what-happens-to-your-medtronic-stock/2026-10-06)).
- **Estate-tax correction.** Medtronic's 10-K says its shares are **Irish-situated property for Irish capital acquisitions tax (CAT)**, which applies "regardless of where the parties live" (€400k tax-free threshold for a child from a parent in the FY25 10-K) [H] ([MDT FY2026 10-K](https://www.sec.gov/Archives/edgar/data/0001613103/000162828026044354/mdt-20260424.htm)). Whether the shares are US-situs remains unverified.

**Elevance.**
- 2026 guide ≥$27; management says ≥12% growth in 2027; Medicaid at about −1.75% is the trough [M] ([MarketBeat 2026-07-15](https://www.marketbeat.com/instant-alerts/elevance-health-q2-earnings-call-highlights-2026-07-15/)).
- **Medicaid work requirements start at the beginning of 2027**, and the CFO expects membership to decline [M] ([Healthcare Dive](https://www.healthcaredive.com/news/elevance-outperforms-q3-2025-warns-medicaid-challenges/803326/)).
- **The final MA 2027 rate is +2.48% net** (~4.98% including risk-score trend) [H] ([Fierce Healthcare](https://www.fiercehealthcare.com/regulatory/cms-gives-medicare-advantage-rates-248-bump-2027-plan-year-final-rule); [Becker's](https://www.beckerspayer.com/?p=23851)).
- The average price target is $440.90 [L].

**Uber.**
- Waymo's February four-city expansion announcement did not mention Uber, and the Phoenix arrangement with Uber has ended. Dow Jones reads this as Waymo moving to its own app in dense markets [M] ([Dow Jones via iTiger](https://www.itiger.com/news/2646393060)).
- The stock fell ~17% from late September 2025 on AV fears [M] ([Investing.com](https://uk.investing.com/news/-4693530)).

**Index alternative.**
- Irish-domiciled S&P 500 UCITS ETFs (CSPX/VUAA) can be bought under LRS (LSE, USD). The vendor claims they are not US-situs and that 15% US withholding is paid inside the fund, with no Indian foreign tax credit [L, vendor source] ([Paasa](https://paasa.com/blog/invest-in-ireland-ucits-stocks-from-india)). Verify with an adviser.

**Valuation reference.**
- FactSet S&P 500 forward P/E was **19.2 on Sep 25**; the 10-year average is ~18.8–19.0 and the 5-year ~19.9 [H] ([FactSet 2026-09-25](https://advantage.factset.com/hubfs/Website/Resources%20Section/Research%20Desk/Earnings%20Insight/EarningsInsight_092526.pdf)).

**The 2010–13 analogue.**
- Partly corroborated: the rupee went 44 → 52 in 2011 and 53 → 66 in 2013; from Aug 2011 to Jun 2012 the rupee fell 26% while the Nifty lost 12% [M] ([BloombergQuint](https://www.bloombergquint.com/amp/charts/nifty-and-rupee-no-longer-correlated); [Capitalmind 2013](https://www.capitalmind.in/2013/09/nifty-drops-5-in-aug-2013-worst-month-of-the-year/)).
- The endpoints (Nifty ~6,300 → ~6,200; ₹44.5 → ₹62) remain (mem), but are consistent with these.

---

## 4. Portfolio critique

### 4.1 Concentration
- **Indian financials are 24.75% of the total.**
  - That is *below* index-neutral. A 75% Nifty allocation already carries ~27% in financials, because the Nifty is ~36% financials.
  - The issue is not a factor overweight. It is that **the edge rests on four names sharing one driver (RBI rates and liquidity)**, plus NTPC as a bond proxy, so **~31% of the total is rate-sensitive**.
  - The 30% bear (repo 6–6.5%, CPI 6%+) hits all five together.
  - **If an index core is added, measure the 25% cap on a look-through basis.** My proposal goes to ~30% look-through (calc), so either lift the cap to an explicit "index-neutral +3pp" or hold HDFC Bank only through the index.
- **AI-linked global names are 17% against an 18% cap.**
  - The label mixes **victims** (Intuit) with **spenders** (MSFT, AMZN, GOOGL, which are 35% of the sleeve).
  - The macro brief explicitly says to avoid megacap AI at ~23x and levered builders with negative FCF.
  - **Cap AI-capex spenders at ~15–20% of the sleeve.** That means Microsoft alone, or Microsoft plus a small Amazon.

### 4.2 INR correlation and the 75/25 split
- **75/25 is defensible.** The macro brief has the Nifty at ~10%/yr in INR vs the S&P at ~5.5–6% in INR.
- The USD sleeve (25%) is the hedge for the 2010–13 analogue: if the rupee falls 30%, the sleeve gains ~+40% in INR terms from FX alone.
- With it in place, TCS adds little hedge. Do not cut the USD sleeve below ~20%.
- **Peace-deal risk:** if the rupee goes back to 92–94, the global sleeve loses 4–6% one-off in INR. Accept it, because it is the hedge's premium.

### 4.3 Staging: event-gate the names, not only the calendar

| Name | Gate |
|---|---|
| HDFC Bank | After Q3 FY27 (Jan 2027) |
| Elevance | After Oct 21 |
| Netflix | After Oct 20 |
| Intuit | After Nov 19 |
| Reliance | After the Jio listing (~Oct 28) and RIL Q2 |
| Maruti | After Oct 27 |
| Bajaj Finance (second half) | After the final RBI rule |
| Bharti (top-up) | After a prepaid hike |

- **LRS:** all three tranches fall in FY2026-27, so the 20% TCS applies above ₹10 lakh. If the global sleeve is above ₹10 lakh, **move global tranche 3 to after Apr 1, 2027.** That uses a second TCS-free limit and costs only ~6 weeks.

### 4.4 Tax and rebalancing
- The annual rebalance in October 2027 falls **inside 24 months** for every global lot, so trims are taxed at slab rates (up to ~39%).
- **Rule:** no discretionary trims of foreign names before 24 months; trim only on a sell trigger.
- Indian dividends are slab-taxed, which is another reason to drop TCS (4.5% yield).

### 4.5 Estate tax
- The global sleeve at 25% exceeds $60k once the total is above ~₹2.3 crore (calc at 96.7).
- Medtronic is not a clean shelter (Irish CAT). Use a UCITS index ETF for part of the sleeve, and check with an adviser.

### 4.6 The case for an index core
On the report's own numbers, with 30/50/20 weights:

| India sleeve | Expected, %/yr | Bear, %/yr |
|---|---|---|
| Report picks | 13.4 | 1.8 |
| Proposed core-satellite | 12.9 | 2.2 |
| All index (88% Nifty, 12% cash) | 11.3 | 2.2 |

- The picks add ~2pp over the index **only if their consensus inputs are haircut less than the index's** (§2.2).
- **Proposed India sleeve (% of the sleeve):** ICICI 11, HDFC Bank 6 (staged), SBI Life 7, Bajaj Finance 5, NTPC 8, Reliance 6, Bharti 5, Maruti 5, Apollo 5, **Nifty 50 index fund 30**, reserve 12 (of which gold ~4, i.e. ~3% of total).
- **Proposed global sleeve (% of the sleeve):** Intuit 12, MSFT 15, Visa/MA 14, AMZN 8, NFLX 8, MDT 10, ELV 9, UBER 5, **S&P 500 UCITS ETF 19**.
  - Modelled (same method, with my AI-bust bears): expected 13.3% vs 13.9% for the report's weights, and a bear of −3.1% vs −4.1%.
  - Cost: ~0.6pp of modelled return. Gain: fewer single-name event risks, less estate-tax exposure, and fewer FX tickets.

### 4.7 Number of names
- 20 names plus funds is a lot for a single retail LRS account. Small global tickets (1–4% of the total) each pay a 1–2% FX markup.
- Fewer, larger global positions plus one UCITS core is cheaper and easier to monitor.

---

## 5. Factual corrections

1. **SBI Life price:** ₹1,769.55 (Sep 21), not ₹1,685 (Sep 11), so P/EV is ~2.08x, not 1.98x ([Anand Rathi](https://anandrathi.com/stocks/sbi-life-insurance-company-ltd/share-price-today)). Q1 APE was boosted by lumpy group protection; SBI-channel individual APE grew +10%; VNB margin 26.3% (−120bp) ([PL 2026-07-25](https://plindia.com/ResReport/SBILIFE-25-7-26-PL.pdf)).
2. **Microsoft capex:** the FY27 guide is ~$255–260B, not "~$175B in CY26" ([SentiSense 2026-07-31](https://app.sentisense.ai/stories/microsofts-ai-investments-pay-off-boosting-the-stock-market-and-tech-sector-07312026)).
3. **Amazon "clean" 2027 EPS ($10.3) is unverified.** The consensus mean is $10.47 with a high of $15.04, and the 2026 mean of $12.88 includes gains ([24/7 Wall St 2026-09-24](https://247wallst.com/investing/2026/09/24/amazon-stock-could-have-another-big-run-ahead-heres-my-2027-price-prediction/)).
4. **Medtronic:** shares are Irish-situs for Irish CAT ([FY2026 10-K](https://www.sec.gov/Archives/edgar/data/0001613103/000162828026044354/mdt-20260424.htm)). The split-off ratio was capped at 4.5939 (Oct 7) and the outcome is pending ([Medtronic](https://news.medtronic.com/2026-10-07-Medtronic-Announces-Final-Exchange-Ratio-of-4-5939-in-Split-Off-of-MiniMed-Group,-Inc)). Price $88.82 on Aug 11 ([Upstox](https://upstox.com/us-stocks/mdt-share-price/)).
5. **Intuit:** $275.72 close on Sep 26 per one source ([InvestSmart](https://www.investsmart.com.au/security/nasdaq/intu/intuit/share-price)). FY27 consensus bases conflict ($23.07 vs $26.40 on [Tickflow](https://www.tickflow.io/stock/INTU/forecast)).
6. **Bharti:** no prepaid headline hike yet; a postpaid revision took effect Oct 8, 2026 ([Ventura](https://www.venturasecurities.com/?p=64948)). Vi's AGR dues are frozen to FY32 ([Outlook Business](https://www.outlookbusiness.com/corporate/vodafone-idea-gets-new-agr-relief-as-cabinet-freezes-87695-cr-dues-till-fy32)).
7. **Apollo:** the HealthCo/Apollo Healthtech demerger listing is in Q4 FY27, and 24/7 was not yet at breakeven in Q1 ([PL 2026-08-14](https://www.plindia.com/pl-research/apollo-hospitals-enterprise-aphs-in-q1fy27-result-update-strong-show-in-hospital-segment-buy/)).
8. **HDFC AMC:** ~33–34x TTM at ₹2,252, not ~30x ([Equentis](https://www.equentis.com/stocks-screener/hdfcamc-share-price)). That invalidates it as the TCS replacement.
9. **SBI:** the subsidiary-listing catalyst has already happened (SBI Funds Management IPO, July 2026) ([Groww](https://groww.in/blog/sbi-funds-management-ipo-to-launch-on-july-13-2026)).
10. **HDFC Bank:** Q1 FY27 NIM 3.26% is the lowest since the merger, and PAT rose +5% ([INDmoney](https://www.indmoney.com/blog/stocks/why-hdfc-bank-shares-fell-after-q1-fy27-results)). Q2 is on Oct 17.
11. **Maruti:** the "+28% H1 volume recovery" is the GST 2.0 step-change (PV +36%, entry +96% in Apr–Aug) ([UNI](https://www.uniindia.com/business-economy/car-sales-maruti-capex/188333)).
12. **Elevance:** the final MA 2027 rate is +2.48% ([Fierce](https://www.fiercehealthcare.com/regulatory/cms-gives-medicare-advantage-rates-248-bump-2027-plan-year-final-rule)), and Medicaid work requirements start in 2027 ([Healthcare Dive](https://www.healthcaredive.com/news/elevance-outperforms-q3-2025-warns-medicaid-challenges/803326/)).
13. **India report caveat:** "flat multiples → edge ≈ 0" compares flat picks with a re-rated Nifty. Flat against flat, the edge is ~2.4pp. The real weakness is the haircut asymmetry (§2.2).
14. **Report §1 vs §4:** the text says a 10% reserve while the table shows 12% of the sleeve, i.e. 9% of the total. §1 also quotes a "Nifty hurdle of ~11–14%" that mixes two incompatible methods.
15. **Global "S&P base ~5–6%"** is not comparable with the stock bases. On the same method the S&P base is ~13–14% (§2.4).

---

## 6. Open objections (to track in later rounds)

| ID | Objection | Status | What closes it |
|---|---|---|---|
| O1 | Expected returns use 25/50/25, not the macro's 30/50/20 | Open | Re-run every table at 30/50/20 |
| O2 | The India edge depends on picks being haircut less than the index | Open | Apply the same (~4.5pp or proportional) haircut to the picks, or justify each exception; restate the edge |
| O3 | The global edge compares picks with an index built on a different method | Open | Run the S&P (or a UCITS ETF) through model.py with the same rules; show the edge after a 3pp haircut and flat P/E |
| O4 | 55% of the India sleeve is at or below the model's own hurdle | Open | Replace or justify each of Reliance, Bharti, NTPC, L&T, Maruti and TCS against an index core |
| O5 | TCS is kept against the analyst's own rule; HDFC AMC is not a valid replacement | Open | Drop TCS, or show why the USD sleeve is not enough hedge |
| O6 | L&T: base below the hurdle plus Gulf war exposure | Open | Drop it, or give an explicit diversification case with an index comparison |
| O7 | AI-capex spender bears are milder than the index bear; MSFT capex input is stale | Open | MSFT FY27 capex $255–260B; bears of ~−20% or worse for MSFT, AMZN and GOOGL; cap spenders at ≤20% of the sleeve |
| O8 | Alphabet add contradicts the macro brief | Open | Remove it or replace with an index ETF |
| O9 | Amazon clean 2027 EPS is unverified | Open | Source an ex-gain consensus, or use ~26–27x |
| O10 | Intuit headline 25.5% is 45pp re-rating to a self-chosen anchor; FY28 is single-broker | Open | Headline the flat-P/E base; size at 12% of the sleeve; second FY28 source |
| O11 | SBI Life: stale price, lumpy Q1, banca regulation missing | Open | Live price ≤₹1,850; EV growth 13.5%; add RBI/IRDAI triggers |
| O12 | HDFC Bank staging and exit-P/B assumption | Open | Gate the rest behind Jan 2027; base exit 1.9x |
| O13 | Bharti: base below the hurdle and the tariff hike unconfirmed | Open | Half weight until a prepaid hike; hike trigger in the plan |
| O14 | Maruti growth is a GST one-off | Open | Gate on the Q2 margin; model FY28 growth after the base effect |
| O15 | Apollo demerger changes the security | Open | Re-underwrite on demerger terms |
| O16 | No asset wins in the 30% bear apart from the USD sleeve and cash | Open | Add ~3% gold (or a stated alternative), or accept explicitly |
| O17 | Reserve size inconsistent (9% vs 10%) and trigger undefined | Open | One number; an index-level or cost-based trigger |
| O18 | LRS TCS timing; no trims before 24 months | Open | Move global tranche 3 to after Apr 1, 2027 if the sleeve is above ₹10 lakh; add the no-trim rule |
| O19 | Medtronic estate-tax claim is incomplete (Irish CAT) | Open | Restate the claim |
| O20 | Index core not considered | Open | Show the core-satellite option (§4.6) with look-through factor caps |
| O21 | Visa vs Mastercard unresolved; CCCA not in the bear | Open | Choose or split; add the CCCA |
| O22 | Anchors from memory (Reliance, Maruti, SBI Life, Bajaj COVID-era median, ICICI ADR series) | Open | Source them or flag them in the table; show base returns at flat multiples alongside |
| O23 | ICICI CEO term source is weak | Open (low severity) | Exchange filing |
| O24 | Netflix, Elevance and Intuit should be event-gated (Oct 20, Oct 21, Nov 19) | Open | Add the gates to the tranche plan |

**What survives the attack, stated plainly:**
- ICICI Bank and the "insurers are the cheap way into financialisation" idea (SBI Life, at the corrected inputs).
- Bajaj Finance on growth alone, NTPC as cheap regulated power, and Medtronic plus Visa/MA as defensive ballast.
- The 75/25 split with the USD sleeve as the INR hedge.
- The drops of SBI, Infosys, Adobe, UNH and TSMC (to alternate).
- The overall finding that the edge over an index is small is right. If anything the report understates how much it depends on generous inputs.
