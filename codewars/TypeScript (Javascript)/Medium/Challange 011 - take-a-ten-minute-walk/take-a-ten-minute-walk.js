function isValidWalk(walk) {
  let counter = {
    n: 0,
    s: 0,
    w: 0,
    e: 0,
  };

  if (walk.length != 10) {
    return false;
  } else {
    walk.forEach((el) => (counter[el] += 1));
    return counter["n"] == counter["s"] && counter["w"] == counter["e"];
  }
}
