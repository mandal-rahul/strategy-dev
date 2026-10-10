# Global Equity Research: Buy-Now Quality and Beaten-Down Names

**Prepared:** Saturday 2026-10-10 (last session: Fri 2026-10-09)
**Analyst role:** Global equity research (for red-team fact-check)

---

## READ FIRST: How this data was gathered (and its limits)

The red team should know exactly how far each number has been verified.

1. **WebFetch failed on every domain I tried.** Each call returned `getaddrinfo ENOTFOUND`, or "unable to fetch" for reuters.com. Domains tried: stockanalysis.com, finance.yahoo.com, companiesmarketcap.com, cnbc.com, marketbeat.com, global.morningstar.com, en.wikipedia.org, sec.gov and thriveinmarkets.com. **I could not open any page directly.**
2. **curl/Bash was blocked by the organization's egress policy** (CONNECT 403) for stockanalysis.com, query1.finance.yahoo.com, sec.gov, macrotrends.net, old.reddit.com and google.com. **Reddit could not be accessed directly.**
3. **WebSearch hit its shared per-turn limit** (200 calls across all agents) after about 45 of my queries. Uber/Delivery Hero deal details, Intuit FY26 actuals and several balance-sheet items could therefore not be checked.
4. **As a result, every number below comes from WebSearch result summaries.** Those summaries quote the underlying pages, and each one is cited with its URL and as-of date, but **I did not open the pages myself.** Treat every figure as "search-summary-sourced". Where sources disagreed I say so. Where I calculated a figure myself, it is marked **(calc)**. Anything I could not find is marked **not verified**.
5. Prices are the latest I could find. **Most are Oct 5–9, 2026 closes, and a few are older (labeled).** The red team should re-pull Oct 9 closes for every name.

---

## Market backdrop (as of early October 2026)

- **S&P 500:** Closed at a record **7,818.93 on Oct 6, 2026**, up 1.2% week-to-date per the AP tally ([La Nación/AP, 2026-10-06](https://www.lanacion.com.ar/usa/how-major-us-stock-indexes-fared-tuesday-1062026-nid06102026/)). Total return YTD was about **+13.7%** (price-only +12.9%) as of Oct 2 ([Chartrow](https://chartrow.com/sp500/stock-performance)).
- **Sector leaders and laggards:** As of Sep 28, Energy was **+38.9%** and Tech **+35.1%** YTD. Consumer Discretionary was weakest at **−8.7%** ([Chartrow sectors](https://chartrow.com/sp500/sector-performance)). An Oct 7 Substack puts Energy around +38–42% and IT around +30–31%, with Financials, Utilities, Consumer Discretionary, Communication Services and Real Estate "flat to negative" ([Dagnino, 2026-10-07](https://georgedagninophd.substack.com/p/sector-performance-since-22826)).
- **Macro risk:** On Oct 8, European stocks fell to their lowest since mid-June on an oil spike tied to Middle East tensions ([Trading Economics, 2026-10-08](https://tradingeconomics.com/euro-area/stock-market/news/556957)). Coverage also cites an "oil shock and higher cost of capital" weighing on software ([24/7 Wall St on APP, 2026-10-02](https://247wallst.com/investing/2026/10/02/applovin-has-fallen-nearly-60-in-2026-180-returns-are-in-store-for-investors-according-to-this-wall-street-pro/)).
- **The defining 2026 theme is the "AI-disruption" de-rating of software and IT services.**
  - The S&P 500 Software & Services index fell more than 33% from its Oct 2025 peak to its Apr 2026 low (Reuters figure quoted in search summaries of [24/7 Wall St, 2026-08-26](https://247wallst.com/investing/2026/08/26/intuit-sinks-12-as-ai-disruption-fears-spread-from-turbotax-to-quickbooks-adobe-and-servicenow-drop-3/)).
  - Bloomberg reported software getting "new life from strong earnings" by mid-September ([Bloomberg, 2026-09-18](https://www.bloomberg.com/news/articles/2026-09-18/software-stocks-get-new-life-from-strong-earnings-ai-warnings)), then "AI whiplash", with money swinging out of and back into AI-exposed stocks ([Bloomberg, 2026-09-27](https://www.bloomberg.com/news/articles/2026-09-27/ai-whiplash-jolts-stocks-as-sentiment-lurches-from-fear-to-greed)).
  - On Oct 8, "AI-victim" stocks (Accenture +5.96%, Gartner +5.19%, Cognizant +5.15%) rallied while AI-infrastructure names sank ([24/7 Wall St, 2026-10-09](https://247wallst.com/investing/2026/10/09/the-stocks-wall-street-thought-ai-would-kill-just-jumped-5-while-ai-darlings-sank/)).
- **Magnificent 7:** The group was **+10.85% YTD vs S&P +12.81%** as of Oct 3. Microsoft, Alphabet and Meta were roughly +9% to +12% YTD as of Oct 2, and Tesla was the laggard at about −15% to −18% ([Motley Fool, 2026-10-01](https://www.fool.com/investing/2026/10/01/best-performing-magnificent-seven-stock-2026/); [Chartrow Mag 7](https://chartrow.com/lists/magnificent-7)). **Mega-cap tech is not on sale broadly. The discounts are concentrated in application software, consumer internet, med-tech, GLP-1 pharma and consumer discretionary.**
- **Morningstar:** Its most recent list I could find is from Q2 2026. It said US stocks traded **14% below fair value** and named tech, communication services, real estate and consumer cyclicals as the most undervalued sectors. Its "33 undervalued" list included Elevance, Comcast, Broadcom, Blackstone and Energy Transfer, and it said "most" health-plan stocks looked undervalued ([Morningstar 33 undervalued](https://global.morningstar.com/en-gb/stocks/33-undervalued-us-stocks-buy-volatile-market); [Morningstar outlook](https://global.morningstar.com/en-gb/markets/where-us-stock-market-may-be-heading-next-what-buy-now)). **I could not find an October 2026 Morningstar list.**

**Worst S&P 500 total returns YTD as of the Oct 8 close** ([Chartrow](https://chartrow.com/sp500/stock-performance)): Corteva −79.3% (likely a corporate-action artifact, not verified), Trade Desk −67.5%, AppLovin −58.4%, Fair Isaac −58.2%, **Boston Scientific −55.9%**, CoStar −55.7%, **Lululemon −55.4%**, **Intuit −53.5%**, Insulet −52.7%, Pentair −49.3%.

---

## Uber and Netflix: are they beaten down now? (the user named both)

**Yes, both are materially off their highs today. Unlike in 2022, both are now large free-cash-flow generators.**

| | Price (date) | 52-wk high | % below high | YTD | Key 2026 problem |
|---|---|---|---|---|---|
| **Netflix (NFLX)** | $71.57 (Oct 8 close) | $124.86 (Oct 21, 2025) per stockinvest; $126.71 per Barchart | **about −43%** (calc) | about −27% (Fool, Oct 7) | Engagement decline, slowing growth, lost WBD bid, subscriber-disclosure halt |
| **Uber (UBER)** | $70.24 (Oct 8 close) | $100.35 | **about −30%** (calc) | about −16% (Fool) | Robotaxi capex (>$10B plan), Waymo exclusivity doubts, soft Q3 profit guide |

The parallel to 2022 is partial.

- **Netflix in 2022** was losing subscribers and trading near the mid-teens on P/E. Today it grows revenue about 13% with a 31.5% margin guide and about $12.5B FCF guide, at roughly 19–20x forward earnings and about 24–27x FCF.
- **Uber in 2022–23** was barely FCF-positive. Today it has more than $10B of TTM FCF and trades around 14–15x FCF.

Both are on the shortlist (bucket B). Details are in their sections below.

---

## SUMMARY TABLE (ranked)

Prices are the latest found, with dates shown. P/E figures are as cited in the stock sections. (calc) means my own arithmetic from the cited inputs.

| Rank | Ticker | Bucket | Price (as-of) | % below 52w high | Fwd P/E (approx) | Other valuation | Conviction (1–5) | Next catalyst |
|---|---|---|---|---|---|---|---|---|
| 1 | **INTU** (Nasdaq) | B | $291.08 (Oct 6, intraday) | about −58% | **about 12.7x** FY27 guide (calc) | FY27 rev +9–10% guided | **4** | FQ1 FY27 results (date not verified, likely late Nov) |
| 2 | **NFLX** (Nasdaq) | B | $71.57 (Oct 8) | about −43% | about 19–20.5x | P/FCF 26.7 TTM (Sep 28); about 24.7x on 2026 FCF guide (calc) | **4** | Q3 results **Oct 20** |
| 3 | **UBER** (NYSE) | B | $70.24 (Oct 8) | about −30% | about 15.9x | P/FCF about 14–15x | **4** | Q3 results **Nov 4** |
| 4 | **TSM** (NYSE ADR) | A | $453.31 (Oct 9) | not verified | about 20.3–21.2x | Trailing about 29.7x; 5-yr avg fwd about 21.8x | **4** | Q3 results **Oct 15** |
| 5 | **ADBE** (Nasdaq) | B | $242.25 (Oct 9) | about −33% | not verified (about 8x in Jun/Jul, stale) | Trailing P/E about 13x (calc) | **3** | FQ4 results (date not verified, typically mid-Dec) |
| 6 | **ELV** (NYSE) | A | $400.09 (Oct 6) | near 52w high | **about 14.8x** 2026 guide (calc) | Trailing about 18x | **3** | Q3 results **Oct 21** |
| 7 | **CRM** (NYSE) | A/B | $229.13 (Oct 9) | not verified | about 14.7–15.5x | Trailing 21.1x | **3** | Q3 FY27 results (Nov 30 per one source, not verified) |
| 8 | **BSX** (NYSE) | B | $44.18 (Sep 29) | about −55% YTD | about 12.8x on original 2026 guide (calc, guide now at risk) | — | **3** | Q3/revised guide **Oct 28** (one source) |
| 9 | **GOOGL** (Nasdaq) | A | $348.29 (Oct 8) | not verified | about 16.5–22.8x (sources conflict) | Trailing about 17.3–17.6x | **3** | Q3 results **Oct 28** |
| 10 | **AMZN** (Nasdaq) | A | $259.92 (Oct 7) | not verified | about 19–20x (sources conflict) | FCF negative on $220B capex | **3** | Q3 results (date not verified) |
| 11 | **NOW** (NYSE) | B | $139.75 (Oct 8) | about −40% YTD (tikr) | about 30.8x | P/FCF about 31 vs 10y median 57.7 | **3** | Q3 results (date not verified) |
| 12 | **UNH** (NYSE) | A | $377.42 (Sep 28; Oct not verified) | about −18% | **about 19.1x** 2026 guide (calc) | — | **3** | Q3 results (date not verified) |
| 13 | **NVO** (NYSE ADR) | B | $38.18 (Oct 8) | about −40% | — | P/E about 9.7 | **2** | Q3 results (date not verified, early Nov typical) |
| 14 | **PYPL** (Nasdaq) | B | $54.41 (Oct 5) | about −31% | **about 9.1–9.5x** | Trailing about 10x | **2** | Q3 results (date not verified) |

**Bucket A** = buy-now quality at a fair price. **Bucket B** = beaten down, below fundamentals.

---

# BUCKET B: BEATEN-DOWN, BELOW FUNDAMENTALS

## 1. Intuit (INTU, Nasdaq): Bucket B, Conviction 4

**Price and valuation**
- **Price:** $291.08 intraday on **Oct 6, 2026** (+2.25%), and $281.08 on Oct 2 ([ad-hoc-news, 2026-10-06](https://www.ad-hoc-news.de/boerse/news/corporate-news/intuit-stock-gains-2-25-percent-while-growth-guidance-cools/70243920); [ad-hoc-news](https://www.ad-hoc-news.de/boerse/news/corporate-news/intuit-stock-trades-below-its-consensus-target-despite-growth-guidance/70227544)). **The Oct 9 close is not verified.**
- **52-week range:** High $689.17; low not verified. At $291 the stock is **about 57.8% below its high** (calc). Chartrow puts the YTD total return at **−53.5%** as of Oct 8 ([Chartrow](https://chartrow.com/sp500/stock-performance)).
- **Market cap:** not verified.
- **Forward P/E:** **about 12.7x** on the FY27 (July 2027 year-end) non-GAAP EPS guide of $22.88–23.12 (calc: $291.08 / $23.00). Trailing P/E is not verified.

**Guidance and growth** (guide issued Aug 25, 2026; reaffirmed at the Sep 17 Investor Day)
- FY27 revenue of **$23.28–23.51B (+9–10%)** and non-GAAP EPS of **$22.88–23.12**. That EPS was **below the then-consensus of $27.30**.
- Global Business Solutions is guided to grow 13–14%. FQ1 non-GAAP EPS is guided at $2.44–2.48.
- Sources: [Yahoo, Aug 2026](https://finance.yahoo.com/markets/stocks/articles/intuit-shares-plunge-cautious-fiscal-104320782.html); [StockTitan, Investor Day](https://www.stocktitan.net/news/INTU/intuit-hosts-investor-day-reaffirms-first-quarter-and-fiscal-2027-z9sgro2wbu5j.html); [Seeking Alpha](https://seekingalpha.com/news/4643811-intuit-reaffirms-fiscal-2027-guidance).
- **Not verified:** FY26 revenue/EPS actuals, margins, FCF, net debt and buyback pace. The search budget ran out before I could pull FY26 results.

**Why it fell**
1. AI-agent disruption fears spread from TurboTax to QuickBooks.
2. On **Aug 25–26, 2026** the stock fell **12% to $315.61** on the FY27 guidance reset. It was already −46% YTD at that point ([24/7 Wall St, 2026-08-26](https://247wallst.com/investing/2026/08/26/intuit-sinks-12-as-ai-disruption-fears-spread-from-turbotax-to-quickbooks-adobe-and-servicenow-drop-3/)).
3. Management blamed weaker Mailchimp, a shrinking Desktop business and deliberate TurboTax changes. FY26 online paying customers grew only 3% ([ad-hoc-news](https://www.ad-hoc-news.de/boerse/news/corporate-news/intuit-stock-faces-a-growth-reset-as-fy2027-guide-stays-at-9-to-10-percent/70198414)).

**Why it may be mispriced**
- It is still guiding to roughly 9–10% revenue growth and about 23 dollars of EPS. At about 12.7x forward earnings it is priced like a no-growth business.
- A reverse-DCF sketch (calc): at about 12.7x, a 10% EPS-growth franchise with high returns on capital is discounting either structural decline or a permanent margin collapse. Neither is in management's guide.
- The business-segment (QuickBooks/GBS) growth guide of 13–14% argues against "QuickBooks is being displaced right now".

**Analyst view and catalysts**
- **Consensus target:** about **$406–431** (sources differ: [Yahoo](https://finance.yahoo.com/markets/stocks/articles/intuit-stock-analysis-why-street-134844647.html) says the mean was cut from $456 to $406; [ad-hoc-news](https://www.ad-hoc-news.de/boerse/news/corporate-news/intuit-stock-trades-below-its-consensus-target-despite-growth-guidance/70227544) cites $431.55). The rating breakdown is not verified.
- **Catalysts:** FQ1 FY27 results (date not verified; historically late Nov), then tax season Jan–Apr 2027 (TurboTax unit data).

**Risks and what would prove the thesis wrong**
- A guidance cut at FQ1.
- QuickBooks online subscriber or ARPC deceleration.
- Evidence that AI tax filing (free agents, IRS or bank tools) is taking share in the 2027 season.
- A further fall in online paying customer growth.

**Reddit/retail:** Not directly accessible. Search surfaced no Reddit thread, and secondhand coverage frames Intuit as a 52-week-low "AI victim".

---

## 2. Netflix (NFLX, Nasdaq): Bucket B, Conviction 4

**Price and valuation**
- **Price:** **$71.57, Oct 8, 2026 close** (range $69.72–71.61), from quote pages surfaced by search ([stockinvest.us](https://stockinvest.us/stock/NFLX); [Barchart](https://www.barchart.com/stocks/quotes/NFLX/price-history/historical)). **The Oct 9 close is not verified.**
- **52-week range:**
  - High: **$124.86 (Oct 21, 2025)** per stockinvest, or $126.71 (Sep 5, 2025) per Barchart. *This conflicts between sources.*
  - Low: **$65.08 (Jul 17, 2026)**.
  - At $71.57 the stock is **about 42.7% below its high** (calc).
  - YTD about −27% ([Motley Fool, 2026-10-07](https://www.fool.com/investing/2026/10/07/1-number-explain-nflx-stock-down-2026/)). It lost 14% in September ([Fool, 2026-10-01](https://www.fool.com/investing/2026/10/01/why-netflix-lost-14-in-september/)).
- **Market cap:** about **$308B** (calc, from GuruFocus's P/FCF of 26.73 on $11.152B TTM FCF at $69.23, which implies about 4.31B shares). The Sep 10 snapshot was $316.1B ([heygotrade](https://www.heygotrade.com/en/market-outlook/netflix-stock-forecast/)).
- **Forward P/E:** **about 19–20.5x**. GuruFocus had 20.48 on Aug 4 ([GuruFocus](https://www.gurufocus.com/term/forward-pe-ratio/NFLX)). Motley Fool via heygotrade had about 19x at $67.50 in late July.
- **P/FCF:** **26.73 on TTM FCF of $11.15B (Sep 28)**, which is 54% below its 10-year median of 57.8 ([GuruFocus](https://www.gurufocus.com/term/price-to-free-cash-flow/NFLX); [GuruFocus FCF](https://www.gurufocus.com/term/total-free-cash-flow/NFLX)). On the 2026 FCF guide of about $12.5B it is **about 24.7x** (calc).

**Q2 2026 results** (reported Jul 16, 2026; [SEC 8-K ex99.1](https://www.sec.gov/Archives/edgar/data/0001065280/000106528026000211/ex991_q226.htm); [TradingView](https://www.tradingview.com/news/tradingview:047fc5894e749:0-netflix-posts-q2-revenue-12-6b-operating-margin-33-4-and-narrows-2026-revenue-range/); [CNBC](https://www.cnbc.com/2026/07/16/netflix-nflx-earnings-q2-2026.html))
- Revenue **$12.56B, +13% y/y** (+12% FX-neutral).
- Operating margin **about 33%** (TradingView: 33.4%, operating income $4.19B).
- EPS **$0.80 vs $0.79** consensus.
- Q2 FCF $1.5B (vs $2.3B a year earlier, partly on higher cash taxes).

**Guidance and capital return**
- **FY2026 guide:** revenue **$51.0–51.4B** (narrowed from $50.7–51.7B), operating margin **31.5%**, FCF **about $12.5B**, and ad revenue expected to roughly double to **about $3B**.
- **Q3 guide:** revenue about $12.86B and EPS $0.82 ([Nasdaq/RTT](https://www.nasdaq.com/articles/netflix-q2-profit-rises)). Consensus is about $0.83 on $13.02B ([Earnings Whispers](https://earningswhispers.com/epsdetails/NFLX/202606)).
- **Buybacks:** an additional **$25B authorization (Apr 2026)**, with **$4.7B repurchased in Q2** ([24/7 Wall St, 2026-07-20](https://247wallst.com/investing/2026/07/20/netflix-buy-the-dip-or-wait-for-proof/)).
- **Net debt/cash:** not verified.

**Why it fell (specific events)**
1. The 2026 guide implies one of its slowest growth rates ever ([Fool, Oct 7](https://www.fool.com/investing/2026/10/07/1-number-explain-nflx-stock-down-2026/)).
2. Viewing hours per member are declining, and competition from YouTube and short-form video is growing ([Yahoo/Investing.com](https://finance.yahoo.com/markets/stocks/articles/3-reasons-why-netflix-shares-172551823.html)).
3. Netflix stopped reporting subscriber numbers.
4. Its bid of about $72B in cash for the Warner Bros. Discovery studio and streaming assets raised overpayment fears. It ultimately lost that bid ([Fool, Jul 8](https://www.fool.com/investing/2026/07/08/why-netflix-dropped-24-in-the-first-half-of-2026/)).
5. Reed Hastings stepped down as chairman.
6. After Q2 it fell about 12% over two days when it limited access to engagement data.
7. In September it fell 14% after Co-CEO Sarandos acknowledged disappointing engagement.
8. **Wells Fargo downgraded it to Underweight with a $57 target (from $80) on Sep 18**, expecting hours per member down about 4% y/y in H2 ([Yahoo](https://finance.yahoo.com/markets/stocks/articles/wells-fargo-downgrades-netflix-stock-180752599.html); [Schaeffer's](https://www.schaeffersresearch.com/content/news/2026/09/18/downgrade-steep-price-target-cut-dings-netflix-stock)).
9. HSBC cut it to Hold ([briefs.co](https://www.briefs.co/news/netflix-s-2026-slump-deepens-as-engagement-worries-grow/)).

**Why it may be mispriced**
- The P/FCF is roughly half its 10-year median, while revenue still grows about 13% and the margin guide is intact at 31.5%.
- Ads are doubling.
- Heavy buybacks at depressed prices.
- BofA explicitly compares the setup to 2022 and late 2023, both of which were followed by recoveries ([Yahoo/Investing.com](https://finance.yahoo.com/markets/stocks/articles/3-reasons-why-netflix-shares-172551823.html)).
- The WBD overhang is gone because Netflix lost the bid.

**Analyst view and catalysts**
- **Consensus:** "Moderate Buy". 38 of 52 analysts rate it Buy or Strong Buy (LSEG via CNBC). The mean target is about **$96**. Evercore is Outperform with a $110 target ([Schaeffer's](https://www.schaeffersresearch.com/content/news/2026/09/18/downgrade-steep-price-target-cut-dings-netflix-stock); [Insider Monkey](https://www.insidermonkey.com/news/wells-fargo-cuts-netflix-nflx-to-underweight-as-its-2026-slide-deepens-1841150/)).
- **Catalysts:** **Q3 results Tue Oct 20, 2026, about 1:01pm PT** ([Netflix IR release PDF](https://s22.q4cdn.com/959853165/files/doc_news/Netflix-to-Announce-Third-Quarter-2026-Financial-Results-2026.pdf)). *One search summary said Oct 17; the company release says Oct 20.* The FY2027 outlook is likely with Q4 results in January.

**Risks and what would prove the thesis wrong**
- Engagement keeps falling while content spend rises, so margin guidance gets cut.
- The 2027 revenue guide comes in below about 10%.
- Another large M&A attempt.
- Ad-tier monetization stalls.

**Reddit/retail (secondhand only):** After Q2, the top r/stocks post that week read "Netflix beat earnings, did its biggest buyback and then restricted access to its engagement data and fell 12% through two days" (quoted in [24/7 Wall St, Jul 20](https://247wallst.com/investing/2026/07/20/netflix-buy-the-dip-or-wait-for-proof/)). Sentiment reads as skeptical and frustrated, which is typical of a washed-out name.

**Entry note:** There is binary event risk on Oct 20. The investor can buy now, but sizing should allow for a ±10–15% earnings move.

---

## 3. Uber Technologies (UBER, NYSE): Bucket B, Conviction 4

**Price and valuation**
- **Price:** **$70.24, Oct 8, 2026 close** (+2.62%) ([Seeking Alpha](https://seekingalpha.com/symbol/UBER)). The Oct 7 close was $68.45 ([Motley Fool quote](https://www.fool.com/quote/nyse/uber/)). **The Oct 9 close is not verified.**
- **52-week range:** about **$65.41–100.35** ([Kraken](https://www.kraken.com/stocks/uber)), so the stock is **about 30% below its high** (calc). It is −16% YTD and about −30% over one year (Motley Fool period returns).
- **Market cap:** about **$141.8B** (Yahoo key stats, date not shown) ([Yahoo](https://finance.yahoo.com/quote/UBER/key-statistics/)).
- **Forward P/E:** **about 15.9** (Yahoo "current"), down from 21.6 on Jun 30, 2026. StockAnalysis showed about 16.8 on an older snapshot.
- **P/FCF:** **15.57 on Sep 4 at $75.48**, 52% below its 10-year median of 32.3 ([GuruFocus](https://www.gurufocus.com/term/price-to-free-cash-flow/UBER)). At $70.24 that is **about 14.5x** (calc).

**Q2 2026 results** (reported Aug 5, 2026; [Uber IR](https://investor.uber.com/news-events/news/press-release-details/2026/Uber-Announces-Results-for-Second-Quarter-2026/default.aspx); [SEC 8-K](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm); [Quartr](https://quartr.com/events/uber-technologies-inc-uber-q2-2026_3PkHdWXK))
- Gross bookings **$58.0B, +24%** (+22% constant currency), versus a $57.23B estimate.
- Revenue **$14.19B, +12%**. Business-model changes cut about 8 points from reported growth.
- Adjusted EBITDA **$2.82B, +33%**, or 4.9% of gross bookings (vs 4.5% a year earlier).
- Q2 FCF **$2.79B**. **TTM FCF passed $10B for the first time.**
- Q2 non-GAAP EPS of $0.81 was either in line or a miss, depending on the source (*conflict*).
- **Net debt/cash:** not verified.

**Q3 guidance**
- Gross bookings $58.25–60.25B (+18–22% constant currency).
- Adjusted EBITDA $2.86–2.96B.
- Non-GAAP EPS **$0.84–0.88**, against an $0.89 consensus ([Yahoo](https://finance.yahoo.com/markets/stocks/articles/uber-q2-2026-earnings-guidance-111918644.html)).

**Why it fell**
1. On Aug 5 the Q3 profit guide disappointed and Uber laid out plans to spend **more than $10B on robotaxis** over the coming years. Shares fell 4.8–5.3% ([BNN Bloomberg/Reuters, 2026-08-05](https://www.bnnbloomberg.ca/business/company-news/2026/08/05/uber-forecasts-weak-quarterly-profit-doubles-down-on-robotaxi-investment-plans/)).
2. Reports said **Waymo may end exclusivity with Uber in Atlanta and Austin**.
3. Melius downgraded it to Sell in January on autonomous-vehicle risk.
4. A **$14.8B acquisition involving Delivery Hero** (deal terms not verified; the search budget ran out).
5. Uber is funding a California ballot measure on attorney fees with $77M ([eciks.org](https://eciks.org/10607-16119-uber-stock-robotaxi-legal-pressures)).

**Why it may be mispriced**
- About 14–15x FCF for a business compounding gross bookings near 20% with EBITDA up 33%.
- The market is pricing robotaxis as a terminal threat. The bull view is that Uber becomes the demand aggregator for multiple autonomous-vehicle fleets.
- 2022–23 parallel: back then Uber had to prove profitability. Now the debate is about capital allocation and autonomous vehicles, not survival.

**Analyst view and catalysts**
- **Consensus:** "Buy" from 50 analysts, with a target of **$100.86** ([StockAnalysis via search](https://stockanalysis.com/stocks/uber/)). BofA has a $103 target ([tikr](https://www.tikr.com/blog/uber-stock-is-down-9-in-2026-heres-why-analysts-still-see-upside-to-103)).
- **Catalysts:** **Q3 results Nov 4, 2026** (StockAnalysis); Waymo/Tesla city launches; Delivery Hero deal close (not verified).

**Risks and what would prove the thesis wrong**
- Waymo or Tesla going direct-to-consumer at scale in Uber's top cities.
- Gross bookings growth falling below about 15%.
- Robotaxi capex eroding FCF below about $8B.
- An adverse ruling on driver classification or regulation.

**Reddit/retail:** Not verified (no Reddit access).

---

## 4. Adobe (ADBE, Nasdaq): Bucket B, Conviction 3

**Price and valuation**
- **Price:** **$242.25 on Oct 9, 2026** (Robinhood quote; day range $240.55–245.16; whether intraday or close is not confirmed). Market cap is **about $94.3B** ([Robinhood](https://robinhood.com/us/en/stocks/ADBE/)). The Oct 7 close was $232.77 ([WallStreetZen](https://www.wallstreetzen.com/stocks/us/nasdaq/adbe)).
- **52-week range:** **$190.12–363.70**, so the stock is **about 33% below its high** and +27% off the mid-2026 low (calc).
- **Trailing P/E:** 12.97 at $232.77 on Oct 7, which is about 13.5x at $242.25 (calc).
- **Forward P/E:** **not verified for October.** It was about 8x in June/July at much lower prices ([24/7 Wall St, Jul 1](https://247wallst.com/investing/2026/07/01/adobe-nearing-52-week-low-buy-sell-or-hold/); [tikr](https://www.tikr.com/blog/adobe-stock-is-trading-near-52-week-low-heres-where-shares-could-go-in-2026)).

**Not verified:** latest-quarter revenue/EPS, guidance, FCF, net cash and the buyback figure. Earlier coverage notes buybacks lifting per-share earnings.

**Why it fell:** Generative-AI disruption of creative and document workflows, and fears for seat-based SaaS models. In February, Adobe, Salesforce and ServiceNow were each down about 25–30% YTD ([Motley Fool, Feb 18](https://www.fool.com/investing/2026/02/18/the-2026-software-stock-sell-off-ai-disruption-fea/)).

**Why it may be mispriced:** A low-teens trailing P/E for a business with historically very high gross margins and heavy buybacks. The market is pricing secular decline.

**Catalysts:** FQ4 FY26 results (date not verified, historically mid-December) and FY27 guidance.

**Risks and what would prove the thesis wrong**
- Digital Media ARR growth turning negative.
- Gross-margin compression from AI compute costs.
- Share loss to AI-native tools.

**Reddit/retail (secondhand):** 24/7 Wall St's "Reddit Radar" showed Adobe drawing heavy traffic (657 comments) with **bearish** sentiment, as retail argues "AI tools are coming for its software moat" (date unclear) ([24/7 Wall St Reddit Radar](https://247wallst.com/cards/retail-traders-are-piling-into-microsoft-with-1-367-comments-msft-reddit-radar-01m4ge3k5gm8cg2ps0kmqspwbr)).

**Why conviction is only 3:** Fundamentals for the latest quarter could not be verified, and the AI disruption risk is more direct here than at Intuit.

---

## 5. Boston Scientific (BSX, NYSE): Bucket B, Conviction 3

**Price and valuation**
- **Price:** **$44.18 on Sep 29, 2026**, near its **52-week low of $42.63** ([Pluang](https://pluang.com/en/news-feed/boston-scientific-saham-tertekan-penurunan-pandangan-pasar)). **The October price is not verified.**
- **YTD:** −55.9% total return to Oct 8 ([Chartrow](https://chartrow.com/sp500/stock-performance)). The 52-week high is not verified.
- **Market cap:** not verified.
- **Forward P/E:** about **12.8x** on the *original* 2026 adjusted EPS guide midpoint of $3.46 (calc). **That guide is no longer reliable** (see below).

**Guidance history**
- **Feb 4, 2026:** guided adjusted EPS of **$3.43–3.49** (midpoint below consensus) and sales growth of **10.5–11.5%**, down from **19.9% in 2025**. The stock fell about 10–18% ([Investing.com](https://www.investing.com/news/company-news/boston-scientific-shares-tumble-on-weak-2026-outlook-93CH-4485850); [Yahoo](https://finance.yahoo.com/healthcare/articles/why-bsx-stock-lost-more-163125666.html)).
- **July:** **cut 2026 organic revenue growth to 5–6%** on a Watchman slowdown. Management attributes it to newly published clinical evidence on atrial-fibrillation stroke risk that changed referral patterns ([IndexBox](https://www.indexbox.io/blog/boston-scientific-stock-plunges-over-50-in-2026-amid-repeated-guidance-cuts/)).
- **Late Aug:** a **cyberattack** disrupted manufacturing and logistics. BSX warned it is **unlikely to meet 2026 sales and EPS guidance**. Operations have since been restored ([ad-hoc-news](https://www.ad-hoc-news.de/boerse/news/corporate-news/boston-scientific-stock-falls-as-cyberattack-forces-2026-guidance-rethink/70130922)).
- **March:** Raymond James downgraded it from Strong Buy to Outperform, citing slower US electrophysiology and Watchman growth ([tikr](https://www.tikr.com/blog/boston-scientific-bsx-stock-tumbles-9-following-raymond-james-downgrade)).
- **Not verified:** FY25 actuals, Q2 2026 numbers, net debt and FCF.

**Why it may be mispriced:** A high-quality med-tech franchise (Farapulse PFA, Watchman) now trades at roughly a low-teens P/E on depressed numbers, after being a premium compounder. The cyberattack is a one-off. **27 of 31 analysts still rate it Buy** (per Pluang/GuruFocus coverage).

**Catalysts:** **Q3 results and revised guidance around Oct 28** (per one source; not confirmed by the company).

**Risks and what would prove the thesis wrong**
- If the new clinical evidence permanently shrinks the Watchman (LAAO) market, the growth algorithm is structurally lower. That would be a "broken thesis", not a "temporary" problem.
- Pulsed-field ablation (PFA) competition from Medtronic, J&J and others compressing electrophysiology share.
- 2027 guidance below about 8% organic growth.

**Reddit/retail:** Not verified.

---

## 6. ServiceNow (NOW, NYSE): Bucket B, Conviction 3

**Price and valuation**
- **Price:** **about $139.75 on Oct 8, 2026** ([StockAnalysis stats via search](https://stockanalysis.com/stocks/now/statistics/)). The price reflects a post-split share count; split details are not verified here.
- **Drawdown:** **about −40% YTD** ([tikr](https://www.tikr.com/blog/servicenow-is-down-40-in-2026-heres-what-investors-should-know)).
- **P/E:** trailing **87.3**, forward **30.8** (30.4 on Oct 1).
- **FCF:** TTM **$4.58B**, so P/FCF is **about 31.5**. GuruFocus has P/FCF **30.9 vs a 10-year median of 57.7** (Sep 27) ([GuruFocus](https://www.gurufocus.com/term/price-to-free-cash-flow/NOW)). Implied market cap is about $144B (calc).

**Latest results:** Q2 2026 subscription revenue was **+24.5% y/y to $3.877B**, and AI annual contract value passed **$1B** (per search summaries of software-selloff coverage; the exact page was not pinned). Revenue growth is about 22%. Yahoo shows FCF growth negative in Q1/Q2 FY2026, so FCF is volatile.

**Why it fell:** The thesis that AI agents will automate IT service management and break seat-based pricing. On Aug 26 it fell about 3% to $122.90 in sympathy with Intuit ([24/7 Wall St](https://247wallst.com/investing/2026/08/26/intuit-sinks-12-as-ai-disruption-fears-spread-from-turbotax-to-quickbooks-adobe-and-servicenow-drop-3/)).

**Why it may be mispriced:** About 25% subscription growth at about half its historical FCF multiple, plus an AI product line already past $1B in contract value.

**Catalysts:** Q3 results (late Oct; date not verified).

**Risks and what would prove the thesis wrong**
- Even at a discount, about 31x forward earnings is not cheap. It needs sustained growth above 20%.
- Subscription growth below about 18%.
- Net-new ACV declines.

**Reddit/retail:** Not verified.

---

## 7. Novo Nordisk (NVO, NYSE ADR; NOVO-B Copenhagen): Bucket B, Conviction 2

**Price and valuation**
- **Price:** **$38.18 at the Oct 8, 2026 close** (−0.21%) ([heygotrade](https://www.heygotrade.com/en/us-stock/nvo/); [Seeking Alpha](https://seekingalpha.com/symbol/NVO)).
- **52-week range:** **$35.12–64.16**, so it is **about 40.5% below its high** (calc).
- **P/E:** about **9.7** (EUR 34.05 line) ([ad-hoc-news](https://www.ad-hoc-news.de/boerse/news/corporate-news/novo-nordisk-stock-trades-at-eur-34-05-with-a-9-7-p-e-ratio/70279336)).

**Latest results and guidance** (Q2 reported Aug 4, 2026; [CNBC](https://www.cnbc.com/2026/08/04/novo-nordisk-releases-earnings-and-guidance.html); [SEC 6-K](https://www.sec.gov/Archives/edgar/data/0000353278/000117184326005184/f6k_080426.htm))
- Q2 adjusted sales grew **+7% at constant exchange rates** and adjusted operating profit **+11% at constant exchange rates**.
- 2026 guidance was raised to an adjusted sales and operating profit change of **"0% to 6%" at constant exchange rates**. The search summary wording says "fall between 0% and 6%". **Whether this means a decline of 0–6% or growth must be checked against the 6-K.**
- US operations are expected to decline because of GLP-1 prescription trends, competition and Medicaid coverage changes. Shares fell about 6% on the day.
- The oral Wegovy pill beat forecasts in May ([CNBC, May 6](https://www.cnbc.com/2026/05/06/wegovy-glp1-weight-loss-novo-nordisk-earnings-stock-nvo-ozempic.html)).

**Why it fell:** US GLP-1 price erosion and share loss to Lilly, competition, and Medicaid changes.

**Analyst view:** Mostly Hold. Morgan Stanley downgraded to **Sell with a $40 target on Sep 11**. BMO is Hold at $47, and TD Cowen and Jefferies are Hold at $42 ([StockAnalysis forecast via search](https://stockanalysis.com/stocks/nvo/forecast/)).

**Why it may be mispriced:** About 10x P/E for a global obesity and diabetes franchise with oral and next-generation pipeline options.

**Why conviction is low:**
- Earnings are flat to down, and the Street is moving toward Sell. This is the classic **value-trap profile**.
- It belongs on the shortlist only as a contrarian, small-position idea.

**Risks:** Further US price cuts; Lilly oral GLP-1 share gains; generic semaglutide in ex-US markets (not verified for 2026 timing).

**Catalyst:** Q3 results (date not verified; early November typical).

**Reddit/retail:** Not verified.

---

## 8. PayPal (PYPL, Nasdaq): Bucket B, Conviction 2

**Price and valuation**
- **Price:** **$54.41 on Oct 5, 2026** ([StockAnalysis stats via search](https://stockanalysis.com/stocks/pypl/statistics/)) and $54.61 on Oct 6 ([Yahoo key stats](https://finance.yahoo.com/quote/PYPL/key-statistics/)).
- **52-week range:** **$38.46–79.22**, so it is **about 31% below its high** and +41% off its low (calc).
- **Forward P/E:** **9.07–9.51**. Trailing P/E is 9.98 at $52.80, 77% below its median ([GuruFocus](https://www.gurufocus.com/term/pettm/PYPL)).
- **Guidance:** a 2026 EPS guide of **$5.38** is cited. The average target is **$56.92** ([Admiral Markets](https://admiralmarkets.com/education/articles/shares/paypal-stock-forecast)).

**Why it is cheap:** Branded-checkout share loss and low growth. Detailed 2026 drivers are not verified.

**Why it may be mispriced:** A single-digit P/E with large buybacks, as cited in earlier Motley Fool coverage.

**Why conviction is 2:**
- The consensus target ($56.92) is only about 5% above the price, so the Street does not see a large gap.
- Growth is low.
- Without verified Q2 numbers I cannot confirm a re-acceleration.

**Catalyst:** Q3 results (late Oct/early Nov; not verified).

**Risks:** Apple Pay and agentic-commerce disintermediation; Braintree margin; take-rate pressure.

---

# BUCKET A: BUY-NOW QUALITY AT A FAIR PRICE

## 9. Taiwan Semiconductor (TSM, NYSE ADR; 2330.TW): Bucket A, Conviction 4

**Price and valuation**
- **Price:** **$453.31 at the Oct 9, 2026 close** ([StockAnalysis via search](https://stockanalysis.com/stocks/tsm/)).
- **52-week range:** not verified.
- **Forward P/E:** **20.27** (StockAnalysis, Oct 9) and **21.19** (GuruFocus, Oct 8) ([GuruFocus](https://www.gurufocus.com/term/forward-pe-ratio/TSM)). An outlier figure of 28.44 (Insider Monkey, Oct 6) conflicts.
- **5-year average forward P/E:** about **21.78** (Insider Monkey).
- **Trailing P/E:** about 29.7–30.0.

**Fundamentals:** Profits grew **77.4%** (headline from [Insider Monkey](https://insidermonkey.com/news/taiwan-semiconductor-tsm-grew-profits-77-4-is-its-premium-valuation-justified-1849930); the period is not verified). It is a critical AI-capex beneficiary ([24/7 Wall St, Oct 9](https://247wallst.com/investing/2026/10/09/one-of-the-most-important-ai-stocks-isnt-nvidia-its-tsmc)).

**Not verified:** revenue growth, margins, net cash and FCF.

**Why it fits bucket A:** It is the AI-capex beneficiary trading **at or below its 5-year average forward P/E (about 20–21x vs 21.8x)**, despite earnings acceleration. It is not stretched relative to AI peers.

**Analyst view:** "Strong Buy", target **$555.01** ([StockAnalysis forecast](https://stockanalysis.com/stocks/tsm/forecast/)).

**Catalyst:** **Q3 results Thu Oct 15, 2026 (before market open)**.

**Risks**
- AI-capex digestion. The Oct 8 rotation out of AI-infrastructure names is an early warning.
- Taiwan geopolitics.
- US tariffs/Section 232 on chips.
- Margin dilution from overseas fabs.

---

## 10. Elevance Health (ELV, NYSE): Bucket A, Conviction 3

**Price and valuation**
- **Price:** **$400.09 at the Oct 6, 2026 close** ([Gotrade](https://www.heygotrade.com/en/us-stock/elv/)). Yahoo showed about $413.41 (date unclear).
- **Position in range:** up about 36% over 12 months and **near the top of its 52-week range** ([Yahoo](https://finance.yahoo.com/markets/stocks/articles/36-last-12-months-does-133832947.html)). Exact 52-week figures are not verified.
- **Trailing P/E:** about 18.
- **Forward P/E:** **about 14.8x** on 2026 adjusted EPS of ≥$27.00 (calc).

**Guidance:** Raised after Q2 to **adjusted EPS of at least $27.00** (GAAP at least $20.10). This was **reaffirmed Sep 10**, along with a benefit expense ratio of 90.2% ±50bp ([SEC Q2 release](https://www.sec.gov/Archives/edgar/data/0001156039/000115603926000058/a2q2026elvearningsrelease.htm); [SEC 8-K Sep 10](https://www.sec.gov/Archives/edgar/data/0001156039/000115603926000063/elv-20260910.htm)). Medicaid is expected to run about a −1.75% operating margin, and Elevance is exiting the DC Medicaid market ([Simply Wall St](https://simplywall.st/stocks/us/healthcare/nyse-elv/elevance-health/news/elevance-health-elv-raises-2026-targets-and-exits-weak-medic)).

**Not verified:** revenue growth, FCF and net debt.

**Why it fits bucket A:** Managed care repriced hard in 2024–25. ELV is recovering on margin repair and still sits at about 15x forward. Morningstar's Q2 list named ELV as undervalued.

**Analyst view:** Buy (9 analysts), average target about **$447**. Barclays raised its target to $469 on Oct 7.

**Catalyst:** **Q3 results Oct 21, 2026**.

**Risks**
- Medicaid redeterminations and acuity.
- Medicare Advantage rate notices.
- Policy risk (ACA subsidies; not verified for 2027).
- Since it is not beaten down, a miss could cause a sharp pullback.

---

## 11. Salesforce (CRM, NYSE): Bucket A/B, Conviction 3

**Price and valuation**
- **Price:** **$229.13 at the Oct 9, 2026 close**; market cap about **$188.6B** ([StockAnalysis via search](https://stockanalysis.com/stocks/crm/)).
- **52-week high/low:** not verified. Trails the market in 2026 ([Insider Monkey](https://www.insidermonkey.com/news/salesforce-crm-trails-the-market-in-2026-what-could-fuel-a-re-rating-1848733/)).
- **P/E:** trailing 21.1. Forward **15.5** (StockAnalysis), **14.66 on Oct 4** (GuruFocus), and 14.88 (Simply Wall St). GuruFocus's software-industry median is 16.85 and its "GF Value" is $347.41 ([GuruFocus](https://www.gurufocus.com/term/forward-pe-ratio/CRM)).

**Latest results:** "Strong Q2 growth" ([ad-hoc-news](https://www.ad-hoc-news.de/boerse/news/corporate-news/salesforce-stock-faces-a-valuation-gap-after-strong-q2-growth/70243840)). **Specific figures not verified.**

**Why it fits:** About 15x forward earnings is a large discount to its history and roughly the S&P multiple. Salesforce is the incumbent CRM system of record, and AI-agent monetization (Agentforce) is the swing factor.

**Analyst view:** Average target **$281.08** from 54 analysts (MarketScreener, Sep 23).

**Catalyst:** Q3 FY27 results, **Nov 30** per one search summary (not confirmed).

**Risks**
- Seat compression from AI agents.
- Large M&A.
- Growth slipping to the high single digits.

---

## 12. Alphabet (GOOGL, Nasdaq): Bucket A, Conviction 3

**Price and valuation**
- **Price:** **$348.29 on Oct 8** (fullratio) and $343.50 on Oct 5 (GuruFocus).
- **Market cap:** about **$4.30T** (Yahoo) ([fullratio](https://fullratio.com/stocks/nasdaq-googl/pe-ratio); [GuruFocus](https://www.gurufocus.com/term/forward-pe-ratio/GOOGL); [Yahoo](https://finance.yahoo.com/quote/GOOGL/)).
- **Trailing P/E:** about 17.3–17.6. The trailing figure may be flattered by non-operating investment gains (not verified).
- **Forward P/E:** **conflicting**, between 16.5 (valueinvesting.io) and 22.8 (GuruFocus).
- **YTD:** about +9% (Oct 2).

**Why it fits bucket A:** One of the lowest mega-cap multiples. Cloud and AI demand support it, and it is not stretched after only about +9% YTD.

**Not verified:** Q2 numbers, capex guide and FCF.

**Catalyst:** **Q3 results Oct 28** (Yahoo).

**Risks:** Search disruption by AI assistants; antitrust remedies; capex intensity.

---

## 13. Amazon (AMZN, Nasdaq): Bucket A, Conviction 3

**Price and valuation**
- **Price:** **$259.92 at the Oct 7 close**; market cap about **$2.80T** ([TradingKey, 2026-10-08](https://www.tradingkey.com/analysis/stocks/us-stocks/262205651-amazon-amzn-stock-forecast-october-8-2026-tradingkey)).
- **Forward P/E:** **about 19–20** (valueinvesting.io 20.13 on Aug 31; Simply Wall St about 19). One earlier article put it at 29, so the sources conflict.
- **Trailing P/E:** 20.3 (fullratio) vs 34.9 (macrotrends). The basis differs and is not reconciled.

**Fundamentals:** **AWS growth accelerated to about 37%** in Q2, from 28% in Q1 ([Motley Fool, Aug 19](https://www.fool.com/investing/2026/08/19/prediction-amazons-stock-price-end-of-2026/)). 2026 capex is about **$220B**, and **FCF has turned negative**.

**Analyst view:** Consensus target about **$314** (Yahoo).

**Why it fits:** Accelerating AWS at about 20x forward. YTD it is about +9%, so it is not extended.

**Catalyst:** Q3 results (date not verified, late Oct typical).

**Risks:** Negative FCF if AI capex returns lag; retail margin pressure from tariffs.

---

## 14. UnitedHealth Group (UNH, NYSE): Bucket A, Conviction 3

**Price and valuation**
- **Price:** **$375.26 at the Sep 17 close**, $377.42 on Sep 28 ([ad-hoc-news](https://www.ad-hoc-news.de/boerse/news/corporate-news/unitedhealth-group-stock-holds-near-usd-375-after-guidance-lift/70124700); [Pluang](https://pluang.com/en/news-feed/unitedhealth-dividen-berkualitas-dari-asuransi-kesehatan)). **The October price is not verified.**
- **52-week range:** **$255.97–461.62**, so it is about 18% below its high (calc).
- **Forward P/E:** **about 19.1x** on 2026 guidance (calc).

**Guidance:** Raised after Q2 to **adjusted EPS of $19.50–20.00** (GAAP $18.45–18.95), operating cash flow of about $24B and buybacks of at least $5B ([SEC Q2 release](https://www.sec.gov/Archives/edgar/data/0000731766/000073176626000191/earningsrelease2q26_7152.htm)). Q2 adjusted EPS was **$6.38 vs a $4.91 estimate**, and the medical cost ratio hit a two-year low ([TradingKey](https://www.tradingkey.com/analysis/stocks/us-stocks/262037053-unitedhealth-unh-q2-2026-earnings-beat-medical-cost-ratio-454-target-tradingkey)). Zacks consensus is $19.82 (Sep 18).

**Why it fits:** The recovery is underway but the stock is still well below prior highs, and the earnings rebuild is ahead.

**Catalyst:** Q3 results (date not verified; mid-October typical).

**Risks:** DOJ/regulatory investigations (not verified for status); Medicare Advantage rates; Optum Health execution. About 19x is not "cheap".

---

# CONSIDERED AND REJECTED (or watchlist)

| Name | Data point (source, date) | Verdict |
|---|---|---|
| **Fair Isaac (FICO)** | Fell 26.5% in one session from $840.89 (about Sep 29) after FHFA put **VantageScore on a single pricing grid with Classic FICO**. BofA downgraded to Neutral and **halved its target to $700** ([Motley Fool, 2026-09-29](https://www.fool.com/investing/2026/09/29/why-fair-isaac-corporation-plunged-today/); [Schaeffer's](https://www.schaeffersresearch.com/content/news/2026/09/29/fair-issac-stock-crumbles-after-mortgage-pricing-monopoly-ends); [24/7 Wall St, 2026-10-01](https://247wallst.com/investing/2026/10/01/bank-of-america-cut-its-fair-isaac-price-target-in-half-and-the-stock-still-fell-below-it/)) | **Reject.** A structural moat and pricing-power break, not a temporary drop. |
| **Trade Desk (TTD)** | About $12 (Oct 6), 52-week range $11.92–54.13. **Q2 revenue +3% to $715M**. **Removed from the S&P 500** (announced Sep 4). EPS forecast −42% ([24/7 Wall St, 2026-09-28](https://247wallst.com/investing/2026/09/28/trade-desk-is-down-68-this-year-is-it-time-to-sell-or-is-this-a-lifetime-opportunity/); [Pluang](https://pluang.com/en/asset/usstock/TTD/10241)) | **Reject.** Broken growth thesis. |
| **AppLovin (APP)** | Nearly −60% YTD. Q2 revenue $1.92B (+53%) missed $1.94B. Facing a **securities class action** and a short-seller AML report ([Motley Fool, Aug 9](https://www.fool.com/investing/2026/08/09/applovin-revenue-jump-why-stock-plunge/); [Yahoo](https://finance.yahoo.com/markets/stocks/articles/applovin-stock-down-54-2026-114303125.html)) | **Reject for now.** Governance and legal overhang; valuation not verified. |
| **Nike (NKE)** | **Guided FY27 revenue down by a high single-digit %** (Oct 1). About 17x trailing earnings. **Dividends exceed FCF** ([Foreign Policy Journal, 2026-10-04](https://www.foreignpolicyjournal.com/2026/10/04/lululemon-nasdaq-lulu-edges-out-nike-nyse-nke-on-margins-and-financial-discipline-despite-shared-decline/)) | **Reject.** Value trap, earnings still falling. |
| **Lululemon (LULU)** | $95.86 (Oct 1). **About 10.7x forward** (Zacks 12.45x). Outlook cut twice. $380M tariff hit. **Interim CEO** (same source) | **Watchlist.** Cheap, but brand momentum and leadership are unresolved. |
| **Microsoft (MSFT)** | $535.07 (Oct 9 close). Market cap $3.97T. Forward P/E 26.4. 52-week range $349.20–553.72. Target $587.63 (Strong Buy, 56 analysts). Earnings Oct 28 ([StockAnalysis via search](https://stockanalysis.com/stocks/msft/)). Most Reddit buzz in 2026 but bearish ([24/7 Wall St Reddit Radar](https://247wallst.com/cards/retail-traders-are-piling-into-microsoft-with-1-367-comments-msft-reddit-radar-01m4ge3k5gm8cg2ps0kmqspwbr)) | **Not a dip.** About 3% off its high. Fairly valued. |
| **Meta (META)** | About $728 (Oct 3). Trailing 27.4x, close to its 10-year median. Forward 19.7x (Sep 18). **2026 capex guide raised to $125–145B** ([GuruFocus](https://www.gurufocus.com/term/pe-ratio/META)) | **Fair, not cheap.** Capex/FCF risk into the Oct 28 print. |
| **Visa / Mastercard** | V about $376 (Oct 8), forward 25.7, near its 52-week high of $385.57. MA forward 24.6 (Oct 6) ([GuruFocus MA](https://www.gurufocus.com/term/forward-pe-ratio/MA)) | **Quality but not discounted.** Wait. |
| **ASML** | About $1,770 (Oct 8). **About +66% in 2026** ([Macrotrends](https://www.macrotrends.net/stocks/charts/ASML/asml-holding/stock-price-history)) | **Reject for this mandate.** Big run, not a dip. |
| **Merck / BMY / PFE** | MRK about +43.5% YTD (Sep 25). BMY about 8.6–9x and PFE about 9.4–10x forward, with patent cliffs ([Motley Fool, 2026-10-08](https://www.fool.com/coverage/better-buy/2026/10/08/bristol-myers-squibb-vs-pfizer-which-healthcare-stock-is-a-better-buy-in-2026/)) | MRK has run. BMY/PFE are cheap for a reason (patent cliffs), so **watchlist**. |
| **Zoetis (ZTS)** | **52-week low of $69.48 on Oct 1**, about −52% over a year, market cap about $30B. Q2 revenue of $2.47B missed $2.50B ([Investing.com](https://www.investing.com/news/company-news/zoetis-stock-hits-52week-low-at-6948-93CH-4927685)) | **Watchlist.** Interesting quality name, but valuation and the drivers of the drop were not verified. |
| **SAP** | About −35% YTD (MarketScreener). 2026 P/E 19.3x vs historical average 39.3x (mid-July). Last price found was **$210.47 on Aug 18** (stale) ([MarketScreener](https://www.marketscreener.com/news/sap-a-cloud-giant-in-the-sales-during-the-ai-era-ce7f5ed2d18ff520)) | **Watchlist.** A strong candidate, but the October price is not verified. |
| **Accenture / Gartner** | ACN **+22% on Oct 1** on its FY27 guide of 3–6% growth, then $208.36 on Oct 8. Gartner lost about 49% in H1, then $195.41 on Oct 8 ([ResultSense](https://www.resultsense.com/news/2026-10-02-accenture-forecast-it-services-rally/); [24/7 Wall St](https://247wallst.com/investing/2026/10/09/the-stocks-wall-street-thought-ai-would-kill-just-jumped-5-while-ai-darlings-sank/)) | **Watchlist.** ACN already re-rated sharply. IT valuation not verified. |
| **Thermo Fisher (TMO)** | About $655 (Oct 7), about 5.6% below its 52-week high of $694.33. Q3 due Oct 21 ([ad-hoc-news](https://www.ad-hoc-news.de/boerse/news/corporate-news/thermo-fisher-scientific-stock-heads-into-october-21-results-after-a-2-27-percent-drop/70243953)) | **Not a dip.** |
| **Corteva (CTVA)** | Chartrow shows −79.3% YTD | **Excluded.** Likely a spin-off or corporate-action artifact (not verified). |

---

## Reddit / forum sentiment: what could and could not be verified

- **Direct access failed.** reddit.com and old.reddit.com were blocked by the egress proxy (403) and WebFetch had DNS failures. Search engines returned **no** r/ValueInvesting, r/stocks, r/investing, r/SecurityAnalysis or r/wallstreetbets threads from Aug–Oct 2026. **The Reddit evidence below is all secondhand.**
- **Netflix:** The r/stocks top post after Q2 complained about the engagement-data restriction and the 12% two-day fall ([24/7 Wall St, Jul 20](https://247wallst.com/investing/2026/07/20/netflix-buy-the-dip-or-wait-for-proof/)).
- **Microsoft and Adobe:** Microsoft had the most Reddit buzz in 2026 (1,367 comments) and Adobe had 657, **both bearish**. Retail argues AI is "coming for" the software moat (date unclear) ([24/7 Wall St Reddit Radar](https://247wallst.com/cards/retail-traders-are-piling-into-microsoft-with-1-367-comments-msft-reddit-radar-01m4ge3k5gm8cg2ps0kmqspwbr)).
- **Older sentiment data:**
  - MarketWise found 61% of AI-stock discussions positive across five investing subreddits, through Mar 2026 ([MarketWise](https://marketwise.com/research-center/ai-stock-sentiment-reddit-analysis/)).
  - A Stocktwits poll (about 7 months old) found fewer retail traders expecting a software rebound, with a preference for semis ([Stocktwits](https://stocktwits.com/news-articles/markets/equity/ai-chip-stocks-over-software-retail-traders-lean-more-on-semiconductor-plays-amid-tech-selloff/cZdhur2RIEj)).
- **Read-through:** Retail sentiment on application software is negative and crowded into AI hardware. That is contrarian-supportive for INTU, ADBE, CRM and NOW, but it is **not evidence**.

---

## Key unresolved data conflicts for the red team

1. **NFLX 52-week high:** $124.86 (stockinvest) vs $126.71 (Barchart). The Q3 date is Oct 20 per the company release, though one summary said Oct 17.
2. **NVO 2026 guidance wording:** "0% to 6%". The direction (growth or decline) needs checking against the Aug 4 6-K.
3. **INTU consensus target:** $406 vs $431.55.
4. **UBER Q2 EPS:** in line vs a miss. The Delivery Hero deal terms are unverified.
5. **GOOGL and AMZN forward P/E:** each spans a wide range across providers.
6. **BSX:** the Oct 28 guidance date comes from one source only, and the October price is unverified.
7. **Oct 9 closes:** verified only for MSFT ($535.07), TSM ($453.31) and CRM ($229.13), plus ADBE ($242.25, which may be intraday). All others are Oct 5–8 or older.

---

## Sources

**Important:** Because of the tool failures described at the top, **I was not able to open any of these pages directly**. Every URL below was surfaced and quoted in WebSearch result summaries, and that is how each data point was obtained. Pages I tried and failed to open (WebFetch DNS errors or proxy 403s) are listed separately at the end.

### Market / screens
- https://chartrow.com/sp500/stock-performance
- https://chartrow.com/sp500/sector-performance
- https://chartrow.com/lists/magnificent-7
- https://georgedagninophd.substack.com/p/sector-performance-since-22826
- https://www.lanacion.com.ar/usa/how-major-us-stock-indexes-fared-tuesday-1062026-nid06102026/
- https://tradingeconomics.com/euro-area/stock-market/news/556957
- https://www.fool.com/investing/2026/10/01/best-performing-magnificent-seven-stock-2026/
- https://global.morningstar.com/en-gb/stocks/33-undervalued-us-stocks-buy-volatile-market
- https://global.morningstar.com/en-gb/markets/where-us-stock-market-may-be-heading-next-what-buy-now
- https://www.fool.com/investing/2026/02/18/the-2026-software-stock-sell-off-ai-disruption-fea/
- https://www.bloomberg.com/news/articles/2026-09-18/software-stocks-get-new-life-from-strong-earnings-ai-warnings
- https://www.bloomberg.com/news/articles/2026-09-27/ai-whiplash-jolts-stocks-as-sentiment-lurches-from-fear-to-greed
- https://247wallst.com/investing/2026/10/09/the-stocks-wall-street-thought-ai-would-kill-just-jumped-5-while-ai-darlings-sank/

### Intuit
- https://247wallst.com/investing/2026/08/26/intuit-sinks-12-as-ai-disruption-fears-spread-from-turbotax-to-quickbooks-adobe-and-servicenow-drop-3/
- https://finance.yahoo.com/markets/stocks/articles/intuit-shares-plunge-cautious-fiscal-104320782.html
- https://www.stocktitan.net/news/INTU/intuit-hosts-investor-day-reaffirms-first-quarter-and-fiscal-2027-z9sgro2wbu5j.html
- https://seekingalpha.com/news/4643811-intuit-reaffirms-fiscal-2027-guidance
- https://www.ad-hoc-news.de/boerse/news/corporate-news/intuit-stock-gains-2-25-percent-while-growth-guidance-cools/70243920
- https://www.ad-hoc-news.de/boerse/news/corporate-news/intuit-stock-trades-below-its-consensus-target-despite-growth-guidance/70227544
- https://www.ad-hoc-news.de/boerse/news/corporate-news/intuit-stock-faces-a-growth-reset-as-fy2027-guide-stays-at-9-to-10-percent/70198414
- https://finance.yahoo.com/markets/stocks/articles/intuit-stock-analysis-why-street-134844647.html

### Netflix
- https://stockinvest.us/stock/NFLX
- https://www.barchart.com/stocks/quotes/NFLX/price-history/historical
- https://www.fool.com/investing/2026/10/07/1-number-explain-nflx-stock-down-2026/
- https://www.fool.com/investing/2026/10/01/why-netflix-lost-14-in-september/
- https://www.fool.com/investing/2026/07/08/why-netflix-dropped-24-in-the-first-half-of-2026/
- https://finance.yahoo.com/markets/stocks/articles/3-reasons-why-netflix-shares-172551823.html
- https://www.briefs.co/news/netflix-s-2026-slump-deepens-as-engagement-worries-grow/
- https://www.sec.gov/Archives/edgar/data/0001065280/000106528026000211/ex991_q226.htm
- https://www.tradingview.com/news/tradingview:047fc5894e749:0-netflix-posts-q2-revenue-12-6b-operating-margin-33-4-and-narrows-2026-revenue-range/
- https://www.cnbc.com/2026/07/16/netflix-nflx-earnings-q2-2026.html
- https://www.gurufocus.com/term/price-to-free-cash-flow/NFLX
- https://www.gurufocus.com/term/forward-pe-ratio/NFLX
- https://www.gurufocus.com/term/total-free-cash-flow/NFLX
- https://www.heygotrade.com/en/market-outlook/netflix-stock-forecast/
- https://s22.q4cdn.com/959853165/files/doc_news/Netflix-to-Announce-Third-Quarter-2026-Financial-Results-2026.pdf
- https://www.nasdaq.com/articles/netflix-q2-profit-rises
- https://earningswhispers.com/epsdetails/NFLX/202606
- https://finance.yahoo.com/markets/stocks/articles/wells-fargo-downgrades-netflix-stock-180752599.html
- https://www.schaeffersresearch.com/content/news/2026/09/18/downgrade-steep-price-target-cut-dings-netflix-stock
- https://www.insidermonkey.com/news/wells-fargo-cuts-netflix-nflx-to-underweight-as-its-2026-slide-deepens-1841150/
- https://247wallst.com/investing/2026/07/20/netflix-buy-the-dip-or-wait-for-proof/

### Uber
- https://seekingalpha.com/symbol/UBER
- https://www.fool.com/quote/nyse/uber/
- https://www.kraken.com/stocks/uber
- https://stockanalysis.com/stocks/uber/
- https://investor.uber.com/news-events/news/press-release-details/2026/Uber-Announces-Results-for-Second-Quarter-2026/default.aspx
- https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm
- https://quartr.com/events/uber-technologies-inc-uber-q2-2026_3PkHdWXK
- https://finance.yahoo.com/markets/stocks/articles/uber-q2-2026-earnings-guidance-111918644.html
- https://www.bnnbloomberg.ca/business/company-news/2026/08/05/uber-forecasts-weak-quarterly-profit-doubles-down-on-robotaxi-investment-plans/
- https://eciks.org/10607-16119-uber-stock-robotaxi-legal-pressures
- https://www.gurufocus.com/term/price-to-free-cash-flow/UBER
- https://finance.yahoo.com/quote/UBER/key-statistics/
- https://www.tikr.com/blog/uber-stock-is-down-9-in-2026-heres-why-analysts-still-see-upside-to-103

### Adobe / Salesforce / ServiceNow
- https://robinhood.com/us/en/stocks/ADBE/
- https://www.wallstreetzen.com/stocks/us/nasdaq/adbe
- https://247wallst.com/investing/2026/07/01/adobe-nearing-52-week-low-buy-sell-or-hold/
- https://www.tikr.com/blog/adobe-stock-is-trading-near-52-week-low-heres-where-shares-could-go-in-2026
- https://stockanalysis.com/stocks/crm/
- https://www.gurufocus.com/term/forward-pe-ratio/CRM
- https://www.insidermonkey.com/news/salesforce-crm-trails-the-market-in-2026-what-could-fuel-a-re-rating-1848733/
- https://www.ad-hoc-news.de/boerse/news/corporate-news/salesforce-stock-faces-a-valuation-gap-after-strong-q2-growth/70243840
- https://stockanalysis.com/stocks/now/statistics/
- https://www.gurufocus.com/term/price-to-free-cash-flow/NOW
- https://www.tikr.com/blog/servicenow-is-down-40-in-2026-heres-what-investors-should-know

### Boston Scientific
- https://pluang.com/en/news-feed/boston-scientific-saham-tertekan-penurunan-pandangan-pasar
- https://www.investing.com/news/company-news/boston-scientific-shares-tumble-on-weak-2026-outlook-93CH-4485850
- https://finance.yahoo.com/healthcare/articles/why-bsx-stock-lost-more-163125666.html
- https://www.indexbox.io/blog/boston-scientific-stock-plunges-over-50-in-2026-amid-repeated-guidance-cuts/
- https://www.ad-hoc-news.de/boerse/news/corporate-news/boston-scientific-stock-falls-as-cyberattack-forces-2026-guidance-rethink/70130922
- https://www.tikr.com/blog/boston-scientific-bsx-stock-tumbles-9-following-raymond-james-downgrade

### Novo Nordisk / PayPal
- https://www.heygotrade.com/en/us-stock/nvo/
- https://seekingalpha.com/symbol/NVO
- https://www.ad-hoc-news.de/boerse/news/corporate-news/novo-nordisk-stock-trades-at-eur-34-05-with-a-9-7-p-e-ratio/70279336
- https://www.cnbc.com/2026/08/04/novo-nordisk-releases-earnings-and-guidance.html
- https://www.cnbc.com/2026/05/06/wegovy-glp1-weight-loss-novo-nordisk-earnings-stock-nvo-ozempic.html
- https://www.sec.gov/Archives/edgar/data/0000353278/000117184326005184/f6k_080426.htm
- https://stockanalysis.com/stocks/nvo/forecast/
- https://stockanalysis.com/stocks/pypl/statistics/
- https://finance.yahoo.com/quote/PYPL/key-statistics/
- https://www.gurufocus.com/term/pettm/PYPL
- https://admiralmarkets.com/education/articles/shares/paypal-stock-forecast

### TSMC / Alphabet / Amazon / Microsoft / Meta / Visa
- https://stockanalysis.com/stocks/tsm/
- https://stockanalysis.com/stocks/tsm/forecast/
- https://www.gurufocus.com/term/forward-pe-ratio/TSM
- https://insidermonkey.com/news/taiwan-semiconductor-tsm-grew-profits-77-4-is-its-premium-valuation-justified-1849930
- https://247wallst.com/investing/2026/10/09/one-of-the-most-important-ai-stocks-isnt-nvidia-its-tsmc
- https://fullratio.com/stocks/nasdaq-googl/pe-ratio
- https://www.gurufocus.com/term/forward-pe-ratio/GOOGL
- https://finance.yahoo.com/quote/GOOGL/
- https://www.tradingkey.com/analysis/stocks/us-stocks/262205651-amazon-amzn-stock-forecast-october-8-2026-tradingkey
- https://www.fool.com/investing/2026/08/19/prediction-amazons-stock-price-end-of-2026/
- https://valueinvesting.io/AMZN/metric/forward-pe
- https://stockanalysis.com/stocks/msft/
- https://www.gurufocus.com/term/pe-ratio/META
- https://www.gurufocus.com/term/forward-pe-ratio/MA
- https://stockanalysis.com/stocks/v/

### Managed care
- https://www.heygotrade.com/en/us-stock/elv/
- https://www.sec.gov/Archives/edgar/data/0001156039/000115603926000058/a2q2026elvearningsrelease.htm
- https://www.sec.gov/Archives/edgar/data/0001156039/000115603926000063/elv-20260910.htm
- https://finance.yahoo.com/markets/stocks/articles/36-last-12-months-does-133832947.html
- https://simplywall.st/stocks/us/healthcare/nyse-elv/elevance-health/news/elevance-health-elv-raises-2026-targets-and-exits-weak-medic
- https://www.sec.gov/Archives/edgar/data/0000731766/000073176626000191/earningsrelease2q26_7152.htm
- https://www.ad-hoc-news.de/boerse/news/corporate-news/unitedhealth-group-stock-holds-near-usd-375-after-guidance-lift/70124700
- https://pluang.com/en/news-feed/unitedhealth-dividen-berkualitas-dari-asuransi-kesehatan
- https://www.tradingkey.com/analysis/stocks/us-stocks/262037053-unitedhealth-unh-q2-2026-earnings-beat-medical-cost-ratio-454-target-tradingkey

### Rejected / watchlist
- https://www.fool.com/investing/2026/09/29/why-fair-isaac-corporation-plunged-today/
- https://www.schaeffersresearch.com/content/news/2026/09/29/fair-issac-stock-crumbles-after-mortgage-pricing-monopoly-ends
- https://247wallst.com/investing/2026/10/01/bank-of-america-cut-its-fair-isaac-price-target-in-half-and-the-stock-still-fell-below-it/
- https://247wallst.com/investing/2026/09/28/trade-desk-is-down-68-this-year-is-it-time-to-sell-or-is-this-a-lifetime-opportunity/
- https://pluang.com/en/asset/usstock/TTD/10241
- https://www.fool.com/investing/2026/08/09/applovin-revenue-jump-why-stock-plunge/
- https://finance.yahoo.com/markets/stocks/articles/applovin-stock-down-54-2026-114303125.html
- https://247wallst.com/investing/2026/10/02/applovin-has-fallen-nearly-60-in-2026-180-returns-are-in-store-for-investors-according-to-this-wall-street-pro/
- https://www.foreignpolicyjournal.com/2026/10/04/lululemon-nasdaq-lulu-edges-out-nike-nyse-nke-on-margins-and-financial-discipline-despite-shared-decline/
- https://www.macrotrends.net/stocks/charts/ASML/asml-holding/stock-price-history
- https://www.fool.com/coverage/better-buy/2026/10/08/bristol-myers-squibb-vs-pfizer-which-healthcare-stock-is-a-better-buy-in-2026/
- https://www.investing.com/news/company-news/zoetis-stock-hits-52week-low-at-6948-93CH-4927685
- https://www.marketscreener.com/news/sap-a-cloud-giant-in-the-sales-during-the-ai-era-ce7f5ed2d18ff520
- https://www.resultsense.com/news/2026-10-02-accenture-forecast-it-services-rally/
- https://www.ad-hoc-news.de/boerse/news/corporate-news/thermo-fisher-scientific-stock-heads-into-october-21-results-after-a-2-27-percent-drop/70243953

### Sentiment
- https://247wallst.com/cards/retail-traders-are-piling-into-microsoft-with-1-367-comments-msft-reddit-radar-01m4ge3k5gm8cg2ps0kmqspwbr
- https://marketwise.com/research-center/ai-stock-sentiment-reddit-analysis/
- https://stocktwits.com/news-articles/markets/equity/ai-chip-stocks-over-software-retail-traders-lean-more-on-semiconductor-plays-amid-tech-selloff/cZdhur2RIEj

### Attempted but could NOT open (tool failures)
- **WebFetch, ENOTFOUND:** stockanalysis.com/stocks/uber, stockanalysis.com/stocks/nflx, finance.yahoo.com/quote/UBER, companiesmarketcap.com/uber/marketcap, cnbc.com/quotes/UBER, marketbeat.com/stocks/NYSE/UBER, global.morningstar.com (outlook article), en.wikipedia.org/wiki/Uber, thriveinmarkets.com (weekend recap), and the sec.gov Uber Q2 8-K.
- **WebFetch, "unable to fetch":** reuters.com/markets.
- **curl, proxy 403 (organization policy):** stockanalysis.com, query1.finance.yahoo.com, sec.gov, macrotrends.net, old.reddit.com, google.com.
