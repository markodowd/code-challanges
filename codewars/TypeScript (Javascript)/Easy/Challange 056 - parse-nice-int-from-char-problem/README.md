# The Challange

https://www.codewars.com/kata/parse-nice-int-from-char-problem/train/javascript

```
Ask a small girl - "How old are you?". She always says strange things... Lets help her!

For correct answer program should return int from 0 to 9.

Assume test input string always valid and may look like "1 year old" or "5 years old", etc.. The first char is number only.
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- parseInt only worked because [0] was a number
- That's why fav answer makes most sense

# Favourite Answer (By Others)

```
function getAge(inputString){
  return parseInt(inputString[0]);
}
```
