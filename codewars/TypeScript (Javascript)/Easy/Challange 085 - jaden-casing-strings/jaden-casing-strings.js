String.prototype.toJadenCase = function () {
  var arrayOfWords = this.split(" ");
  var newString = "";

  for (var i = 0; i < arrayOfWords.length; i++) {
    newString +=
      arrayOfWords[i].charAt(0).toUpperCase() + arrayOfWords[i].slice(1);

    if (i < arrayOfWords.length - 1) {
      newString += " ";
    }
  }
  return newString;
};
