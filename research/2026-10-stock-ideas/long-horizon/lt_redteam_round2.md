# Red team, round 2: lt_report_v2.md

**Date:** Sat 2026-10-10.
**What I did:**
- Read v2 in full and checked its weights and arithmetic.
- Re-ran the sleeves with the per-name inputs v2 now quotes. Script: `scratchpad/redteam/rt_round2.py`; run with `python3 -I`.
- Ran 11 new WebSearch queries, only on claims that are new in v2. Each fact comes from a search-result summary.

**Tags:** [H] filing or several sources; [M] one credible source; [L] weak; (calc) my arithmetic.

**Bottom line:** the structure, name selection and weights in v2 are right.
- I would **sign off once the 8 changes in §5 are made.** They are mechanical edits, not new research.
- The most material one is my own fault. In round 1, `rt_proposed.py` scored the proposed portfolio with the **original** inputs for ICICI (2.95x anchor), HDFC Bank (2.05x exit), Bajaj Finance (32x re-rating), Intuit (re-rated) and Visa. v2 quotes the **corrected** inputs name by name but carries the old aggregate, so the sleeve figures and the edge are overstated by ~0.5–0.6pp.

---

## 1. Status of objections O1–O24

| ID | Status | Why |
|---|---|---|
| O1 Weights 30/50/20 | **Closed** | All headline figures use 30/50/20. |
| O2 Equal haircuts (India) | **Open (numbers only)** | The wording ("small, uncertain edge") is right, but +1.6pp is overstated. With v2's own corrected inputs the India sleeve's expected return is **12.4%**, not 12.9%, against 11.3% for all-index: an edge of **+1.1pp**. With an equal haircut it is **+0.3pp**; with the picks cut a further 3pp it is **−0.6pp** (calc). |
| O3 Same-method S&P | **Closed** (restate the number) | The method is now consistent. With V/MA split 50/50 and Intuit at its flat-multiple headline, the global sleeve's expected return is **12.7%** (bear −3.0 / base 15.4 / bull 24.9) against 10.4%: an edge of **+2.3pp**, not 2.9pp (calc). |
| O4 Below-hurdle names | **Closed** | L&T and TCS are out. Reliance, Bharti, Maruti and Apollo are cut and gated. NTPC is justified as ballast. |
| O5 TCS / HDFC AMC | **Closed** | |
| O6 L&T | **Closed** | |
| O7 AI-capex bears, Microsoft capex | **Closed** | Bears and capex are fixed. The 23% cap is a little above my ~20%; I accept it at 0.75% of the total. Note that the UCITS ETF adds ~3pp of hyperscaler exposure on a look-through basis. |
| O8 Alphabet | **Closed** | |
| O9 Amazon's clean EPS | **Closed** (action) | Priced at 26–27x and cut to 8%. But the quoted "~14%" base is wrong; see N3. |
| O10 Intuit headline | **Open (aggregate only)** | The row correctly shows ~15% on a flat multiple (calc 15.1%). The sleeve total still uses the re-rated 25.5%. A second FY28 source is still missing; I accept that at 3% of the total. |
| O11 SBI Life | **Closed** | Minor: define the "adverse bancassurance rule" trigger (§4). |
| O12 HDFC Bank staging and exit | **Open** | The NIM thresholds have no basis and sit on top of the current level; see N4. |
| O13 Bharti | **Closed** | |
| O14 Maruti | **Open** | The entry gate and the sell trigger are the same number, the margin basis is ambiguous, and the Eicher fallback fails its own valuation test; see N5. |
| O15 Apollo | **Closed** | |
| O16 Bear hedge | **Closed** (gold 3%) | |
| O17 Reserve | **Closed** | Minor: the "−15% from cost" clause in the response table is missing from the sleeve table. Add "subject to caps". |
| O18 LRS timing, no trims | **Closed** | |
| O19 Medtronic estate tax | **Closed** | |
| O20 Index core | **Closed**, with a new cap problem | See N10. |
| O21 V vs MA, CCCA | **Closed** | Split 50/50, with the CCCA as a sell trigger. Quote the blended returns (N11). |
| O22 Anchors from memory | **Open (low)** | Reliance ~25x and Maruti ~29x are still from memory. This is not blocking because both are small and event-gated. |
| O23 ICICI CEO source | **Open (low)** | Not blocking. |
| O24 Event gates for NFLX, ELV, INTU | **Closed** | The Elevance wording needs fixing; see N8. |

---

## 2. New errors and inconsistencies in v2

**N1. The sleeve aggregates don't match the per-name inputs (blocking).** Re-run with the inputs v2 quotes, at 30/50/20:

| | Bear | Base | Bull | Expected | vs index |
|---|---|---|---|---|---|
| India, as quoted in v2 | 2.2 | 15.1 | 21.4 | 12.9 | +1.6pp |
| **India, corrected** | **2.2** | **14.4** | **20.8** | **12.4** | **+1.1pp** |
| Global, as quoted in v2 | −3.1 | 16.6 | 24.7 | 13.3 | +2.9pp |
| **Global, corrected** (V/MA 50/50, Intuit flat) | **−3.0** | **15.4** | **24.9** | **12.7** | **+2.3pp** |

**N2. The Nifty fund row quotes the wrong figures.** "13.4 / 2.2" is the all-index *sleeve* including 12% cash. The Nifty itself, on the same model, is a **base of 14.3 and a bear of 1.6** (bull 19.5).

**N3. Amazon's base is ~16%, not ~14%.**
- With g at 17% and the P/E moving halfway to 25x from today's multiple:
  - from 26x, the base is 16.2%;
  - from 26.5x, 15.9%;
  - from 27x, 15.5%.
- The bear (g 3%, exit 18x) is **−26% over 3 years (−9.5%/yr) at 26.5x**, not −22% (calc).

**N4. HDFC Bank's NIM gate and sell trigger don't work as written.**
- Q1 FY27 NIM was **3.26% on total assets and 3.40% on interest-earning assets** [M] ([Tribune](https://www.tribuneindia.com/news/business/hdfc-banks-net-profit-jumps-4-98-to-rs-19059-72-crore-in-q1-fy27/); [Muthoot](https://www.muthootsecurities.com/News/Detailed-News/HDFC-Bank-Q1-PAT-rises-5-percent-YoY-to-Rs-19060-crore/1711278)).
- On the total-assets basis, the gate (≥3.3%) is not met today and the sell trigger (<3.2%) is 6bp away. The 1/3 starter would probably be sold inside 12 months at 20% short-term tax.
- On the interest-earning basis, the gate is already passed.
- The "1/3 now" also comes before the **Oct 17** Q2 results and the **Oct 27** CEO handover.

**N5. Maruti's gate and fallback don't work as written.**
- Q1 margin was **8.2% on revenue from operations, but 8.6% on net sales** in the company's own presentation [M/H] ([NSE investor presentation, Jul 31, 2026](https://nsearchives.nseindia.com/corporate/MARUTI_31072026165807_STxIntimation_InvestorPresentation_Q1_FY2026_27.pdf); [Angel One](https://www.angelone.in/news/stocks/maruti-suzuki-q1-fy27-results-out-revenue-jumps-36)).
- The entry gate (≥9%) and the sell trigger (<9% for 2 quarters) are the same number, so the position can whipsaw.
- **The Eicher fallback fails the analyst's own ≤33x condition.** Eicher was ₹7,021.5 on Oct 5 at **~36x TTM**; other sources show 36–39x [M] ([IIFL](https://www.indiainfoline.com/company/eicher-motors-share-price/151); [Anand Rathi](https://anandrathi.com/stocks/eicher-motors-ltd/share-price-today)).

**N6. ICICI's sell trigger is too tight.** "ROE <15% or NIM <4% for 2 quarters" is stricter than the analyst's "ROE <15% for 2 years".
- ICICI's NIM was below 4% in FY21–22 (mem).
- The macro base case has RBI cuts in 2028, which compress NIM mechanically.
- The trigger would probably force a taxable sale in the base case.

**N7. Reliance's sell trigger has already fired.** Retail EBITDA **already fell** in Q1 FY27: ₹6,309 cr, −1.1% y/y, margin 7.9% (−80bp). Management guides near-term margin pressure from its quick-commerce build-out for ~2 years [M] ([Upstox](https://upstox.com/news/market-news/earnings/reliance-retail-q1-results-ril-vertical-s-profit-declines-14-yo-y-ebitda-margin-contracts/article-197141/); [Outlook Business](https://www.outlookbusiness.com/markets/reliance-retail-q1-results-profit-declines-revenue-ebitda-margins-grow-share-price)). "Keeps falling" would therefore fire on management's own plan.

**N8. Elevance's gate can't be met when v2 says.** Elevance gives its formal next-year guide in **late January**: the 2026 guide (≥$25.50) came on **Jan 28, 2026** [H] ([SEC 8-K](https://www.sec.gov/Archives/edgar/data/1156039/000115603926000006/a4q2025elvearningsrelease.htm)). At Q3 (Oct 21) it can only restate the "≥12% in 2027" target, as it already did in July. As worded, the gate either passes trivially in October or can't be checked until late January.

**N9. There is no rule for money whose gate fails.** It is unclear where the allocation goes, and by when, if:
- SBI Life stays above ₹1,850;
- Maruti misses its margin;
- Elevance drops its target;
- the RBI's final rule for Bajaj is delayed;
- Bharti never hikes;
- HDFC Bank's NIM fails its gate.

**N10. Look-through exposure breaches two caps.**
- The Nifty fund holds ICICI at ~9.1–9.4%, HDFC Bank at ~9.9–10% and financials at ~35% [M] ([Taurus constituent list, Aug 17, 2026](https://taurusmutualfund.com/sites/default/files/2026-08/nifty-index-constituent-as-on-17_08_2026.pdf); [sharpely](https://sharpely.in/mutual-funds/hdfc-nifty-50-index-fund-directgrowth/16069/holdings)).
- So **ICICI is ~10.3% of the total on a look-through basis** (8.25 direct + ~2.1 via the fund), above the 9% single-stock cap.
- Financials are ~29.6% against a 30% cap: no headroom on day one, so normal drift will breach it.

**N11. Wording and blended figures.**
- Microsoft is called "the single AI-capex spender", but Amazon is also held.
- The V+MA row quotes Visa-only returns. Mastercard is base 17.7 / bear 1.4, so the blend is ~16.2 / 1.0 (calc).
- The line "Dropped vs the near-term list: … Maruti kept but gated" is garbled.

**N12. Smaller trigger gaps.**
- NTPC "cuts generation ROE": specify a threshold (the analyst's is below ~14.5%).
- Bajaj Finance "ROE <18%": add a duration.
- SBI Life "adverse bancassurance rule": define it, e.g. a cap on the parent bank's share or a ban on bank sales incentives.

**N13. The UCITS ETF tax line is missing.**
- International funds moved outside Section 50AA when "specified mutual fund" was redefined (to funds with more than 65% in debt). LTCG at 12.5% after 24 months is therefore likely, but confirm with an adviser [M] ([TaxGuru](https://taxguru.in/?p=1057273); [ICICI Pru tax reckoner](https://www.icicipruamc.com/blob/knowledgecentre/tax_reckoner/Tax_Reckoner_2025_26.pdf)).
- The 15% US withholding paid inside the fund is **not** creditable in India [L, vendor] ([Paasa](https://paasa.com/etfs/cspx-l)).

**Checked and fine:**
- Weights sum to 100/100 and 75/25. The %-of-total column is correct.
- Every per-name base/bear figure except Amazon and the Nifty row matches the model.
- MSFT's −22% bear and Intuit's ~15% flat-multiple base are correct.
- The LRS move of tranche 3 to after Apr 1, the no-trim rule and the reserve triggers can all be executed.
- Medtronic: the split-off result is still unpublished (the offer expired Oct 9) [H] ([Medtronic 2026-10-07](https://news.medtronic.com/2026-10-07-Medtronic-Announces-Final-Exchange-Ratio-of-4-5939-in-Split-Off-of-MiniMed-Group,-Inc)). The trigger "split-off outcome dilutive" can be checked in the next week or so.

---

## 3. Can the event gates and tranches actually be executed?

| Gate | Date | Executable? |
|---|---|---|
| Netflix Q3 | Oct 20 | Yes (October tranche) |
| Elevance Q3 | Oct 21 | Only with N8's wording |
| Maruti Q2 | Oct 27 | Yes, with N5 fixed |
| Jio listing / RIL Q2 | ~Oct 28 (unofficial) / RIL Q2 date unannounced | Yes; slips into the December tranche if delayed |
| Intuit FQ1 | Nov 19 | Yes (December tranche) |
| HDFC Bank Q3 FY27 | ~mid-Jan 2027 | Yes (February tranche) |
| RBI final revolving-credit rule | Unknown | Needs a deadline (N9) |
| Bharti prepaid hike | Unknown | Has a deadline already (end-2027 sell trigger) |
| Apollo demerger terms | Q4 FY27 | Yes |
| Global tranche 3 | After Apr 1, 2027 (if the sleeve > ₹10 lakh) | Yes |

---

## 4. Verdicts, round 2

**AGREE\*** means agree, with a cosmetic fix listed in §5. **CONDITIONAL** means a change to the rule or gate is needed before sign-off.

| Line | % of total | Verdict | Minimal change |
|---|---|---|---|
| Nifty 50 index fund | 22.5 | AGREE\* | Row figures: 14.3 / 1.6 (N2) |
| ICICI Bank | 8.25 | **CONDITIONAL** | Sell trigger → "ROE <15% for 4 consecutive quarters"; drop the NIM leg, or set it at <3.8% for 4 quarters. State the 9% cap as direct-only, or let ICICI run to ~10.5% look-through (N10). |
| NTPC | 6 | AGREE\* | "CERC cuts generation ROE below 14.5%" |
| SBI Life | 5.25 | AGREE\* | Define the bancassurance trigger (N12) |
| HDFC Bank | 4.5 | **CONDITIONAL** | Use the NIM basis on interest-earning assets. Buy the 1/3 starter **after Oct 17**. Gate for the rest: NIM ≥3.40% (IEA) in Q3 FY27. Sell: NIM <3.25% (IEA) for 2 consecutive quarters, or FY28 ROA <1.7%. |
| Reliance | 4.5 | **CONDITIONAL** | Replace "Retail EBITDA keeps falling" with "FY28 Retail EBITDA below FY26". |
| Bajaj Finance | 3.75 | AGREE\* | "ROE <18% for 4 quarters". If there is no final RBI rule by Jun 30, 2027, buy the second half (or move it to the index) on a pre-agreed decision. |
| Bharti Airtel | 3.75 | AGREE | — |
| Maruti Suzuki | 3.75 | **CONDITIONAL** | State the basis (company "operating EBITDA % of net sales"). Gate ≥9.5% on that basis. Sell <8% for 2 quarters. If the gate fails, the money goes to the **Nifty fund, not Eicher** (~36x). |
| Apollo Hospitals | 3.75 | AGREE | — |
| Indian gold ETF | 3 | AGREE | — |
| Cash reserve | 6 | AGREE\* | Add the "−15% from cost, thesis intact, subject to caps" clause to the table. |
| S&P 500 UCITS ETF | 4.75 | AGREE\* | Add the tax line (N13) |
| Microsoft | 3.75 | AGREE\* | Wording ("the larger of two AI-capex holdings") |
| Visa + Mastercard | 3.5 | AGREE\* | Blended base/bear ~16.2 / 1.0 |
| Intuit | 3 | AGREE | (The aggregate fix is in N1) |
| Medtronic | 2.5 | AGREE | — |
| Elevance | 2.25 | **CONDITIONAL** | Gate: "after Q3 (Oct 21) if the ≥12% 2027 target is reiterated; confirm on the formal guide in late January before the February tranche" (N8). |
| Amazon | 2 | AGREE\* | Base ~16% at 26–27x; bear −26% (−9.5%/yr) (N3) |
| Netflix | 2 | AGREE | — |
| Uber | 1.25 | AGREE | — |

---

## 5. Sign-off

**I do not sign off on v2 as written. I will sign off on v2 + these 8 edits.** All are mechanical and need no new research. A round-3 check of them needs no searches.

1. Restate the sleeve aggregates: India **12.4% vs 11.3% (+1.1pp; +0.3pp with equal haircuts; −0.6pp with picks cut 3pp)**; global **12.7% vs 10.4% (+2.3pp)**. Also restate the bottom line's "~0–3pp" edge as **"~0–2pp"**.
2. Fix the Nifty row (14.3 / 1.6) and Amazon (~16% base; −26% / −9.5%/yr bear).
3. Fix HDFC Bank's NIM basis, thresholds and starter timing (N4).
4. Fix Maruti's basis, separate the gate from the sell trigger, and send the fallback to the Nifty fund (N5).
5. Fix the ICICI (N6) and Reliance (N7) sell triggers, and the Elevance gate wording (N8).
6. Add a failed-gate rule: unspent gated money goes to the sleeve's index core at the February tranche (global: April tranche). Bajaj's and Bharti's top-ups wait until Jun 30, 2027 and Dec 31, 2027 respectively.
7. Define the caps on a look-through basis with headroom: single stock ≤10.5% look-through (or direct-only ≤9%); Indian financials ≤ index-neutral +5pp (~32%) (N10).
8. Cosmetic fixes: N11–N13.

**What I am signing off on in substance:**
- The core-satellite structure, the 75/25 split, and the name selection and weights.
- Gold as the bear hedge, the LRS and tax rules, and the honest framing that most of the expected return is market return.
- Above all, the explicit advice that an investor who will not review annually should hold the two index funds plus ICICI Bank and Microsoft.
