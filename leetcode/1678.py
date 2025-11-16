# Author: Mark O'Dowd
# Email: contact@markodowd.dev
# LeetCode: https://leetcode.com/u/markodowd

class Solution:
    def interpret(self, command: str) -> str:
        result = ""

        for idx, char in enumerate(command):
            if char == "G":
                result += "G"

            if char == "(" and command[idx + 1] == ")":
                result += "o"

            if char == "(" and command[idx + 1] == "a":
                result += "al"

        return result
