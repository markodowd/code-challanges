const countBits = (n) =>
  n
    .toString(2)
    .split("")
    .reduce((total, el) => total + Number(el), 0);
