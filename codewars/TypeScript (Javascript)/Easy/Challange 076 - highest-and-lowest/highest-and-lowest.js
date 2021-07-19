function highAndLow(numbers) {
  var splitArray = numbers.split(" ");
  splitArray.sort(function (a, b) {
    return a - b;
  });
  return splitArray[splitArray.length - 1] + " " + splitArray[0];
}
