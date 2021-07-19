function accum(s) {
  var newString = "";
  for (var i = 0; i < s.length; i++) {
    newString += s[i].toUpperCase() + s[i].repeat([i]).toLowerCase();
    if (i < s.length - 1) {
      newString += "-";
    }
  }
  return newString;
}
