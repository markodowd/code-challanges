function powersOfTwo(n) {
  let newArray = [];

  for (let i = 0; i <= n; i++) {
    newArray.push(2 ** i);
  }

  return newArray;
}
