function mxdiflg(a1, a2) {
  if (a1.length == 0 || a2.length == 0) {
    return -1;
  }

  let a1Sort = a1.sort((a, b) => b.length - a.length);
  let a2Sort = a2.sort((a, b) => b.length - a.length);

  let longestA1 = a1Sort[0].length;
  let longestA2 = a2Sort[0].length;

  let shortestA1 = a1Sort[a1Sort.length - 1].length;
  let shortestA2 = a2Sort[a2Sort.length - 1].length;

  return Math.max(
    Math.abs(longestA1 - shortestA2),
    Math.abs(longestA2 - shortestA1)
  );
}
