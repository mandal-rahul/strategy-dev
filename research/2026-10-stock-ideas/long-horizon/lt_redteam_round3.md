# Red team, round 3: lt_report_v3.md (final check)

**Date:** Sat 2026-10-10. No searches were needed: nothing new appears in v3.

**Method:** I checked v3 against the 8 required edits from round 2 and re-checked the arithmetic. Weights sum to 100/100 and 75/25. The sleeve totals match `rt_round2.py`: India 12.4 vs 11.3; global 12.7 vs 10.4. The Visa/Mastercard blend (14.8/0.7 and 17.7/1.4 → ~16.2/1.0) and the look-through financials (21.75 + 22.5 × ~35% ≈ 29.6) also match.

## 1. Required edits: status

| # | Edit | In the body (§1–4)? | Consistent? |
|---|---|---|---|
| 1 | Corrected totals and edge; headline "~0–2pp" | Yes (§1, O2, O3) | Yes |
| 2 | Nifty row 14.3/1.6; Amazon 15.5–16.2 / −9.5 (−26%) | Yes | Yes in §2–3. **The O7 row still says the Amazon bear is ~−22%.** |
| 3 | HDFC Bank: interest-earning-asset basis, starter after Oct 17, gate ≥3.40%, sell <3.25% for 2 quarters or FY28 ROA <1.7% | Yes (§2) | **The O12 row still says "one-third now … NIM ≥3.3%".** |
| 4 | Maruti: net-sales basis, gate ≥9.5%, sell <8%, failed gate → Nifty fund; Eicher rejected | Yes (§2) | **The O14 row still says "≥9%; Eicher is the swap".** |
| 5 | ICICI, Reliance and Elevance rules | Yes | Yes |
| 6 | Failed-gate rule with the Jun 30 and Dec 31, 2027 deadlines | Yes (§4) | Yes. HDFC Bank's gate (mid-Jan) and Elevance's (late Jan) both resolve before the February tranche. |
| 7 | Caps: ≤10.5% look-through (ICICI ~10.3%) or 9% direct; financials ≤ index-neutral +5pp (~32%; now 29.6%) | Yes (§2, §4) | **The O20 row still says "+3pp, 30%".** |
| 8 | Smaller fixes (Microsoft wording, V/MA blend, NTPC/Bajaj/SBI Life triggers, UCITS tax line, dropped list) | Yes | Yes. Bajaj uses 2 quarters rather than my 4; acceptable. |

**Remaining inconsistency.** The "Response to red-team round 1" table at the top was not updated. It is still headed "v2 response", and five rows contradict the body:
- **O7:** gives the Amazon bear as −22% (the body says −26%).
- **O12:** HDFC Bank, "one-third now" and NIM ≥3.3%.
- **O14:** Maruti gate at 9% with Eicher as the swap.
- **O17:** the reserve clause "or into any holding −15% from cost" appears here but not in the reserve row of §2.
- **O20:** the "+3pp, ~30%" financials cap.

The source line also cites `rt_proposed.py`; the totals now come from `rt_round2.py`. A reader following the top table would apply the wrong HDFC Bank and Maruti rules.

**Fix, with no re-review needed:** either update those five rows and the source line, or label the table "historical; superseded by §2–4". In the reserve row of §2, add "or into any holding −15% from cost with its thesis intact, subject to caps", or delete that clause from O17.

## 2. Final verdicts

| Line | % of total | Verdict |
|---|---|---|
| Nifty 50 index fund | 22.5 | AGREE |
| ICICI Bank | 8.25 (~10.3 look-through) | AGREE |
| NTPC | 6 | AGREE |
| SBI Life | 5.25 | AGREE |
| HDFC Bank | 4.5 | AGREE |
| Reliance | 4.5 | AGREE |
| Bajaj Finance | 3.75 | AGREE |
| Bharti Airtel | 3.75 | AGREE |
| Maruti Suzuki | 3.75 | AGREE |
| Apollo Hospitals | 3.75 | AGREE |
| Indian gold ETF | 3 | AGREE |
| Cash reserve | 6 | AGREE (reconcile the O17 clause, as above) |
| S&P 500 UCITS ETF | 4.75 | AGREE |
| Microsoft | 3.75 | AGREE |
| Visa + Mastercard | 3.5 | AGREE |
| Intuit | 3 | AGREE |
| Medtronic | 2.5 | AGREE |
| Elevance | 2.25 | AGREE |
| Amazon | 2 | AGREE |
| Netflix | 2 | AGREE |
| Uber | 1.25 | AGREE |

No line is CONDITIONAL or REJECT.

## 3. Objections

- **Closed:** O1–O21 and O24.
- **Still open, low severity and not blocking:**
  - **O22:** the Reliance (~25x) and Maruti (~29x) medians are still from memory. Both names are small and event-gated.
  - **O23:** the ICICI CEO-term source is weak.
- **Standing caveats** (data limits that no further review can fix):
  - Prices are 1–7 weeks old: Medtronic, SBI Life and Intuit should be checked live before buying.
  - The Medtronic split-off result is still pending.
  - Intuit's FY28 estimate comes from a single broker.
  - Amazon's clean 2027 EPS is unverified.

## 4. Sign-off

**I sign off on v3 as a whole.** This covers the structure, the names, the weights, the gates, the sell triggers, the caps and the stated edge of ~0–2pp a year. It is conditional only on the documentary fix in §1 before the report is published or shared: correct the five stale rows of the response table (or mark that table as superseded) and reconcile the reserve clause. That fix changes no number or rule in §1–4, so no further red-team round is needed.
