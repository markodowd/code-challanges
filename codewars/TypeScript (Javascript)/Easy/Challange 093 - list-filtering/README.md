# The Challange

https://www.codewars.com/kata/list-filtering/train/javascript

```
In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.
Example

filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- filter() with a typeof() check

# Favourite Answer (By Others)

```
function filter_list(l) {
  return l.filter(e => Number.isInteger(e));
}
```
