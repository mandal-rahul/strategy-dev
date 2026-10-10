# Red-team sensitivity tests on the LT models (India + global). Self-contained copies of the inputs.
def ann(x): return (1+x)**(1/3)-1
# ---------------- INDIA ----------------
# name, m0, (g bear,base,bull), (M bear,base,bull), y, weight in India sleeve (invested only)
IN = [
 ("ICICI Bank",2.30,(0.10,0.14,0.17),(2.00,2.63,2.95),0.008,11),
 ("HDFC Bank",1.70,(0.06,0.11,0.14),(1.45,2.05,2.40),0.016,9),
 ("SBI Life",1.98,(0.11,0.15,0.18),(1.70,2.30,2.60),0.002,7),
 ("Bajaj Finance",29.5,(0.12,0.19,0.23),(22.0,32.0,34.5),0.006,6),
 ("Reliance",21.2,(0.05,0.11,0.14),(17.0,23.0,25.0),0.005,9),
 ("Bharti Airtel",27.9,(0.10,0.18,0.22),(20.0,24.0,28.0),0.009,9),
 ("NTPC",10.9,(0.04,0.08,0.10),(9.0,12.2,13.5),0.029,8),
 ("L&T",30.7,(0.06,0.13,0.17),(25.0,30.7,34.0),0.010,8),
 ("Maruti",25.0,(0.03,0.11,0.15),(20.0,27.0,30.0),0.012,8),
 ("Apollo",43.0,(0.13,0.20,0.24),(31.0,38.0,43.0),0.0025,7),
 ("TCS",14.2,(0.01,0.06,0.09),(11.5,14.2,21.0),0.045,6),
]
NIFTY=("Nifty 50",18.3,(0.06,0.11,0.14),(15.5,19.4,20.5),0.013,0)
def tr_in(m0,g,M,y,k,gcut=0.0,flat=False):
    gg=g[k]-gcut; mm=m0 if (flat and k==1) else M[k]
    return (1+gg)**3*(mm/m0)-1 + y*sum((1+gg)**t for t in range(3))
def port(rows,k,**kw):
    W=sum(r[-1] for r in rows); return sum(r[-1]*tr_in(r[1],r[2],r[3],r[4],k,**kw) for r in rows)/W
def report(label,wts,**kw):
    pb=[port(IN,k,**kw) for k in range(3)]; nb=[tr_in(*NIFTY[1:5],k,**kw) for k in range(3)]
    pe=sum(w*x for w,x in zip(wts,pb)); ne=sum(w*x for w,x in zip(wts,nb))
    print(f"{label:58s} picks base {ann(pb[1])*100:5.1f} exp {ann(pe)*100:5.1f} | Nifty base {ann(nb[1])*100:5.1f} exp {ann(ne)*100:5.1f} | edge(exp) {ann(pe)*100-ann(ne)*100:4.1f}pp")
print("INDIA sleeve (invested 88%, weights as in report); weights given as (bear,base,bull)")
report("Report: 25/50/25",(0.25,0.5,0.25))
report("Macro-consistent weights 30/50/20",(0.30,0.5,0.20))
report("30/50/20 + extra 2pp g haircut (picks AND Nifty)",(0.30,0.5,0.20),gcut=0.02)
report("30/50/20 + flat base multiples (picks AND Nifty)",(0.30,0.5,0.20),flat=True)
report("30/50/20 + flat base + 2pp haircut",(0.30,0.5,0.20),flat=True,gcut=0.02)
# Names vs Nifty hurdle under report method
nb=tr_in(*NIFTY[1:5],1)
print("\nIndia names: base pct-per-yr vs Nifty base %.1f (same method)"%(ann(nb)*100))
for r in IN:
    b=tr_in(r[1],r[2],r[3],r[4],1); f=tr_in(r[1],r[2],r[3],r[4],1,flat=True)
    flag = "BELOW/AT hurdle" if ann(b)-ann(nb) < 0.01 else ""
    print(f"  {r[0]:14s} w{r[5]:3d}  base {ann(b)*100:5.1f}  flat-mult {ann(f)*100:5.1f}  {flag}")
# share of India-sleeve invested weight within 1pp of/below hurdle
w_below=sum(r[5] for r in IN if ann(tr_in(r[1],r[2],r[3],r[4],1))-ann(nb)<0.01)
print("  weight at/below hurdle (+1pp): %d of %d invested points"%(w_below,sum(r[5] for r in IN)))
# ---------------- GLOBAL ----------------
# name, pe0, anchor, d, (g base,bear,bull), (pe bear,bull), weight
GL=[("Intuit",12.6,20.0,0.019,(0.13,0.05,0.16),(10.0,20.0),15),
    ("Microsoft",26.4,27.0,0.007,(0.15,0.09,0.18),(20.0,30.0),15),
    ("Visa",25.2,28.0,0.007,(0.12,0.08,0.14),(20.0,29.0),13),
    ("Amazon",25.2,25.0,0.0,(0.17,0.08,0.21),(19.0,30.0),12),
    ("Netflix",18.7,22.0,0.0,(0.15,0.07,0.19),(14.0,25.0),10),
    ("Medtronic",15.6,17.0,0.030,(0.075,0.03,0.09),(13.0,18.0),10),
    ("Elevance",13.6,14.0,0.017,(0.11,0.04,0.13),(10.5,15.5),9),
    ("Uber",15.9,20.0,0.0,(0.17,0.05,0.21),(11.0,22.0),8),
    ("Alphabet",23.4,23.0,0.003,(0.13,0.06,0.17),(17.0,26.0),8)]
def tr_g(pe0,anc,d,g,pe,k,gcut=0.0,anc_mult=1.0,flat=False):
    if k==1:
        pex = pe0 if flat else pe0+0.5*(anc*anc_mult-pe0); gg=g[0]-gcut
    elif k==0: pex=pe[0]; gg=g[1]-gcut
    else: pex=pe[1]; gg=g[2]-gcut
    return (1+gg)**3*(pex/pe0)*(1+d)**3-1
def gport(k,**kw):
    W=sum(r[-1] for r in GL); return sum(r[-1]*tr_g(r[1],r[2],r[3],r[4],r[5],k,**kw) for r in GL)/W
# S&P 500 on the SAME stock method: CY27 fwd 18.65x; ~10y median fwd ~18.5x; consensus-ish CY27-30 g 12% (bottom-up 15.8% CY27)
SPX=("S&P 500",18.65,18.5,0.012,(0.12,0.03,0.14),(15.5,20.0))
def greport(label,wts,**kw):
    pb=[gport(k,**kw) for k in range(3)]; sb=[tr_g(*SPX[1:6],k,**kw) for k in range(3)]
    pe=sum(w*x for w,x in zip(wts,pb)); se=sum(w*x for w,x in zip(wts,sb))
    print(f"{label:58s} picks base {ann(pb[1])*100:5.1f} exp {ann(pe)*100:5.1f} | SPX(same method) base {ann(sb[1])*100:5.1f} exp {ann(se)*100:5.1f} | edge {ann(pe)*100-ann(se)*100:4.1f}pp")
print("\nGLOBAL sleeve (weights as in report, Alphabet included); (bear,base,bull)")
greport("Report: 25/50/25",(0.25,0.5,0.25))
greport("Macro weights 30/50/20",(0.30,0.5,0.20))
greport("30/50/20 + 3pp g haircut (LTG bias; picks AND SPX)",(0.30,0.5,0.20),gcut=0.03)
greport("30/50/20 + 3pp haircut + anchors x0.85 (10y>5%)",(0.30,0.5,0.20),gcut=0.03,anc_mult=0.85)
greport("30/50/20 + 3pp haircut + flat base P/E",(0.30,0.5,0.20),gcut=0.03,flat=True)
print("\nGlobal names base with 3pp haircut + flat P/E:")
for r in GL:
    print(f"  {r[0]:10s} report base {ann(tr_g(*r[1:6],1))*100:5.1f}  haircut+flat {ann(tr_g(*r[1:6],1,gcut=0.03,flat=True))*100:5.1f}  re-rating share of base TR {(tr_g(*r[1:6],1)-tr_g(*r[1:6],1,flat=True))*100:5.0f}pp")
# Harsher AI-bust bears for the capex spenders
print("\nHarsher AI-capex-bust bears (depreciation drag + de-rating):")
for n,pe0,d,g,pe in [("Microsoft",26.4,0.007,0.04,18.0),("Amazon",25.2,0.0,0.03,18.0),("Alphabet",23.4,0.003,0.02,16.0)]:
    x=(1+g)**3*(pe/pe0)*(1+d)**3-1; print(f"  {n:10s} g {g*100:.0f}% exit {pe}x -> {x*100:5.0f}% ({ann(x)*100:5.1f}%/yr)")
# Equalise consensus haircut: Nifty is cut ~4.5pp (15.5->11); picks are cut ~3pp on average. Cut picks a further 1.5pp only.
def report2(label,wts,pick_cut,nifty_cut=0.0,flat=False):
    pb=[port(IN,k,gcut=pick_cut,flat=flat) for k in range(3)]; nb=[tr_in(*NIFTY[1:5],k,gcut=nifty_cut,flat=flat) for k in range(3)]
    pe=sum(w*x for w,x in zip(wts,pb)); ne=sum(w*x for w,x in zip(wts,nb))
    print(f"{label:58s} picks exp {ann(pe)*100:5.1f} | Nifty exp {ann(ne)*100:5.1f} | edge {ann(pe)*100-ann(ne)*100:4.1f}pp")
print("\nIndia, equal-haircut tests (30/50/20):")
report2("picks extra -1.5pp (equal haircut to Nifty)",(0.3,0.5,0.2),0.015)
report2("picks extra -1.5pp, flat base multiples both",(0.3,0.5,0.2),0.015,flat=True)
report2("picks extra -3pp (Indian consensus >=10% too high)",(0.3,0.5,0.2),0.03)
# India sleeve incl. 12% reserve at 6% and total portfolio blend with global at INR drift 1.5%/yr
