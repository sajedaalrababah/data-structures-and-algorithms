def reverse_array(array):
    reverse_array = []
    for i in range(len(array)):
        reverse_array.append(array[len(array) - 1 - i])
    return reverse_array

reverse_array([5, 4, 3, 2, 1]) # return [1, 2, 3, 4, 5]
