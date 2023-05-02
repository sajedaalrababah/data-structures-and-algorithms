def reverse_array(array):
    reverse_arr = []
    for i in range(len(array)):
        reverse_arr.append(array[len(array) - 1 - i])
    print(reverse_arr)
    return reverse_arr
   

reverse_array([5, 4, 3, 2, 1])
