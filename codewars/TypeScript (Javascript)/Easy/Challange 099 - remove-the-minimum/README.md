# The Challange

https://www.codewars.com/kata/remove-the-minimum/train/javascript

```
Task

Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with a lower index. If you get an empty array/list, return an empty array/list.

Don't change the order of the elements that are left.
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- My answer incredibly hacky/elaborate
- Was focusing too much on making it an arrow func
- Fav - It had a similar approach only used variable for index
- Fav - and [...numbers] so it wasn't mutating

# Favourite Answer (By Others)

```
function removeSmallest(numbers) {
  let indexOfMin = numbers.indexOf(Math.min(...numbers));
  return [...numbers.slice(0, indexOfMin), ...numbers.slice(indexOfMin + 1)];
}
```
