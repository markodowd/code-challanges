# The Challange

https://www.codewars.com/kata/stop-gninnips-my-sdrow/train/javascript

```
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") => returns "This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- newArray[i].split('').reverse().join('') inside if seems too convoluted
- Fav - they used the same 'convoluted' way but way cleaner in a ternary operator
- Fav - could be cleaned up further with arrow functions

# Favourite Answer (By Others)

```
function spinWords(words){
  return words.split(' ').map(function (word) {
    return (word.length > 4) ? word.split('').reverse().join('') : word;
  }).join(' ');
}
```
