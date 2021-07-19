# The Challange

https://www.codewars.com/kata/dubstep/train/javascript

```
Input

The input consists of a single non-empty string, consisting only of uppercase English letters, the string's length doesn't exceed 200 characters
Output

Return the words of the initial song that Polycarpus used to make a dubsteb remix. Separate the words with a space.
Examples

songDecoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
  // =>  WE ARE THE CHAMPIONS MY FRIEND
```

# My Answer

```
- See .js file
```

# Comments & Hurdles

- split('WUB') for separate chars, filter(Boolean) removes '' elements in the array then rejoined for answer.
- Fav - Regex answer is nice but regex generally takes more effort to come up with.

# Favourite Answer (By Others)

```
function songDecoder(song){
  return song.replace(/(WUB)+/g," ").trim()
}
```
