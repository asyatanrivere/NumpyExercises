import numpy as np
from numpy import random
import seaborn as sb
import matplotlib.pyplot as plt

"""
random.seed(8)
arr=random.normal(loc=5,scale=10,size=1000)
# loc is mean
# scale is standard deviation

print(arr)

sb.displot(arr,kind="kde")
plt.title("normal distribution")
plt.show()"""



"""
random.seed(8)
data=random.binomial(n=10,p=0.5,size=1000)

print(data)

sb.displot(data)
plt.title("binomial distribution")
plt.show()"""



"""
random.seed(8)
data=random.binomial(n=10,p=0.2,size=1000)

print(data)

sb.displot(data)
plt.title("binomial distribution")
plt.show()"""

data={
    "binomial":random.binomial(n=10,p=0.5,size=1000),
    "normal":random.normal(loc=5,scale=1,size=1000)
}

sb.displot(data,kind="kde")
plt.title("difference between binomial and normal distribution")
plt.show()