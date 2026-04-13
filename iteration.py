import numpy as np

main_array=np.array([[1,2,3],[4,5,6],[7,8,9]])
other_main_array=np.array([1,2,3,4,5,6,7,8,9])

for column in other_main_array:
    print(column, end=" ") # 1 2 3 4 5 6 7 8 9 
print("\n-----------------")
for item in main_array:
    print(item) # but we couldn't reach the value of items
for column in main_array:
    for row in column:
        print(row, end=" ") # 1 2 3 4 5 6 7 8 9
    print() # to move to the next row
print("-----------------------")

my_3d_array=np.array([[[1,2,3],
                       [4,5,6]],

                       [[7,8,9],
                        [10,11,12]],

                        [[13,14,15],
                         [16,17,18]]])

for item in my_3d_array:
    print(item)

print()

for matrix in my_3d_array:
    for column in matrix:
        for row in column:
            print(row, end=" ")
        print()
    print()
print("WITH 'NDITER' FUNCION:")
for item in np.nditer(my_3d_array):
    print(item) # reaches every value in array
print("------------------------------")

print("TYPE CHANGE")

my_1d_arr=np.array([14,0,49,98,33,0,29])

for item in np.nditer(my_1d_arr,flags=["buffered"],op_dtypes=["S"]):
    print(item) # transfered bytes string and returns

for item in np.nditer(my_1d_arr, flags=["buffered"], op_dtypes=[np.bool_],casting="unsafe"):
    print(item, end=" ") # True True False True True True False True
print("-----------------------------")

my_2d_array=np.array([[1,2,3],
                      [4,5,6],
                      [7,8,9]])
for item in np.nditer(my_2d_array[:,1:]):
    print(item, end=" ") # 2 3 5 6 8 9

for index_,value_ in np.ndenumerate(my_2d_array):
    print(index_,value_) # returns indexes as tuples and values in array