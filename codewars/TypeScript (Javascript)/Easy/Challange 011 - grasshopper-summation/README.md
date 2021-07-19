# The Challange

https://www.codewars.com/kata/grasshopper-summation/train/javascript

```
Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

For example:

summation(2) -> 3
1 + 2

summation(8) -> 36
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- Took a decent time on this one
- console.log() until i figured out the for loop was ending early so had to add (num + 1)
- Thought I tried the favourite answer approach but mustn't have used <= num

# Favourite Answer (By Others)

```
var summation = function (num) {
  let result = 0;
  for (var i = 1; i <= num; i++) {
    result += i;
  }

  return result;
}
```
