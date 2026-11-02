class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)  # easiest sol

        # map sol
        map_s = {}
        for char in s:
            if char not in map_s:
                map_s[char] = 0
            count = map_s[char]
            map_s[char] = count + 1

        for char in t:
            if char not in map_s:
                return False
            count = map_s[char]
            map_s[char] = count - 1

        for val in map_s.values():
            if val != 0:
                return False
        return True
