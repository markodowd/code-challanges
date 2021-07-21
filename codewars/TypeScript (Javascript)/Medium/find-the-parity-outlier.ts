// https://www.codewars.com/kata/5526fc09a1bbd946250002dc

export const findOutlier = (integers: number[]): any => {
  let evenNumbers = [];
  let oddNumbers = [];
  let num;

  for (num of integers) {
    if (num % 2 === 0) {
      evenNumbers.push(num);
    } else {
      oddNumbers.push(num);
    }
  }

  if (evenNumbers.length === 1) {
    return evenNumbers[0];
  } else {
    return oddNumbers[0];
  }
};
