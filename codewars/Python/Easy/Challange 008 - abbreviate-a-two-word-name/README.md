# The Challange

https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python

```
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

Patrick Feeney => P.F

```

# My Answer

```
- See .py file
```

# Comments & Hurdles

- Old answer of mine - simple to understand
- Fav - clever

# Favourite Answer (By Others)

```
def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()
```
