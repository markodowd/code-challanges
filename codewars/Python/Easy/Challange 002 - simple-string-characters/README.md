# The Challange

https://www.codewars.com/kata/5a29a0898f27f2d9c9000058/train/python

```
In this Kata, you will be given a string and your task will be to return a list of ints detailing the count of uppercase letters, lowercase, numbers and special characters, as follows.

solve("*'&ABCDabcde12345") = [4,5,5,3].
--the order is: uppercase letters, lowercase, numbers and special characters.
```

# My Answer

```
- See .py file
```

# Comments & Hurdles

- Feel like my answer is over complicated
- Fav - actually wasn't too different just slightly better aproach

# Favourite Answer (By Others)

```
def solve(s):
    upper, lower, digit, other = 0, 0, 0, 0

    for c in s:
        if   c.isupper(): upper += 1
        elif c.islower(): lower += 1
        elif c.isdigit(): digit += 1
        else:             other += 1

    return [upper, lower, digit, other]
```
