decodeMorse = function (morseCode) {
  let splitWords = morseCode.split("   ");
  let arr = Array.from(splitWords);
  let decodedString = "";

  for (let i = 0; i < arr.length; i++) {
    let eachWord = arr[i].split(" ");

    for (let i = 0; i < eachWord.length; i++) {
      decodedString += MORSE_CODE[eachWord[i]];
    }

    decodedString += " ";
  }

  let strippedString = decodedString.replace(/undefined/g, " ");

  return strippedString.trim();
};
