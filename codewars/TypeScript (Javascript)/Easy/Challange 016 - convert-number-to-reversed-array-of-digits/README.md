# The Challange

https://www.codewars.com/kata/convert-number-to-reversed-array-of-digits/train/javascript

```
Convert number to reversed array of digits

Given a random number:

    C#: long;
    C++: unsigned long;

You have to return the digits of this number within an array in reverse order.
Example:

348597 => [7,9,5,8,4,3]
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- Converted number to string first to get the length so could loop each digit
- Created a new array then used parseInt() to change each 'string digit' back to an int
- Used reverse() on the new array to get the result

# Favourite Answer (By Others)

```
function digitize(n) {
  return String(n).split('').map(Number).reverse()
}
```
