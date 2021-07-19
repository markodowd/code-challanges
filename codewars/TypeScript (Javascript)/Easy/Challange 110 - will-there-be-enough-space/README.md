# The Challange

https://www.codewars.com/kata/will-there-be-enough-space/train/javascript

```
Task Overview:

You have to write a function that accepts three parameters:

    cap is the amount of people the bus can hold excluding the driver.
    on is the number of people on the bus.
    wait is the number of people waiting to get on to the bus.

If there is enough space, return 0, and if there isn't, return the number of passengers he can't take.
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- Managed to make it a concise 1 line arrow func
- Fav - even cleaner but does require Math module

# Favourite Answer (By Others)

```
const enough = (cap, on, wait) => Math.max(0,wait-cap+on);
```
