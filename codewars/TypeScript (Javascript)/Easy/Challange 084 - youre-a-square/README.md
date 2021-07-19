# The Challange

https://www.codewars.com/kata/youre-a-square/train/javascript

```
Task

Given an integral number, determine if it's a square number:

    In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.

The tests will always use some integral number, so don't worry about that in dynamic typed languages.
Examples

is_square (-1) # => false
is_square   0 # => true
is_square   3 # => false
is_square   4 # => true
is_square  25 # => true
is_square  26 # => false
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- Math.sqrt(n) perfect to solve

# Favourite Answer (By Others)

```
const isSquare = n => Number.isInteger(Math.sqrt(n));
```
