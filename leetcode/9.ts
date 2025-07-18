function isPalindrome(x: number): boolean {
  const numberArray = x.toString().split("");

  for (let i = 0; i < Math.floor(numberArray.length / 2); i++) {
    if (numberArray[i] !== numberArray.slice(-Math.abs(i + 1))[0]) {
      return false;
    }
  }

  return true;
}
