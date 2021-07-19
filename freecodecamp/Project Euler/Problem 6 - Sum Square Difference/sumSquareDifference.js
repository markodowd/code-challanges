function sumSquareDifference(n) {
  var sumOfSquares = function (n) {
    var total = 0;
    for (var i = 1; i <= n; i++) {
      total += Math.pow(i, 2);
    }
    return total;
  };
  var squareOfSum = function (n) {
    var total = 0;
    for (var i = 1; i <= n; i++) {
      total += i;
    }
    return Math.pow(total, 2);
  };
  return squareOfSum(n) - sumOfSquares(n);
}
sumSquareDifference(100);
