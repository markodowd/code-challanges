# The Challange

https://www.codewars.com/kata/sort-and-star/train/javascript

```
You will be given an vector of string(s). You must sort it alphabetically (case-sensitive!!) and then return the first value.

The returned value must be a string, and have "***" between each of its letters.

You should not remove or add elements from/to the array.
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- sort() alphabetically
- split() into separate characters
- reduce() to single value with the \*\*\* added
- fav - didn't need reduce join() can add extra

# Favourite Answer (By Others)

```
function twoSort(s) {
  return s.sort()[0].split('').join('***');
}
```
