function sortArray(array) {
  const oddArr = [];
  const evenArr = [];
  const result = [];

  //Sorts values into new odd/even array
  for (let i = 0; i < array.length; i += 1) {
    if (array[i] % 2 === 0) {
      evenArr.push(array[i]);
    } else {
      oddArr.push(array[i]);
    }
  }

  oddArr.sort((a, b) => a - b);

  //Go through original array only but push in new sorted value
  for (let i = 0; i < array.length; i += 1) {
    if (array[i] % 2 === 0) {
      result.push(evenArr.shift());
    } else {
      result.push(oddArr.shift());
    }
  }
  return result;
}
