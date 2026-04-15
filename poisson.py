import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from numpy import random

# the probability of an event occurring within a given timeframe -> poison

"""
data=random.poisson(lam=3,size=1000)
print(data)

sb.displot(data)
plt.title("POISSON DISTRIBUTION")
plt.show()"""

# every value has an equal probability within a given range -> uniform
"""
data=random.uniform(low=0.0,high=10.0,size=1000)
print(data)

sb.displot(data)
plt.title("UNIFORM DISTRIBUTION")
plt.show()"""


"""
data=random.choice([1,2,3,4,5,6,7,8],size=1000)
print(data)

sb.displot(data,kind="hist")
plt.title("UNIFORM DISTRIBUTION")
plt.show()"""

# logistic distribution

data=random.logistic(loc=0.0,scale=1.0,size=1000)
# scale is not standart deviation -> it is width of distribution
# standart deviation = scale * pi / (root of 3)
print(data)

sb.histplot(data,kde=True)
plt.title("LOGISTIC DISTRIBUTION")
plt.show()
# The end points of the graph are larger than those in a normal distribution.