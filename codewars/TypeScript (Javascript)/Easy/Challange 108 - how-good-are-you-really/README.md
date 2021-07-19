# The Challange

https://www.codewars.com/kata/how-good-are-you-really/train/javascript

```
There was a test in your class and you passed it. Congratulations!
But you're an ambitious person. You want to know if you're better than the average student in your class.

You receive an array with your peers' test scores. Now calculate the average and compare your score!

Return True if you're better, else False!
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- Simple check after getting average
- Fav - chose because mine was same as best

# Favourite Answer (By Others)

```
function betterThanAverage(classPoints, yourPoints) {
  // Your code here
  var classAvg = 0;
  for (var i = 0; i < classPoints.length; i++){
    classAvg += classPoints[i];
  }
  classAvg = classAvg/classPoints.length;
  return yourPoints > classAvg;
}
```
