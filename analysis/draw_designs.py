# Draws the top view of the four channel floors (plain, straight, V-irregular, slanted).
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle
W,GW,P,LIN,GAP=200,50,100,200,100
plt.rcParams["font.family"]="serif"
def chan(ax,L,title):
    ax.add_patch(Rectangle((0,0),L,W,fc="white",ec="k",lw=1.2));ax.set_xlim(-20,3420);ax.set_ylim(-20,250);ax.set_aspect("equal");ax.axis("off")
    ax.text(0,225,title,fontsize=13,weight="bold",va="bottom")
fig,axs=plt.subplots(4,1,figsize=(13,7.2))
chan(axs[0],3400,"1. Plain channel")
chan(axs[1],3400,"2. Straight grooves (90°)")
x=LIN
for k in range(4):
    for i in range(6): axs[1].add_patch(Rectangle((x+i*P,0),GW,W,fc="0.3"))
    x+=6*P+GAP
chan(axs[2],3200,"3. V-grooves, irregular tip (our design)")
x=LIN
for a_,n in zip([.25,.67,.40,.75],[4,7,5,6]):
    a=a_*W
    for i in range(n):
        x0=x+i*P; axs[2].add_patch(Polygon([(x0+a,0),(x0,a),(x0+W-a,W),(x0+W-a+GW,W),(x0+GW,a),(x0+a+GW,0)],fc="0.3"))
    x+=n*P+GAP
chan(axs[3],3400,"4. Slanted grooves (45°)")
x=LIN
for k in range(4):
    for i in range(6):
        x0=x+i*P; axs[3].add_patch(Polygon([(x0,0),(x0+W,W),(x0+W+GW,W),(x0+GW,0)],fc="0.3"))
    x+=6*P+GAP
axs[3].annotate("flow →",(3300,-15),ha="right",va="top",fontsize=11)
plt.tight_layout();plt.savefig("img/designs4_topview.png",dpi=160)
