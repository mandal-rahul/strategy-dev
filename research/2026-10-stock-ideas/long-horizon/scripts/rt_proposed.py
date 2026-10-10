# Compare report weights vs red-team proposed weights, 30/50/20 (bear/base/bull), report inputs unless noted.
def ann(x): return (1+x)**(1/3)-1
W=(0.30,0.50,0.20)
def tin(m0,g,M,y,k): return (1+g[k])**3*(M[k]/m0)-1 + y*sum((1+g[k])**t for t in range(3))
IN={"ICICI":(2.30,(0.10,0.14,0.17),(2.00,2.63,2.95),0.008),
 "HDFC Bank":(1.70,(0.06,0.11,0.14),(1.45,2.05,2.40),0.016),
 "SBI Life":(1.98,(0.11,0.15,0.18),(1.70,2.30,2.60),0.002),
 "SBI Life (RT: EV 13.5%, px 1770 -> 2.08x)":(2.08,(0.10,0.135,0.17),(1.70,2.30,2.60),0.002),
 "Bajaj Fin":(29.5,(0.12,0.19,0.23),(22.0,32.0,34.5),0.006),
 "Reliance":(21.2,(0.05,0.11,0.14),(17.0,23.0,25.0),0.005),
 "Bharti":(27.9,(0.10,0.18,0.22),(20.0,24.0,28.0),0.009),
 "NTPC":(10.9,(0.04,0.08,0.10),(9.0,12.2,13.5),0.029),
 "L&T":(30.7,(0.06,0.13,0.17),(25.0,30.7,34.0),0.010),
 "Maruti":(25.0,(0.03,0.11,0.15),(20.0,27.0,30.0),0.012),
 "Apollo":(43.0,(0.13,0.20,0.24),(31.0,38.0,43.0),0.0025),
 "TCS":(14.2,(0.01,0.06,0.09),(11.5,14.2,21.0),0.045),
 "Nifty 50 fund":(18.3,(0.06,0.11,0.14),(15.5,19.4,20.5),0.013),
 "HDFC AMC (RT: 33.7x)":(33.7,(0.05,0.12,0.17),(23.0,32.5,38.0),0.022),
 "ICICI (RT: anchor 2.6x)":(2.30,(0.10,0.14,0.17),(2.00,2.45,2.60),0.008),
 "HDFC Bank (RT: exit 1.9x)":(1.70,(0.06,0.11,0.14),(1.45,1.90,2.40),0.016),
}
for k in ["SBI Life (RT: EV 13.5%, px 1770 -> 2.08x)","HDFC AMC (RT: 33.7x)","ICICI (RT: anchor 2.6x)","HDFC Bank (RT: exit 1.9x)"]:
    m0,g,M,y=IN[k]; print(f"{k:45s} base {ann(tin(m0,g,M,y,1))*100:5.1f}%/yr  bear {ann(tin(m0,g,M,y,0))*100:5.1f}")
def sleeve(wts,cash=0.06):
    tot=sum(wts.values()); res=[]
    for k in range(3):
        r=sum(w*tin(*IN[n],k) for n,w in wts.items() if n!="cash")
        r+= wts.get("cash",0)*((1+cash)**3-1)
        res.append(r/tot)
    e=sum(p*x for p,x in zip(W,res)); return [ann(x)*100 for x in res]+[ann(e)*100]
rep={"ICICI":11,"HDFC Bank":9,"SBI Life":7,"Bajaj Fin":6,"Reliance":9,"Bharti":9,"NTPC":8,"L&T":8,"Maruti":8,"Apollo":7,"TCS":6,"cash":12}
prop={"ICICI":11,"HDFC Bank":6,"SBI Life (RT: EV 13.5%, px 1770 -> 2.08x)":7,"Bajaj Fin":5,"Reliance":6,"Bharti":5,"NTPC":8,"Maruti":5,"Apollo":5,"Nifty 50 fund":30,"cash":12}
print("\nINDIA sleeve incl. reserve @6%  [bear, base, bull, expected 30/50/20]")
print(" report  ",["%.1f"%x for x in sleeve(rep)])
print(" proposed",["%.1f"%x for x in sleeve(prop)])
print(" all-index (88 Nifty + 12 cash)",["%.1f"%x for x in sleeve({"Nifty 50 fund":88,"cash":12})])
# Look-through financials (Nifty ~36% financials incl. ICICI ~8%, HDFC ~12%? assume 36%)
fin_rep=(11+9+7+6)*0.75; fin_prop=(11+6+7+5+30*0.36)*0.75
print(f" look-through Indian financials as % of TOTAL: report {fin_rep:.1f}  proposed {fin_prop:.1f}")
# GLOBAL
def tg(pe0,anc,d,g,pe,k):
    if k==1: return (1+g[0])**3*((pe0+0.5*(anc-pe0))/pe0)*(1+d)**3-1
    if k==0: return (1+g[1])**3*(pe[0]/pe0)*(1+d)**3-1
    return (1+g[2])**3*(pe[1]/pe0)*(1+d)**3-1
GL={"Intuit":(12.6,20.0,0.019,(0.13,0.05,0.16),(10.0,20.0)),
 "Microsoft":(26.4,27.0,0.007,(0.15,0.09,0.18),(20.0,30.0)),
 "Microsoft (RT bear)":(26.4,27.0,0.007,(0.15,0.04,0.18),(18.0,30.0)),
 "Visa":(25.2,28.0,0.007,(0.12,0.08,0.14),(20.0,29.0)),
 "Amazon":(25.2,25.0,0.0,(0.17,0.08,0.21),(19.0,30.0)),
 "Amazon (RT: 26.5x clean, bear)":(26.5,25.0,0.0,(0.17,0.03,0.21),(18.0,30.0)),
 "Netflix":(18.7,22.0,0.0,(0.15,0.07,0.19),(14.0,25.0)),
 "Medtronic":(15.6,17.0,0.030,(0.075,0.03,0.09),(13.0,18.0)),
 "Elevance":(13.6,14.0,0.017,(0.11,0.04,0.13),(10.5,15.5)),
 "Uber":(15.9,20.0,0.0,(0.17,0.05,0.21),(11.0,22.0)),
 "Alphabet":(23.4,23.0,0.003,(0.13,0.06,0.17),(17.0,26.0)),
 "Alphabet (RT bear)":(23.4,23.0,0.003,(0.13,0.02,0.17),(16.0,26.0)),
 "S&P 500 UCITS (same method)":(18.65,19.0,0.012,(0.12,0.03,0.14),(15.5,20.0)),
}
def gs(wts):
    tot=sum(wts.values()); res=[sum(w*tg(*GL[n],k) for n,w in wts.items())/tot for k in range(3)]
    e=sum(p*x for p,x in zip(W,res)); return [ann(x)*100 for x in res]+[ann(e)*100]
grep={"Intuit":15,"Microsoft":15,"Visa":13,"Amazon":12,"Netflix":10,"Medtronic":10,"Elevance":9,"Uber":8,"Alphabet":8}
grep_rtbears={"Intuit":15,"Microsoft (RT bear)":15,"Visa":13,"Amazon (RT: 26.5x clean, bear)":12,"Netflix":10,"Medtronic":10,"Elevance":9,"Uber":8,"Alphabet (RT bear)":8}
gprop={"Intuit":12,"Microsoft (RT bear)":15,"Visa":14,"Amazon (RT: 26.5x clean, bear)":8,"Netflix":8,"Medtronic":10,"Elevance":9,"Uber":5,"S&P 500 UCITS (same method)":19}
print("\nGLOBAL sleeve USD [bear, base, bull, expected 30/50/20]")
print(" report weights, report bears ",["%.1f"%x for x in gs(grep)])
print(" report weights, RT AI-bust bears",["%.1f"%x for x in gs(grep_rtbears)])
print(" proposed (RT bears)           ",["%.1f"%x for x in gs(gprop)])
print(" all S&P UCITS                 ",["%.1f"%x for x in gs({"S&P 500 UCITS (same method)":1})])
