# The Challange

https://www.codewars.com/kata/57158fb92ad763bb180004e7/train/python

```
You have an award-winning garden and everyday the plants need exactly 40mm of water. You created a great piece of JavaScript to calculate the amount of water your plants will need when you have taken into consideration the amount of rain water that is forecast for the day. Your jealous neighbour hacked your computer and filled your code with bugs.

Your task is to debug the code before your plants die!
```

# My Answer

```
- See .py file
```

# Comments & Hurdles

- Simple if else
- Fav - clever lambda approach

# Favourite Answer (By Others)

```
rain_amount = lambda m: ["Your plant has had more than enough water for today!", "You need to give your plant {}mm of water"][m<40].format(40-m)
```
