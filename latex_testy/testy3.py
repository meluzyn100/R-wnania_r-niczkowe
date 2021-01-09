from numpy import *
import matplotlib.pyplot as plt
import numpy as np
e=np.e
p0=2
def f(t,a,b,c,d):
    px=(a+c)/(b+d)
    return (p0-px)*e**(-(b+d)*t)+px

x = np.arange(1,10,0.1)

fig, axs = plt.subplots(2,3)
# a,b,c,d=1,1,1,1
# y = [f(i,a,b,c,d) for i in x]
# axs[0,0].plot(x,y)
# axs[0,0].set_title(r"$\alpha$=%a ,$\beta$=%a ,$\gamma$=%a ,$\delta$=%a" %(a,b,c,d) )

a,b,c,d=0,1,0,1
y = [f(i,a,b,c,d) for i in x]
axs[0,0].plot(x,y)
axs[0,0].set_title(r"$\alpha$=%a,$\beta$=%a,$\gamma$=%a,$\delta$=%a" %(a,b,c,d) )

a,b,c,d=1,0,0,1
y = [f(i,a,b,c,d) for i in x]
axs[0,1].plot(x,y)
axs[0,1].set_title(r"$\alpha$=%a,$\beta$=%a,$\gamma$=%a,$\delta$=%a" %(a,b,c,d) )

a,b,c,d=0,0,0.2,0.3
y = [f(i,a,b,c,d) for i in x]
axs[0,2].plot(x,y)
axs[0,2].set_title(r"$\alpha$=%a,$\beta$=%a,$\gamma$=%a,$\delta$=%a" %(a,b,c,d) )

# a,b,c,d=0.2,0.2,0,0
# y = [f(i,a,b,c,d) for i in x]
# axs[0,1].plot(x,y)
# axs[0,1].set_title(r"$\alpha$=%a,$\beta$=%a,$\gamma$=%a,$\delta$=%a" %(a,b,c,d) )

a,b,c,d=4,1,1,1
y = [f(i,a,b,c,d) for i in x]
axs[1,0].plot(x,y)
axs[1,0].set_title(r"$\alpha$=%a,$\beta$=%a,$\gamma$=%a,$\delta$=%a" %(a,b,c,d) )

a,b,c,d = 4,0.1,0.5,1
y = [f(i,a,b,c,d) for i in x]
axs[1,1].plot(x,y)
axs[1,1].set_title(r"$\alpha$=%a,$\beta$=%a,$\gamma$=%a,$\delta$=%a" %(a,b,c,d) )

a,b,c,d = 4,0.1,2,0.2
y = [f(i,a,b,c,d) for i in x]
axs[1,2].plot(x,y)
axs[1,2].set_title(r"$\alpha$=%a,$\beta$=%a,$\gamma$=%a,$\delta$=%a" %(a,b,c,d) )

# a,b,c,d = 0,0.5,0,0.5
# y = [f(i,a,b,c,d) for i in x]
# axs[1,2].plot(x,y)
# axs[1,2].set_title(r"$\alpha$=%a,$\beta$=%a,$\gamma$=%a,$\delta$=%a" %(a,b,c,d) )

# fig.tight_layout(pad=0.1)
fig.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)

# for ax in axs.flat:
    # ax.set(xlabel='Czas', ylabel='Kapitał')
    # ax.ylim(0,10)
# Hide x labels and tick labels for top plots and y ticks for right plots.
# for ax in axs.flat:
#     ax.label_outer()
plt.savefig("lin_mod_gosp.png")
plt.show()

