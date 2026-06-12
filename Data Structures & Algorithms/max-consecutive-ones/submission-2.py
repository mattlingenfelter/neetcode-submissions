class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones = 0
        max = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                ones += 1
            else:
                if ones != 0 and ones > max:
                    max = ones
                    print(max)
                ones = 0
        if ones > max:
            max = ones
                
        return max