import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from numpy import random
random.seed(8)
# imagine we will roll a dice

data=random.multinomial(n=10,pvals=[1/6,1/6,1/6,1/6,1/6,1/6]) # or pvals=[1/6]*6
print(data) # [3 4 2 0 0 1]
"""
1 -> 3 times
2 -> 4 times
3 -> 2 times
4 -> 0 times
5 -> 0 times
6 -> 1 times
"""
data2=random.multinomial(n=10,pvals=[0.2,0.5,0.3],size=7) # repeated 70 times
# for example, they ask 10 people from each of the 7 cities which makeup look they would most like.
print(data2) 
"""
[[0 7 3]
 [2 5 3]
 [2 5 3]
 [2 4 4]
 [3 4 3]
 [2 6 2]
 [5 4 1]]"""
# A continuous probability distribution that models the time it takes for an event to occur
data3=random.exponential(scale=0.5,size=1000)
"""
lambda=2 -> number of events occurring per unit of time
scale = 1/lambda = 1/2 = 0.5"""
sb.histplot(data3,bins=30,kde=True)
plt.xlabel("time")
plt.ylabel("frequency")
plt.title("Exponantial Distribution")
plt.show()