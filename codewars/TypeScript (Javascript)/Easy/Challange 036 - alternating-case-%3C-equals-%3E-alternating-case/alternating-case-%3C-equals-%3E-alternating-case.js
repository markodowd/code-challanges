String.prototype.toAlternatingCase = function () {
  let newString = "";

  for (let i = 0; i < this.length; i++) {
    if (this[i] == this[i].toUpperCase()) {
      newString += this[i].toLowerCase();
    } else {
      newString += this[i].toUpperCase();
    }
  }
  return newString;
};
