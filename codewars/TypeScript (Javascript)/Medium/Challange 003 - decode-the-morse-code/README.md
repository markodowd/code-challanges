# The Challange

https://www.codewars.com/kata/decode-the-morse-code/train/javascript

```
Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.

For example:

decodeMorse('.... . -.--   .--- ..- -.. .')
//should return "HEY JUDE"
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- Found fairly difficult but passed all tests
- Nested for loops and hacky stripping of undefined doesn't seem optimal
- Need to really analyse methods used by others

# Favourite Answer (By Others)

```
decodeMorse = function(morseCode){
  function decodeMorseLetter(letter) {
    return MORSE_CODE[letter];
  }
  function decodeMorseWord(word) {
    return word.split(' ').map(decodeMorseLetter).join('');
  }
  return morseCode.trim().split('   ').map(decodeMorseWord).join(' ');
}
```

# Favourite Analysed

- The final return started with .trim() to remove all spaces from the tests
- Avoided the 'undefined' problem I had by doing this
- split(' ') then created an array with each individual word as an array string aka ["hey", "jude"]
- The map() method creates a new array with the results of calling a function for every array element.
- So the .map() goes to his word function that then splits each word down to individual character
- Each letter is then checked against the MORSE_CODE dictionary
- Each individual letter then joined back to 1 word with .join('') in the decodeMorseWord function
- .join(' ') in final return adds a space between each word and returns it back as a string
