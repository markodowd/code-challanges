const duplicateEncode = (word) => {
  let letterCount = {};
  let arrayWord = word.toLowerCase().split("");

  //creates Object counting how many times each letter appeared
  arrayWord.forEach((el) => (letterCount[el] = (letterCount[el] || 0) + 1));

  //Check if letter appeared 1 time or more and return
  return arrayWord.map((el) => (letterCount[el] == 1 ? "(" : ")")).join("");
};
