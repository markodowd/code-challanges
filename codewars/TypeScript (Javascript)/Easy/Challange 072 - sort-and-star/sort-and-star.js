const twoSort = (arr) =>
  arr
    .sort()[0]
    .split("")
    .reduce((total, value) => total + "***" + value);
