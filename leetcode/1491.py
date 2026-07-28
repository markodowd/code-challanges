class Solution:
    def average(self, salary: list[int]) -> float:
        low = min(salary)
        high = max(salary)
        remove_values = {low, high}

        filtered_salaries = list(filter(lambda x: x not in remove_values, salary))

        avg = sum(filtered_salaries) / len(filtered_salaries)

        return avg


## Better
# class Solution:
#     def average(self, salary: list[int]) -> float:
#         total_sum = sum(salary)
#         min_sal = min(salary)
#         max_sal = max(salary)
#
#         return (total_sum - min_sal - max_sal) / (len(salary) - 2)


tester = Solution()

ans_1 = tester.average([4000, 3000, 1000, 2000])

assert ans_1 == 2500.00000
