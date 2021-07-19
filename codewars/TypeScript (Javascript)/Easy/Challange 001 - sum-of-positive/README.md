# The Challange

https://www.codewars.com/kata/sum-of-positive/train/javascript

```
You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- Was stuck because 'return total;' was within statement so wasn't getting full tally.
- Had to use the >= to pass over the negative numbers.

# Favourite Answer (By Others)

```
function positiveSum(arr) {
  var total = 0;
  for (i = 0; i < arr.length; i++) {    // setup loop to go through array of given length
    if (arr[i] > 0) {                   // if arr[i] is greater than zero
      total += arr[i];                  // add arr[i] to total
    }
  }
  return total;                         // return total
}
```
