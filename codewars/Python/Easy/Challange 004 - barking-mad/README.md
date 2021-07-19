# The Challange

https://www.codewars.com/kata/54dba07f03e88a4cec000caf/train/python

```
Teach snoopy and scooby doo how to bark using object methods. Currently only snoopy can bark and not scooby doo.

snoopy.bark() #return "Woof"
scoobydoo.bark() #undefined

Use method prototypes to enable all Dogs to bark.

```

# My Answer

```
- See .py file
```

# Comments & Hurdles

- Technically I got the answer but it wasn't the right approach to take
- Fav - proper use of class

# Favourite Answer (By Others)

```
class Dog ():
  def __init__(self, breed):
    self.breed = breed
  def bark(self):
    return "Woof"

snoopy = Dog("Beagle")

scoobydoo = Dog("Great Dane")
```
