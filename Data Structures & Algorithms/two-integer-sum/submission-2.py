class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # i need to return the indices
        # the indices cannot be the same
        # return the smaller index first
        
        hashmap = {} # number : index

        # nums.sort()
        for i,n in enumerate(nums):
            diff = target -  n
            if diff in hashmap:
                return [hashmap[diff],i]
            else:
                hashmap[n] = i
