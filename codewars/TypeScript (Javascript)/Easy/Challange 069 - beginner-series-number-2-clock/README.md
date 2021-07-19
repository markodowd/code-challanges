# The Challange

https://www.codewars.com/kata/beginner-series-number-2-clock/train/javascript

```
Clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.

Your task is to make 'Past' function which returns time converted to miliseconds.

#####Example:

past(0, 1, 1) == 61000
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- Simple maths

# Favourite Answer (By Others)

```
function past(h, m, s){
  return ((h*3600)+(m*60)+s)*1000;
}
```
