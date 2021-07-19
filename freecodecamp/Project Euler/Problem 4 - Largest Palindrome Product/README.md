# The Challange

https://learn.freecodecamp.org/coding-interview-prep/project-euler/problem-4-largest-palindrome-product

```
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two n-digit numbers.
```

# My Answer

```
function largestPalindromeProduct(n) {
  let max = Number("9".repeat(n));
  let min = Number(("1" + "0".repeat(n - 1)))
  let maxPalindrome = 0;

for (let i = max; i >= min; i--){
  for (let j =  max; j >= min; j--){
    let num = i * j;
    let numReverse = String(num).split('').reverse().join('');

    if (String(num) == String(numReverse)) {
      if(num > maxPalindrome) {
        maxPalindrome = num;
      }
    }
  }
}

  return maxPalindrome;
}

largestPalindromeProduct(3);
```

# Comments & Hurdles

* max and min first calulated example 999 & 100, 9999 & 1000, etc
* 2 loops means every value tested (999 * 999), (999 * 998) then (998 * 998), (998 * 997)
* Don't like - this answer had a lot of iteration
* Had an answer that was more effient but lost it and wanted to move on