import numpy as np


class Solution:
    def concatHex36(self, n: int) -> str:
        squared = n**2
        trippled = n**3

        return np.base_repr(squared, base=16) + np.base_repr(trippled, base=36)
