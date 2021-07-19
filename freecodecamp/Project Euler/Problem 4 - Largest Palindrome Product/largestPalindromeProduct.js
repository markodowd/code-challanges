function largestPalindromeProduct(n) {
  let max = Number("9".repeat(n));
  let min = Number("1" + "0".repeat(n - 1));
  let maxPalindrome = 0;

  for (let i = max; i >= min; i--) {
    for (let j = max; j >= min; j--) {
      let num = i * j;
      let numReverse = String(num).split("").reverse().join("");

      if (String(num) == String(numReverse)) {
        if (num > maxPalindrome) {
          maxPalindrome = num;
        }
      }
    }
  }

  return maxPalindrome;
}

largestPalindromeProduct(3);
