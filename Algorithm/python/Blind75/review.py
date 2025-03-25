from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}:{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []

        start = 0
        while start < len(s):
            colon = start
            while s[colon] != ":":
                colon += 1
            length = int(s[start:colon])
            colon += 1
            end = colon + length
            res.append(s[colon:end])
            start = end

        return res
