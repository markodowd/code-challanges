function descendingOrder(n) {
  var desArray = n
    .toString()
    .split("")
    .sort(function (a, b) {
      return b - a;
    });
  var newString = "";

  for (var i = 0; i < desArray.length; i++) {
    newString += desArray[i];
  }
  return parseInt(newString);
}
