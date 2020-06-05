''' Given an input string, reverse the string word by word.
Example 1:
Input: "the sky is blue"      Output: "blue is sky the"
Example 2:
Input: "  hello world!  "     Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:
Input: "a good   example"     Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
Note:
A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or 
trailing spaces. You need to reduce multiple spaces between two words to a single space in the reversed string.'''


# Solution: using .join()
class ReverseString:
    def revStr(self, string):
        li = string.split()
        rev = (li[:])[::-1]
        ans = ' '.join(rev)
        return ans

obj = ReverseString()
obj.revStr("  hello world!  ")


# Solution 2: whitout any func use
class ReverseString:
    def revStr(self, string):
        li = string.split()
        rev = (li[:])[::-1]
        ans = ''
        for word in rev:
            ans += ' ' + word
        return ans

obj = ReverseString()
obj.revStr("a good   example")
