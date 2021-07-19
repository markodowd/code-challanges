# The Challange

https://www.codewars.com/kata/powers-of-2/train/javascript

```
Complete the function that takes a non-negative integer n as input, and returns a list of all the powers of 2 with the exponent ranging from 0 to n (inclusive).
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- for loop with \*\* exoponential

# Favourite Answer (By Others)

```
function powersOfTwo(n){
  var result = [];
  for (var i = 0; i <= n; i++) {
    result.push(Math.pow(2, i));
  }
  return result;
}
```
