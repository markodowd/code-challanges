# The Challange

https://www.codewars.com/kata/reverse-words/train/javascript

```
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
Examples

"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- A bit of back and forth there might be a simpler way

# Favourite Answer (By Others)

```
function reverseWords(str) {
  return str.split("").reverse().join("").split(" ").reverse().join(" ");
}
```
