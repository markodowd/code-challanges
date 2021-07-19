# The Challange

https://www.codewars.com/kata/get-the-mean-of-an-array/train/javascript

```
It's the academic year's end, fateful moment of your school report. The averages must be calculated. All the students come to you and entreat you to calculate their average for them. Easy ! You just need to write a script.

Return the average of the given array rounded down to its nearest integer.

The array will never be empty.
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- Math.floor() to round down
- reduce() to get total
- divide by array length for average

# Favourite Answer (By Others)

```
function getAverage(marks){
  return Math.floor(marks.reduce((sum, x) => sum + x) / marks.length);
}
```
