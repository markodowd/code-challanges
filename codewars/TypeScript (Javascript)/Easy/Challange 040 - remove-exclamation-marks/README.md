# The Challange

https://www.codewars.com/kata/remove-exclamation-marks/train/javascript

```
Write function RemoveExclamationMarks which removes all exclamation marks from a given string.
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- split("!") made array without !
- join("") just added string back together

# Favourite Answer (By Others)

```
function removeExclamationMarks(s) {
  return s.replace(/!/gi, '');
}
```

# Favourite Analysed

- replace() + regex expression
