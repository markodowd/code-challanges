class SmallestIntegerFinder {
  findSmallestInt(args) {
    var sortedArray = args.sort(function (a, b) {
      return a - b;
    });
    return sortedArray[0];
  }
}
