# The Challange

https://www.codewars.com/kata/two-to-one/train/javascript

```
Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters,

    each taken only once - coming from s1 or s2.

Examples:

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- if (newString.search(combinedString[i]) == -1) felt hacky way to find it string didn't have letter in it
- in favourite answer Set() got rid of duplicates. very smart.

# Favourite Answer (By Others)

```
const longest = (s1, s2) => [...new Set(s1+s2)].sort().join('')
```
