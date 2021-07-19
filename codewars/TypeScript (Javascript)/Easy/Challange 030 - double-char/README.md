# The Challange

https://www.codewars.com/kata/double-char/train/javascript

```
Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

doubleChar("String") ==> "SSttrriinngg"

doubleChar("Hello World") ==> "HHeelllloo  WWoorrlldd"

doubleChar("1234!_ ") ==> "11223344!!__  "
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- Learned challange 26 and didn't make it as convoluted

# Favourite Answer (By Others)

```
function doubleChar(str) {
  return str.replace(/(.)/g, "$1$1")
}
```
