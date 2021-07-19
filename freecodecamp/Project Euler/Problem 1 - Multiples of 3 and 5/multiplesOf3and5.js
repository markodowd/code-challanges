function multiplesOf3and5(number) {
  let total = 0;

  for (let i = 3; i < number; i++) {
    if (i % 3 == 0 || i % 5 == 0) {
      total += i;
    }
  }

  return total;
}

multiplesOf3and5(1000);
