class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []

        for char in s:
            if char == "#":
                if len(s_stack) > 0:
                    s_stack.pop()
                continue

            s_stack.append(char)

        for char in t:
            if char == "#":
                if len(t_stack) > 0:
                    t_stack.pop()
                continue

            t_stack.append(char)

        return "".join(s_stack) == "".join(t_stack)
