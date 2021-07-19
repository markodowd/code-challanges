function grow(x) {
  function myFunction(total, value, index, array) {
    return total * value;
  }
  return x.reduce(myFunction);
}
