# Global Macro Briefing, as of Sat 2026-10-10 (last session Fri 2026-10-09)

Analyst: Global Macro (research subagent). Audience: stock-picking orchestrator and red team.

## 0. How the data was gathered (read this first)

- **I could not open any web page.** WebFetch failed with DNS `ENOTFOUND` on every domain I tried (federalreserve.gov, cnbc.com, thestreet.com, finance.yahoo.com, tradingeconomics.com, insight.factset.com). Direct curl through the proxy returned 403 (policy denial) for cnbc.com. old.reddit.com was refused.
- **Every figure below comes from WebSearch result summaries** of the URLs cited inline. Those summaries are written by the search tool from the underlying pages; I did not read the pages myself. Treat every number as "reported by search summary of <URL>". The red team should re-check key numbers against primary pages.
- **The shared WebSearch budget (200 calls per turn, shared by all agents) ran out partway through.** Sections I could not research at all are marked **NOT VERIFIED**: Russia–Ukraine, Taiwan, Europe growth and defense spending, EM flows, RBI/India macro, Reddit sentiment, and the current CNN Fear & Greed reading.
- Where sources disagree I give both. Confidence: **H** = several consistent sources or a primary-source URL in the results; **M** = one or two credible secondary sources; **L** = a single or weak source, or sources that conflict.

---

## 1. Executive summary: what matters for buying stocks now

1. **Bonds and stocks are pointing in different directions.** The S&P 500 (7,811.54) is within 0.1% of its record close, while the US 10y yield (~5.24%) hit its highest level since 2002 this week. At a forward P/E of 19.0, the S&P 500's forward earnings yield is about 5.26%, roughly equal to the 10y yield. **The equity risk premium is about zero** (my calculation). Valuation support comes only from very strong earnings growth (Q3 est. +29.6%, CY26 about +30%, CY27 +15.8%).
2. **An energy supply shock is driving a hiking cycle.** The US–Israel war with Iran (since late Feb 2026) pushed Brent to a $126 intraday peak on Apr 30. It is still about $102. US CPI is 3.4% and euro area HICP 3.3%. **The Fed (Sept 16), ECB (Sept 10) and BoJ (Sept 18) all hiked in September.** The Fed signals one more hike in 2026, and markets price about 70–85% odds of a December hike.
3. **The labor market is weakening while the Fed tightens.** September payrolls were +29k with -60k of revisions, unemployment is 4.2%, and wage growth of 3.0% y/y is below CPI of 3.4%, so real wages are falling. GDPNow for Q3 is 3.6%, but that rests on AI investment. This mix carries stagflation and policy-error risk.
4. **The AI capex supercycle is intact but now faces a financing debate.** Big-4 hyperscaler 2026 capex is about $710–750B, and the 2027 consensus is about $0.93–1.0T+. Nvidia guided FQ3 to $108B. TSMC's September sales were +54.6% y/y. Micron posted an 87% gross margin. Against that, the FT reported on Oct 8 that OpenAI's annualized revenue is about $50B, not about $70B. Amazon and Alphabet have negative FCF, about half of Oracle's RPO depends on OpenAI, and hyperscalers sold about $220B of bonds by August.
5. **Leadership is extremely narrow.** Only Energy (~+40%) and Tech (~+30%) beat the index YTD. The Mag 7 are about 35% of market cap. Nvidia and Micron reportedly account for about one-third of 2026 S&P profit growth.
6. **Upcoming catalysts:** Sept CPI (Oct 14), bank earnings (Oct 13–14), TSMC (~Oct 15), FOMC (Oct 27–28), ECB (Oct 29), BoJ (Oct 30), US midterms (Nov 3), shutdown deadline (Dec 11), FOMC with SEP (Dec 8–9), and the US–China truce expiry (Jan 10, 2027).

---

## 2. US economy and the Fed

### 2.1 Policy rate and the latest FOMC (Sept 15–16, 2026)
| Item | Value | As of | Source | Conf. |
|---|---|---|---|---|
| Fed funds target | **3.75%–4.00%** (+25bp, the first hike since 2023) | 2026-09-16 | [Fed statement PDF](https://www.federalreserve.gov/monetarypolicy/files/monetary20260916a1.pdf), [CNBC](https://www.cnbc.com/2026/09/16/fed-rate-decision-september-2026.html), [Atlanta Fed](https://www.atlantafed.org/news-and-events/2026/09/16/fomc-statement) | H |
| Vote | 12–0 unanimous. Three members had favored a hike in July | 2026-09-16 | CNBC (above) | M |
| IORB / primary credit | 3.90% / 4.00%, effective Sept 17 | 2026-09-16 | Fed implementation note (search summary) | M |
| Statement | Inflation "remains elevated." Warsh: underlying inflation not moving to target "clearly and quickly enough." He framed the hike as removing "a dose of accommodation" and said "this summer's inflation readings do not tell me that underlying trends have meaningfully improved." He dislikes forward guidance | 2026-09-16 | [Press conf. transcript](https://www.federalreserve.gov/mediacenter/files/FOMCpresconf20260916.pdf), [CNBC Sept 18](https://www.cnbc.com/2026/09/18/three-words-from-kevin-warsh-have-wall-street-wondering-how-far-the-fed-will-go-with-rate-hikes.html) | M |
| SEP medians | GDP 2.3% (2026), 2.4% (2027). PCE inflation 3.7% (2026) falling to 2.3% (2027). Unemployment ~4.1%. Inflation risks skewed up, labor risks balanced | 2026-09-16 | Transcript (above) | M |
| Dot plot | Median 4.1% end-2026 (one more hike), held at 4.1% in 2027, cuts in 2028–29. 16 of 18 see at least one more hike, 4 of whom see two; 2 see none. **Warsh does not submit a dot** | 2026-09-16 | [Chase](https://www.chase.com/personal/investments/learning-and-insights/article/federal-reserve-raises-rates-officials-signal-one-more-hike-in-2026), [Advisor Perspectives](https://www.advisorperspectives.com/dshort/updates/2026/09/16/feds-interest-rate-decision-september-16-2026) | M |

### 2.2 Fed chair and independence
- **Chair: Kevin Warsh.** Trump nominated him and he succeeded Powell (Powell's chair term ended May 2026). His first meeting was June 16–17, 2026. Sources: [WealthProfessional](https://www.wealthprofessional.ca/news/industry-news/fed-rate-hike-2026-now-possible/392758), Fed transcript. Conf. H.
- **Trump's response to the hike.** He wants rates at "1% or less" and called the Board "very hostile" and "very political," but spared Warsh personally. Warsh replied: "Independence is a two-way street." On Oct 9, CNN reported Trump saying he "probably would have voted against the Board" if he were Warsh. Sources: [CNN Sept 17](https://www.cnn.com/2026/09/17/economy/fed-trump-rate-hike-warsh), [Time](https://time.com/article/2026/09/17/fed-interest-rate-hike-trump-kevin-warsh/), [Yahoo/Reuters](https://finance.yahoo.com/economy/policy/articles/trump-says-us-interest-rates-204406419.html), [CNN Oct 9](https://www.cnn.com/2026/10/09/economy/white-house-investigation-fed-lisa-cook). Conf. M.
- **Lisa Cook.** In *Trump v. Cook* (June 29, 2026, 5–4, Roberts), the Supreme Court held that Cook stays for now, that "for cause" removal requires notice and a chance to respond, and that courts can review the stated cause. It left the door open for another attempt. The White House sent a new letter on Aug 5, 2026 giving 21 days to respond. CNN (Oct 9) headlines a **"new effort to oust Fed Governor Lisa Cook"** (I saw the headline only). Sources: [CNBC](https://www.cnbc.com/2026/06/29/supreme-court-lisa-cook-trump-federal-reserve.html), [Axios](https://www.axios.com/2026/06/30/trump-cook-fed-supreme-court), [SCOTUSblog](https://www.scotusblog.com/2026/08/trump-informs-lisa-cook-that-he-is-considering-her-removal/). Conf. M/H.
- **Reading:** independence risk is live but contained for now, because the Trump-appointed chair is hiking. The tail risk is a Cook removal or Board reshaping after the midterms, which could be negative for long bonds and the dollar and positive for gold.

### 2.3 Next FOMC meetings and market pricing
- **Oct 27–28** (no SEP) and **Dec 8–9** (with SEP). Sources: [Admiral Markets](https://admiralmarkets.com/analytics/traders-blog/fed-rate-decision-october-2026), Kiplinger. Conf. H.
- **FedWatch (about Oct 9):** October hold about 80–83%, hike about 17–18%. **December hike about 70–85%** (sources vary). Odds of an October hike fell after the weak jobs report. Goldman expects the next hike in December; Citi expects no further change in 2026. Sources: [CNBC Oct 2](https://www.cnbc.com/2026/10/02/fed-rate-hike-odds-decline-after-september-jobs-report.html), [Mitrade](https://mitrade.com/insights/more/inflation/us-cpi-preview-december-fed-hike-20261010J1122), [Outlook Money](https://outlookmoney.com/invest/us-fed-rate-hike-impact-india-stocks-rupee-bonds-gold). Conf. M.
- A Reuters report (via the 10y-yield coverage) said traders expect **at least three more hikes before mid-2027**. The 2y yield at 4.80% versus a funds midpoint of 3.875% is consistent with that. Conf. M.

### 2.4 Inflation
| Series | Latest | Prior/notes | As of | Source | Conf. |
|---|---|---|---|---|---|
| CPI headline | **3.4% y/y**, +0.4% m/m | Unchanged from July. Peak 4.2% in April 2026. Energy +16.3% y/y, gasoline +3.9% m/m | Aug 2026 (rel. Sept 11) | [CNBC](https://www.cnbc.com/2026/09/11/cpi-inflation-report-august-2026.html), [Morningstar](https://www.morningstar.com/economy/august-cpi-report-shows-inflation-34-annual-rate-above-forecasts), [Yahoo](https://finance.yahoo.com/economy/articles/u-cpi-rose-0-4-123718937.html) | H |
| CPI core | **2.4% y/y**, +0.3% m/m | Down from 2.5%. Lowest since Mar 2021 | Aug 2026 | Morningstar, Kiplinger | H |
| Sept CPI consensus | Headline **~3.7% y/y**, core ~2.5% | **Release Wed Oct 14** | preview | [Reuters via Investing.com](https://www.investing.com/news/economy-news/bank-earnings-cpi-headline-busy-markets-week-as-sp-500-hovers-near-records-4940595), [Admiral](https://admiralmarkets.com/analytics/traders-blog/us-cpi-preview-september-2026-forecasts-and-the-core-cpi-outlook) | M |
| PCE headline | 3.4% y/y, +0.3% m/m | Annual revisions back to 2021 | Aug 2026 (rel. Sept 30) | [Trading Economics](https://tradingeconomics.com/united-states/core-pce-price-index-mom/news/588257), secondary sites | L/M |
| PCE core | **3.0% y/y** (+0.2% m/m) | **Flag:** core PCE above core CPI is unusual. Possibly a data error in the secondary sources, or methodology/weighting effects. Verify on bea.gov | Aug 2026 | same | **L** |

### 2.5 Labor market: the September report (released Oct 2)
- **NFP +29k** versus about 84k consensus (Dow Jones); Bloomberg's survey median was about 90k. **Revisions -60k** over the prior two months.
- **Unemployment 4.2%** (from 4.1%), partly because more people joined the labor force. Participation 61.8%. Unemployment has held in a 4.1–4.3% range since March.
- **Average hourly earnings +0.1% m/m and +3.0% y/y, the slowest since 2021.** With CPI at 3.4%, **real wages are negative.**
- Sources: [BLS](https://www.bls.gov/news.release/empsit.nr0.htm), [CNBC](https://www.cnbc.com/2026/10/02/jobs-report-september-2026.html), [Bloomberg](https://www.bloomberg.com/news/articles/2026-10-02/us-firms-add-just-29-000-jobs-unemployment-rate-ticks-up). Conf. H.

### 2.6 Growth
- **Q2 2026 GDP (third estimate, Sept 30): 2.2% saar**, revised up from 1.5%. Real final sales to private domestic purchasers +4.6%. Sources: [BEA PDF](https://www.bea.gov/sites/default/files/2026-09/gdp2q26-3rd.pdf), [Advisor Perspectives](https://www.advisorperspectives.com/dshort/updates/2026/09/30/q2-gdp-third-estimate-real-gdp-at-2-2). Conf. H.
- **Atlanta Fed GDPNow Q3: 3.6%** (Oct 8), down from 3.7% on Oct 6, 5.0% on Sept 25 and 6.2% on Aug 3. Net exports subtract about 2.7pp. Private investment is nowcast at about +21.5%, which is AI capex. Source: [Trading Economics](https://tradingeconomics.com/united-states/gdpnow/news/590577), [fedpolicy.org](https://fedpolicy.org/releases/2026-10-06/gdpnow-2026-q3-oct-6/). Conf. M.
- **Recession probabilities: NOT VERIFIED.** No current Polymarket, Kalshi or bank-economist recession odds were found before the budget ran out.

### 2.7 Rates, dollar, fiscal
| Item | Level | As of | Source | Conf. |
|---|---|---|---|---|
| UST 10y | **5.23–5.24%** close. Intraday high about 5.35–5.36% on Oct 5–7, **the highest since April 2002**. Q3 was its biggest quarterly rise this century | 2026-10-09 | [ETF Trends snapshot](https://www.etftrends.com/fixed-income-content-hub/treasury-yields-snapshot-october-9-2026/), [CNBC Oct 7](https://www.cnbc.com/amp/2026/10/07/treasury-yields-auction-fomc-minutes.html), [Reuters via Investing](https://www.investing.com/news/economy-news/10-year-us-treasury-yield-hits-highest-since-2002-4926542), [Forbes](https://www.forbes.com/sites/garthfriesen/2026/10/07/why-the-10-year-treasury-yield-just-hit-a-24-year-high/) | H |
| UST 2y | **4.80%** | 2026-10-09 | ETF Trends / Seeking Alpha (same syndicated snapshot) | M |
| UST 30y | 5.61% (also at highs last seen in 2002 this week) | 2026-10-08 | [StreetStats](https://streetstats.finance/rates/treasuries/), CNBC | M |
| 2s10s | about +44bp (positive slope; my calculation) | 2026-10-09 | derived | M |
| 30y mortgage | 7.49% (from 7.30%) | ~Oct 7 | Forbes (above) | M |
| DXY | **~102.2–102.3**, a 4th straight weekly gain. One feed says 102.73 | 2026-10-09 | [Trading Economics](https://tradingeconomics.com/united-states/currency), [FXStreet](https://fxstreet.com/news/euro-struggles-as-french-fiscal-concerns-and-firm-us-dollar-dominate-202610091544) | M |
| EUR/USD | ~1.12 (weighed down by French fiscal worries) | 2026-10-09 | FXStreet | M |
| USD/JPY | ~156.6 after the BoJ's Sept 18 hike. About 158 implied on Oct 9 from EUR/JPY 177.15 | Sept 18 / Oct 9 | [CNBC](https://www.cnbc.com/2026/09/18/japan-raises-rates-30-year-high-yen-jgb.html), TE | L/M |
| FY2026 deficit | **~$1.9T** (CBO projection) | cited Oct 7 | Forbes (above) | M |
| Shutdown | **Averted Oct 1.** A CR (Continuing Appropriations Act 2027, Div. A of P.L. 119-103) funds government **through Dec 11, 2026**. Next cliff Dec 12 | Sept 2026 | [CRS R49353](https://www.congress.gov/crs-product/R49353), [NASFAA](https://www.nasfaa.org/news-item/39735/House_Passes_Continuing_Resolution_Funding_Government_Through_December_11) | M/H |
| Debt ceiling | NOT VERIFIED (the 2025 OBBBA raised it by $5T, from my memory, so it is probably not binding in 2026) | n/a | n/a | L |

Drivers of the yield spike cited in coverage: energy-driven inflation from the Iran war (Gulf refining offline), heavy federal borrowing, Fed hikes, and record hyperscaler bond supply. **BofA FMS (September): "disorderly rise in bond yields" is the #1 tail risk (33%).**

### 2.8 Politics
- **Midterms Tue Nov 3, 2026.** Prediction markets (mid-2026 snapshots, possibly stale): Democrats about 85% to win the House; Senate close to a toss-up. Sources: [DeFiRate](https://defirate.com/news/democrats-85-percent-to-flip-house-2026-midterms-senate-still-toss-up/), [Action Network](https://www.actionnetwork.com/politics/2026-midterms-predictions-markets-vs-polls-tracker). Conf. L/M.
- Midterm-year seasonality: the average intra-year S&P drawdown is about 18% (per [Saxo](https://home.saxo/learn/guides/us-election/2026-us-midterm-elections-what-different-outcomes-could-mean-for-markets) and similar sources). Post-midterm Q4 to Q2 has historically been strong (general history, not verified this session).
- Trump has reportedly threatened **post-midterm attacks on Iran** ([CBS live blog](https://www.cbsnews.com/live-updates/iran-war-us-negotiations-strait-of-hormuz-oil/)). Team India notes (same folder, not verified by me) say Trump stated on Oct 9 there would be no attack before Nov 3, which eased oil.

---

## 3. Trade and policy

### 3.1 Legal basis of US tariffs (timeline)
| Date | Event | Source | Conf. |
|---|---|---|---|
| 2026-02-20 | **SCOTUS, *Learning Resources v. Trump* (6–3): IEEPA does not authorize tariffs.** The "reciprocal" and fentanyl IEEPA tariffs fell. Refunds are left to the CIT (about 2,000 suits; one estimate puts them at about $35.5B plus interest across about 8.3M entries; could take years) | [Holland & Knight](https://www.hklaw.com/en/insights/publications/2026/02/supreme-court-strikes-down-ieepa-tariffs), [Flexport](https://www.flexport.com/blog/the-supreme-courts-ieepa-tariff-ruling-next-steps-potential-refunds-and/), [Snell & Wilmer](https://www.swlaw.com/publication/tariffs-redux-what-importers-should-know-about-ieepa-refunds-and-section-122/) | H |
| 2026-02-24 | **Section 122** global surcharge of 10% (150-day limit, cap 15%) | [Wiley](https://www.wiley.law/alert-Trump-Imposes-Section-122-Tariffs-After-Halting-IEEPA-Tariffs-Previews-New-Section-301-Investigations), [BDO](https://www.bdo.com/insights/tax/supreme-court-invalidates-ieepa-tariffs-administration-replaces-with-new-surcharge-what-importers) | H |
| 2026-05-07 | CIT holds Section 122 unlawful, but relief is limited to 3 plaintiffs. Under appeal; collection continued | [Skadden](https://www.skadden.com/insights/publications/2026/05/us-trade-court-strikes-down-section-122-tariffs) | M |
| 2026-07-24 | Section 122 expires. **New Section 301 tariffs of 10% or 12.5% on about 60 partners (about 99% of imports)**: 10% Mexico; 12.5% China, Vietnam, Thailand. The rate depends on forced-labor-import commitments. Exemptions include some energy products, aircraft, fertilizers and some foods. USTR plans further 301 probes on "excess capacity" | [Morgan Lewis](https://www.morganlewis.com/pubs/2026/07/us-administration-rebuilds-global-tariff-program-under-section-301), [WWL](https://worldwidelogisticsltd.com/2026/07/24/new-section-301-tariffs-replace-expired-section-122-duties/), 10-Q filings | M/H |

### 3.2 Sector (Section 232) tariffs, unaffected by the SCOTUS ruling
- **Steel and aluminum: 50%.** Autos, lumber and trucks are also in force. Source: [Ashurst](https://www.ashurst.com/en/insights/tariffs-impact-of-the-recent-us-supreme-court-ruling/), [Covington](https://www.cov.com/news-and-insights/insights/2026/04/current-and-forthcoming-section-232-actions-by-the-trump-administration). Conf. M.
- **Semiconductors:** a **narrow 25%** on certain advanced computing chips from Jan 15, 2026, with **exemptions for US data-center, R&D and some consumer and public uses**. Broader semis negotiations are ongoing. Source: [EY](https://globaltaxnews.ey.com/news/2026-0209-us-section-232-proclamation-imposes-25-percent-tariff-on-certain-semiconductors), [White & Case](https://www.whitecase.com/insight-alert/president-trump-orders-narrowly-targeted-25-section-232-tariff-certain-advanced). Conf. M.
- **Pharmaceuticals: 100% on patented drugs and their APIs**, phased in from July 31, 2026 for 17 named companies (Annex III) and from Sept 29, 2026 for all others. **Caps: 15% for the EU, Japan, Korea and Switzerland; 10% for the UK; 0% for generics.** Source: [Mallory Group](https://www.mallorygroup.com/blog-posts/100-duties-two-deadlines-section-232-pharmaceutical-tariffs-take-effect-july-31-2026), [Deemed Consulting](https://www.deemedconsulting.com/insights/2026-08-01-section-232-pharmaceutical-tariff). Conf. M. **This is relevant to Indian generics exporters, which sit at 0% if they hold for generics.**

### 3.3 Bilateral status
- **US–China:** the truce was extended on **Sept 24 to Jan 10, 2027** (from Nov 10), which is shorter than the six-plus months many expected. Current tariffs are held. China's tighter rare-earth export controls remain suspended, but deliveries are short (magnet shipments to the US were 512t in August, -20% m/m). China is meeting its 25Mt soybean commitment but is behind on $17B of other farm goods. Xi made a state visit to Washington. The next leader meetings are summits in Shenzhen (APEC) and Miami (G20) before year-end. Sources: [CNBC Sept 24](https://www.cnbc.com/2026/09/24/us-china-trade-truce-bessent-trump-xi.html), [CNBC Sept 23](https://www.cnbc.com/2026/09/23/trump-xi-summit-us-china-trade-rare-earth-soybean-plane.html), [investingLive](https://investinglive.com/news/trump-and-xi-buy-two-more-months-of-trade-truce-leaving-tariffs-and-rare-earths-in-limbo/). Conf. H.
- **US–India:** on Feb 2, 2026 a framework cut the US tariff to 18% (from 25% reciprocal; the overall rate was 50% in 2025). After SCOTUS, India fell under the 10% Section 122 tariff and then the **Section 301 tariff of 10% (one source) or 12.5% (IMPRI)**. The figure is unresolved. **The first tranche of the bilateral trade agreement is not yet in force.** Commerce Minister Goyal says it will take effect once the US restores India's tariff advantage over Vietnam, Bangladesh and others. Sources: [India Briefing](https://www.india-briefing.com/news/india-us-trade-deal-tariff-cuts-timeline-42471.html/), [CFR](https://www.cfr.org/articles/u-s-india-trade-truce-announced), [Upstox](https://upstox.com/news/business-news/latest-updates/when-will-india-us-trade-deal-s-first-tranche-come-into-force-goyal-spells-out-condition/article-197807/), [IMPRI](https://www.impriindia.com/centres/center-for-international-relations-and-strategic-studies/section-301-a-new-challenge-in-india-us-interim-trade-agreement/). Conf. L/M on the current rate.
- **US–EU:** after SCOTUS the EU **paused ratification** of the Aug 2025 framework ("a deal is a deal"). **Status after March 2026 is NOT VERIFIED.** The EU gets the 15% pharma cap. Sources: [Supply Chain Dive](https://www.supplychaindive.com/news/eu-us-trade-deal-halted-supreme-court-tariffs/812832/), [Fortune](https://fortune.com/2026/02/22/eu-pause-us-trade-deal-ratification-tariff-chaos-trump-supreme-court). Conf. L.
- **H-1B $100k fee: blocked.** D. Mass. (Judge Sorokin) vacated it on June 8, 2026. The **First Circuit refused to reinstate it on July 24, 2026**. A second court struck down the September 2026 re-issued version ([Forbes Oct 1](https://www.forbes.com/sites/stuartanderson/2026/10/01/judge-strikes-down-latest-version-of-100000-h-1b-immigration-fee/)). The fee is not being collected; the government may seek further review. Indian nationals received 71% of H-1B approvals in FY2025. Sources: [Clark Hill](https://www.clarkhill.com/news-events/news/h1b-fee-struck-down-massachusetts-court-2026/), [Democracy Forward](https://democracyforward.org/news/press-releases/second-federal-court-blocks-trump-vance-administrations-unlawful-innovation-ban/). Conf. M/H. **This is a modest positive for Indian IT services costs. The bigger overhang for that sector is AI disruption, per team India notes.**

---

## 4. Markets snapshot (close Fri 2026-10-09 unless noted)

| Asset | Level | Day / week | YTD and vs. high | Source | Conf. |
|---|---|---|---|---|---|
| S&P 500 | **7,811.54** | +0.59% / +1.15% wk | Record close **7,818.93 (Oct 6)**; intraday record 7,844.52 this week. **-0.1% from the record close.** YTD about **+14.1%** (my calculation, assuming a 2025 close of ~6,845.5 from memory). Reuters says ">13%" in one edition and ">14%" in another; Macrotrends +13.4% through Oct 8. The first record close since mid-August came on Oct 6 | [Yahoo](https://finance.yahoo.com/markets/live/stock-market-today-friday-october-9-dow-sp-500-nasdaq-080148117.html), [TheStreet](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-oct-09-2026), [CNBC Oct 5](https://www.cnbc.com/2026/10/05/stock-market-today-live-updates.html) | H |
| Dow | **51,655.01** | +0.83% / +0.93% wk (TheStreet: +1.15%) | n/a | same | H |
| Nasdaq Comp. | **27,366.17** | +0.64% / +0.64% wk | Record close 27,599.79 (~Oct 6), so -0.8% | same | H |
| Nasdaq 100 | **NOT VERIFIED** | n/a | n/a | n/a | n/a |
| Russell 2000 | **NOT VERIFIED for Oct 9.** An undated Yahoo quote shows 3,001.55; IWM was 281.52 on Oct 2 | n/a | Record about 3,067 on Aug 13 (then +23% YTD). Fell >5% in September; about +12% YTD at Sept 30. Roughly 2% below the record | [CNBC Sept 30](https://www.cnbc.com/2026/09/30/stock-market-today-live-updates.html), [ChartRow](https://chartrow.com/russell-2000/year-by-year) | L |
| VIX | **14.84** | -3.7% | 52-week low 13.38 (Dec 2025) | [CNBC quote](https://www.cnbc.com/quotes/.VIX), [Investing.com](https://www.investing.com/indices/volatility-s-p-500-historical-data) | M/H |
| Brent | **$102.60** | -1.6% | Pre-war about $72 (Feb 27). Peak **$126.41 intraday on Apr 30**. Now +42% vs. pre-war and -19% vs. peak | [Trading Economics](https://tradingeconomics.com/commodity/brent-crude-oil), [CNN Apr 30](https://www.cnn.com/2026/04/30/energy/oil-prices-iran-war-wartime-high-blockade-hnk) | M |
| WTI | **$90.39** | -1.2% | n/a | Trading Economics | M |
| Gold | **~$4,125–4,185/oz** | Two straight weekly declines into Oct 2; a one-week high on Oct 9 | Pressured by real yields and the strong USD | [RoboForex](https://roboforex.com/beginners/analytics/forex-forecast/gold/xau-usd-gold-weekly-forecast-2026-10-12/), [Investing.com](https://investing.com/news/commodities-news/gold-rises-on-softer-dollar-easing-yields-fed-outlook-in-focus-4940135), Kalshi strikes | L/M |
| Copper | **NOT VERIFIED for October.** LME cash record **$14,850/t on Aug 17, 2026** (Cochilco) | n/a | n/a | [MiningReporters](https://www.miningreporters.com/noticia/news/2026/08/copper-price-new-all-time-high-673-lb-london-cochilco) | M (Aug) |
| Bitcoin | **~$82,123** | -2.8% wk. Month-to-date low $80,308 on Oct 8. Spot-ETF outflows >$700M this week | Ether ~$2,488 (-6.8% wk) | [Rio Times](https://riotimesonline.com/crypto-markets-bitcoin-majors-friday-october-9-2026), [Fortune](https://fortune.com/article/price-of-bitcoin-10-09-2026/) | M |
| US 10y / 2y | 5.24% / 4.80% | n/a | 10y at its highest since 2002 | see §2.7 | H/M |

**This week's narrative:** stocks hit records on Tue Oct 6, then fell on Wed–Thu as yields spiked. On **Thu Oct 8 the Nasdaq fell 1.4% and the S&P 0.5%** after the **FT reported OpenAI's annualized revenue at about $50B versus about $70B previously reported**; Oracle fell 4.9% and the Nikkei 2.2%. Stocks rebounded on Friday as yields and oil eased ([Investing.com/FT](https://www.investing.com/news/stock-market-news/openai-annualized-revenue-at-50bn-far-below-reports--ft-4939530), [Bloomberg](https://www.bloomberg.com/news/articles/2026-10-08/openai-s-annualized-revenue-nears-50-billion-ft-says)). Bloomberg says OpenAI expects at least $70B run-rate by the end of 2026. The gap is partly an accounting difference: Anthropic counts cloud-partner resale revenue and OpenAI does not.

### 4.1 Earnings and valuation (FactSet unless noted)
| Metric | Value | As of | Source | Conf. |
|---|---|---|---|---|
| Q3 2026 S&P EPS growth (blended estimate) | **29.6%** (26.7% on Jun 30). LSEG IBES: ">30%" | Oct 9 | [FactSet Oct 9](https://insight.factset.com/sp-500-likely-to-report-earnings-growth-above-35-for-q3), [Reuters week-ahead](https://www.investing.com/news/economy-news/bank-earnings-cpi-headline-busy-markets-week-as-sp-500-hovers-near-records-4940595) | H |
| Likely reported Q3 growth | **>35%**, based on the 10-year average +6.9pp improvement through a season | Oct 9 | FactSet | M |
| Early beat rate | 84% of 19 reporters | Oct 9 | FactSet | H |
| Q3 guidance | 44 negative vs. 72 positive | ~Oct 2 | [FactSet preview](https://insight.factset.com/sp-500-earnings-season-preview-q3-2026) | M |
| Forward 12m P/E | **19.0** vs. 5y avg 19.8 and 10y avg 19.1 | ~Oct 2 | FactSet preview | M/H |
| CY2026 EPS growth | about 29–32% (FactSet figures vary by date: 29.1% Jul 31; 32.4% in one preview; ~31.8% per Motley Fool) | Jul–Oct | FactSet, [Fool](https://www.fool.com/investing/2026/09/24/prediction-the-s-and-p-500-finishes-2027-above-9-000-here-s-the-earnings-math/) | M |
| CY2027 EPS / revenue growth | **15.8% / 9.3%** (was 16.8% in June, so drifting down) | ~Oct 2 | [FactSet EI](https://www.factset.com/earningsinsight) | M |
| Bottom-up 12m target | **9,280.66** (+21.3% vs. 7,651.54) | ~Sept 30 | FactSet EI | M |
| Strategist YE2026 targets | Goldman 8,000 (2027 EPS $385); JPM 7,600 (Apr), possibly 8,000 later (unclear); Yardeni 8,400; UBS 8,100; **Reuters poll median 7,900**. Bear: Panmure Liberum **5,000 by end-2027** (Oct 5) | various | [Goldman](https://www.goldmansachs.com/insights/articles/s-and-p-500-forecast-to-climb-as-earnings-growth-powers-stocks-higher), [Yahoo/Yardeni](https://finance.yahoo.com/markets/stocks/articles/ed-yardeni-raises-p-500-125931405.html), [MarketScreener](https://marketscreener.com/news/panmure-liberum-sets-2027-year-end-s-p-500-target-at-5-000-ce785ddbdf80f72c), [Quartz](https://qz.com/wall-street-sp500-targets-8000-pullback-risks-090926) | M |
| Bank Q3 EPS growth | about 10% expected. **S&P banks index -7.5% (one edition says -9%) over the past month** | Oct 9 | [CNBC](https://www.cnbc.com/2026/10/09/earnings-season-kicks-into-high-gear-as-big-banks-report-next-week.html), Reuters | M |
| JPM Q3 consensus | EPS $5.90 (+16.4%), revenue $51.3B (+8.8%) | Oct 9 | [CMC Markets](https://www.cmcmarkets.com/en-gb/news-and-analysis/the-week-ahead-us-cpi-eurozone-cpi-jpmorgan-earnings) | M |

**Valuation point (my calculation):** a forward P/E of 19.0 gives a forward earnings yield of about 5.26%, against a 10y UST of about 5.24%. **The equity risk premium is roughly zero.** The last comparable readings were around 2000–2002 (history from memory). P/E has actually de-rated from about 22x in 2025 because EPS grew about 30%. The index rose less than earnings.

### 4.2 Breadth, concentration, sectors
- **Mag 7 ≈ 34.9% of S&P 500 market cap** (Oct 7; MacroMicro 35.6% in September) but **only about 26% of next-four-quarters earnings**. Mag 7 forward P/E is about 23 versus **about 17.3 for the other 493** (Yardeni via [Motley Fool Sept 27](https://www.fool.com/investing/2026/09/27/does-the-sp-500-have-a-magnificent-seven-problem-h/), [MacroMicro](https://en.macromicro.me/series/46223/share-of-m7-total-market-cap), [Forbes](https://www.forbes.com/sites/investor-hub/article/sp-500-weight-mag-7-stocks-diversification-risk/)). Conf. M.
- **Nvidia and Micron reportedly drive about one-third of 2026 S&P profit growth** (via [Quartz](https://qz.com/wall-street-sp500-targets-8000-pullback-risks-090926)). Conf. L/M.
- Breadth: **only about 59% (295 of 501) of S&P constituents are up YTD**, and the median stock trails the index ([ChartRow](https://chartrow.com/sp500/stock-performance)). Conf. M.
- **Sector YTD (price, around late Sept to early Oct). Sources conflict.** **Energy about +38–42% and Info Tech about +30% are the only two sectors beating the index.** Laggards: **Consumer Discretionary about -8.7%, Utilities about -8.1%, Communication Services about -5.6%** (ChartRow as of Sept 28). Sources: [Seeking Alpha](https://seekingalpha.com/article/4952113-2-tickets-to-outperformance), [Dagnino Substack](https://georgedagninophd.substack.com/p/sector-performance-since-22826), [ChartRow sectors](https://chartrow.com/sp500/sector-performance). Conf. L/M (method and date differences).

### 4.3 Q3 earnings season: what to watch
- **Kick-off: Tue Oct 13** with JPM, GS, C and WFC. **Wed Oct 14:** MS, BAC, BLK. Also that week: J&J, UnitedHealth, ASML, **TSMC (~Oct 15, unconfirmed)** and Schwab ([CNBC](https://www.cnbc.com/2026/10/09/earnings-season-kicks-into-high-gear-as-big-banks-report-next-week.html), [Globe and Mail/Reuters](https://www.theglobeandmail.com/investing/article-wall-streets-week-ahead-bank-earnings-cpi-headline-busy-markets-week/)).
- Things to watch:
  - Bank commentary on **consumer credit** given negative real wages and 7.5% mortgages.
  - NII given the steeper curve.
  - Energy-cost pass-through and margins outside Tech and Energy.
  - **Hyperscaler 2027 capex guides** in late October. Alphabet has already signaled a "significant increase."
  - OpenAI-exposed names (ORCL, CoreWeave, AMD) after the FT report.
  - Memory pricing durability.
  - Tariff refund accounting from IEEPA refunds, which could be a one-off EPS tailwind for importers. **Unverified**.

---

## 5. AI and the capex cycle

### 5.1 Hyperscaler capex (latest guidance)
| Company | 2026 capex guidance | 2027 signal | Other datapoints | Source | Conf. |
|---|---|---|---|---|---|
| Alphabet | **$195–205B** (raised from $180–190B at Q2; the second raise this year) | "Significant increase" in 2027. Guggenheim estimates about $350B vs. Street about $265B; Street consensus elsewhere is $284.8B | Cloud backlog $514B. Q2 FCF **-$5.9B**. Cloud growth reported as +82% y/y (**seems very high, verify**). Stock fell about 5.7% after the report | [S&P Global MI](https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/07/alphabet-postq-ai-growth-accelerates-as-spending-weighs-on-cash-flow), [Webull](https://www.webull.com/news/15277620003939328) | M |
| Microsoft | Reported CY2026 about **$175B**; FY26 (June) about $190B. FQ1'27 about $50B. **Lease accounting changed** (data-center leases now spread over 25 years instead of 15), which lowers reported capex | FY27 guide reported at **about $255–260B by secondary sources only**. Street CY27 about $207.6B | Azure +43% cc; guided +45% for the Sept quarter. Stock +8% after the report | [The Star/Reuters](https://www.thestar.com.my/business/business-news/2026/07/31/microsoft-sees-strong-cash-flow-lower-capex), [SentiSense](https://app.sentisense.ai/stories/microsofts-ai-investments-pay-off-boosting-the-stock-market-and-tech-sector-07312026) | L/M |
| Amazon | **~$220B** (raised from ~$200B, mostly due to memory costs) | Street 2027 about $256.5B | AWS +37% to $42.2B, the fastest in 18 quarters. Backlog $496B. **TTM FCF -$7.6B**. Q2 capex $54.2B | [LetsDataScience](https://letsdatascience.com/news/aws-revenue-growth-outruns-available-ai-capacity-b0361d90), [iAmsterdam](https://startupmap.iamsterdam.com/news/feed/amazon-to-spend-over-220b-on-ai-capex-in-2026-as-aws-hits-42b-revenue-up-37) | M |
| Meta | **$130–145B** (low end raised from $125B). Total 2026 expenses $165–169B | No company guide. Citi about $205B; buy-side whispers about $225–250B; Street $185.6B | Q2 capex plus finance leases $31.1B | [247WallSt](https://247wallst.com/investing/2026/07/29/live-will-meta-crush-q2-earnings-tonight-after-market-close/liveupdates/7/), [IG](https://www.ig.com/au/news-and-trade-ideas/meta-q2-2026-earnings-preview-260727) | M |
| Oracle (FY ends May) | FY27 gross capex **about $90–95B**, of which **about $70B is net of customer-funded portion** | n/a | **RPO $664B (about half reportedly OpenAI).** Q1 FCF -$5B. $20B ATM equity done as part of a **$40B financing plan**. FY27 revenue ≥$90B, EPS $8.10. **BBB / negative outlook** | [Oracle PR](https://www.oracle.com/news/announcement/q1fy27-earnings-release-2026-09-10/), [Outlook Business](https://www.outlookbusiness.com/corporate/oracle-forecasts-95-bn-in-capex-for-fy27-plans-to-raise-40-bn-in-debt-and-equity), [FourWeekMBA](https://fourweekmba.com/ai-oracle-q1-fy2027-backlog-capex-analysis/) | M |
| **Big-4 total** | **about $710–745B** (Goldman about $750B). 2025 was about $410B | **2027: Street sum about $935B** (GOOGL 284.8 + AMZN 256.5 + MSFT 207.6 + META 185.6). **Evercore and BofA model above $1T** | Morgan Stanley: about **$3T** of AI infrastructure through 2028, with only half covered by cash flow | [YieldTheory](https://www.yieldtheory.app/research/hyperscaler-ai-capex-tracker-2026), [ValueAddVC](https://valueaddvc.com/blog/big-tech-ai-capex-in-2025-microsoft-google-meta-amazon-and-the-spending-race), [Sage](https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure) | M |

### 5.2 Semis demand
- **Nvidia FQ2 FY27 (Jul quarter, reported Aug 26):** revenue **$96.2B (+106%)**; data center $89.0B (+117%), of which hyperscale $48.7B and AI cloud/enterprise $40.3B (+138%). **FQ3 guide $108B ±2%** (about $3.8B above consensus) with no China DC compute assumed. GM about 74%. **The CFO sees FY28 revenue up about 70%** (Street had about 45%). Sources: [Nasdaq/Zacks](https://www.nasdaq.com/articles/nvidia-q2-earnings-beat-blackwell-ultra-data-center-strength), [Webull](https://www.webull.com/blog/304-Nvidia-Q2-FY2027-Earnings-Beats-Revenue-EPS-Estimates-Guides-Q3-to-108B). Conf. M/H.
- **TSMC:** September revenue **NT$511.9B (+54.6% y/y)**; Jan–Sep NT$3,898.7B (+41.1%). Q3 guide $44.6–45.8B, GM 65–67%. 2026 USD growth "slightly above 40%". **Capex $60–64B.** Q3 results about Oct 15 (unconfirmed). Sources: [TSMC 6-K (SEC)](https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000680/tsm-revenue20261008.htm), [Hudson Labs](https://www.hudson-labs.com/research/tsmc-q3-2026-earnings-preview-tsm-revenue-and-margins). Conf. H.
- **Micron FQ4 FY26 (reported about Sept 30):** revenue **$54.2B**, **non-GAAP GM 87.0%**, EPS $33.42. **FQ1 guide $61.5B.** HBM sold out for 2026. DRAM spot +52% since January. Management sees tightness beyond CY2027. Sources: [NextPlatform](https://www.nextplatform.com/store/2026/10/02/microns-numbers-show-why-hbm4-memory-is-worth-15x-its-weight-in-gold/5300701), [Zacks](https://www.zacks.com/stock/news/2756578/micron-beats-on-q4-earnings:-will-strong-guidance-lift-the-stock). Conf. M. **Memory margins this high have historically marked late-cycle conditions. Watch for capacity additions.**

### 5.3 AI labs and mega-deals
- **OpenAI:** annualized revenue about $50B at end-September (FT, Oct 8). Bloomberg: the company expects at least $70B by year-end. **Nvidia is reportedly discussing a $250B backstop** of lease and construction debt for OpenAI's 10GW Ohio campus (WSJ; still talks). The Stargate Texas site will be more than 75% complete within about 90 days, per Oracle. Sources: [Vantage](https://www.vantagemarkets.com/market-news/openai-revenue-50-billion-vs-70-billion-bloomberg-ft-figures-compared-october-9-2026/), [Outlook Business](https://www.outlookbusiness.com/explainers/inside-the-ai-bubble-how-openai-nvidia-are-weaving-a-web-of-circular-deals). Conf. M.
- **Anthropic:** run-rate **above $65B at end-July** (up from $47B in May and about $9B at end-2025). The NYT reports it is on track to pass $100B this year. IPO talk. Google is reportedly backstopping data-center leases at five sites for Anthropic (about $35B). Valuation figures such as $965B (Series H) come from aggregators only and are **unverified**. Sources: [CNBC Aug 17](https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html), [TechCrunch](https://techcrunch.com/2026/08/17/anthropics-annualized-revenue-surges-to-65b/), [Axios](https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai). Conf. M.

### 5.4 Financing and credit
- **Hyperscaler bond issuance was about $220B by Aug 10, 2026** (BNP via Reuters). That compares with $194B by Jul 7, which was already up 79% on full-year 2025.
- New-issue concessions have risen to **12bp median, from 2.25bp in 2025**. 78 of 91 2026 hyperscaler bonds trade at higher yields than at issue.
- AI-linked debt is about 15% of IG issuance (Barclays).
- Goldman: debt funds about one-third of 2026 capex and about 35% of 2027 capex.
- Sources: [Yahoo/Reuters](https://finance.yahoo.com/markets/stocks/articles/hyperscaler-debt-binge-pushes-yields-134825104.html), [MLQ](https://mlq.ai/news/hyperscaler-bond-issuance-reaches-about-220-billion-as-ai-financing-costs-rise/), [Sage Advisory](https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure). Conf. M.
- **BofA FMS (Sept): 42% name hyperscaler capex as the most likely source of a credit event. A record 33% say semis companies are over-investing.**

### 5.5 Power, grid and data centers
- **GE Vernova:** gas-turbine backlog plus slot reservations of **116GW at the end of Q2** (100GW in Q1, 83GW at end-2025), of which only **53GW is firm**. Targeting at least 125GW by year-end. It is taking reservations for **2031 delivery**. Data centers are about 20% of the mix. Electrification orders $6.3B (+66% organic), book-to-bill about 1.7. Sources: [Utility Dive](https://www.utilitydive.com/news/ge-vernova-gas-turbine-backlog-climbs-to-116-gw/826039/), [GEV 8-K](https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000147/gevpressrelease2q26.htm). Conf. H.
- **US data-center power demand (Goldman):** 31GW (2025), 41GW (2026), **66GW (2027)** ([Yahoo](https://finance.yahoo.com/energy/articles/gas-turbine-shortage-just-became-210000180.html)). Conf. M.

### 5.6 The AI-bubble debate
**Bull case:**
- Demand is visible in reported numbers: NVDA +106%, TSMC +55%, MU revenue more than 2x, Azure +43–45%, AWS +37%.
- Lab revenue run-rates have grown 5–7x in a year (Anthropic about $9B to more than $65B).
- Backlogs are contracted: Oracle RPO $664B, Google Cloud $514B, AWS $496B, GEV turbines into 2031.
- The S&P forward P/E of 19 is below its 5-year average. The other 493 trade at about 17x.

**Bear case:**
- The OpenAI revenue gap ($50B vs. $70B) undermines the narrative.
- Circular and vendor financing: NVDA reportedly discussing a $250B backstop for OpenAI; Google backstopping Anthropic leases.
- **Free cash flow is now negative at Amazon (TTM) and Alphabet (Q2).**
- About $220B of bonds issued by August, with widening concessions.
- Oracle is BBB/negative with about half its RPO from one customer.
- Semis were the most crowded trade for 4 straight months (peaking at 82% in July). Memory margins of 87% are at historical peaks.
- Morgan Stanley sees a cash-flow shortfall of about $1.5T through 2028.
- Cramer and others draw dot-com comparisons ([CNBC Jul 27](https://www.cnbc.com/2026/07/27/jim-cramer-warns-ai-circular-financing-echoes-dot-com-bubble.html)).

**Second-order beneficiaries** (based on the above, not stock-verified):
- Memory: MU, SK Hynix, Samsung.
- Foundry and packaging: TSMC.
- Semicap: ASML and others, given TSMC capex of $60–64B.
- Power generation equipment: GEV, Siemens Energy, Mitsubishi Heavy.
- Grid and electrical: transformers, switchgear and cooling.
- Gas supply for on-site generation.
- Networking and optics.
- AI-cloud/enterprise names: Nvidia's fastest-growing segment (+138%).
- **Ranking by risk:** contracted, cash-generating suppliers carry less risk than OpenAI-dependent leveraged builders.

---

## 6. Rest of the world

### 6.1 Iran war, oil and OPEC+
**Timeline:**
- War (US–Israel vs. Iran) began in late Feb 2026. Brent rose from about $72 on Feb 27 and gained 51% in March.
- April ceasefire mediated by Pakistan, with talks in Islamabad.
- US naval blockade of Iranian ports from Apr 13.
- **Brent peaked at $126.41 intraday on Apr 30.**
- MoU framework in June. By early July Brent was down more than 38% from the peak.
- Ceasefire lapsed around mid-August, after Iranian attacks on Hormuz shipping brought US operations back.
- Sources: [CNBC timeline](https://www.cnbc.com/2026/04/21/oil-price-iran-war-middle-east.html), [CNN](https://www.cnn.com/2026/04/30/energy/oil-prices-iran-war-wartime-high-blockade-hnk), [Al Jazeera Jul 2](https://www.aljazeera.com/economy/2026/7/2/oil-prices-fall-to-levels-not-seen-since-start-of-us-israel-war-on-iran). Conf. M/H.

**Status as of about Oct 4:**
- **Talks stalled.** Trump rejected Iran's 7-point proposal (ceasefire, unfrozen assets, oil-sanctions relief, end of the blockade). The US has shifted toward economic pressure ([France 24](https://www.france24.com/en/middle-east/20261004-iran-us-military-middle-east-war-peace-talks), [CBS](https://www.cbsnews.com/live-updates/iran-war-us-trump-talks-strait-of-hormuz/)). Conf. M.
- **Hormuz flows (Sept 30):** crude is near pre-war levels, but **refined products are about 677k bpd vs. 3.6M bpd pre-war**. Total flows are about 80% of the 17M bpd baseline ([CNBC](https://www.cnbc.com/2026/09/30/iran-war-strait-hormuz-gulf-oil-fuel.html)). The IEA calls it the **largest supply disruption in history**.
- **US SPR at 311.4M bbl (Jul 17), the lowest since 1983.** This limits policy buffers.
- **Implication:** product cracks and refiners are structurally supported, and inflation runs through diesel and jet fuel.

**OPEC+:**
- Seven core members kept **November** targets unchanged (Oct 4) after holding October (Sept 6). **Next meeting Nov 1.**
- Actual output is below target because of Hormuz and Russia constraints. The capacity review that sets 2027 quotas is delayed, so no change is expected before 2027 ([CNBC Oct 4](https://www.cnbc.com/2026/10/04/opec-agrees-to-keep-november-oil-output-targets-steady.html), [Enerdata](https://www.enerdata.net/publications/daily-energy-news/opec-keeps-november-2026-production-targets-unchanged-amid-supply-disruptions.html)). Conf. H.

### 6.2 Europe
- **ECB hiked 25bp on Sept 10 to DFR 2.50%** (MRO 2.65%). This is the second hike of 2026 (June hike, July pause). **Euro-area HICP 3.3% in August, with energy +14.3%.** Lagarde is going meeting by meeting. **Next meeting Oct 29.** Sources: [ECB](https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.mp260910~314e508016.en.html), [CNBC](https://www.cnbc.com/2026/09/10/ecb-interest-rate-hike-lagarde-iran.html). Conf. H.
- French fiscal worries are weighing on the euro (EUR/USD about 1.12) ([FXStreet](https://fxstreet.com/news/euro-struggles-as-french-fiscal-concerns-and-firm-us-dollar-dominate-202610091544)). Conf. M.
- **Euro-area GDP, German fiscal stimulus, defense spending and European equity levels are NOT VERIFIED** (search budget exhausted).

### 6.3 Japan
- **BoJ hiked to 1.25% on Sept 18 (7–2 vote; Asada and Sato dissented), the highest since 1995.** The hike came alongside a **coordinated US–Japan FX intervention** to support the yen. USD/JPY was about 156.6 after the decision. JGB 10y about 2.95%. Japan's August CPI was 1.9%. The US is pressing Tokyo to keep hiking, against PM **Takaichi**'s easy-money and fiscal-expansion preference. **Next BoJ meeting Oct 30.** Sources: [CNBC](https://www.cnbc.com/2026/09/18/japan-raises-rates-30-year-high-yen-jgb.html), [BoJ](https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2026/k260918a.pdf). Conf. H.
- **Nikkei 225: 69,030.92 (Oct 9, -0.02% d/d, -0.39% w/w). Topix 4,104.81.** The Nikkei fell 2.2% on Oct 8 on the OpenAI news. Investing.com shows 69,008 / +0.71%, which conflicts. Sources: [Business Recorder](https://brecorder.com/news/40443513/nikkei-limps-to-weekly-loss-as-bond-stress-weigh), [Investing.com](https://www.investing.com/indices/japan-ni225-historical-data). Conf. M.

### 6.4 China
- **August data (Sept 15):** retail sales **+0.4% y/y** (vs. 0.8% expected; autos -18.5%); industrial production **+5.2%**; **FAI -7.2% YTD; property investment -19.9% YTD**; unemployment 5.3%. The NBS cites an "acute" imbalance between strong supply and weak demand ([CNBC](https://www.cnbc.com/2026/09/15/china-august-retail-sales-industrial-output-investment-exports-.html), [FXStreet](https://www.fxstreet.com/news/chinas-retail-sales-rise-04-in-august-industrial-production-up-52-202609150207)). Conf. H.
- **Markets (Oct 9):**
  - **Hang Seng 24,211.35** (+1.79%, +1% w/w).
  - **HS Tech 4,197, near a two-year low.**
  - **Shanghai Composite about 3,813**, closing the holiday-shortened week near its lowest in more than a year.
  - Sources: [BBN Times](https://www.bbntimes.com/financial/hang-seng-jumps-to-24-211-35-as-xiaomi-tencent-and-internet-stocks-lead-a-sharp-rebound-in-hong-kong), [RTHK](https://news.rthk.hk/rthk/en/component/k2/1873307-20261009.htm). Conf. M/H.
- **New stimulus announcements and the Q3 GDP consensus are NOT VERIFIED.** Q3 GDP is due around Oct 19–20 (date unverified).

### 6.5 NOT VERIFIED (search budget exhausted)
- **Russia–Ukraine** status. The only indirect signal is that OPEC+ cites "constraints on Russian oil flows."
- **Taiwan** cross-strait risk.
- **EM fund flows.**
- **India macro** (RBI October decision, CPI, rupee, FPI flows). India-analyst notes in this folder (not verified by me) report: Nifty about 22,520 on Oct 9, about 14.6% below its 52-week high; rupee at a record low; heavy FII selling; Nifty IT about -25% YTD.
- **Macro read-across for India from my verified data:**
  - **Brent above $100 is a terms-of-trade negative** for India.
  - **US 10y above 5.2% and DXY rising** pressure EM flows.
  - The lower US tariff (10–12.5% under Section 301, vs. 50% in 2025) and the blocked H-1B fee are positives at the margin.

---

## 7. Sentiment and positioning
| Gauge | Reading | As of | Source | Conf. |
|---|---|---|---|---|
| AAII | **Bull 40.3% / Neutral 20.8% / Bear 39.0%**; bull–bear spread +1.3 (from -11.8). Long-run averages are 37.5 / 31.0 / 31.5, so neutral is well **below** average. 1-year bearish high 53.3% (week to Sept 16) | week ending Oct 7 | [Seeking Alpha/AAII](https://seekingalpha.com/article/4952892-aaii-sentiment-survey-pessimism-plummets), [AAII](https://www.aaii.com/sentimentsurvey) | M/H |
| BofA Global FMS (Sept 4–10; 190 panelists, $512B AUM) | **Cash 3.9%** (from 3.5%), **still below the 4.0% "sell signal" threshold**. Most crowded trade: **long semis 53%** (record 82% in July), short Treasuries 18%, long Mag 7 7%. Top tail risk: **disorderly bond-yield rise, 33%**. **42%** see hyperscaler capex as the likely credit-event source. A record 33% say semis are over-investing | Sept 15 release | [TradingView/MNI](https://www.tradingview.com/news/macenews:fec1f37da094b:0-bofa-global-research-fund-manager-survey-fund-managers-cut-back-on-risk-in-september-amid-rising-uncertainty/), [Investing.com](https://www.investing.com/news/stock-market-news/bofa-survey-shows-investor-cash-levels-rise-amid-policy-concerns-93CH-4901056), [BigGo](https://finance.biggo.com/news/76890938-d6d1-46ac-afa9-3875500a99d5) | M/H |
| CNN Fear & Greed | **Current reading NOT VERIFIED.** Last found: 60 ("greed") on Aug 17; 35 on Jul 29; **16 ("extreme fear") on Apr 12**, during the oil-spike selloff | Aug 17 | [econdash](https://econdash.org/chart/fear-and-greed-index/US) (secondary) | L |
| VIX | 14.84, which is calm, low implied volatility | Oct 9 | §4 | M/H |
| Retail and crypto flows | Spot BTC ETFs had **>$700M outflows** this week | Oct 9 | Rio Times | M |
| Reddit | **NOT VERIFIED.** reddit.com was unreachable and the search budget ran out. A Stocktwits headline lists MSFT, NFLX, "SPCX" and ASTS as in focus ([Stocktwits](https://stocktwits.com/news-articles/markets/equity/s-and-p-500-nasdaq-100-dow-end-week-higher-with-traders-eyeing-earnings-season/cZxGPMYRBnl)); "SPCX" is unidentified, possibly a SpaceX listing (unverified) | n/a | n/a | L |

**Reading:** positioning is not euphoric (AAII balanced, FMS cash rising, VIX low but not extreme), but it is **crowded in semis and AI**. The October FMS (due around Oct 13–14, unverified) is worth checking.

---

## 8. Calendar: next about 3 months
Dates marked * are typical or expected timing that I did not verify this session.

| Date | Event |
|---|---|
| Tue Oct 13 | JPM, GS, C, WFC Q3 earnings |
| Wed Oct 14 | **US Sept CPI** (consensus about 3.7% y/y headline); MS, BAC, BLK earnings |
| ~Oct 13–14* | BofA October Global FMS |
| ~Thu Oct 15 | TSMC Q3 results (date per Zacks); ASML, JNJ, UNH also that week |
| ~Oct 19–20* | China Q3 GDP and September activity data |
| Late Oct* | Mega-cap earnings (MSFT, GOOGL, META, AMZN, AAPL); **2027 capex guides** |
| Tue–Wed Oct 27–28 | **FOMC** (no SEP); about 80% hold priced |
| Thu Oct 29 | ECB decision |
| ~Oct 29–30* | US Q3 GDP advance estimate (GDPNow 3.6%); September PCE |
| Fri Oct 30 | BoJ decision |
| Sun Nov 1 | OPEC+ (7-country) meeting |
| **Tue Nov 3** | **US midterm elections.** Iran escalation risk afterwards (reported Trump threats) |
| ~Fri Nov 6* | US October jobs report |
| ~Nov 18–19* | Nvidia FQ3 FY27 earnings (guide $108B) |
| Nov* | APEC leaders' meeting (Shenzhen), a possible Trump–Xi meeting |
| Tue–Wed Dec 8–9 | **FOMC with SEP and dots**; December hike priced at about 70–85% |
| Fri Dec 11 | **CR expires; shutdown risk from Dec 12** |
| Dec* | G20 (Miami), another Trump–Xi opportunity |
| Jan 10, 2027 | **US–China truce expiry** |
| Ongoing | IEEPA refund litigation at the CIT; Section 122 appeal; new Section 301 "excess capacity" probes; Cook removal effort; H-1B appeal |

---

## 9. Implications (6–18 month horizon)

### 9.1 Favored
1. **AI "picks and shovels" with contracted backlogs and real cash flow.**
   - Names: TSMC; memory (MU, SK Hynix, Samsung); semicap; power-generation and grid equipment (GE Vernova-type backlogs into 2031); electrical and cooling.
   - Evidence: NVDA, TSMC, MU and GEV numbers above.
   - **Caveats:** semis are the most crowded trade, and memory margins (87%) are cyclical-peak-like. Prefer suppliers with multi-year contracts, scale entries, and avoid chasing. Conf. M.
2. **Large, cash-rich quality compounders and the cheaper "S&P 493" (about 17x forward).**
   - With an equity risk premium near zero and 10y above 5%, balance-sheet strength and FCF yield matter. Equal-weight and quality tilts are favored over speculative growth. Conf. M.
3. **Energy, especially refining and products, and select integrateds.**
   - Brent above $100. Product flows through Hormuz are only about 19% of pre-war. SPR depleted. OPEC+ is constrained.
   - **Risk:** a sudden Iran deal could knock $15–25 off Brent (my estimate). Energy is already +40% YTD. Size as a hedge, not a core bet. Conf. M.
4. **Financials with deposit franchises.**
   - The curve is positive (2s10s about +44bp), rates are higher for longer, and banks are -7.5% to -9% over the past month into earnings.
   - A tactical opportunity if Oct 13–14 commentary on credit is benign. **Watch consumer credit** given negative real wages. Conf. L/M.
5. **Japan financials and BoJ-hike beneficiaries.**
   - The BoJ is at 1.25% and under US pressure to continue. A weak yen supports exporters, but intervention risk is high. Conf. L/M.

### 9.2 Unfavored
- **Long-duration, rate-sensitive sectors:** utilities (about -8% YTD despite the power theme), REITs, homebuilders (30y mortgage 7.49%), and unprofitable small caps with floating-rate debt. Russell 2000 fell more than 5% in September.
- **Consumer discretionary:** the worst sector YTD; real wages negative; gasoline and energy +16% y/y.
- **Highly levered AI builders dependent on one customer:** Oracle-like profiles (BBB/negative, about half of RPO tied to OpenAI, negative FCF), and neoclouds. Risk rose after the FT's OpenAI revenue report.
- **China consumer and property:** retail +0.4%, property investment -20%.
- **Oil importers' cyclicals:** airlines and chemicals, given jet fuel and diesel tightness. India is macro-exposed through oil.

### 9.3 Top 5 macro risks
1. **Bond-market tantrum and term premium.** The 10y is at 5.24% (the highest since 2002). Contributors: $1.9T deficit, Fed and ECB hikes, record IG supply. A move to 5.5–6% would compress multiples with an ERP already about zero. This is the #1 FMS tail risk.
2. **Iran and energy escalation.** Talks are stalled, there are threats of post-midterm strikes, product flows remain choked and the SPR is at 1983 lows. A second oil spike would extend the global hiking cycle.
3. **AI financing and credit event.**
   - OpenAI revenue credibility.
   - Circular financing (NVDA backstops).
   - Negative FCF at AMZN and GOOGL.
   - About $220B of hyperscaler bonds with widening concessions.
   - 35% Mag 7 concentration, and NVDA plus MU at about one-third of profit growth.
   - A capex-guide cut or financing hiccup would hit the index disproportionately.
4. **Stagflation and policy error.** Payrolls of +29k, unemployment 4.2% and negative real wages, while the Fed hikes and markets price about 3 more hikes by mid-2027. Fed-independence noise (Cook removal; Trump wants 1%) adds term premium.
5. **Political and trade cliffs.**
   - Midterms Nov 3 (likely a Democratic House means gridlock and investigations).
   - Shutdown deadline Dec 11.
   - US–China truce only to Jan 10, 2027, with rare-earth delivery shortfalls.
   - New Section 301 escalation.
   - 100% pharma tariff on non-capped countries.
   - Possible appellate reversal on Section 122 refunds.

### 9.4 Arguments for caution about buying right now
- The index is **within 0.1% of its record** while the **10y hit a 24-year high this week**. The ERP is about 0% by the forward-earnings-yield method.
- **Narrow leadership:** only 2 of 11 sectors beat the index, 41% of stocks are down YTD, and the Mag 7 are about 35% of market cap.
- **BofA FMS cash 3.9% is still a "sell signal".** Semis are the most crowded trade for 4 months running.
- In a midterm year, history shows an average intra-year drawdown of about 18%. Event density in the next 8 weeks is high: CPI, two Fed meetings, midterms, Iran, shutdown.
- **Counterpoints, so caution is not the same as bearishness:**
  - EPS growth about 30% in 2026 and about 16% in 2027.
  - Forward P/E of 19 is **below** the 5-year average.
  - The early beat rate is 84%.
  - The FactSet bottom-up target implies +21%.
  - VIX is low and AAII is balanced, not euphoric.
- **Practical stance:** stay invested, but stage entries over the CPI, Fed and midterm window; tilt to quality, cash flow and contracted-backlog AI suppliers; hedge duration and energy; avoid leverage and single-customer AI exposure.

---

## 10. Internal inconsistencies and open items for the red team
1. **Core PCE 3.0% vs. core CPI 2.4% (August).** This is atypical and may be an error in secondary sources. Check bea.gov.
2. **S&P YTD:** Reuters editions say ">13%" and ">14%". My +14.1% assumes a 2025 close of about 6,845.5 (from memory).
3. **Sector YTD tables differ by source and method.** ChartRow shows Tech at "+60%", inconsistent with the other sources' +30%.
4. **India's Section 301 rate:** 10% vs. 12.5%.
5. **Microsoft's FY27 capex guide of about $255–260B** comes only from secondary sources. Alphabet Cloud at "+82%" growth is unusually high.
6. **Nikkei Oct 9 change:** -0.02% (Business Recorder) vs. +0.71% (Investing.com).
7. **No Oct 9 Russell 2000, Nasdaq 100 or copper level.** No current CNN Fear & Greed reading. No recession odds.
8. **Not researched** (budget): Russia–Ukraine, Taiwan, Europe growth and defense, EM flows, RBI/India macro, Reddit.

---

## Sources
**Important:** no page could be opened (WebFetch DNS failure on all domains; proxy 403 for cnbc.com). The URLs below were **surfaced by WebSearch, and the figures come from the search tool's summaries of them.** None was opened directly. The list is grouped by topic.

**Fed and US macro**
- https://www.federalreserve.gov/monetarypolicy/files/monetary20260916a1.pdf
- https://www.federalreserve.gov/mediacenter/files/FOMCpresconf20260916.pdf
- https://www.cnbc.com/2026/09/16/fed-rate-decision-september-2026.html
- https://www.cnbc.com/2026/09/18/three-words-from-kevin-warsh-have-wall-street-wondering-how-far-the-fed-will-go-with-rate-hikes.html
- https://www.atlantafed.org/news-and-events/2026/09/16/fomc-statement
- https://www.chase.com/personal/investments/learning-and-insights/article/federal-reserve-raises-rates-officials-signal-one-more-hike-in-2026
- https://www.advisorperspectives.com/dshort/updates/2026/09/16/feds-interest-rate-decision-september-16-2026
- https://www.wealthprofessional.ca/news/industry-news/fed-rate-hike-2026-now-possible/392758
- https://www.cnn.com/2026/09/17/economy/fed-trump-rate-hike-warsh
- https://time.com/article/2026/09/17/fed-interest-rate-hike-trump-kevin-warsh/
- https://finance.yahoo.com/economy/policy/articles/trump-says-us-interest-rates-204406419.html
- https://www.cnn.com/2026/10/09/economy/white-house-investigation-fed-lisa-cook
- https://www.cnbc.com/2026/06/29/supreme-court-lisa-cook-trump-federal-reserve.html
- https://www.axios.com/2026/06/30/trump-cook-fed-supreme-court
- https://www.scotusblog.com/2026/08/trump-informs-lisa-cook-that-he-is-considering-her-removal/
- https://www.cnbc.com/2026/10/02/fed-rate-hike-odds-decline-after-september-jobs-report.html
- https://admiralmarkets.com/analytics/traders-blog/fed-rate-decision-october-2026
- https://mitrade.com/insights/more/inflation/us-cpi-preview-december-fed-hike-20261010J1122
- https://outlookmoney.com/invest/us-fed-rate-hike-impact-india-stocks-rupee-bonds-gold
- https://www.cnbc.com/2026/09/11/cpi-inflation-report-august-2026.html
- https://www.morningstar.com/economy/august-cpi-report-shows-inflation-34-annual-rate-above-forecasts
- https://finance.yahoo.com/economy/articles/u-cpi-rose-0-4-123718937.html
- https://admiralmarkets.com/analytics/traders-blog/us-cpi-preview-september-2026-forecasts-and-the-core-cpi-outlook
- https://tradingeconomics.com/united-states/core-pce-price-index-mom/news/588257
- https://www.bls.gov/news.release/empsit.nr0.htm
- https://www.cnbc.com/2026/10/02/jobs-report-september-2026.html
- https://www.bloomberg.com/news/articles/2026-10-02/us-firms-add-just-29-000-jobs-unemployment-rate-ticks-up
- https://www.bea.gov/sites/default/files/2026-09/gdp2q26-3rd.pdf
- https://www.advisorperspectives.com/dshort/updates/2026/09/30/q2-gdp-third-estimate-real-gdp-at-2-2
- https://tradingeconomics.com/united-states/gdpnow/news/590577
- https://fedpolicy.org/releases/2026-10-06/gdpnow-2026-q3-oct-6/
- https://www.etftrends.com/fixed-income-content-hub/treasury-yields-snapshot-october-9-2026/
- https://www.cnbc.com/amp/2026/10/07/treasury-yields-auction-fomc-minutes.html
- https://www.investing.com/news/economy-news/10-year-us-treasury-yield-hits-highest-since-2002-4926542
- https://www.forbes.com/sites/garthfriesen/2026/10/07/why-the-10-year-treasury-yield-just-hit-a-24-year-high/
- https://streetstats.finance/rates/treasuries/
- https://tradingeconomics.com/united-states/currency
- https://fxstreet.com/news/euro-struggles-as-french-fiscal-concerns-and-firm-us-dollar-dominate-202610091544
- https://www.congress.gov/crs-product/R49353
- https://www.nasfaa.org/news-item/39735/House_Passes_Continuing_Resolution_Funding_Government_Through_December_11
- https://defirate.com/news/democrats-85-percent-to-flip-house-2026-midterms-senate-still-toss-up/
- https://www.actionnetwork.com/politics/2026-midterms-predictions-markets-vs-polls-tracker
- https://home.saxo/learn/guides/us-election/2026-us-midterm-elections-what-different-outcomes-could-mean-for-markets

**Trade**
- https://www.hklaw.com/en/insights/publications/2026/02/supreme-court-strikes-down-ieepa-tariffs
- https://www.flexport.com/blog/the-supreme-courts-ieepa-tariff-ruling-next-steps-potential-refunds-and/
- https://www.swlaw.com/publication/tariffs-redux-what-importers-should-know-about-ieepa-refunds-and-section-122/
- https://www.wiley.law/alert-Trump-Imposes-Section-122-Tariffs-After-Halting-IEEPA-Tariffs-Previews-New-Section-301-Investigations
- https://www.bdo.com/insights/tax/supreme-court-invalidates-ieepa-tariffs-administration-replaces-with-new-surcharge-what-importers
- https://www.skadden.com/insights/publications/2026/05/us-trade-court-strikes-down-section-122-tariffs
- https://www.morganlewis.com/pubs/2026/07/us-administration-rebuilds-global-tariff-program-under-section-301
- https://worldwidelogisticsltd.com/2026/07/24/new-section-301-tariffs-replace-expired-section-122-duties/
- https://globaltaxnews.ey.com/news/2026-0209-us-section-232-proclamation-imposes-25-percent-tariff-on-certain-semiconductors
- https://www.whitecase.com/insight-alert/president-trump-orders-narrowly-targeted-25-section-232-tariff-certain-advanced
- https://www.cov.com/news-and-insights/insights/2026/04/current-and-forthcoming-section-232-actions-by-the-trump-administration
- https://www.mallorygroup.com/blog-posts/100-duties-two-deadlines-section-232-pharmaceutical-tariffs-take-effect-july-31-2026
- https://www.deemedconsulting.com/insights/2026-08-01-section-232-pharmaceutical-tariff
- https://www.ashurst.com/en/insights/tariffs-impact-of-the-recent-us-supreme-court-ruling/
- https://www.cnbc.com/2026/09/24/us-china-trade-truce-bessent-trump-xi.html
- https://www.cnbc.com/2026/09/23/trump-xi-summit-us-china-trade-rare-earth-soybean-plane.html
- https://investinglive.com/news/trump-and-xi-buy-two-more-months-of-trade-truce-leaving-tariffs-and-rare-earths-in-limbo/
- https://www.india-briefing.com/news/india-us-trade-deal-tariff-cuts-timeline-42471.html/
- https://www.cfr.org/articles/u-s-india-trade-truce-announced
- https://upstox.com/news/business-news/latest-updates/when-will-india-us-trade-deal-s-first-tranche-come-into-force-goyal-spells-out-condition/article-197807/
- https://www.impriindia.com/centres/center-for-international-relations-and-strategic-studies/section-301-a-new-challenge-in-india-us-interim-trade-agreement/
- https://www.supplychaindive.com/news/eu-us-trade-deal-halted-supreme-court-tariffs/812832/
- https://fortune.com/2026/02/22/eu-pause-us-trade-deal-ratification-tariff-chaos-trump-supreme-court
- https://www.clarkhill.com/news-events/news/h1b-fee-struck-down-massachusetts-court-2026/
- https://democracyforward.org/news/press-releases/second-federal-court-blocks-trump-vance-administrations-unlawful-innovation-ban/
- https://www.forbes.com/sites/stuartanderson/2026/10/01/judge-strikes-down-latest-version-of-100000-h-1b-immigration-fee/

**Markets and earnings**
- https://finance.yahoo.com/markets/live/stock-market-today-friday-october-9-dow-sp-500-nasdaq-080148117.html
- https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-oct-09-2026
- https://www.cnbc.com/2026/10/05/stock-market-today-live-updates.html
- https://www.cnbc.com/2026/09/30/stock-market-today-live-updates.html
- https://chartrow.com/russell-2000/year-by-year
- https://www.cnbc.com/quotes/.VIX
- https://www.investing.com/indices/volatility-s-p-500-historical-data
- https://tradingeconomics.com/commodity/brent-crude-oil
- https://roboforex.com/beginners/analytics/forex-forecast/gold/xau-usd-gold-weekly-forecast-2026-10-12/
- https://investing.com/news/commodities-news/gold-rises-on-softer-dollar-easing-yields-fed-outlook-in-focus-4940135
- https://www.miningreporters.com/noticia/news/2026/08/copper-price-new-all-time-high-673-lb-london-cochilco
- https://riotimesonline.com/crypto-markets-bitcoin-majors-friday-october-9-2026
- https://fortune.com/article/price-of-bitcoin-10-09-2026/
- https://www.investing.com/news/stock-market-news/openai-annualized-revenue-at-50bn-far-below-reports--ft-4939530
- https://www.bloomberg.com/news/articles/2026-10-08/openai-s-annualized-revenue-nears-50-billion-ft-says
- https://www.vantagemarkets.com/market-news/openai-revenue-50-billion-vs-70-billion-bloomberg-ft-figures-compared-october-9-2026/
- https://insight.factset.com/sp-500-likely-to-report-earnings-growth-above-35-for-q3
- https://insight.factset.com/sp-500-earnings-season-preview-q3-2026
- https://www.factset.com/earningsinsight
- https://www.fool.com/investing/2026/09/24/prediction-the-s-and-p-500-finishes-2027-above-9-000-here-s-the-earnings-math/
- https://www.investing.com/news/economy-news/bank-earnings-cpi-headline-busy-markets-week-as-sp-500-hovers-near-records-4940595
- https://www.theglobeandmail.com/investing/article-wall-streets-week-ahead-bank-earnings-cpi-headline-busy-markets-week/
- https://www.cnbc.com/2026/10/09/earnings-season-kicks-into-high-gear-as-big-banks-report-next-week.html
- https://www.cmcmarkets.com/en-gb/news-and-analysis/the-week-ahead-us-cpi-eurozone-cpi-jpmorgan-earnings
- https://www.goldmansachs.com/insights/articles/s-and-p-500-forecast-to-climb-as-earnings-growth-powers-stocks-higher
- https://finance.yahoo.com/markets/stocks/articles/ed-yardeni-raises-p-500-125931405.html
- https://marketscreener.com/news/panmure-liberum-sets-2027-year-end-s-p-500-target-at-5-000-ce785ddbdf80f72c
- https://qz.com/wall-street-sp500-targets-8000-pullback-risks-090926
- https://www.fool.com/investing/2026/09/27/does-the-sp-500-have-a-magnificent-seven-problem-h/
- https://en.macromicro.me/series/46223/share-of-m7-total-market-cap
- https://www.forbes.com/sites/investor-hub/article/sp-500-weight-mag-7-stocks-diversification-risk/
- https://chartrow.com/sp500/stock-performance
- https://chartrow.com/sp500/sector-performance
- https://seekingalpha.com/article/4952113-2-tickets-to-outperformance
- https://georgedagninophd.substack.com/p/sector-performance-since-22826

**AI and capex**
- https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/07/alphabet-postq-ai-growth-accelerates-as-spending-weighs-on-cash-flow
- https://www.webull.com/news/15277620003939328
- https://www.thestar.com.my/business/business-news/2026/07/31/microsoft-sees-strong-cash-flow-lower-capex
- https://app.sentisense.ai/stories/microsofts-ai-investments-pay-off-boosting-the-stock-market-and-tech-sector-07312026
- https://letsdatascience.com/news/aws-revenue-growth-outruns-available-ai-capacity-b0361d90
- https://startupmap.iamsterdam.com/news/feed/amazon-to-spend-over-220b-on-ai-capex-in-2026-as-aws-hits-42b-revenue-up-37
- https://247wallst.com/investing/2026/07/29/live-will-meta-crush-q2-earnings-tonight-after-market-close/liveupdates/7/
- https://www.ig.com/au/news-and-trade-ideas/meta-q2-2026-earnings-preview-260727
- https://www.oracle.com/news/announcement/q1fy27-earnings-release-2026-09-10/
- https://www.outlookbusiness.com/corporate/oracle-forecasts-95-bn-in-capex-for-fy27-plans-to-raise-40-bn-in-debt-and-equity
- https://fourweekmba.com/ai-oracle-q1-fy2027-backlog-capex-analysis/
- https://www.yieldtheory.app/research/hyperscaler-ai-capex-tracker-2026
- https://valueaddvc.com/blog/big-tech-ai-capex-in-2025-microsoft-google-meta-amazon-and-the-spending-race
- https://www.nasdaq.com/articles/nvidia-q2-earnings-beat-blackwell-ultra-data-center-strength
- https://www.webull.com/blog/304-Nvidia-Q2-FY2027-Earnings-Beats-Revenue-EPS-Estimates-Guides-Q3-to-108B
- https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000680/tsm-revenue20261008.htm
- https://www.hudson-labs.com/research/tsmc-q3-2026-earnings-preview-tsm-revenue-and-margins
- https://www.nextplatform.com/store/2026/10/02/microns-numbers-show-why-hbm4-memory-is-worth-15x-its-weight-in-gold/5300701
- https://www.zacks.com/stock/news/2756578/micron-beats-on-q4-earnings:-will-strong-guidance-lift-the-stock
- https://www.outlookbusiness.com/explainers/inside-the-ai-bubble-how-openai-nvidia-are-weaving-a-web-of-circular-deals
- https://www.cnbc.com/2026/07/27/jim-cramer-warns-ai-circular-financing-echoes-dot-com-bubble.html
- https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html
- https://techcrunch.com/2026/08/17/anthropics-annualized-revenue-surges-to-65b/
- https://www.axios.com/2026/08/17/anthropic-revenue-run-rate-ipo-openai
- https://finance.yahoo.com/markets/stocks/articles/hyperscaler-debt-binge-pushes-yields-134825104.html
- https://mlq.ai/news/hyperscaler-bond-issuance-reaches-about-220-billion-as-ai-financing-costs-rise/
- https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure
- https://www.utilitydive.com/news/ge-vernova-gas-turbine-backlog-climbs-to-116-gw/826039/
- https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000147/gevpressrelease2q26.htm
- https://finance.yahoo.com/energy/articles/gas-turbine-shortage-just-became-210000180.html

**Rest of world, oil, sentiment**
- https://www.cnbc.com/2026/04/21/oil-price-iran-war-middle-east.html
- https://www.cnn.com/2026/04/30/energy/oil-prices-iran-war-wartime-high-blockade-hnk
- https://www.aljazeera.com/economy/2026/7/2/oil-prices-fall-to-levels-not-seen-since-start-of-us-israel-war-on-iran
- https://www.france24.com/en/middle-east/20261004-iran-us-military-middle-east-war-peace-talks
- https://www.cbsnews.com/live-updates/iran-war-us-trump-talks-strait-of-hormuz/
- https://www.cbsnews.com/live-updates/iran-war-us-negotiations-strait-of-hormuz-oil/
- https://www.cnbc.com/2026/09/30/iran-war-strait-hormuz-gulf-oil-fuel.html
- https://www.iea.org/topics/the-middle-east-and-global-energy-markets
- https://www.cnbc.com/2026/10/04/opec-agrees-to-keep-november-oil-output-targets-steady.html
- https://www.enerdata.net/publications/daily-energy-news/opec-keeps-november-2026-production-targets-unchanged-amid-supply-disruptions.html
- https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.mp260910~314e508016.en.html
- https://www.cnbc.com/2026/09/10/ecb-interest-rate-hike-lagarde-iran.html
- https://www.cnbc.com/2026/09/18/japan-raises-rates-30-year-high-yen-jgb.html
- https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2026/k260918a.pdf
- https://brecorder.com/news/40443513/nikkei-limps-to-weekly-loss-as-bond-stress-weigh
- https://www.investing.com/indices/japan-ni225-historical-data
- https://www.cnbc.com/2026/09/15/china-august-retail-sales-industrial-output-investment-exports-.html
- https://www.fxstreet.com/news/chinas-retail-sales-rise-04-in-august-industrial-production-up-52-202609150207
- https://www.bbntimes.com/financial/hang-seng-jumps-to-24-211-35-as-xiaomi-tencent-and-internet-stocks-lead-a-sharp-rebound-in-hong-kong
- https://news.rthk.hk/rthk/en/component/k2/1873307-20261009.htm
- https://seekingalpha.com/article/4952892-aaii-sentiment-survey-pessimism-plummets
- https://www.aaii.com/sentimentsurvey
- https://www.tradingview.com/news/macenews:fec1f37da094b:0-bofa-global-research-fund-manager-survey-fund-managers-cut-back-on-risk-in-september-amid-rising-uncertainty/
- https://www.investing.com/news/stock-market-news/bofa-survey-shows-investor-cash-levels-rise-amid-policy-concerns-93CH-4901056
- https://finance.biggo.com/news/76890938-d6d1-46ac-afa9-3875500a99d5
- https://econdash.org/chart/fear-and-greed-index/US
- https://stocktwits.com/news-articles/markets/equity/s-and-p-500-nasdaq-100-dow-end-week-higher-with-traders-eyeing-earnings-season/cZxGPMYRBnl
