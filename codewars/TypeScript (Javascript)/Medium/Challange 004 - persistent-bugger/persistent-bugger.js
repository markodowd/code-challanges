function persistence(num) {
  let steps = 0;

  while (num.toString().length > 1) {
    num = num
      .toString()
      .split("")
      .reduce((total, value) => total * value);
    steps++;
  }
  return steps;
}
