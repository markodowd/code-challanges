function squareSum(numbers) {
  var sum = 0;

  for (var i = 0; i < numbers.length; i++) {
    sum = sum + numbers[i] ** 2;
  }
  return sum;
}
