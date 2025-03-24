from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        response = []
        left = 0

        while left < len(s):
            right = left
            while s[right] != "#":
                right += 1
            length = int(s[left:right])

            left = right + 1
            right = left + length
            response.append(s[left:right])

            left = right

        return response


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

if __name__ == "__main__":
    c = Codec()
    e = c.encode(["Hello", "World"])
    assert c.decode(e) == ["Hello", "World"]
