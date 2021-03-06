import matplotlib.pyplot as plt
plt.plot(((0,0),(2,2)))
plt.plot(((0,2),(2,0)),color="black")
plt.xlabel("Cena",fontsize=15)
plt.ylabel("Ilość towaru  ",fontsize=15)
plt.tick_params(labelbottom=False)
plt.tick_params(labelleft=False)
plt.text(0.5,1.1,r"$P^*$",fontsize=15)
plt.text(0.8,0.45,"D",fontsize=15)
plt.text(0.8,1.7,"S",fontsize=15)
plt.savefig("punkt_równowagi.png")
plt.show()
