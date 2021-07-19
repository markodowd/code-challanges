# The Challange

https://www.codewars.com/kata/shortest-word/train/javascript

```
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- Turned to array then compared length of words starting with first word

# Favourite Answer (By Others)

```
const findShort = (s) => s
  .split(' ')
  .sort((a, b) => b.length - a.length)
  .pop()
  .length;
```
