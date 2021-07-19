function order(words) {
  let sortArray = [];

  if (words == "") {
    return words;
  } else {
    words
      .split(" ")
      .forEach((val) => (sortArray[Number(val.match(/\d/)[0]) - 1] = val));
    return sortArray.join(" ");
  }
}
