from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        decoded = [first]

        for i in range(len(encoded)):
            decoded.append(encoded[i] ^ decoded[i])

        return decoded
