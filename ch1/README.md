# Challenge Title : array-reverse

Create function called reverseArray which takes an array as an argument. Without utilizing any of the built-in methods available in python language, return an array with elements in reversed order.

#Whiteboard
![code Challenge 01](./Untitled.jpg "reversArray")

## Approach & Efficiency
1- Calculate the length n of the input array arr.
2- Calculate the index of the middle element of the array arr using integer division (//) and the modulo operator (%). If the length of the array is even, the middle index will be n // 2, where n is the length of the array. If the length of the array is odd, the middle index will be (n // 2) + (n % 2).
3-Create a new array shifted with an additional element to accommodate the new value.



## Solution

``` python
def reverse_array(array):
    reverse_arr = []
    for i in range(len(array)):
        reverse_arr.append(array[len(array) - 1 - i])
    print(reverse_arr)
    return reverse_arr
   

reverse_array([5, 4, 3, 2, 1])
```
