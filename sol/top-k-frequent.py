class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}  # num : count

        for num in nums:
            if num not in m:
                m[num] = 0

            m[num] += 1

        return sorted(m, key=m.get, reverse=True)[:k]
