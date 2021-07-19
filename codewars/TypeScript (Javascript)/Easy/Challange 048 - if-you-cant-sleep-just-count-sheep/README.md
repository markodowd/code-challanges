# The Challange

https://www.codewars.com/kata/if-you-cant-sleep-just-count-sheep/train/javascript

```
Task:

Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- Easier to do standard loop than convert to array and mess around

# Favourite Answer (By Others)

```
var countSheep = function (num){
  let str = "";
  for(let i = 1; i <= num; i++) { str+= `${i} sheep...`; }
  return str;
}
```
