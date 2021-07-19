function removeEveryOther(arr) {
  let newArr = [];

  for (let i = 0; i < arr.length; i += 2) {
    newArr.push(arr[i]);
  }
  return newArr;
}
