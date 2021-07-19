function solution(number) {
  var totalSum = 0;

  for (var i = 1; i < number; i++) {
    if (i % 3 == 0 || i % 5 == 0) {
      totalSum += i;
    }
  }
  return totalSum;
}
