function sumArray(array) {
  var total = 0;

  if (array === null || array.length < 1) {
    return 0;
  }

  orderedArray = array.sort(function (a, b) {
    return a - b;
  });

  for (var i = 1; i <= orderedArray.slice(1, -1).length; i++) {
    total += orderedArray[i];
  }
  return total;
}
