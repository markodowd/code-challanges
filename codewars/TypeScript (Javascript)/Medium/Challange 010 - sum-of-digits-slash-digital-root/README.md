# The Challange

https://www.codewars.com/kata/sum-of-digits-slash-digital-root/train/javascript

```
A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- Googled digital root and found this simple modulo9 formula
- Maybe my best answer for a complicated question
- Fav - probably my approach if I didn't find the simple approach

# Favourite Answer (By Others)

```
function digital_root(n) {
  if (n < 10)
    return n;

  for (var sum = 0, i = 0, n = String(n); i < n.length; i++)
    sum += Number(n[i]);

  return digital_root(sum);
}
```
