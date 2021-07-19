# The Challange

https://www.codewars.com/kata/reversed-sequence/train/javascript

```
Get the number n (n>0) to return the reversed sequence from n to 1.

Example : n=5 >> [5,4,3,2,1]
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- For loop but decreasing for once (let i = n; i > 0; i--)

# Favourite Answer (By Others)

```
const reverseSeq = n => {
let arr = [];
  for (let i=n; i>0; i--) {
    arr.push(i);
    } return arr;
};
```
