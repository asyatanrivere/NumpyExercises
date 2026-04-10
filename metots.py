import numpy as np
main_array=np.array([42,86,3,23,8])

new_array_copy=main_array.copy()
new_array_copy[0]= 92
print("main array:", main_array) # [42 86  3 23  8]
print("new array with 'copy'", new_array_copy) # [92 86  3 23  8]
print("---------------------")

new_array_view=main_array.view()
new_array_view[0]=56
print("main array:", main_array) # [56 86  3 23  8]
print("new array with 'view':", new_array_view) # [56 86  3 23  8]
print("----------------------------")

print("base method with 'view array:'",new_array_view.base)
print("base method with 'copy array:'",new_array_copy.base)
print("----------------------------")

arr1d=np.array([1,2,3,4])
arr2d=np.array([[1,2,3,4],[5,6,7,8]])
arr3d=np.array([[[1,2,3,4],
                 [5,6,7,8]],

                [[9,10,11,12],
                 [13,14,15,16]]])
print("shape with 1d array:",arr1d.shape) # shape with 1d array: (4,)
print("shape with 2d array:",arr2d.shape) # shape with 2d array: (2, 4)
print("shape with 3d array:",arr3d.shape) # shape with 3d array: (2, 2, 4)
# returns a tuple