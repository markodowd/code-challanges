# The Challange

https://www.codewars.com/kata/credit-card-mask/train/javascript

```
Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'.
Examples

maskify("4556364607935616") == "############5616"
maskify(     "64607935616") ==      "#######5616"
maskify(               "1") ==                "1"
maskify(                "") ==                 ""
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- Only applies to strings longer than 4
- Replaced 0 up to -4 with #s of the same amount
- fav - slice before replace much easier

# Favourite Answer (By Others)

```
function maskify(cc) {
  return cc.slice(0, -4).replace(/./g, '#') + cc.slice(-4);
}
```
