const oddOrEven = (array) =>
  (array.length == 0 ? "even" : array.reduce((acc, val) => acc + val) % 2 == 0)
    ? "even"
    : "odd";
