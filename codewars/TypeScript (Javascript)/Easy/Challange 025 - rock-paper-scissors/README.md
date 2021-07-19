# The Challange

https://www.codewars.com/kata/rock-paper-scissors/train/javascript

```
Rock Paper Scissors

Let's play! You have to return which player won! In case of a draw return Draw!.

Examples:

rps('scissors','paper') // Player 1 won!
rps('scissors','rock') // Player 2 won!
rps('paper','paper') // Draw!
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- The if statement seems a little convoluted
- Didn't think switch statement allowed on codewars because of 'break';

# Favourite Answer (By Others)

```
function rps(p1, p2) {
  var choices = ['rock', 'paper', 'scissors'];
  var x = choices.indexOf(p1);
  var y = choices.indexOf(p2);

  if (x === y) return 'Draw!';
  if (x === 0 && y === 2) return 'Player 1 won!';
  if (x === 2 && y === 0) return 'Player 2 won!';
  if (x > y) return 'Player 1 won!'
  else return 'Player 2 won!';
}
```
