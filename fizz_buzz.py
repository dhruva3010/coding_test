from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            result.append(self.isFizzBuzz(i))
        return result

    def isFizzBuzz(self, n: int) -> str:
        if (n % 3 == 0) and (n % 5 == 0):
            return "FizzBuzz"
        if (n % 3 == 0):
            return "Fizz"
        if (n % 5 == 0):
            return "Buzz"
        return str(n)
    
print(Solution().fizzBuzz(3))
print(Solution().fizzBuzz(5))
print(Solution().fizzBuzz(15))
