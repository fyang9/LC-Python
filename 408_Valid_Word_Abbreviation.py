class Solution:
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i, j = 0, 0
        while i < len(abbr):
            if j >= len(word):
                return False
            if not abbr[i].isdigit():
                if abbr[i] != word[j]:
                    return False
                i += 1
                j += 1
            else:
                if abbr[i] == '0':
                    return False
                n = ''
                while i < len(abbr) and abbr[i].isdigit():
                    n += abbr[i]
                    i += 1
                j += int(n)
        return j == len(word)






    """
        Time Complexity = O(n)
        Space Complexity = O(1)

        Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.

        A string such as "word" contains only the following valid abbreviations:

        ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
        Notice that only the above abbreviations are valid abbreviations of the string "word". Any other string is not a valid
        abbreviation of "word".

        Note:
        Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.

        Example:
        Given s = "internationalization", abbr = "i12iz4n":
        Return true.
    """
