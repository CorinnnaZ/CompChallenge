# probablly not a necessary section
# just as a test to how plotting stuff works and it's incredibly easy
import matplotlib.pyplot as plt
import random
inp = random.randint(60, 100)
x = [i for i in range(int(inp))]
y = [(i)**2 for i in x]

x2 = [i for i in range(inp)]
y2 = [i**1.5 for i in x2]


plt.scatter(x,y, label ='x^2', s=1)
plt.plot(x2, y2, label = "x^1.5")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Title")
plt.show()
