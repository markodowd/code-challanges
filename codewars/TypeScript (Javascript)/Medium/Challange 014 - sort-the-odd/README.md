# The Challange

https://www.codewars.com/kata/sort-the-odd/train/javascript

```
You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- Got answer from google but I was thinking the same approach

# Favourite Answer (By Others)

```
function sortArray(array) {
  const odd = array.filter((x) => x % 2).sort((a,b) => a - b);
  return array.map((x) => x % 2 ? odd.shift() : x);
}
```
