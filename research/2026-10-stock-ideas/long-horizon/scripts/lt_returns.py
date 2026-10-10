# 3-year expected return model: TR = (1+g)^3 * (M_exit/M_now) - 1 + dividends
# dividends = yield * sum_{t=0..2}(1+g)^t  (paid on initial price, growing with EPS, not reinvested)
# scenario weights: bear 25 / base 50 / bull 25
# post-tax: LTCG 12.5% on price gain (ignores the Rs1.25 lakh exemption), dividends at 31.2% slab (30% + 4% cess)
import json
C = [
 # name, metric, M_now, median_ref, (g_bear,g_base,g_bull), (M_bear,M_base,M_bull), yield, consensus_g_label
 ("ICICI Bank","fwd P/B",2.30,2.95,(0.10,0.14,0.17),(2.00,2.63,2.95),0.008,"16% PAT (MOSL FY26-28)"),
 ("HDFC Bank","fwd P/B",1.70,2.40,(0.06,0.11,0.14),(1.45,2.05,2.40),0.016,"14-15% (MOSL/Emkay FY26-28)"),
 ("SBI","P/E FY26",11.1,11.0,(0.04,0.09,0.12),(8.5,11.0,13.0),0.017,"8-11% (MOSL/AR/JM FY26-28)"),
 ("TCS","fwd P/E",14.2,28.4,(0.01,0.06,0.09),(11.5,14.2,21.0),0.045,"~6-8% INR (FY28E Rs164)"),
 ("Infosys","fwd P/E",13.3,25.0,(0.00,0.05,0.08),(11.0,13.3,19.0),0.047,"~6-8% (FY27E ~Rs77)"),
 ("NTPC","P/E TTM",10.9,13.5,(0.04,0.08,0.10),(9.0,12.2,13.5),0.029,"7-10% (PL/Nuvama/HSIE FY26-28)"),
 ("Power Grid","P/E TTM",15.0,12.5,(0.04,0.07,0.10),(11.0,13.75,15.0),0.036,"~15% (I-Sec FY28E Rs21.9, Feb-26)"),
 ("Reliance","P/E TTM",21.2,25.0,(0.05,0.11,0.14),(17.0,23.0,25.0),0.005,"~11% PAT; 18% EBITDA (MOSL)"),
 ("Maruti Suzuki","P/E TTM",25.0,29.0,(0.03,0.11,0.15),(20.0,27.0,30.0),0.012,"~13-20% (FY28E Rs548-656)"),
 ("Larsen & Toubro","P/E TTM",30.7,34.4,(0.06,0.13,0.17),(25.0,30.7,34.0),0.010,"~15-18% (guide +10-12% rev)"),
 ("SBI Life","P/EV (Jun-26 EV)",1.98,2.6,(0.11,0.15,0.18),(1.70,2.30,2.60),0.002,"EV +15% (Q1)"),
 ("HDFC Life","P/EV (Jun-26 EV)",1.80,2.4,(0.09,0.12,0.14),(1.50,2.10,2.60),0.004,"EV +13%, VNB +9% (Q1)"),
 ("HDFC AMC","P/E TTM",30.0,35.0,(0.05,0.12,0.17),(23.0,32.5,38.0),0.023,"PAT +12% (Q1)"),
 ("Bajaj Finance","P/E TTM",29.5,34.5,(0.12,0.19,0.23),(22.0,32.0,34.5),0.006,"PAT +23-24% (guide)"),
 ("Bharti Airtel","fwd P/E FY27E",27.9,None,(0.10,0.18,0.22),(20.0,24.0,28.0),0.009,"FY27-28 +28% (Rs63.9->81.7)"),
 ("Titan","fwd P/E FY27E",62.0,85.0,(0.09,0.17,0.22),(40.0,50.0,60.0),0.003,"~20%+ (FY28E Rs86.1)"),
 ("Trent","fwd P/E FY27E",70.0,110.0,(0.14,0.22,0.27),(40.0,55.0,65.0),0.001,"~22-25%"),
 ("Mahindra & Mahindra","fwd P/E FY27E",22.2,20.0,(0.06,0.13,0.16),(17.0,21.1,25.0),0.008,"14.5% (FY27-28 Rs139->159)"),
 ("Bajaj Auto","fwd P/E",25.0,19.0,(0.07,0.14,0.17),(18.0,22.0,25.0),0.018,"~15%"),
 ("Eicher Motors","P/E TTM",35.0,33.0,(0.06,0.13,0.17),(26.0,34.0,36.0),0.012,"~15%"),
 ("Apollo Hospitals","fwd P/E FY27E",43.0,75.0,(0.13,0.20,0.24),(31.0,38.0,43.0),0.0025,"24% PAT (Antique/Choice)"),
 ("Max Healthcare","fwd P/E FY27E",52.0,None,(0.12,0.20,0.25),(32.0,42.0,50.0),0.0015,"~25% EBITDA"),
 ("Sun Pharma","P/E TTM",34.7,33.0,(0.05,0.13,0.18),(24.0,30.0,35.0),0.010,"11% organic (MOSL) + Organon"),
 ("Bharat Electronics","fwd P/E FY27E",40.0,33.0,(0.09,0.14,0.18),(25.0,32.0,40.0),0.007,"~15% (FY28E Rs11)"),
 ("Polycab","P/E TTM",43.0,38.0,(0.10,0.17,0.20),(27.0,35.0,43.0),0.0045,"18% (FY26-29)"),
 ("ITC","P/E TTM",17.0,24.0,(-0.02,0.04,0.07),(14.0,17.0,20.5),0.056,"5% (Emkay 3-yr)"),
]
rows=[]
for n,met,m0,med,g,M,y,cons in C:
    res={}
    for k,(gg,mm) in zip(("bear","base","bull"),zip(g,M)):
        price=(1+gg)**3*(mm/m0)-1
        div=y*sum((1+gg)**t for t in range(3))
        tr=price+div
        ann=(1+tr)**(1/3)-1
        post=price*(1-0.125 if price>0 else 1)+div*(1-0.312)
        pann=(1+post)**(1/3)-1
        res[k]=dict(tr=tr,ann=ann,price=price,div=div,post_ann=pann)
    exp_tr=0.25*res["bear"]["tr"]+0.5*res["base"]["tr"]+0.25*res["bull"]["tr"]
    exp_ann=(1+exp_tr)**(1/3)-1
    spread=(res["bull"]["ann"]-res["bear"]["ann"])/2
    rows.append(dict(name=n,metric=met,m0=m0,med=med,g=g,M=M,y=y,cons=cons,res=res,exp_tr=exp_tr,exp_ann=exp_ann,spread=spread,ratio=exp_ann/spread))
rows.sort(key=lambda r:-r["ratio"])
print(f"{'name':22s} {'bear':>14s} {'base':>14s} {'bull':>14s} {'exp':>13s} {'basePT':>7s} {'ratio':>6s}")
for r in rows:
    b,m,u=r["res"]["bear"],r["res"]["base"],r["res"]["bull"]
    print(f"{r['name']:22s} {b['tr']*100:6.0f}% ({b['ann']*100:5.1f}) {m['tr']*100:6.0f}% ({m['ann']*100:5.1f}) {u['tr']*100:6.0f}% ({u['ann']*100:5.1f}) {r['exp_tr']*100:5.0f}% ({r['exp_ann']*100:4.1f}) {m['post_ann']*100:6.1f} {r['ratio']:6.2f}")
json.dump(rows,open("/tmp/claude-0/-home-user-strategy-dev/039bb5b6-f32b-5555-8e98-35ba2adb1428/scratchpad/scripts/lt_returns.json","w"),indent=1,default=str)
