const reverseSeq = (n) => {
  let newArray = [];

  for (let i = n; i > 0; i--) {
    newArray.push(i);
  }
  return newArray;
};
