function longest(s1, s2) {
  var combinedString = s1 + s2;
  var newString = "";

  for (var i = 0; i < combinedString.length; i++) {
    if (newString.search(combinedString[i]) == -1) {
      newString += combinedString[i];
    }
  }
  return newString.split("").sort().join("");
}
