const getAverage = (marks) =>
  Math.floor(marks.reduce((total, value) => (total += value)) / marks.length);
