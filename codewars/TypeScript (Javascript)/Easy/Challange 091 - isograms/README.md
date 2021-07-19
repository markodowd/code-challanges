# The Challange

https://www.codewars.com/kata/isograms/train/javascript

```
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

isIsogram( "Dermatoglyphics" ) == true
isIsogram( "aba" ) == false
isIsogram( "moOse" ) == false // -- ignore letter case
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- Set() doesn't allow duplicates
- toLowerCase().split('') to create a case insensitive array
- Set has to use .size instead of length
- Compare this to the original str length
- fav - i knew there was a regex but it's much harder to read
- other fav - i didn't need to split(''), set can be created from string

# Favourite Answer (By Others)

```
function isIsogram(str){
  return !/(\w).*\1/i.test(str)
}
```
