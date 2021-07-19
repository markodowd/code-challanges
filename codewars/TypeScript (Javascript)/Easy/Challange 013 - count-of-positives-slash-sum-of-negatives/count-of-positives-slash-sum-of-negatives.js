function countPositivesSumNegatives(input) {
  var counter = 0;
  var negativeCounter = 0;

  if (input === null || input.length < 1) {
    return [];
  }

  for (var i = 0; i < input.length; i++) {
    if (input[i] > 0) {
      counter++;
    }
  }

  for (var i = 0; i < input.length; i++) {
    if (input[i] < 0) {
      negativeCounter += input[i];
    }
  }

  return [counter, negativeCounter];
}
