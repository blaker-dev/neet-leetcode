class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []  # array of sublists

        m = {}  # sorted str : List[str]

        for i, word in enumerate(strs):
            sstr = "".join(sorted(word))
            if sstr not in m:
                m[sstr] = []  # add a default value (new list)
            m[sstr].append(word)  # update list with word
        # add all words to output
        for sublists in m.values():
            out.append(sublists)
        return out
