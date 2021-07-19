# The Challange

https://www.codewars.com/kata/mumbling/train/javascript

```
This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

The parameter of accum is a string which includes only letters from a..z and A..Z.

```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- Probably a better way to achieve the "-" divider rather than my if check

# Favourite Answer (By Others)

```
function accum(s) {
  return s.split('').map((c, i) => (c.toUpperCase() + c.toLowerCase().repeat(i))).join('-');
}
```
