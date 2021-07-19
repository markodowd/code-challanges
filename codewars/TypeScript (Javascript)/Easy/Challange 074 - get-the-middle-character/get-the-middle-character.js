function getMiddle(s) {
  var halfLength = s.length / 2;

  if (s.length % 2 == 0) {
    return s.slice(halfLength - 1, halfLength + 1);
  } else {
    var middlePos = Math.floor(halfLength);
    return s.slice(middlePos, middlePos + 1);
  }
}
