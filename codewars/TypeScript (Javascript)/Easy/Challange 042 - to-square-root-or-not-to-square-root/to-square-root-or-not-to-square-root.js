function squareOrSquareRoot(array) {
  function myFunction(value) {
    if (value % Math.sqrt(value) == 0) {
      return Math.sqrt(value);
    } else {
      return value ** 2;
    }
  }

  return array.map(myFunction);
}
