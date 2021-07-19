const removeSmallest = (numbers) =>
  numbers
    .slice(0, numbers.indexOf(Math.min.apply(null, numbers)))
    .concat(numbers.slice(numbers.indexOf(Math.min.apply(null, numbers)) + 1));
