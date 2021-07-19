function invert(array) {
  for (var i = 0; i < array.length; i++) {
    if (array[i] > 0) {
      array[i] = -Math.abs(array[i]);
    } else {
      array[i] = Math.abs(array[i]);
    }
  }
  return array;
}
