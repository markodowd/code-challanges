# The Challange

https://www.codewars.com/kata/bit-counting/train/javascript

```
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- Impressed with my answer - toString(2) to make binary from other tests
- Fav - very witty spliting ('0') and the length check at end

# Favourite Answer (By Others)

```
countBits = n => n.toString(2).split('0').join('').length;
```
