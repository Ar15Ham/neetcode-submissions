class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Input: 
        # 1) nums: array of integers
        # 2) target: integer
        # 
        # Output:
        # 1) [i, j]
        # 2) nums[i] + nums[j] == target
        # 3) i != j
        # 4) One pair satisfying condition
        #
        # Example: [3, 4, 5, 7] 
        # dif = 7 - 3 = 4
        # {'3': 0}
        # dif = 7 - 4 = 3
        # 
        hashmap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i






   
        