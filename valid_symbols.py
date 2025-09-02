class Solution:
    def valid_symbols(self, s: str) -> bool:
        stack = []
        match = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in match.values():          # opening bracket
                stack.append(ch)
            elif ch in match:                  # closing bracket
                if not stack or stack[-1] != match[ch]:
                    return False
                stack.pop()
            else:
                # Unexpected character (if inputs may include others)
                return False

        return not stack
