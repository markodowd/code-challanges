function nbYear(p0, percent, aug, p) {
  var totalPopulation = p0;
  var totalYears = 0;

  while (totalPopulation < p) {
    totalPopulation = totalPopulation + totalPopulation * (percent / 100) + aug;
    totalYears++;
  }
  return totalYears;
}
