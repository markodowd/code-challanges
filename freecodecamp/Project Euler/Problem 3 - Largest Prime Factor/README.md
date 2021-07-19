# The Challange

https://learn.freecodecamp.org/coding-interview-prep/project-euler/problem-3-largest-prime-factor

```
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the given number?
```

# My Answer

```
function largestPrimeFactor(number) {

  for(let i = 2; i < (number / 2); i++) {
      if(number % i == 0) {
        number = number / i;
    }
  }
  // console.log(number)
  return number;
}

largestPrimeFactor(13195);
```

# Comments & Hurdles

* Only have to check up to half the number in question
* Loop and the highest number to return % 0 is the answer