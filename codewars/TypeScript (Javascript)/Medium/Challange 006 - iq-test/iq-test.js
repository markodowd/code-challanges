function iqTest(numbers) {
  let evenNumbers = [];
  let oddNumbers = [];
  let numbersArray = numbers.split(" ");

  numbersArray.forEach((item) => {
    if (item % 2 == 0) {
      evenNumbers.push(item);
    } else {
      oddNumbers.push(item);
    }
  });

  if (evenNumbers.length == 1) {
    return numbersArray.indexOf(evenNumbers.toString()) + 1;
  } else {
    return numbersArray.indexOf(oddNumbers.toString()) + 1;
  }
}
