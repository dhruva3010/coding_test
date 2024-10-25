class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while(1):
            if num == 0:
                break

            if num % 2 == 0:
                num /= 2
                steps += 1
            else:
                num -= 1
                steps += 1

        return steps

print(Solution().numberOfSteps(14))
