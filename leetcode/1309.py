class Solution:
    # Defining a method: defining a function has no runtime/memory cost at execution.
    def num_to_char(self, n: str) -> str:
        # Time: O(1) | Space: O(1)
        # int(n) takes constant time since n is at most 2 digits long.
        # Adding 96 and converting via chr() operate on fixed-size integers.
        return chr(int(n) + 96)

    def freqAlphabets(self, s: str) -> str:
        # Time: O(1) | Space: O(1)
        # Variable assignment creates an empty string; uses constant initial space.
        answer = ""

        # Time: O(1) | Space: O(1)
        # Initializing a local variable with a tiny string literal.
        temp = ""

        # Time: O(1) | Space: O(1)
        # Primitive integer allocation takes fixed 64-bit space.
        count = 0

        # Time: O(1) | Space: O(1)
        # Primitive boolean allocation takes fixed space.
        tracking = False

        # Time: O(N) | Space: O(N)
        # Slicing s[::-1] constructs a new string copy of length N, using O(N) memory.
        # The loop header itself executes N times, controlling overall time complexity.
        for val in s[::-1]:
            # Time: O(1) | Space: O(1)
            # Comparing single-character strings takes constant time per iteration.
            if val == "#":
                # Time: O(1) | Space: O(1)
                # Reassigning a boolean state variable takes constant time and memory.
                tracking = True

                # Time: O(1) | Space: O(1)
                # Continuing to the next loop iteration is a instantaneous control flow step.
                continue

            # Time: O(1) | Space: O(1)
            # Evaluating a boolean variable takes constant time per iteration.
            if tracking:
                # Time: O(1) | Space: O(1)
                # Incrementing a tiny integer is an O(1) primitive arithmetic operation.
                count += 1

                # Time: O(1) | Space: O(1)
                # Appending a character to temp; since temp length <= 2, it is strictly O(1).
                temp += val

                # Time: O(1) | Space: O(1)
                # Integer comparison takes constant time per iteration.
                if count == 2:
                    # Time: O(1) | Space: O(1)
                    # Reversing temp (max length 2) and calling num_to_char are both O(1).
                    # Appending 1 char to 'answer' averages O(1) time (amortized).
                    # Cumulatively across all steps, 'answer' consumes up to O(N) space.
                    answer += self.num_to_char(temp[::-1])

                    # Time: O(1) | Space: O(1)
                    # Reassigning a boolean flag back to False takes constant time.
                    tracking = False

                    # Time: O(1) | Space: O(1)
                    # Resetting integer counter takes constant time.
                    count = 0

                    # Time: O(1) | Space: O(1)
                    # Resetting string buffer to empty string takes constant time.
                    temp = ""

            # Time: O(1) | Space: O(1)
            # Executed when tracking is False; evaluates in constant time.
            else:
                # Time: O(1) | Space: O(1)
                # Converting single char via num_to_char and appending takes O(1) time.
                answer += self.num_to_char(val)

        # Time: O(N) | Space: O(N)
        # Slicing answer[::-1] reads up to N characters to build the final output string,
        # incurring a final O(N) time and O(N) auxiliary space allocation.
        return answer[::-1]
