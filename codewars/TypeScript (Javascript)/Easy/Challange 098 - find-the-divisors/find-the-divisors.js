function divisors(integer) {
  let arr = [];

  for (i = 2; i < integer; i++) {
    if (integer % i == 0) {
      arr.push(i);
    }
  }

  return arr.length == 0 ? `${integer} is prime` : arr;
}
