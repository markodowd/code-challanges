const isDivideBy = (number, a, b) =>
  Math.abs(number) % Math.abs(a) == 0 && Math.abs(number) % Math.abs(b) == 0
    ? true
    : false;
