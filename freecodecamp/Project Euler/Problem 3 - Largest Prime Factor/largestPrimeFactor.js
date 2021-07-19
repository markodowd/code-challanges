function largestPrimeFactor(number) {
  for (let i = 2; i < number / 2; i++) {
    if (number % i == 0) {
      number = number / i;
    }
  }
  // console.log(number)
  return number;
}

largestPrimeFactor(13195);
