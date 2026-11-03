class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        # 5#hello4#test
        #  ^^----
        #  ji
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            i = j + 1
            res.append(s[i : i + length])

            # Jump the pointer past the word
            i += length

        return res
