class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l_ptr = 0
        r_ptr = len(s) - 1
        s_arr = list(s)

        while l_ptr < r_ptr:
            if not s_arr[l_ptr].isalpha():
                l_ptr += 1
            elif not s_arr[r_ptr].isalpha():
                r_ptr -= 1
            else:
                s_arr[l_ptr], s_arr[r_ptr] = s_arr[r_ptr], s_arr[l_ptr]
                l_ptr += 1
                r_ptr -= 1

        return "".join(s_arr)


tester = Solution()

ans_1 = tester.reverseOnlyLetters("ab-cd")
ans_2 = tester.reverseOnlyLetters("a-bC-dEf-ghIj")

assert ans_1 == "dc-ba"
assert ans_2 == "j-Ih-gfE-dCba"
