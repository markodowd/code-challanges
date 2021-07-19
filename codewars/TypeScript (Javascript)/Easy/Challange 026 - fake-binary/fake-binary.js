function fakeBin(x) {
  var newArray = [];

  for (var i = 0; i < x.length; i++) {
    if (x[i] < 5) {
      newArray.push("0");
    } else {
      newArray.push("1");
    }
  }
  var newString = newArray.toString();
  return newString.replace(/,/g, "");
}
