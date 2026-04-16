
import seaborn as sb
import matplotlib.pyplot as plt
from numpy import random
"""
data=random.chisquare(df=10,size=1000)
print(data)

sb.histplot(data,bins=30,kde=True)
plt.xlabel("value")
plt.ylabel("frequency")
plt.title("Chi Square Distribution")
plt.show()
"""
data=random.rayleigh(scale=2.0,size=1000)
print(data)

sb.histplot(data,bins=30,kde=True)
plt.xlabel("value")
plt.ylabel("frequency")
plt.title("Rayleigh Distribution")
plt.show()