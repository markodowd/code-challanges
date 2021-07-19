function findOdd(A) {
  var objCounter = {};

  //Filling objCounter
  for (var i = 0; i < A.length; i++) {
    if (objCounter[A[i]] == true) {
      objCounter[A[i]]++;
    } else {
      objCounter[A[i]] = 1;
    }
  }

  //Checking objCounter
  for (var key in objCounter) {
    if (objCounter[key] % 2 !== 0) {
      return Number(key);
    }
  }
}
