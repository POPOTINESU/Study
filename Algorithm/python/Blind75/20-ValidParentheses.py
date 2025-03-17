class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        start_parentheses = ("(", "{", "[")

        for c in s:
            if c in start_parentheses:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if (
                    (c == ")" and top != "(")
                    or (c == "}" and top != "{")
                    or (c == "]" and top != "[")
                ):
                    return False

        return len(stack) == 0
