# The Challange

https://www.codewars.com/kata/reversed-words/train/javascript

```
Complete the solution so that it reverses all of the words within the string passed in.

Example:

reverseWords("The greatest victory is that which requires no battle")
// should return "battle no requires which that is victory greatest The"
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- Combined the 3 functions - split, reverse, join
- It split each word into array, reversed then joined all together into string
- Favourite was same as mine

# Favourite Answer (By Others)

```
function reverseWords(str){
  return str.split(' ').reverse().join(' ');
}
```
