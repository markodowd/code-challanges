# Author: Mark O'Dowd
# Email: contact@markodowd.dev
# LeetCode: https://leetcode.com/u/markodowd

class Solution:  # Define a class named Solution (commonly used in LeetCode problems).
    def isValid(
        self, s: str
    ) -> bool:  # Define a method that checks if a string of brackets is valid.
        opening_brackets = "({["  # Define a string containing opening brackets.
        stack = []  # Initialize an empty list to use as a stack.

        for char in s:  # Iterate over each character in the input string.
            if char in opening_brackets:  # If the character is an opening bracket,
                stack.append(char)  # Push it onto the stack.
                continue  # Continue to the next iteration of the loop.

            if (
                not stack
            ):  # If the stack is empty (i.e., there's no matching opening bracket),
                return False  # The string is invalid, so return False.

            top = stack.pop()  # Pop the last added opening bracket from the stack.
            if (  # Check if the current closing bracket does not match the popped opening bracket.
                (char == ")" and top != "(")  # Mismatch for parentheses.
                or (char == "}" and top != "{")  # Mismatch for curly brackets.
                or (char == "]" and top != "[")  # Mismatch for square brackets.
            ):
                return False  # If there’s a mismatch, return False.

        return (
            not stack
        )  # If the stack is empty at the end, return True; otherwise, return False.


solution = Solution()

assert solution.isValid("()") is True
assert solution.isValid("()[]{}") is True
assert solution.isValid("(]") is False
assert solution.isValid("([])") is True
assert solution.isValid("]") is False
