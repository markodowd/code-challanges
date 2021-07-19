function sumSquareDifference(n: number) {
  const sumOfSquares = (n: number) => {
    let total = 0;

    for (let i = 1; i <= n; i++) {
      total += i ** 2;
    }

    return total;
  };

  const squareOfSum = (n: number) => {
    let total = 0;

    for (let i = 1; i <= n; i++) {
      total += i;
    }

    return total ** 2;
  };
  return squareOfSum(n) - sumOfSquares(n);
}

sumSquareDifference(100);
