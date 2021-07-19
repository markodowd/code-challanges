const betterThanAverage = (classPoints, yourPoints) =>
  yourPoints >
  classPoints.reduce((acc, el) => (acc += el)) / classPoints.length;
