# The Challange

https://www.codewars.com/kata/count-odd-numbers-below-n/train/javascript

```
Given a number n, return the number of positive odd numbers below n, EASY!

oddCount(7) //=> 3, i.e [1, 3, 5]
oddCount(15) //=> 7, i.e [1, 3, 5, 7, 9, 11, 13]
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- realised the answer was / 2 rounded down

# Favourite Answer (By Others)

```
function oddCount(n){
  var returnArray = [];
  for(var i=1;i<n;i=i+2) {
    returnArray.push(i);
  }
  return returnArray.length;
}
```
