function findShort(s) {
  var stringSplit = s.split(" ");
  var shortestWord = stringSplit[0];

  for (var i = 0; i < stringSplit.length; i++) {
    if (stringSplit[i].length < shortestWord.length) {
      shortestWord = stringSplit[i];
    }
  }
  return shortestWord.length;
}
