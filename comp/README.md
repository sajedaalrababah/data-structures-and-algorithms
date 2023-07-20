## Sorting: Comparisons
- Code Challenge 28

---
<br>

#### When sorting an array, a key step in the algorithm is determining what their order should be. In the insertion sort algorithm, the insertion phase has a while loop that checks for whether the number to insert is less than the number at the iteration index. The first time the number to insert is greater, the algorithm inserts at the previous index. Merge Sort applies the same logic when recombining sub-arrays, as it needs to choose whether to pull from the left or the right array.

#### For numbers, this comparison is easy - they go in ascending order. JavaScript, Python, and all the languages have a built-in operator to make this check for numbers: <, the less-than operator.

#### However, we very rarely want to sort an array of numbers. Usually, we want to sort an array of some complex data object we have created for our programs. For instance, we could sort an array of CookieStand objects by cookies sold, or an array of HornedBeasts by the name of their species.

#### All our programming languages have a built-in sort function. And all our programming languages include a mechanism to provide a “comparator callback”! We have seen callback functions in other places. A filter callback function returns a boolean, to decide whether to keep a certain item. A map callback transforms each input value into some other output value. A reduce callback combines together all the items in an array into a single value.

#### The sort functions take a callback which tells the sort algorithm in what order two items should be placed. This callback takes two parameters, a and b, and returns a number. When the number is less than 0, the a parameter should be sorted to the left of the b parameter. When the number is greater than 0, a should be sorted to the right of b! When the comparator returns 0, it means that (as far as the comparator is concerned) the items are equivalent, and it doesn’t matter which order they go in.

<br>

---
<br>

Sorting Numbers

#### The comparator function takes a and b, and returns a number less than zero if a should come before b when sorting is completed. There are two approaches for numbers to implement such a function. The first uses the < operator, and by convention returns -1 if a < b. If a > b, it returns 1, and if a == b, it returns 0. While the contract of the comparator function says any number is a valid return so long as the less-than-0 rule holds, by convention we return -1, 0, or 1.

```
function compareNumbers(a, b) {
  if (a == b) return 0;
  if (a < b) return -1;
  if (a > b) return 1;
}
```
<br>

#### For numbers, you could also achieve this property by using b - a.

#### We will see why in the next sections, but to make it more obvious, let’s first look at another way we can compare numbers with the same rule.

#### We start by thinking about the 0 case. 0 for the comparator means that two numbers are equal. Using subtraction can tell if two numbers are zero.

```
a &= b
a - b &= b - b
a - b &= 0
```

<br>

#### Does this work for the comparator as a whole?

```
a - b &> 0, a < b
a - b &= 0, a = b
a - b &< 0, a > b
```

<br>

#### So a - b is backwards from what the comparator needs. Flipping it around gives exactly what we want:

```
b - a &< 0, a < b
b - a &= 0, a = b
b - a &> 0, a > b
```

<br>

#### Thus, the canonical comparator function for two numbers is (a, b) => b - a.

<br>

---

<br>

### Sorting Strings

#### Strings seem easy, but are in truth very messy. This is largely because of character encodings and international languages. For the most part, we don’t need to worry about that, if we use what the programming languages give us!

#### In JavaScript and Python, we can actually use the < and > operators on strings!

```
def compare(a, b):
  if a > b:
    return 1
  if a < b:
    return -1
  return 0
```

<br>

#### Unfortunately, this does not work in Java or C#.


#### However, a more general solution already exists in all our languages! Each language provides a built-in function that will compare two strings, lexicographically, following all the syntax rules of the user’s (written) language.

- JavaScript: String.prototype.localeCompare
- Python: locale.strcol
- Java: String.Compare
- .NET: Collator.getInstance

<br>

---
<br>

### Sorting Objects


#### Sorting objects typically comes down to sorting based on properties in the object. This is similar to filtering, which often checks one property’s value. When this is necessary, your callback function will take an a and a b object, apply some logic to choose which properties, and compare them using either the number or string comparisons above. In some applications, this may need to be repeated. For instance, if you are sorting alphabetically for the phone book, you would sort first by last name, and if last names are equal, then by first name. If there are multiple people with the same first and last name, you may decide to then sort by phone number!

<br>

---
<br>

### Assignment

#### In the first half of this code challenge, you will write functions which sort domain objects. Your functions will receive an array of Movie objects. Each Movie object has a title (string), a year (number), and a list of genres (array of strings). One function will sort the movies by most recent year first. One function will sort the movies, alphabetical by title, but will ignore any leading “A”s, “An”s, or “The”s. Test outputs for these functions, and an array of sample data, have been provided in test and movies.

#### In the second half of the code challenge, you will write tests for your comparator functions. This may necessitate refactoring the code you wrote in part one. Your tests will need to call the comparator functions directly, and make assertions about the response values given test inputs.

<br>

---