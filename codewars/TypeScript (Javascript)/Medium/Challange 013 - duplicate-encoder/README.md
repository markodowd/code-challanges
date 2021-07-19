# The Challange

https://www.codewars.com/kata/duplicate-encoder/train/javascript

```
The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.
Examples

"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))(("
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- Got the answer from googled after I thought of the approach but didn't want to do the work late at night (1:15am)
- Fav - so clever - w.indexOf(a) == w.lastIndexOf(a) meant count make this single line if wanted
- Fav - supposedly not effiencient because indexOf and lastIndexOf keep looping but its so easily read

# Favourite Answer (By Others)

```
function duplicateEncode(word){
  return word
    .toLowerCase()
    .split('')
    .map( function (a, i, w) {
      return w.indexOf(a) == w.lastIndexOf(a) ? '(' : ')'
    })
    .join('');
}
```
