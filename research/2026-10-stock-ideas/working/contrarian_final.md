# Contrarian teardown of the final report (REPORT.md / report_final_detail.md)

Reviewer: independent sceptical CIO. I took no part in producing the report or in the three red-team rounds.
Date: Sat 2026-10-10 (last session Fri 2026-10-09).
Method: I read the final report, the detail file, all three red-team rounds and the four research briefs. I then ran about 53 WebSearch calls. WebFetch and the finance sites are blocked, so every new fact below is a search-result summary. I opened no page. Tags: **(calc)** = my arithmetic; **(mem)** = background knowledge I did not re-verify; [H]/[M]/[L] = confidence.

**Base-case assumption:** the user is an India-resident individual who will buy the global sleeve through the Liberalised Remittance Scheme (LRS). The report never says this, never prices it in, and its global sleeve is written as if for a US investor. If the user is an NRI or a US resident, section 3 changes materially; everything else stands.

---

## 0. Bottom line

The three red-team rounds fixed numbers inside each sleeve. They never asked who is buying, in what currency, at what tax cost, with what split between sleeves, or when the money is fully invested relative to the report's own top risk. The stock-level work is mostly sound and the key earnings guides check out. The portfolio-level advice is not usable as written by an India-based investor.

- **Survives as written:** ICICI Bank (now, full); TotalEnergies (now, full, through the NYSE ADR); Elevance (but only after Oct 21).
- **Survives smaller:** Intuit, Uber, Adobe, TCS, NTPC, SBI, HDFC Bank.
- **Buy only after the event:** TSMC, Netflix, Infosys, Maruti, Reliance, L&T.
- **Drop:** UnitedHealth.
- **Change the cash line:** do not remit money at 96.7/US$ and pay 20% TCS (tax collected at source) to earn ~3.9% in US T-bills. Indian 91-day bills pay ~5.6%.

---

## 1. New issues, ranked by severity (not raised in rounds 1–3)

### CRITICAL

**C1. No split between the sleeves, and no sizing against wealth or horizon.** Each sleeve sums to 100%, but the report never says how much goes to India versus global. v1 said "the user decides the India vs global split" (report_v1.md line 214); the final REPORT.md dropped even that line. It gives no horizon, no share of net worth, no liquidity reserve and no maximum position as a share of total wealth. For an India-based investor the split drives everything else that matters: FX exposure, LRS headroom, the TCS cash lock-up, US estate-tax exposure, and the cross-sleeve factor concentration in C3. **The weights cannot be executed as written.**

**C2. Buying USD assets at a record-low rupee, with no FX analysis at all.**
- The rupee closed at **96.78 on Oct 7** after the RBI hike [M], near its record of ~96.96. The pre-war level was ~91 (implied) [L/M]. After the April 8 ceasefire the rupee rallied to **92.59** within days [M].
- The **RBI itself has said the rupee may be undervalued** [L/M].
- The report's own "peace deal" scenario therefore carries an unpriced currency loss on the whole global sleeve: back to the April level ≈ **−4.3%** in INR terms; back to pre-war ≈ **−6%** (calc). That loss comes on top of the TTE and IT losses the scenario map already lists.
- The risk is two-way. BMI forecasts **97 by Mar-2027 and 99 by Mar-2028** [M], and long-run rupee drift has helped LRS investors. But the report must state it and size it.
- **The "IT is the INR hedge" logic double-counts.** For an INR investor the whole global sleeve is already a long-USD position. Adding TCS + Infosys (23% of the India sleeve) makes **~46–62% of the combined portfolio** a bet on a weaker rupee (calc; 70/30 to 50/50 India/global).

**C3. A cross-sleeve factor concentration that nobody added up.**
- The AI-disruption victims are Intuit + Adobe (25% of global), TCS + Infosys (23% of India), plus the LTIMindtree look-through in L&T (~1.3%; calc: 9% × ~14.5%).
- That is **~24–25% of the total portfolio in one factor, whatever the split** (calc). The report shows it per sleeve and never combines the two.
- The report's own scenario row ("AI disruption proves real for seat software / IT services") hurts both sleeves at once, and TSMC (10–15% of one sleeve) is the only offset.

**C4. The entry rule finishes buying just as the report's #1 risk begins.**
- Risk #1 in Part E is "Iran escalation after the Nov 3 midterms". Trump's pledge was only "no strikes before Nov 3", and reports say the White House has asked the Pentagon for options (india_macro.md).
- The entry rule is "buy the rest straight after the event, whatever the price". It completes almost every position between **Oct 13 and Nov 4**: 13–14 of 17 names have a result, IPO or CEO change in that window (calc from the key dates, adding RIL Q2, which is missing).
- The tranche rule spreads **company** risk but concentrates **macro** timing: the portfolio becomes fully invested the day the main binary risk opens.
- Brent shows how violent the headline moves are. It **settled at $83.77 on Aug 3** after Trump postponed an attack [M], and it is ~$102 now.
- For a "buy now" mandate, the honest fix is to finish the tranches through mid-November, or to hold a pre-committed dry-powder reserve for a post-Nov-3 shock. Do not complete everything by Oct 28.

**C5. India-investor frictions are ignored entirely** (detail in §3). They are: 20% TCS on LRS remittances above ₹10 lakh a year; the US$250k LRS cap; slab-rate tax on foreign gains held under 24 months; no ₹1.25 lakh exemption on foreign shares; 25% US withholding on dividends; Schedule FA disclosure with a ₹10 lakh penalty; and **US estate tax on US-situs holdings above US$60,000 at up to 40%**, with no India–US estate treaty. 2330.TW and Euronext Paris are not practically accessible through Indian LRS apps. FX markups run ~1–2%. These frictions change the ranking of names and the case for a cash line.

### MAJOR

**M1. "Far below fundamentals" is asserted, not shown.**
- The report gives **no fair-value estimate, upside target or expected return for any name.**
- By its own labels, 8 of 17 names are not "below fundamentals": TSMC, ICICI, Elevance, UNH, L&T, SBI and NTPC are "fair", "at median" or "quality at fair price", and Netflix is "moderate value".
- Only 2 names score 4/5 and 13 score 3/5. The user asked for names "we strongly believe will rise". The report's own convictions say it does not strongly believe in most of them. That is honest, but it means **the core ask was not delivered**, and the "BUY" headline overstates it.

**M2. The valuation bases are inconsistent, which flatters Adobe.**
- Intuit is valued on GAAP (≈14.4x), because its non-GAAP now includes stock comp.
- Adobe's headline "~10x" is non-GAAP, which **excludes** stock comp. The like-for-like figure is the report's own "~13.5x trailing GAAP".
- Intuit and Adobe are therefore priced about the same on a comparable basis. The summary table's "~10x" is the wrong number to show.
- Uber's "~16x fwd" basis (adjusted or GAAP) is never stated.

**M3. Intuit carries the largest weight (16%) and the highest conviction (4/5) despite three 2026 shocks.**
- **May 2026:** −20% in one day, to $307.07, on a TurboTax outlook cut and ~3,000 layoffs, the worst day since 2003 [M].
- **August 2026:** FY27 guide of **TurboTax revenue +2–3% and Consumer +4–6%**; only GBS grows 13–14% [H, guide verified]. Intuit "lost on price" with filers under $50k.
- The report's moat argument (regulated, liability-bearing workflows are hardest for AI to break) conflicts with management cutting DIY prices to compete.
- The valuation is real (GAAP guide $20.12–20.36 verified; ~$292 in late September [M]). The **sizing** is not: 16% at 4/5 is a "strong belief" bet on a contested question.

**M4. Adobe: the leadership vacuum is understated.**
- The report discloses the Dec 1 CEO change and the creative-business head's exit. It omits that **CFO Dan Durn left in June 2026 for Marvell; Adobe has an interim CFO** [H].
- That is CEO, CFO and creative head all turning over within a year. On Jul 21 Morgan Stanley went **Underweight with a $240 target**, about today's price [L/M; one source].

**M5. Managed care is "one factor", and the weaker leg was kept.**
- UNH is ~20x clean 2026 EPS, at its 5-year median. Commercial cost trend is >11% "with no moderation"; Medicare Advantage membership was **7.565M at Jun 30, −785k y/y** [M]; DOJ probes are open; Part D delinking starts in 2028.
- Elevance is ~13x 2027.
- If one diversifier is needed, keep ELV and drop UNH. The 15% cap leaves two names with one risk.

**M6. The macro view is internally inconsistent, in both directions.**
- *Too sanguine on rates.* The report itself describes ERP ≈ 0, a 10-year that peaked at **5.33–5.34% in early October** [H], a Fed hiking into +29k payrolls with negative real wages, and an average ~18% intra-year drawdown in midterm years. Yet the global sleeve is 84% equities, and 61% of it is long-duration growth. The US 10-year at ~5.2% and the Indian 10-year G-sec at 7.28% are never considered as assets.
- *Too bearish on the earnings engine.* The "30% earnings growth" that props up index valuation (FactSet: Q3 +29.5%, CY26 +31.8%, fwd P/E 19.0 on Oct 2 [H]) is concentrated in AI hardware. The portfolio barely owns it: TSMC only. The chosen names grow EPS ~10–15%. **So the index's earnings defence does not transfer to this portfolio.** The global sleeve is a bet on narrative mean-reversion (the AI-victim re-rating), not on earnings momentum. Fine, but say so.

**M7. The India sleeve holds 0% cash.** The RBI has said "only a hike or a pause" lies ahead, FPI selling is at a record, Jio and IPO supply are heavy, the monsoon was the worst since 2015, and capex faces fiscal-slippage risk. Axis Securities itself advises 10–15% cash. The global sleeve holds 16% cash, but in the wrong currency (C5).

**M8. Missing asset classes, markets and sectors.**
- **Gold:** the traditional Indian hedge against war, stagflation and Fed-independence shocks (~$4.1–4.2k/oz) is absent.
- **No in-India oil hedge was screened** (ONGC, Oil India, Coal India), even though the India sleeve is 54% short oil. These come with windfall-tax risk, but so does TTE, and they need no LRS or TCS.
- **Untouched areas:** Asia ex-India (Korea memory, Japan), Europe beyond TTE, Indian insurers and AMCs. Small and mid caps were avoided, which is defensible, but the report does not say why.

**M9. Maruti's biggest demand risk is missing.** The monsoon ended ~12.6% deficient, the worst since 2015, and El Niño persists (india_macro.md). The report's risk list has margins and the festive base effect, but not rural or small-car demand. Maruti is losing share (<40%) and set fresh lows: ₹12,159 on Sep 16 [M], ~₹11,2xx now.

**M10. Reliance's event cluster is understated, and its "buy-now" reason is weak.**
- **RIL's Q2 FY27 results date is missing from the calendar.** It is unannounced; last year it was Oct 17 [M], which would land inside the Jio IPO window.
- The shareholder-quota reason for a first tranche is trivial: bids of **≤₹2 lakh** [L/M].
- The IPO is ~2.9% of post-issue capital [M]. A thin float makes the listing price a noisy anchor for the holdco value.
- As of my searches the RHP and band are **still not official** [M].

**M11. There is no exit discipline.** "What would prove us wrong" lists exist, but there are no price targets, trim rules, review dates or rebalancing bands. Three tax facts make this costly:
- A kill-criterion exit within 24 months on a foreign share is taxed at slab rates (up to ~39% with surcharge, mem).
- Indian STCG is 20% under 12 months.
- Several kill criteria sit at or above company guidance. Example: the L&T exit trigger is "margin <8.5%" while L&T guides **~8.3%** core margin for FY27 [M]. The basis is ambiguous.

**M12. The sign-off was procedural.** Round 3 ran **zero new searches** and only checked whether round 2's edits had been made. The process converged on the red team's own framing (per-sleeve concentration, per-name disclosures). The investor-level questions in C1–C5 were never on the checklist.

### MINOR
- **HDFC Bank P/B basis.** The 1.8x uses BV ₹390.56, which is likely consolidated (Sharekhan: 1.86x at ₹726 on Aug 21). Standalone BV is ₹367 (Mar-26, BOBCAPS) to ~₹378 (Fyers), so **standalone P/B ≈ 1.87–1.93x** (calc). The 5-year average it is compared with is standalone, so the discount is a bit smaller than shown.
- **ICICI 52-week high.** A Sep-10 source gives **₹1,547**, not ₹1,480, so it is ~−12.5% from the high, not −8.5% (calc).
- **L&T Middle East exposure.** ~**40%** of the order book (US$77.7B at Mar-31) and **34% of FY revenue** (Upstox, Sep 23), vs the "37%" stated.
- **Uber–Delivery Hero.** It is a board-backed **public tender offer** needing >50% acceptance, with antitrust review pending (DH is selling 14 overlapping markets to SSW Partners for ~€1.4B). It is not a completed or "signed" merger, so there is completion risk both ways.
- **Netflix fee.** The $2.8B fee was paid by PSKY on WBD's behalf and is **"refundable to PSKY in certain circumstances"** (WBD 8-K). Q2 buybacks ($4.7B) ran ~3x Q2 FCF.
- **TotalEnergies tax.** The French surtax is **extended into 2027 at reduced rates** (~€5B yield vs €7.3B; PLF 2027 tabled Oct 1, debate from Oct 12). TTE paid none in 2025 for lack of French profit. The red team's tax objection was overstated; the volume-loss objection stands.
- **Elevance.** Its 2026 Medicaid margin is ~−1.75% (the "trough"). Management warns of "material contraction" in ACA if enhanced subsidies lapse. Mizuho's target is $400, about today's price.
- **Intuit 52-week high.** $696.14 per one source, vs $689–694.
- **US 10-year.** The 5.24% close is consistent; the intraday peak was 5.33–5.34% (Oct 1–5).

---

## 2. Data-integrity spot-check (the load-bearing numbers)

| Figure in report | Check | Verdict |
|---|---|---|
| Intuit FY27 GAAP EPS $20.12–20.36; revenue +9–10% | Confirmed by several sources (guide table $23.28–23.51B) | **Holds [H]**. The price ($291.08, Oct 6) is stale; ~$292 late Sep [M]. |
| HDFC Bank ~1.8x book (BV ₹390.06) | Consolidated-style BV; standalone ₹367–378 | **Basis wrong; ~1.8–1.9x [M]** |
| Jio band / RHP | Still unofficial; no RHP found | **Holds (unofficial) [M]** |
| TCS Q2: PAT ₹13,884 cr, CC +0.5% q/q | Confirmed (PAT +4% q/q, ~+15% y/y; CC +0.5% q/q) | **Holds [H]**. Underlying ~+5% is the red team's calc. |
| Netflix FCF guide $12.5B incl. fee; ~28x underlying | Confirmed; plus a refundability caveat | **Holds [H]** |
| Uber–Delivery Hero | Offer launched Jul 16; >50% acceptance; close H2-27; remedy sale | **Holds, but "signed" overstates it [M]** |
| Nifty 22,520 | Sep 30 close 22,620 [M]; Oct 9 not found | **Plausible, unverified [L/M]** |
| US 10y 5.24% | Peak 5.33–5.34% Oct 1–5; 5.26% Oct 6 [H] | **Holds** |
| Brent ~$102 | Oct 9 not found; Aug 3 $83.77 shows headline beta | **Plausible, unverified [L]** |
| USD/INR 96.7 | 96.78 close Oct 7 [M] | **Holds** |
| S&P earnings +30%, fwd P/E 19 | FactSet Oct 2: Q3 +29.5%, CY26 +31.8%, 19.0x | **Holds [H]** |
| Infosys Q2 Oct 23; Netflix Oct 20; ELV Oct 21; UNH Oct 13; HDFC CEO Oct 27 | All confirmed (Infosys: most sources) | **Holds [M/H]** |

**How much do the conclusions depend on unverifiable data?**
- Not much at the stock level. The theses rest on company guides and filings, which mostly verify; prices that are 1–4 days old do not change any call.
- **A lot at the portfolio level, but for a different reason.** The missing inputs are not data errors. They are facts the report never sought: the investor's domicile, the split, tax, FX and access.
- Several India numbers rest on retail aggregators (5paisa, Univest, Sahi, Kalkine) rather than exchange filings. The report's "trustworthy financial sites" claim is weaker than its disclaimer suggests.

---

## 3. India-based investor: what the report ignored (verified where possible)

| Issue | 2026 rule / fact | Effect on the report |
|---|---|---|
| **LRS cap** | US$250,000 per person per FY. **I found no 2026 cut.** The RBI defended the rupee with an FCNR(B)/swap window (~$133–143B), not LRS curbs. Precedent: in Aug 2013, at a record-low rupee, the RBI cut LRS from $200k to $75k overnight. | Tail risk. If the rupee breaks 100, an LRS curb is the obvious tool. Unwinding is unaffected, but adding later could be blocked. |
| **TCS on remittance** | **20% on LRS investment remittances above ₹10 lakh per FY** (aggregated per PAN). Budget 2026 cut education/medical TCS but not investment TCS [M; sources conflict slightly]. Creditable against tax or refundable at ITR. | A cash-flow lock-up. Example: remitting ₹50 lakh now → ~₹8 lakh TCS held until the ITR is processed, unless offset against advance tax (calc). It favours fewer, larger, higher-conviction global positions and argues against parking cash abroad. |
| **Capital gains on foreign shares** | >24 months: **12.5% LTCG**, no indexation, **no ₹1.25 lakh exemption**. ≤24 months: **slab rate** (up to ~39%, mem). The US does not tax a non-resident's capital gains. | The kill criteria and tranche logic imply possible exits within 24 months at slab rates. |
| **Indian listed equity** | STCG 20% (<12 months); LTCG 12.5% above ₹1.25 lakh. **Unchanged in Budget 2026.** Buybacks are now taxed as capital gains. | Exits from the India sleeve inside 12 months cost 20%. |
| **Dividends** | Taxed at slab in India. **US withholds 25%** under the treaty (W-8BEN); claim credit via **Form 67**. Taiwan and France withhold too (rates per treaty; mem). | TTE's 4.6% yield is worth less than headline after withholding and slab tax. |
| **Disclosure** | Foreign assets must be reported in **Schedule FA**. Penalty ₹10 lakh (relief if aggregate non-immovable foreign assets < ₹20 lakh). **FAST-DS 2026** is a one-time window to Dec 31, 2026, for past non-disclosure. | Compliance burden; relevant if the user already holds foreign assets. |
| **US estate tax** | Non-resident aliens: only **~US$60,000** of US-situs assets is effectively sheltered; rates up to **40%**; **no India–US estate treaty.** US-listed shares count; ADR treatment is debated. | At 96.7/US$, US$60k ≈ ₹58 lakh. A global sleeve above that carries a real tail risk the report never mentions. Mitigations to discuss with an adviser: Irish-domiciled UCITS funds, or holding through structures. |
| **Access** | US-listed names (INTU, ADBE, UBER, NFLX, ELV, UNH, TSM ADR, TTE ADR) are available through Indian LRS apps (INDmoney, Vested, Tickertape/ViewTrade IFSC) and GIFT City. **2330.TW: no named Indian retail route** ("limited"). **Euronext Paris: not offered by mainstream Indian apps**; Interactive Brokers is the usual route. NSE IX UDRs cover only a limited list. | "Investors with access can buy 2330.TW" is moot for this user, so they pay the ~15% ADR premium (2026 snapshot; 13.7% average in May). Use the **TTE NYSE ADR**, not Paris. |
| **Costs** | Brokerage ~0.25%; **FX markup ~1–2%**; bank remittance costs. | ~2–3% round-trip friction (calc) erodes a "moderate value" thesis such as Netflix. The half-now rule doubles some fixed costs. |
| **Cash line** | US 3-month bill ~3.9–4.0% vs **India 91-day T-bill ~5.57%, 364-day ~6.29%** (Oct 7 auction; one secondary source) [L/M]. | Holding 16% "dry powder" in US T-bills means remitting at a record-low rupee, paying TCS, and earning ~1.7pp less. **Keep dry powder in INR** (T-bills or liquid funds) and remit only when deploying. |
| **Alternative route** | Indian MFs' overseas cap is **US$7B industry-wide and nearly used up**; several international funds are closed to new money. | The MF route is largely unavailable, so direct LRS is the realistic channel. That makes the frictions above binding. |

**Net for the India-based user:**
1. Size the global sleeve deliberately: say 20–35% of equities, stated explicitly.
2. Keep global cash in INR.
3. Prefer fewer global names held more than 24 months.
4. Watch the US$60k estate-tax line.
5. Treat the global sleeve as the portfolio's main INR/war hedge, and cut Indian IT accordingly.

---

## 4. Portfolio and macro

**Combined exposures** (calc; India/global split of 50/50 and 70/30):

| Factor | 50/50 | 70/30 | Comment |
|---|---|---|---|
| AI-disruption victims (INTU, ADBE, TCS, INFY, LTIM look-through) | ~24.6% | ~24.5% | One factor. Neither sleeve reports the total. |
| Long USD / INR-weakness winners (global sleeve + Indian IT) | ~61.5% | ~46% | IT's "hedge" role duplicates the global sleeve. |
| India oil/war-hurt names (HDFC, ICICI, SBI, L&T, Maruti) | 27% | 38% | For an INR investor, partly offset by the USD sleeve. |
| Rate-shock losers (global long-duration 61% + India banks 33% + NTPC 12%) | ~53% | ~50% | No duration or rates hedge anywhere. |
| Cash | 8% (in USD) | 4.8% (in USD) | Wrong currency; zero in India. |

**Other concentrations the report waves through**
- **Three banks at 33%**, plus SBI's deposit gap (deposits +9.7% vs loans +18.6%), going into an RBI tightening cycle. Plus expected-credit-loss provisioning from Apr-2027. Plus the HDFC kitchen-sink risk in Jan-2027.
- **IT overlap:** TCS + Infosys + L&T's LTIMindtree.
- **Event clustering** (C4): 13–14 of 17 names have events Oct 13–Nov 4, then the Iran window opens.

**Is the macro view one-sided?** Both ways (M6). It is too sanguine on rates and valuation for how fully invested it is. And it is too dismissive of the AI-earnings engine, which it barely owns. The honest description: "a contrarian, narrative-reversion portfolio in a market whose earnings growth sits elsewhere, held at ~zero ERP, bought at a record-low rupee." That can still be a good bet. But it is not "quality names far below fundamentals that we strongly believe will rise".

**Missing entirely:**
- gold;
- government bonds (US 10y ~5.2%, India 10y 7.28%);
- an in-INR oil hedge;
- Asia ex-India and Europe beyond TTE;
- insurers and AMCs;
- a recession-probability estimate;
- sizing against total wealth and horizon;
- exit rules and review dates;
- a post-Nov-3 contingency.

---

## 5. Per-stock teardown and FINAL calls

Calls are for an India-based investor. Indicative weights are within each sleeve. The weight freed in the global sleeve stays **in INR** until deployed.

### Global sleeve

| Name | Biggest overstatement / underplay | FINAL call | Indicative weight |
|---|---|---|---|
| **Intuit** | 16% at 4/5 conviction on a stock with three 2026 shocks. TurboTax revenue guided at **+2–3%**, Consumer +4–6%; management "lost on price". The moat claim contradicts the price cuts. The valuation (~14x GAAP, verified) is real. | **BUY SMALLER** (now, full of the smaller size) | 10% (from 16%) |
| **TSMC (ADR)** | Not below fundamentals: ~5% off its high, +45% YTD, record margins that management says will dip with the 2nm ramp, a ~15% ADR premium that an Indian investor cannot avoid. Prints in 5 days. | **BUY ONLY AFTER EVENT** (Oct 15) | 10% (from 15%) |
| **Uber** | The "signed" Delivery Hero deal is a tender offer with antitrust risk, financed by a ~€14B bridge. FCF goes to M&A and debt, not buybacks. Waymo leaves Austin and Atlanta in Jan-2028. A 3/5 "show-me" name at 13%. | **BUY SMALLER** | 9% |
| **Adobe** | "~10x" is non-GAAP excluding stock comp; ~13.5x GAAP is the like-for-like figure. CFO left in June (interim CFO) on top of the CEO and creative-head changes. MS target $240 ≈ price. | **BUY SMALLER** | 6% |
| **Netflix** | ~28x underlying FCF is fair value, not "below fundamentals". The fee is refundable in some circumstances. Buybacks ~3x quarterly FCF. Less engagement disclosure. The 2022 levers are used up. | **BUY ONLY AFTER EVENT** (Oct 20), and only if engagement stabilises | 5% |
| **Elevance** | Labelled fair value, correctly. The underplayed risks are a Medicaid margin of ~−1.75% and ACA "material contraction". It is the cheaper managed-care leg (~13x 2027). | **BUY ONLY AFTER EVENT** (Oct 21) | 9% |
| **TotalEnergies** | Hedge labelled "partial", correctly. Underplayed: for an INR investor it is a **double** war hedge (oil up, INR down) and a double loser on peace. The French tax risk was overstated: TTE had no 2025 French surtax and the 2027 extension is at reduced rates. | **BUY NOW (full)** through the **NYSE ADR**; the hedge must be in place before Nov 3 | 9% |
| **UnitedHealth** | ~20x clean, at its 5-year median; commercial trend >11% with no moderation; MA members −785k y/y; DOJ; PBM delinking in 2028. It duplicates ELV's policy factor. | **DROP** (fold into ELV or cash) | 0% |
| **Cash** | 3.9% in USD after remitting at a record-low rupee and paying TCS. | **Hold in INR** (Indian T-bills/liquid funds, ~5.6–6.3%) | ~42% of the sleeve stays un-remitted, or shrink the global sleeve |

### India sleeve

| Name | Biggest overstatement / underplay | FINAL call | Indicative weight |
|---|---|---|---|
| **ICICI Bank** | The ~8.5% "off high" uses ₹1,480; a Sep source gives ₹1,547 (~−12.5%). A low-variance print does not justify waiting a week. | **BUY NOW (full)** | 14% |
| **TCS** | Underlying PAT ~+5%, CC +0.5% q/q, AI deflation conceded. Its "INR hedge" role is duplicated by the global sleeve. | **BUY SMALLER** | 9% |
| **Infosys** | A guidance cut to ~0.5–2% CC is widely expected on Oct 23. It is the same factor as TCS and the AI-victim software names. | **BUY ONLY AFTER EVENT** (Oct 23) | 6% |
| **Maruti** | The monsoon deficit (worst since 2015) and rural/small-car demand are absent from the risks. Share <40%. Fresh lows. ~25x trailing is not cheap for a share-loser, even on trough margins. | **BUY ONLY AFTER EVENT** (Oct 27 margin print) | 8% |
| **NTPC** | 12% for a 3/5 bond proxy in a cycle where the RBI says only hikes or a pause lie ahead (10y +75bp y/y). Not beaten down (−8% YTD). | **BUY SMALLER** (now) | 8% |
| **Reliance** | RIL's own Q2 date is missing from the calendar (likely inside the IPO window). The quota is ≤₹2 lakh. The band is still unofficial. A thin 2.9% float makes the listing a poor value anchor. Export levies reviewed fortnightly. | **BUY ONLY AFTER EVENT** (Jio listing ~Oct 28 and RIL Q2) | 9% |
| **HDFC Bank** | P/B is ~1.87–1.93x standalone, not 1.8x vs a standalone history. The real de-risking event is **Q3 FY27 (Jan-2027) under the new CEO**, not Oct 17. Its 3.5/5 conviction is the sleeve's second-highest despite open MSRDC/RBI and SDNY matters. | **BUY SMALLER** (starter now, add after Jan-2027) | 7% |
| **SBI** | At its median P/E (fair, not cheap). Deposits +9.7% vs loans +18.6% after a hike. Q2 treasury hit. ECL from Apr-2027. Strike status still unconfirmed. | **BUY SMALLER** | 8% |
| **L&T** | PEG ~2.5 ("fair"). Middle East ~40% of the book and 34% of revenue. The kill trigger (<8.5% margin) sits above the ~8.3% core-margin guide. LTIM overlap. Plain war-beta. | **BUY ONLY AFTER EVENT** (Q2, late Oct) | 7% |
| **Cash (INR)** | The report holds none. | **Hold** INR T-bills/liquid funds; deploy after Nov 3 or on a shock | ~24% (mostly after-event tranches plus a reserve) |

Tally: BUY NOW (full): 2 (ICICI, TTE). BUY SMALLER: 7 (INTU, UBER, ADBE, TCS, NTPC, HDFC Bank, SBI). BUY ONLY AFTER EVENT: 7 (TSM, NFLX, ELV, INFY, MARUTI, RIL, L&T). DROP: 1 (UNH).

---

## 6. Delivery against the user's ask

| Ask | Delivered? |
|---|---|
| Comprehensive markets / macro / India news / capex | **Mostly.** Good macro and India capex coverage. Not covered (budget): Russia–Ukraine, Taiwan, Europe and EM flows, GST/PMI, current account. |
| Indian and global stocks buyable **today** | **Partly.** 9 of 17 are "half now", so most are not fully bought today. The rule is honest but contradicts "without waiting". |
| Quality names **far below fundamentals** | **Partly.** About 9 names qualify by the report's own labels. **No fair values or upside targets anywhere.** |
| "We **strongly believe** will rise" (Uber/Netflix-style) | **No.** 2 names at 4/5, 13 at 3/5. The report itself says Uber and Netflix are *not* recovery setups. The truthful answer is "we have moderate conviction"; the headline should say so. |
| Reddit and trustworthy financial sites | **No for Reddit**: blocked. The report used two secondhand anecdotes and zero r/IndiaInvestments or ValuePickr material. I could not get Reddit content through search either. Retail-sentiment proxies were not used systematically (e.g., heavy bearish Reddit traffic on Adobe is a classic contrarian positive). "Trustworthy sites": many India figures come from retail aggregators. |
| Usable by an India-based investor | **No.** No split, no FX, tax, LRS, estate-tax or access analysis, and cash in the wrong currency. |

---

## 7. Factual corrections, with sources (URL + date)

1. **HDFC Bank book value basis.** BV ₹390.56 / P/B 1.86 at ~₹726 (Sharekhan, 2026-08-21): https://www.sharekhan.com/stock/HDFC-Bank-Ltd. Standalone BV ₹367 at Q4 FY26 (BOBCAPS review, 2026-04-19): https://www.barodaetrade.com/Reports/HDFCBank-Q4FY26ResultReview19Apr26-Research.pdf. BV ₹377.77 / P/B 1.94 (Fyers, undated): https://fyers.in/stocks/hdfc-bank-ltd/profit-loss.
2. **ICICI Bank 52-week high ₹1,547** (price ₹1,382.40 on 2026-09-10): https://univest.in/blogs/icici-bank-q2-results-fy27-preview-date-expectations.
3. **Adobe CFO exit** (left Jun 15, 2026 for Marvell; interim CFO Steven Day), Business Standard, 2026-06-12: https://www.business-standard.com/world-news/adobe-cfo-dan-durn-departs-while-company-also-searches-for-new-ceo-126061200125_1.html. Morgan Stanley Underweight, $240 target (2026-07-21; search summary of a mirror page, L): https://www.webull.ca/news-detail/15266786951963648.
4. **Intuit FY27 segment guide** (TurboTax +2–3%, Consumer +4–6%, GBS +13–14%; revenue $23.28–23.51B), 2026-08: https://www.01net.it/intuit-reports-fourth-quarter-and-full-year-fiscal-2026-results-sets-fiscal-2027-guidance/. May shock (−20% to $307.07), 2026-05-22: https://www.cpapracticeadvisor.com/2026/05/22/intuit-sees-worst-plunge-since-2003-after-announcing-layoffs/183830/. Price ~$292 and 52-week high $696.14, 2026-09-23: https://247wallst.com/investing/2026/09/23/intuit-crashed-over-agentic-ai-fears-in-2026-one-wall-street-analyst-says-nope-near-50-gains-on-the-way/.
5. **Netflix fee refundable to PSKY in certain circumstances** (WBD Q1-26 8-K): https://www.sec.gov/Archives/edgar/data/0001437107/000143710726000055/a991wbd1q26earningsrelea.htm. Q3 on Oct 20 confirmed: https://www.insiderfinance.io/news/netflix-q3-2026-earnings-oct-20.
6. **Uber–Delivery Hero is a tender offer** (>50% acceptance; DH sells 14 overlapping markets to SSW Partners for ~€1.4B; close H2-2027), 2026-07-16: https://www.thestar.com.my/business/business-news/2026/07/16/uber-launches-us148bil-offer-for-delivery-hero-to-create-global-platform.
7. **UNH Medicare Advantage membership 7.565M, −785k y/y at Jun 30**; Q3 on Oct 13 (Zacks preview): https://www.zacks.com/stock/news/3001305/unitedhealth-q3-coming-up-two-questions-investors-cant-ignore.
8. **Elevance:** Q3 on Oct 21 (company notice, 2026-10-05): https://www.biopharmawatch.com/news/ELV/elevance-health-conference-call-q3-2026-results. Mizuho target $400: https://www.tipranks.com/news/the-fly/elevance-health-price-target-lowered-to-400-from-420-at-mizuho-thefly. Medicaid −1.75% / ACA risk: https://www.marketbeat.com/instant-alerts/elevance-health-q2-earnings-call-highlights-2026-07-15/.
9. **French surtax extended into 2027 at reduced rates** (PLF 2027 tabled 2026-10-01): https://www.legifiscal.fr/actualites-fiscales/4612-plf-2027-retour-contribution-exceptionnelle-benefices-grandes-entreprises-confirme.html and https://www.tradingsat.com/actualites/marches-financiers/ils-reclamaient-sa-suppression-la-surtaxe-sur-les-grands-groupes-dont-ceux-du-cac-40-sera-reduite-de-30-dans-le-budget-2027-1170981. TTE escaped the 2025 surtax for lack of French profit (cited in red-team round 2): https://www.linfodurable.fr/surtaxe-sur-les-entreprises-totalenergies-y-echappe-en-2025-faute-de-benefices-en-france-54498.
10. **L&T Middle East ~40% of the US$77.7B order book (Mar-31), 34% of FY revenue; FY27 margin guide ~8.3%** (Upstox, 2026-09-23): https://upstox.com/news/market-news/stocks/l-and-t-shares-down-5-in-q2-so-far-despite-1-48-lakh-crore-order-inflows-is-the-firm-gearing-up-for-growth-next/article-200760/.
11. **Rupee:** 96.78 close on 2026-10-07: https://dailypioneer.com/news/rupee-slumps-43-paise-to-close-at-96-78-against-us-dollar. Ceasefire rally to 92.59 (April 2026): https://www.deccanherald.com/business/markets/rupee-surges-47-paise-to-close-at-9259usd-on-us-iran-ceasefire-rbi-pause-on-policy-rates-3960537. RBI sees the rupee as possibly undervalued: https://easemyprep.in/news/3459-rbi-sees-rupee-as-undervalued-fcnrb-inflows-cross-32-billion. BMI 97 (Mar-27) / 99 (Mar-28): https://www.outlookbusiness.com/news/indian-rupee-seen-weakening-to-97-per-dollar-by-fy2026-27-end-bmi. FCNR(B) window: https://www.outlookmoney.com/banking/rbi-to-close-fcnrb-scheme-early-after-52-3-billion-inflows.
12. **US 10-year peak 5.33–5.34%** (2026-10-01 to 10-06): https://news.bgov.com/insurance/treasury-10-year-yield-hits-highest-since-2002-on-rate-outlook ; https://tradingeconomics.com/united-states/government-bond-yield/news/589866.
13. **FactSet** (2026-10-02): Q3 +29.5%, CY26 +31.8%, fwd P/E 19.0: https://advantage.factset.com/hubfs/Website/Resources%20Section/Research%20Desk/Earnings%20Insight/EarningsInsight_100226.pdf.
14. **Jio:** band and RHP unofficial; 27 cr shares ≈ 2.9% of post-issue capital: https://www.outlookmoney.com/invest/jio-platforms-ipo-launch-date-issue-size-price-band-listing-date. Quota bids up to ₹2 lakh: https://upstox.com/news/market-news/ipo/does-jio-platforms-ipo-have-shareholder-quota-for-reliance-industries-investors/article-196358/.
15. **RIL Q2 FY27 date not announced; last year Oct 17** (2026-09-08): https://univest.in/blogs/reliance-q2-results-fy27-preview-date-expectations.
16. **TSMC Q3 revenue NT$1.494T (+50.9%), above guidance; gross margin to dip on the 2nm ramp:** https://www.kaohooninternational.com/?p=592325. ADR premium ~15% (2026 snapshot), 13.7% average in May: https://biz.heraldcorp.com/article/10805490.
17. **Maruti new 52-week low ₹12,159 on 2026-09-16:** https://www.5paisa.com/blog/maruti-suzuki-india-stock-update-16-sep-26.
18. **HDFC Bank CEO Anup Bagchi, Oct 27, 2026 to Oct 26, 2029, RBI-approved** (2026-10-01): https://www.businesstoday.in/latest/corporate/story/hdfc-bank-appoints-anup-bagchi-as-md-ceo-for-three-year-term-from-october-27-559151-2026-10-01.
19. **UFBU strike:** Sep 28–30 deferred; Oct 26 status unconfirmed (2026-09-28): https://www.theweek.in/news/biz-tech/2026/09/28/bank-strike-postponed-india-ufbu.html.
20. **Indian T-bills** 91d 5.57% / 182d 6.10% / 364d 6.29% (auction 2026-10-07; secondary source, L/M): https://plutusias.com/?p=279438.
21. **Brent settled $83.77 on 2026-08-03** after an attack was postponed: https://qna.org.qa/en/News-Area/News/2026-8/4/oil-prices-drop-7-at-settlement.
22. **TCS Q2 FY27** (PAT ₹13,884 cr, +4% q/q; CC +0.5% q/q), 2026-10-08: https://www.dtnext.in/news/business/tcs-q2-net-profit-jumps-4-pc-to-rs-13884-crore-in-fy27.
23. **Infosys Q2 on Oct 23** (most sources): https://upstox.com/news/market-news/stocks/infosys-q2-results-check-it-firm-s-earnings-date-plans-to-expand-indore-development-centre-stock-to-be-in-focus/article-200374/.
24. **India-investor rules:**
    - TCS 20% above ₹10 lakh (Tickertape, updated 2026-08-18): https://www.tickertape.in/blog/tcs-on-foreign-remittance/ ; https://1finance.co.in/blog/new-tcs-rule-after-budget-2026-know-tcs-rates-on-education-international-trips-foreign-investments/
    - Foreign-share LTCG 12.5% (>24 months), STCG at slab, US dividend WHT 25%, Form 67 (Motilal Oswal, 2026-08): https://www.motilaloswal.com/learning-centre/2026/8/tax-on-us-stocks-for-indian-investors-a-complete-guide-to-capital-gains-tcs-dtaa-and-ftc
    - Indian equity LTCG/STCG unchanged in Budget 2026: https://oga-prod.angelone.in/news/taxation/union-budget-2026-ltcg-tax-unchanged-at-12-5-stt-on-commodity-futures-hiked
    - FAST-DS 2026 / Schedule FA: https://taxguru.in/corporate-law/foreign-assets-small-taxpayers-disclosure-scheme-2026-overview-faqs.html
    - US estate tax for non-resident aliens: https://vestedfinance.com/understanding-us-estate-tax-implication-for-non-us-residents/ ; https://ksandk.com/md/corporate/us-estate-tax-indian-residents-us-shares/
    - Access to Taiwan shares: https://vestedfinance.com/blog/us-stocks/investing-in-the-taiwan-market-from-india-a-complete-guide/
    - NSE IX UDRs: https://zerodha.com/z-connect/varsity/investing-in-us-stocks-from-india
    - MF US$7B cap: https://www.kotakneo.com/news/mutual-funds/amfi-review-7-billion-overseas-mutual-fund-investment-cap-rbi-sebi/
    - FX markups: https://algotest.in/blog/vested-vs-indmoney-for-us-stocks/
    - 2013 LRS cut precedent: https://www.business-standard.com/article/finance/rbi-introduces-more-capital-control-measures-to-defend-rupee-113081401086_1.html

---

## 8. Essential changes (in priority order)

1. **Write an investor section.** State the domicile assumption, the India/global split (e.g., 65–80% India for an India resident) and the horizon (≥24 months, to reach LTCG on foreign shares). Add the FX, TCS, LRS, tax, estate-tax (US$60k) and access rules. Keep dry powder in **INR**, not US T-bills.
2. **Re-sequence the buying around Nov 3.** Do not finish the tranches by Oct 28. Hold a pre-committed INR reserve (~20–25% of the planned equity) for after the midterms or an escalation shock. Put the TTE hedge on before Nov 3.
3. **Cut the duplicated factor bets.** Combine AI-victim exposure across both sleeves and cap it at ~15–18% of the total. Cut Indian IT, since the USD sleeve is already the rupee hedge. Drop UNH (one policy factor; the weaker leg).
4. **Fix the overstatements.** Show Adobe on GAAP. Cut Intuit to ~10% and conviction to 3.5. Add RIL's Q2 date and the Maruti monsoon risk. Add Adobe's CFO exit. Restate HDFC P/B on a standalone basis. Retitle the report to match its moderate conviction.
5. **Add exit discipline.** For every name: a fair-value range, an upside/downside estimate, a review date and a trim/sell rule consistent with the tax holding periods.
