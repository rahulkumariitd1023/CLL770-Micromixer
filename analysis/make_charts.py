# Makes the mixing-index and pressure-drop charts from the COMSOL TABLE 1 / TABLE 2 values.
# Mixing index: M = 1 - sqrt(mean((c-0.5)^2)) / 0.5
import numpy as np, matplotlib.pyplot as plt
M=lambda v:1-np.sqrt(np.array(v))/0.5
sb=[0.23346,0.13689,0.099061,0.065292,0.038417,0.023963]
s4=[0.23469,0.15233,0.10772,0.082402,0.061789,0.053646]
s2=[0.23365,0.16822,0.14696,0.12987,0.11410,0.10347]
xb=[1,900,1600,2300,3000,3399]; x4=[1,700,1500,2100,2800,3199]
# ---- B&W (report)
plt.rcParams.update({"font.size":11,"font.family":"serif"})
fig,ax=plt.subplots(figsize=(7.5,4.5))
ax.plot(np.array(xb)/1000,M(s2),"^:",c="k",mfc="white",lw=1.5,label="Design 2 – straight grooves (90°)")
ax.plot(np.array(x4)/1000,M(s4),"s--",c="k",mfc="white",lw=1.5,label="Design 3 – V-grooves, irregular tip")
ax.plot(np.array(xb)/1000,M(sb),"o-",c="k",lw=2,label="Design 4 – slanted grooves (best)")
ax.plot([3.4],[0.40],"kD",ms=7,label="Design 1 – plain channel, outlet only (0.40)")
ax.set_xlabel("Distance along channel, x (mm)");ax.set_ylabel("Mixing index M");ax.set_ylim(0,0.8);ax.grid(alpha=.3,c="gray");ax.legend(fontsize=9,loc="upper left")
plt.tight_layout();plt.savefig("img/bw_mixing.png",dpi=170);plt.close()
fig,ax=plt.subplots(1,2,figsize=(9,3.6))
names=["Plain\n(1)","Straight\n(2)","V irregular\n(3)","Slanted\n(4)"]
Mo=[0.40,M(s2)[-1],M(s4)[-1],M(sb)[-1]]; pl=[8.5/3.4,7.999/3.4,7.48/3.2,7.93/3.4]; hat=["","//","..","xx"]
for a,vals,yl,yl2 in [(ax[0],Mo,"Outlet mixing index M",.8),(ax[1],pl,"Pressure drop per length (Pa/mm)",3)]:
    b=a.bar(names,vals,color="white",edgecolor="k")
    for r,h,v in zip(b,hat,vals): r.set_hatch(h); a.text(r.get_x()+r.get_width()/2,v+yl2*.02,f"{v:.2f}",ha="center")
    a.set_ylabel(yl);a.set_ylim(0,yl2)
ax[0].set_title("Mixing at outlet",fontsize=11);ax[1].set_title("Pumping cost",fontsize=11)
plt.tight_layout();plt.savefig("img/bw_bars.png",dpi=170);plt.close()
# ---- theme (slides)
NAVY,TEAL,GOLD,GREY,CORAL="#0b2545","#13a89e","#f4a259","#9aa5b1","#e76f51"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":13,"axes.spines.top":False,"axes.spines.right":False})
fig,ax=plt.subplots(figsize=(7.2,4.6))
b=ax.bar(["Plain","Straight\n90°","V-irregular\n(ours)","Slanted\n45°"],Mo,color=[GREY,CORAL,TEAL,GOLD],width=.62)
for r,v in zip(b,Mo): ax.text(r.get_x()+r.get_width()/2,v+.015,f"{v:.2f}",ha="center",fontsize=15,weight="bold")
ax.set_ylabel("Outlet mixing index  M");ax.set_ylim(0,.8);ax.grid(axis="y",alpha=.25)
plt.tight_layout();plt.savefig("img/th_bars.png",dpi=200,transparent=True);plt.close()
fig,ax=plt.subplots(figsize=(7.2,4.6))
ax.plot(np.array(xb)/1000,M(sb),"o-",c=GOLD,lw=3.5,ms=9,label="Slanted 45° (best)")
ax.plot(np.array(x4)/1000,M(s4),"s-",c=TEAL,lw=3,ms=8,label="V-irregular (ours)")
ax.plot(np.array(xb)/1000,M(s2),"^-",c=CORAL,lw=3,ms=8,label="Straight 90°")
ax.plot([3.4],[0.40],"D",c=GREY,ms=11,label="Plain (outlet, est.)")
ax.set_xlabel("Distance along channel  (mm)");ax.set_ylabel("Mixing index  M");ax.set_ylim(0,.8);ax.grid(alpha=.25);ax.legend(frameon=False,fontsize=12,loc="upper left")
plt.tight_layout();plt.savefig("img/th_line.png",dpi=200,transparent=True)
