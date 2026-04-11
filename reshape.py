import numpy as np

original_array=np.array([10,20,30,40,50,60,70,80,90,100,110,120])

new_array=original_array.reshape(4,3)
print(new_array) # [[ 10  20  30]
                #[ 40  50  60]
                #[ 70  80  90]
                #[100 110 120]]
print(new_array.base) # [ 10  20  30  40  50  60  70  80  90 100 110 120]
# reshape is a view
print("-------------------------------")

new_array2=new_array.reshape(2,2,3)
print(new_array2)
print("---------------------")

new_array3=original_array.reshape(2,-1) # numpy calculates the the vavlue for "-1"
print(new_array3) # [[ 10  20  30  40  50  60]
                  # [ 70  80  90 100 110 120]]
print("----------------------")

new_array4=new_array3.reshape(-1) # one dimendional array
print(new_array4) # [ 10  20  30  40  50  60  70  80  90 100 110 120]
print("----------------------------")

diagonal_array=np.eye(4)
not_diagonal=diagonal_array.flatten() 
print("my diagonal array:\n",diagonal_array)
print("diagonal array with 'flatten':",not_diagonal)
print(not_diagonal.base) # IT IS A COPY
print("------------------------------")

the_arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
my_the_arr=the_arr.ravel() # same with flatten as funcionality
                           # but it is VIEW
print(my_the_arr)
print(the_arr)
my_the_arr[0]=211
print(my_the_arr)
print(the_arr) # their first elements are 211, it not a copy, VIEW
print("----------------------------")

big_arr=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(big_arr)
# they are not usable for one dimasional arrays
print(np.flip(big_arr,axis=0))
print(np.flipud(big_arr)) # flip up down
print(np.flip(big_arr, axis=1))
print(np.fliplr(big_arr)) # flip left right
print("-----------------------------")
print(big_arr)
print(big_arr.T) # transpose