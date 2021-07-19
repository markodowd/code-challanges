# The Challange

https://www.codewars.com/kata/alternating-case-%3C-equals-%3E-alternating-case/train/javascript

```
Define String.prototype.toAlternatingCase (or a similar function/method such as to_alternating_case/toAlternatingCase/ToAlternatingCase in your selected language; see the initial solution for details) such that each lowercase letter becomes uppercase and each uppercase letter becomes lowercase. For example:

"hello world".toAlternatingCase() === "HELLO WORLD"
"HELLO WORLD".toAlternatingCase() === "hello world"
"hello WORLD".toAlternatingCase() === "HELLO world"
"HeLLo WoRLD".toAlternatingCase() === "hEllO wOrld"
"12345".toAlternatingCase() === "12345" // Non-alphabetical characters are unaffected
"1a2b3c4d5e".toAlternatingCase() === "1A2B3C4D5E"
"String.prototype.toAlternatingCase".toAlternatingCase() === "sTRING.PROTOTYPE.TOaLTERNATINGcASE"

```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- Had to use 'this' because of the tests to manipulate the String
- But straightforward otherwise

# Favourite Answer (By Others)

```
String.prototype.toAlternatingCase = function () {
    return this.split("").map(a => a === a.toUpperCase()? a.toLowerCase(): a.toUpperCase()).join('')
}
```

# Favourite Analysed

- First split("") every character into array
- Then used map() to run a comparrison check on each character
- Ended with join('') to turn back into complete string
