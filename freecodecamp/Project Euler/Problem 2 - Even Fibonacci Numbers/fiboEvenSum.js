function fiboEvenSum(n) {
  let firstNum = 0;
  let secondNum = 1;
  let fibNum = 0;
  let total = 0;

  for (let i = 0; i <= n; i++) {
    fibNum = firstNum + secondNum;
    firstNum = secondNum;
    secondNum = fibNum;

    if (fibNum % 2 == 0) {
      total += fibNum;
    }
  }
  // console.log(total);
  return total;
}

fiboEvenSum(10);
