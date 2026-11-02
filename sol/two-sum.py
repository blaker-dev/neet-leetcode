class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}  # val : index

        for i, n in enumerate(nums):
            b = target - n

            if b in m:
                return [m[b], i]  # index of b and i
            # pair not found
            m[n] = i
