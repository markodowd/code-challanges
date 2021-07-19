function gooseFilter(birds) {
  var geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"];

  function geeseFilter(value) {
    if (geese.includes(value) === false) {
      return value;
    }
  }
  return birds.filter(geeseFilter);
}
