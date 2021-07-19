function feast(beast, dish) {
  const firstLetter = dish[0];
  const lastLetter = dish[dish.length - 1];

  if (beast.startsWith(firstLetter) && beast.endsWith(lastLetter)) {
    return true;
  } else {
    return false;
  }
}
