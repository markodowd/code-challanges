function digitize(n) {
  var stringNum = n.toString();
  var newArray = [];

  for (var i = 0; i < stringNum.length; i++) {
    newArray.push(parseInt(stringNum[i]));
  }
  return newArray.reverse();
}
