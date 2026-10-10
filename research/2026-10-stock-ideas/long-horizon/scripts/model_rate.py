# 3-year USD expected-return model (Oct 2026 -> ~Oct/Dec 2029)
# TR_3y = (1+g)^3 * (PE_exit/PE_now) * (1+d)^3 - 1   (dividends reinvested; buybacks are inside per-share g)
# g = expected EPS CAGR over the 3 years AFTER the forward-P/E year (FY27->FY30 approx.)
# Base PE_exit = PE_now + 0.5*(anchor - PE_now)   ("halfway to anchor")
# anchor = ~10y median forward P/E, or an explicit regime-adjusted anchor (flagged R)
# Bear/Bull: explicit g and PE_exit per name
# Expected = 0.5*base + 0.25*bear + 0.25*bull (annualised); Score = E - 0.5*max(0,-bear_ann)
import math
names = [
# name, pe_now, anchor, regime_flag, d, g_base, g_bear, pe_bear, g_bull, pe_bull
("Intuit",            12.6, 20.0, "R", 0.019, 0.13, 0.05, 10.0, 0.16, 20.0),
("Adobe (non-GAAP)",   9.2, 15.0, "R", 0.000, 0.08, 0.02,  7.5, 0.11, 15.0),
("Uber (adj.)",       15.9, 20.0, "R", 0.000, 0.17, 0.05, 11.0, 0.21, 22.0),
("Netflix",           18.7, 22.0, "R", 0.000, 0.15, 0.07, 14.0, 0.19, 25.0),
("TSMC ADR",          21.0, 20.0, "",  0.010, 0.14, 0.02, 15.0, 0.20, 24.0),
("Elevance",          13.6, 14.0, "",  0.017, 0.11, 0.04, 10.5, 0.13, 15.5),
("TotalEnergies (norm.)",12.0, 11.5, "",  0.046, 0.05,-0.02, 10.0, 0.18,  9.0),
("UnitedHealth",      17.1, 18.0, "",  0.023, 0.12, 0.04, 13.0, 0.15, 19.0),
("Alphabet (clean)",  23.4, 23.0, "",  0.003, 0.13, 0.06, 17.0, 0.17, 26.0),
("Microsoft",         26.4, 27.0, "",  0.007, 0.15, 0.09, 20.0, 0.18, 30.0),
("Amazon (clean)",    25.2, 25.0, "R", 0.000, 0.17, 0.08, 19.0, 0.21, 30.0),
("Meta (clean)",      21.8, 21.0, "",  0.003, 0.13, 0.05, 16.0, 0.17, 25.0),
("Salesforce (clean)",16.1, 20.0, "R", 0.007, 0.09, 0.03, 12.0, 0.12, 22.0),
("Visa",              25.2, 28.0, "",  0.007, 0.12, 0.08, 20.0, 0.14, 29.0),
("Mastercard",        24.6, 30.0, "",  0.006, 0.13, 0.08, 20.0, 0.15, 30.0),
("ASML ADR",          31.0, 30.0, "",  0.012, 0.11, 0.00, 22.0, 0.16, 34.0),
("Medtronic",         15.6, 17.0, "",  0.030, 0.07, 0.03, 13.0, 0.09, 18.0),
("Novo Nordisk ADR",   9.7, 13.0, "R", 0.045, 0.02,-0.05,  8.0, 0.07, 15.0),
("Berkshire (P/B)",    1.45, 1.45,"",  0.000, 0.085,0.05,  1.25,0.10, 1.60),
("Booking",           16.5, 20.0, "",  0.008, 0.12, 0.05, 12.0, 0.15, 21.0),
("Nvidia",            14.5, 20.0, "R", 0.000, 0.05,-0.15, 18.0, 0.17, 22.0),
]
def tr(g,pe0,pe1,d):
    return (1+g)**3*(pe1/pe0)*(1+d)**3-1
def ann(x): return (1+x)**(1/3)-1
rows=[]
for n,pe0,anc,fl,d,gb,gr,per,gu,peu in names:
    pe_base = pe0+0.5*(anc*0.85-pe0)
    b=tr(gb,pe0,pe_base,d); r=tr(gr,pe0,per,d); u=tr(gu,pe0,peu,d)
    ba,ra,ua=ann(b),ann(r),ann(u)
    e=0.5*ba+0.25*ra+0.25*ua
    score=e-0.5*max(0,-ra)
    rows.append((n,pe0,anc,fl,pe_base,d,gb,b,r,u,ba,ra,ua,e,score))
rows.sort(key=lambda x:-x[-1])
print(f"{'name':20s} {'PE0':>5} {'anc':>5} {'PEb':>5} {'d':>5} {'g':>5} | {'base3y':>7} {'bear3y':>7} {'bull3y':>7} | {'base/y':>6} {'bear/y':>6} {'bull/y':>6} | {'E/y':>6} {'score':>6}")
for n,pe0,anc,fl,peb,d,gb,b,r,u,ba,ra,ua,e,s in rows:
    print(f"{n:20s} {pe0:5.1f} {anc:5.1f}{fl:1s}{peb:5.1f} {d*100:5.1f} {gb*100:5.1f} | {b*100:7.0f} {r*100:7.0f} {u*100:7.0f} | {ba*100:6.1f} {ra*100:6.1f} {ua*100:6.1f} | {e*100:6.1f} {s*100:6.1f}")
