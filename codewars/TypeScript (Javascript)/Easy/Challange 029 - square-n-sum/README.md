# The Challange

https://www.codewars.com/kata/square-n-sum/train/javascript

```
Complete the square sum method so that it squares each number passed into it and then sums the results together.

For example: squareSum([1, 2, 2]) should return 9 because 1^2 + 2^2 + 2^2 = 9.

```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- Simple loop with counter adding on sqaured value

# Favourite Answer (By Others)

```
function squareSum(numbers){
  return numbers.reduce(function(sum, n){
    return (n*n) + sum;
  }, 0)
}
```
