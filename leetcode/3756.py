MOD = 10**9 + 7


class Solution:
    def _build_prefix_data(
        self, s: str
    ) -> tuple[list[int], list[int], list[int], list[int]]:
        n = len(s)

        pref_sum = [0] * (n + 1)
        pref_cnt = [0] * (n + 1)
        pref_num = [0] * (n + 1)

        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        for i, ch in enumerate(s):
            val = int(ch)
            pref_sum[i + 1] = pref_sum[i] + val

            if val != 0:
                pref_cnt[i + 1] = pref_cnt[i] + 1
                pref_num[i + 1] = (pref_num[i] * 10 + val) % MOD
            else:
                pref_cnt[i + 1] = pref_cnt[i]
                pref_num[i + 1] = pref_num[i]

        return pref_sum, pref_cnt, pref_num, pow10

    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        pref_sum, pref_cnt, pref_num, pow10 = self._build_prefix_data(s)
        output = []

        for x, y in queries:
            k = pref_cnt[y + 1] - pref_cnt[x]

            if k == 0:
                output.append(0)
                continue

            total_sum = pref_sum[y + 1] - pref_sum[x]
            x_val = (pref_num[y + 1] - pref_num[x] * pow10[k]) % MOD

            output.append((x_val * total_sum) % MOD)

        return output
