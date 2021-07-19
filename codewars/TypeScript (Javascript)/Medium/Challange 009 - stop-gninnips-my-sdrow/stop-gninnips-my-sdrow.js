function spinWords(string) {
  let newArray = string.split(" ");
  let resultArray = [];

  for (let i = 0; i < newArray.length; i++) {
    if (newArray[i].length >= 5) {
      //       console.log("inside", newArray[i]);
      resultArray.push(newArray[i].split("").reverse().join(""));
    } else {
      resultArray.push(newArray[i]);
    }
  }
  return resultArray.join(" ");
}
