# The Challange

https://www.codewars.com/kata/square-every-digit/train/javascript

```
Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- Bit of back and forth from int > string > int

# Favourite Answer (By Others)

```
function squareDigits(num){
  return Number(('' + num).split('').map(function (val) { return val * val;}).join(''));
}
```
