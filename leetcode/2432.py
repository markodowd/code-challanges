# Author: Mark O'Dowd
# Email: contact@markodowd.dev
# LeetCode: https://leetcode.com/u/markodowd

from typing import List


class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        employee_id = 0
        longest_task = 0
        previous_task_time = 0

        for i in range(len(logs)):
            units_worked = logs[i][1] - previous_task_time

            if units_worked > longest_task or (
                units_worked == longest_task and logs[i][0] < employee_id
            ):
                longest_task = units_worked
                employee_id = logs[i][0]

            previous_task_time = logs[i][1]

        return employee_id
