# The Challange

https://learn.freecodecamp.org/coding-interview-prep/algorithms/find-the-symmetric-difference

```
Create a function that takes two or more arrays and returns an array of the symmetric difference (△ or ⊕) of the provided arrays.

Given two sets (for example set A = {1, 2, 3} and set B = {2, 3, 4}), the mathematical term "symmetric difference" of two sets is the set of elements which are in either of the two sets, but not in both (A △ B = C = {1, 4}). For every additional symmetric difference you take (say on a set D = {2, 3}), you should get the set with elements which are in either of the two the sets but not both (C △ D = {1, 4} △ {2, 3} = {1, 2, 3, 4}). The resulting array must contain only unique values (no duplicates).
```

# My Answer

```
function symmetricDifference() {
  // var combinedArray = arguments[0].concat(arguments[1]);

  // var set = [...new Set(combinedArray)];

  // console.log(set);
  let difference = arguments[0]
                 .filter(x => !arguments[1].includes(x))
                 .concat(arguments[1].filter(x => !arguments[0].includes(x)));

  return difference.sort(function(a, b){return a-b});
}

symmetricDifference([1, 2, 3], [5, 2, 1, 4]);
```

# Comments & Hurdles

-
