# Round 2: re-run v2 sleeves with the CORRECTED per-name inputs v2 quotes (30/50/20 bear/base/bull).
def ann(x): return (1+x)**(1/3)-1
W=(0.30,0.50,0.20)
def tin(m0,g,M,y,k): return (1+g[k])**3*(M[k]/m0)-1 + y*sum((1+g[k])**t for t in range(3))
C=lambda k: (1.06)**3-1   # cash/gold proxy at 6%
IN={
 "Nifty":(18.3,(0.06,0.11,0.14),(15.5,19.4,20.5),0.013),
 "ICICI 2.6x":(2.30,(0.10,0.14,0.17),(2.00,2.45,2.60),0.008),
 "ICICI rep":(2.30,(0.10,0.14,0.17),(2.00,2.63,2.95),0.008),
 "HDFC 1.9x":(1.70,(0.06,0.11,0.14),(1.45,1.90,2.40),0.016),
 "HDFC rep":(1.70,(0.06,0.11,0.14),(1.45,2.05,2.40),0.016),
 "SBI Life RT":(2.08,(0.10,0.135,0.17),(1.70,2.30,2.60),0.002),
 "Bajaj flat":(29.5,(0.12,0.19,0.23),(22.0,29.5,34.5),0.006),
 "Bajaj rep":(29.5,(0.12,0.19,0.23),(22.0,32.0,34.5),0.006),
 "Reliance":(21.2,(0.05,0.11,0.14),(17.0,23.0,25.0),0.005),
 "Bharti":(27.9,(0.10,0.18,0.22),(20.0,24.0,28.0),0.009),
 "NTPC":(10.9,(0.04,0.08,0.10),(9.0,12.2,13.5),0.029),
 "Maruti":(25.0,(0.03,0.11,0.15),(20.0,27.0,30.0),0.012),
 "Apollo":(43.0,(0.13,0.20,0.24),(31.0,38.0,43.0),0.0025),
}
for n in ["Nifty","ICICI 2.6x","HDFC 1.9x","SBI Life RT","Bajaj flat"]:
    print(f"{n:12s} base {ann(tin(*IN[n],1))*100:5.1f} bear {ann(tin(*IN[n],0))*100:5.1f} bull {ann(tin(*IN[n],2))*100:5.1f}")
def sleeve(w):
    tot=sum(w.values()); res=[]
    for k in range(3):
        r=sum(v*(C(k) if n=="cash" else tin(*IN[n],k)) for n,v in w.items()); res.append(r/tot)
    e=sum(p*x for p,x in zip(W,res)); return "bear %.1f base %.1f bull %.1f exp %.1f"%tuple([ann(x)*100 for x in res]+[ann(e)*100])
v2_as_run={"Nifty":30,"ICICI rep":11,"HDFC rep":6,"SBI Life RT":7,"Bajaj rep":5,"Reliance":6,"Bharti":5,"NTPC":8,"Maruti":5,"Apollo":5,"cash":12}
v2_corr={"Nifty":30,"ICICI 2.6x":11,"HDFC 1.9x":6,"SBI Life RT":7,"Bajaj flat":5,"Reliance":6,"Bharti":5,"NTPC":8,"Maruti":5,"Apollo":5,"cash":12}
allidx={"Nifty":88,"cash":12}
print("\nINDIA sleeve (30/50/20)")
print(" v2 as quoted (uncorrected ICICI/HDFC/Bajaj):",sleeve(v2_as_run))
print(" v2 with its OWN corrected per-name inputs :",sleeve(v2_corr))
print(" all-index (88 Nifty + 12 cash)            :",sleeve(allidx))
# picks-only extra 3pp haircut
def sleeve_cut(w,cut):
    tot=sum(w.values()); res=[]
    for k in range(3):
        r=0
        for n,v in w.items():
            if n=="cash": r+=v*C(k)
            elif n=="Nifty": r+=v*tin(*IN[n],k)
            else:
                m0,g,M,y=IN[n]; g2=tuple(x-cut for x in g); r+=v*tin(m0,g2,M,y,k)
        res.append(r/tot)
    e=sum(p*x for p,x in zip(W,res)); return ann(e)*100
print(" corrected, picks -1.5pp (equal haircut): exp %.1f"%sleeve_cut(v2_corr,0.015))
print(" corrected, picks -3pp                  : exp %.1f"%sleeve_cut(v2_corr,0.03))
# GLOBAL
def tg(pe0,anc,d,g,pe,k,flat=False):
    if k==1:
        pex=pe0 if flat else pe0+0.5*(anc-pe0); return (1+g[0])**3*(pex/pe0)*(1+d)**3-1
    if k==0: return (1+g[1])**3*(pe[0]/pe0)*(1+d)**3-1
    return (1+g[2])**3*(pe[1]/pe0)*(1+d)**3-1
GL={"Intuit":(12.6,20.0,0.019,(0.13,0.05,0.16),(10.0,20.0)),
 "MSFT RT":(26.4,27.0,0.007,(0.15,0.04,0.18),(18.0,30.0)),
 "Visa":(25.2,28.0,0.007,(0.12,0.08,0.14),(20.0,29.0)),
 "MA":(24.6,30.0,0.006,(0.13,0.08,0.15),(20.0,30.0)),
 "AMZN 26.5":(26.5,25.0,0.0,(0.17,0.03,0.21),(18.0,30.0)),
 "AMZN 26":(26.0,25.0,0.0,(0.17,0.03,0.21),(18.0,30.0)),
 "AMZN 27":(27.0,25.0,0.0,(0.17,0.03,0.21),(18.0,30.0)),
 "NFLX":(18.7,22.0,0.0,(0.15,0.07,0.19),(14.0,25.0)),
 "MDT":(15.6,17.0,0.030,(0.075,0.03,0.09),(13.0,18.0)),
 "ELV":(13.6,14.0,0.017,(0.11,0.04,0.13),(10.5,15.5)),
 "UBER":(15.9,20.0,0.0,(0.17,0.05,0.21),(11.0,22.0)),
 "SPX":(18.65,19.0,0.012,(0.12,0.03,0.14),(15.5,20.0)),
}
print("\nAmazon base at 26/26.5/27x (g 17%, anchor 25x):",["%.1f"%(ann(tg(*GL[n],1))*100) for n in ["AMZN 26","AMZN 26.5","AMZN 27"]], " bear %.1f"%(ann(tg(*GL["AMZN 26.5"],0))*100))
print("Amazon base at 26.5x with flat P/E: %.1f"%(ann(tg(*GL["AMZN 26.5"],1,flat=True))*100))
print("Intuit flat-P/E base %.1f ; MA base %.1f bear %.1f"%(ann(tg(*GL["Intuit"],1,flat=True))*100, ann(tg(*GL["MA"],1))*100, ann(tg(*GL["MA"],0))*100))
def gs(w,flat_names=()):
    tot=sum(w.values()); res=[sum(v*tg(*GL[n],k,flat=(n in flat_names)) for n,v in w.items())/tot for k in range(3)]
    e=sum(p*x for p,x in zip(W,res)); return "bear %.1f base %.1f bull %.1f exp %.1f"%tuple([ann(x)*100 for x in res]+[ann(e)*100])
v2g_as={"Intuit":12,"MSFT RT":15,"Visa":14,"AMZN 26.5":8,"NFLX":8,"MDT":10,"ELV":9,"UBER":5,"SPX":19}
v2g_split={"Intuit":12,"MSFT RT":15,"Visa":7,"MA":7,"AMZN 26.5":8,"NFLX":8,"MDT":10,"ELV":9,"UBER":5,"SPX":19}
print("\nGLOBAL sleeve (30/50/20)")
print(" v2 as quoted (Visa only, Intuit re-rated):",gs(v2g_as))
print(" V/MA split, Intuit re-rated             :",gs(v2g_split))
print(" V/MA split, Intuit FLAT (v2 headline)   :",gs(v2g_split,flat_names=("Intuit",)))
print(" all S&P UCITS                           :",gs({"SPX":1}))
