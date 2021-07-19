# The Challange

https://www.codewars.com/kata/find-the-smallest-integer-in-the-array/train/javascript

```
Given an array of integers your solution should find the smallest integer.

For example:

    Given [34, 15, 88, 2] your solution will return 2
    Given [34, -345, -1, 100] your solution will return -345

You can assume, for the purpose of this kata, that the supplied array will not be empty.

```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- Found sort(function(a,b){return a-b}) to order array smallest to largest
- Just grabbed first value after that for smallest
- Learned ...args in favourite answer can cover many incoming arguments

# Favourite Answer (By Others)

```
class SmallestIntegerFinder {
  findSmallestInt(args) {
    return Math.min(...args)
  }
}
```
