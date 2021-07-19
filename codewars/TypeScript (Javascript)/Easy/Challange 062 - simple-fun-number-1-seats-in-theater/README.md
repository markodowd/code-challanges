# The Challange

https://www.codewars.com/kata/simple-fun-number-1-seats-in-theater/train/javascript

```
Task

Your friend advised you to see a new performance in the most popular theater in the city. He knows a lot about art and his advice is usually good, but not this time: the performance turned out to be awfully dull. It's so bad you want to sneak out, which is quite simple, especially since the exit is located right behind your row to the left. All you need to do is climb over your seat and make your way to the exit.

Given the total number of rows and columns in the theater (nRows and nCols, respectively), and the row and column you're sitting in, return the number of people who sit strictly behind you and in your column or to the left, assuming all seats are occupied.
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- Just math calculation

# Favourite Answer (By Others)

```
function seatsInTheater(nCols, nRows, col, row) {
  var totalObstructedRows = nRows - row;
  var totalObstructedCols = nCols - (col - 1);

  return totalObstructedRows * totalObstructedCols;
}
```
