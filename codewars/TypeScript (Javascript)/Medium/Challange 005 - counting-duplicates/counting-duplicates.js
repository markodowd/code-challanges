function duplicateCount(text) {
  let obj = {};
  let textLower = text.toLowerCase();
  let counter = 0;

  //Each letter added to object
  for (i = 0; i < text.length; i++) {
    obj[textLower[i]] = 0;
  }

  //Tally each letter to object
  for (i = 0; i < text.length; i++) {
    if (obj.hasOwnProperty(`${textLower[i]}`)) {
      obj[textLower[i]] += 1;
    }
  }

  //Check how many letters > 1 and tally
  for (i = 0; i < Object.keys(obj).length; i++) {
    if (obj[Object.keys(obj)[i]] > 1) {
      counter += 1;
    }
  }

  return counter;
}
