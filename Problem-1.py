#  Two Sum
'''
Leetcode all test cases passed: Yes
Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n is the length of nums
        Space Complexity: O(n)
        Time Complexity: O(n)
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
