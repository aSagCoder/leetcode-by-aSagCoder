class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        total = sum(salary) - salary[0] - salary[-1]

        return total / (len(salary) - 2)
