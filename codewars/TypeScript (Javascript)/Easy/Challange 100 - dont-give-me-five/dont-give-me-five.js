function dontGiveMeFive(start, end) {
  let newArray = [];

  for (let i = start; i <= end; i++) {
    if (!i.toString().includes(5)) {
      newArray.push(i);
    }
  }
  return newArray.length;
}
