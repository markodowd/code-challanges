const VOWELS = 'aeiouAEIOU'

function reverseVowels(s: string): string {
    let stringArr = Array(s.length).fill(null);

    let stringVowels: string[] = [];

    for (let i = 0; i < s.length; i++) {
        if (VOWELS.includes(s[i])) {
            stringVowels.push(s[i])
        } else {
            stringArr[i] = s[i]
        }
    }

    for (let i = 0; i < s.length; i++) {
        if (stringArr[i] === null) {
            const char = stringVowels.pop()
            stringArr[i] = char
        }
    }

    return stringArr.join('')
};
