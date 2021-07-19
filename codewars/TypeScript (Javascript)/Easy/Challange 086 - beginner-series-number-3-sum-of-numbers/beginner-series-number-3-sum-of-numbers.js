function GetSum(a, b) {
  if (a > b) {
    var startNumber = b;
    var endNumber = a;
  } else {
    var startNumber = a;
    var endNumber = b;
  }

  var totalCounter = 0;

  for (startNumber; startNumber <= endNumber; startNumber++) {
    totalCounter += startNumber;
  }

  return totalCounter;
}
