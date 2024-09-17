class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        hash_map = {}

        for word in s1.split():
            if word in hash_map:
                hash_map[word] = hash_map[word] + 1
            else:
                hash_map[word] = 1

        for word in s2.split():
            if word in hash_map:
                hash_map[word] = hash_map[word] + 1
            else:
                hash_map[word] = 1

        unique_keys = [key for key, value in hash_map.items() if value == 1]

        return unique_keys
