class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        lookup = {"(": ")", "{": "}", "[": "]"}
        for parenthese in s:
            if parenthese in lookup:
                stack.append(parenthese)
            elif len(stack) == 0 or lookup[stack.pop()] != parenthese:
                print("parenthese:", parenthese)
                return False
        return len(stack) == 0

if __name__ == "__main__":
    print(Solution().isValid("()[]"))






    """
        Time Complexity = O(N)
        Space Complexity = O(N)

        Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
        determine if the input string is valid.

        An input string is valid if:

        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Note that an empty string is also considered valid.

        Example:
        Input: "{[]}"
        Output: true
    """
