import json
rows=json.load(open("lt_returns.json"))
print("name | base g | flat-multiple base ann | rerating share of base TR")
for r in rows:
    g=r["g"][1] if isinstance(r["g"],list) else eval(r["g"])[1]
    y=r["y"]
    flat=(1+g)**3-1+y*sum((1+g)**t for t in range(3))
    fa=(1+flat)**(1/3)-1
    base=r["res"]["base"]["tr"]
    print(f"{r['name']:22s} {g*100:4.0f}% flat {fa*100:5.1f}%/yr  base {r['res']['base']['ann']*100:5.1f}%/yr  rerating adds {(base-flat)*100:5.0f}pp")
# Nifty benchmark
def tr(g,m0,m1,y):
    p=(1+g)**3*(m1/m0)-1; d=y*sum((1+g)**t for t in range(3)); t=p+d; return t,(1+t)**(1/3)-1
for k,(g,m1) in {"bear":(0.06,15.5),"base":(0.11,19.4),"bull":(0.14,20.5)}.items():
    t,a=tr(g,18.3,m1,0.013); print("Nifty",k,f"{t*100:.0f}% ({a*100:.1f}%/yr)")
