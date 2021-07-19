function countSheeps(arrayOfSheep) {
  var sheepCounter = 0;

  for (var i = 0; i < arrayOfSheep.length; i++) {
    if (arrayOfSheep[i] === true) {
      sheepCounter += 1;
    }
  }
  return sheepCounter;
}
