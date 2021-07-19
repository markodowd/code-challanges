const countSheep = function (num) {
  let newString = "";

  for (let i = 1; i <= num; i++) {
    newString += `${i} sheep...`;
  }
  return newString;
};
