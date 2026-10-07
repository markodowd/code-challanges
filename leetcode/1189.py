class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        target = "balloon"
        valid = "balon"
        tracker = {}

        for char in text:
            if char in valid:
                tracker[char] = tracker.get(char, 0) + 1

        count = 0
        text_len = len(text)

        for i in range(text_len):
            for char in target:
                if char in tracker:
                    tracker[char] = tracker[char] - 1

                    if tracker[char] == 0:
                        del tracker[char]
                else:
                    return count

            count += 1

        return count
