function XO(str) {
  var xCount = 0;
  var oCount = 0;

  for (var i = 0; i < str.length; i++) {
    if (str[i].toLowerCase() == "o") {
      oCount += 1;
    } else if (str[i].toLowerCase() == "x") {
      xCount += 1;
    }
  }

  if (oCount == xCount) {
    return true;
  } else {
    return false;
  }
}
