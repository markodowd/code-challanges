function DNAStrand(dna) {
  var stringArray = dna.split("");

  for (var i = 0; i < stringArray.length; i++) {
    if (stringArray[i] == "A") {
      stringArray[i] = "T";
    } else if (stringArray[i] == "T") {
      stringArray[i] = "A";
    } else if (stringArray[i] == "C") {
      stringArray[i] = "G";
    } else if (stringArray[i] == "G") {
      stringArray[i] = "C";
    }
  }
  return stringArray.toString().replace(/,/g, "");
}
