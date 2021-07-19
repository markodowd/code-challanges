# The Challange

https://www.codewars.com/kata/fake-binary/train/javascript

```
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- Supposed to be an easy one but struggled with this and got a very convoluted answer
- The favourite is approach I was taking but Number() was throwing me off

# Favourite Answer (By Others)

```
function fakeBin(str){
  var newStr = "";
  for(var i=0;i<str.length;i++){
    if(Number(str[i])>=5){
      newStr += "1"
    }
    else{
      newStr += "0";
    }
  }
  return newStr;
}
```
