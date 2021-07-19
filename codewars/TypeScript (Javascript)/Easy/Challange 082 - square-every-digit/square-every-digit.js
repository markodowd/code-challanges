function squareDigits(num) {
  var convertString = num.toString();
  var newString = "";

  for (var i = 0; i < convertString.length; i++) {
    newString += convertString[i] ** 2;
  }
  return parseInt(newString);
}
