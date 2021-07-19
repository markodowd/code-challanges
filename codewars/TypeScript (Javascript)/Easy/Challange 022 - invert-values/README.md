# The Challange

https://www.codewars.com/kata/invert-values/javascript

```
Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- My code feels very overcomplicated
- Math.abs and -Math.abs used to flip
- Alot of other people just used map() need to readup on

# Favourite Answer (By Others)

```
function invert(array) {
   return array.map( x => x === 0 ? x : -x);
}
```
