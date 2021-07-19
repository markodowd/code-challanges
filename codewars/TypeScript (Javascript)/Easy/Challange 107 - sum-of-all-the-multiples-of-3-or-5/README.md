# The Challange

https://www.codewars.com/kata/sum-of-all-the-multiples-of-3-or-5/train/javascript

```
Your task is to write function findSum.

Upto and including n, this function will return the sum of all multiples of 3 and 5.

For example:

findSum(5) should return 8 (3 + 5)

findSum(10) should return 33 (3 + 5 + 6 + 9 + 10)
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- Simple for loop with if check - didn't want to overthink
- Fav - challange not as many completions so less comments or clever answers

# Favourite Answer (By Others)

```
function findSum(n) {
  let result = 0;
  for (let i = 0; i <= n; i += 1) {
    if (i % 3 ===0 || i % 5 === 0) result += i
  }
  return result
}
```
