# The Challange

https://www.codewars.com/kata/sum-without-highest-and-lowest-number/train/javascript

```
Sum all the numbers of the array (in F# and Haskell you get a list) except the highest and the lowest element (the value, not the index!).
(The highest/lowest element is respectively only one element at each edge, even if there are more than one with the same value!)

Example:

{ 6, 2, 1, 8, 10 } => 16
{ 1, 1, 11, 2, 3 } => 6


If array is empty, null or None, or if only 1 Element exists, return 0.
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- Used some code from previous challanges
- Had to place the orderedArray after if statement to get past errors with null

# Favourite Answer (By Others)

```
function sumArray(array) {

  if (array == null || array.length <= 2) {
    return 0
  }

  var max = Math.max.apply(Math, array);
  var min = Math.min.apply(Math, array);
  var sum = 0

  for (i = 0; i < array.length; i++) {
    sum += array[i];
   }

  return sum - max - min
}
```
