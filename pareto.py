import seaborn as sb
import matplotlib.pyplot as plt
from numpy import random

"""
xm=1.0 # initial point
data=(random.pareto(9.0,1000)+1)*xm # (pareto(a, size)+1)*xm
print(data)

sb.histplot(data,bins=40, kde=True)
plt.title("Pareto Distribution (p=9.0)")
plt.xlabel("value")
plt.ylabel("frequency")
plt.show()"""

data=random.zipf(2.0,1000)
data=data[data<20]

sb.histplot(data,bins=range(1,21),discrete=True)
plt.xlabel=("value")
plt.ylabel=("rank")
plt.title=("Zipf Distribution (a=2.0)")
plt.show()