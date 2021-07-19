function symmetricDifference() {
  // var combinedArray = arguments[0].concat(arguments[1]);

  // var set = [...new Set(combinedArray)];

  // console.log(set);
  let difference = arguments[0]
    .filter((x) => !arguments[1].includes(x))
    .concat(arguments[1].filter((x) => !arguments[0].includes(x)));

  return difference.sort(function (a, b) {
    return a - b;
  });
}

symmetricDifference([1, 2, 3], [5, 2, 1, 4]);
