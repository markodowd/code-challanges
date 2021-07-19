# The Challange

https://www.codewars.com/kata/array-plus-array/train/javascript

```
I'm new to coding and now I want to get the sum of two arrays...actually the sum of all their elements. I'll appreciate for your help.

P.S. Each array includes only integer numbers. Output is a number too.
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- Destructred to create a combined array
- Then reduce() to calculate the total

# Favourite Answer (By Others)

```
function arrayPlusArray(arr1, arr2) {
  let arr = [...arr1, ...arr2];
  return arr.reduce((a, b) => a + b);
}
```
