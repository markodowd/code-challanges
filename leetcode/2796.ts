// Author: Mark O'Dowd
// Email: contact@markodowd.dev
// LeetCode: https://leetcode.com/u/markodowd

interface String {
    replicate(times: number): string;
}

String.prototype.replicate = function(times): string {
    let original = this.valueOf();
    let answer = "";

    for (let i = 1; i <= times; i++) {
        answer += original;
    }

    return answer;
}

