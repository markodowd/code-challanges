# The Challange

https://www.codewars.com/kata/sum-arrays/train/javascript

```
Sum Array

Write a method sum (sum_array in python, SumArray in C#) that takes an array of numbers and returns the sum of the numbers. These may be integers or decimals for Ruby and any instance of Num for Haskell. The numbers can also be negative. If the array does not contain any numbers then you should return 0.
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- reduce() perfect

# Favourite Answer (By Others)

```
// Sum Numbers
sum = function (numbers) {
  "use strict";
  return numbers.reduce(function(t, n){
    return t + n;
  }, 0);
};
```
