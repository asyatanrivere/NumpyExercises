import numpy as np

x=[26,7,55,63]
y=[14,98,44,26]
z=[]

for i,j in zip(x,y):
    z.append(i+j)
print(z)
print("------------------------------------------------")
xnp=np.array([23,7,5,23])
ynp=np.array([3,15,1,8])

print("function for addition:",np.add(xnp,ynp)) #  [26 22  6 31]
print("function for subtraction:",np.subtract(xnp,ynp)) # [20 -8  4 15]
print("function for multiplication:",np.multiply(xnp,ynp)) #  [ 69 105   5 184]
print("function for division:",np.divide(xnp,ynp)) # [7.66666667 0.46666667 5.         2.875     ]
print("function for true division:",np.true_divide(xnp,ynp)) #  [7.66666667 0.46666667 5.         2.875     ]
print("function for floor division:",np.floor_divide(xnp,ynp)) # [7 0 5 2]
print("function for exponents:",np.power(xnp,ynp)) # [        12167 4747561509943             5   78310985281]
print("function for float power:",np.float_power(xnp,ynp)) 
# [1.21670000e+04 4.74756151e+12 5.00000000e+00 7.83109853e+10]
print("function for remainder with 'mod':",np.mod(xnp,ynp)) # [2 7 0 7]
print("function for remainder with 'remainder':",np.remainder(xnp,ynp)) # [2 7 0 7]
print()
forsquare=np.array([3,5,12,8,1])
print("numbers to square:",forsquare) # [ 3  5 12  8  1]
print("squared numbers:",np.square(forsquare)) # [  9  25 144  64   1]
print()
forsqrt=np.array([121,9,169,100,36,64])
print("numbers to take root:",forsqrt) # [121   9 169 100  36  64]
print("rooted numbers:",np.sqrt(forsqrt)) # [11.  3. 13. 10.  6.  8.]
print()
forcbrt=np.array([8,27,1000,125,729])
print("numbers to take cube root:",forcbrt) # [   8   27 1000  125  729]
print("cube rooted numbers:",np.cbrt(forcbrt)) # [ 2.  3. 10.  5.  9.]
print()
forabs=np.array([-32,-53,-5])
print("negative numbers:",forabs) # [-32 -53  -5]
print("after the absolute values are taken with 'abs':",np.abs(forabs)) #  [32 53  5]
print("after the absolute values are taken with 'absolute':",np.absolute(forabs)) #  [32 53  5]
print()
forfloatabs=np.array([-32.834,-53.835,-5.227])
print("float negative numbers:",forfloatabs) # [-32.834 -53.835  -5.227]
print("after the absolute values are taken with 'fabs':",np.fabs(forfloatabs)) #  [32.834 53.835  5.227]
print()
forsign=np.array([42,0,-62])
print("numbers:",forsign) # [ 42   0 -62]
print("sign of numbers",np.sign(forsign)) # [ 1  0 -1]
print()
forreciprocal=np.array([2,8,14],dtype=float)
print("numbers:",forreciprocal) # [ 2.  8. 14.]
print("reciprocal of numbers",np.reciprocal(forreciprocal)) # [0.5        0.125      0.07142857]
print()
fornegative=np.array([42,0,-62])
print("numbers:",fornegative) # [ 42   0 -62]
print("sign of numbers",np.negative(fornegative)) # [-42   0  62]
print()
quotient=np.array([20,42,63,4,77])
divisor=np.array([4,7,5,2,12])
print(np.divmod(quotient,divisor)) # (array([ 5,  6, 12,  2,  6]), array([0, 0, 3, 0, 5]))
