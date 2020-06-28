''' Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.
We repeatedly make duplicate removals on S until we no longer can.
Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.
Example 1:
Input: "abbaca"  =>  Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca". '''

#Solution:
class Duplicate:
    def remove_dulplicates(self, s):
        li = list(s)
        li1 = []
        for elem in li:
            if elem not in li1:
                li1.append(elem)
            else:
                li1.remove(elem)
        s1 = ''.join(elem for elem in li1)
        return s1
string_1 = Duplicate()
string_1.remove_dulplicates('abbaca')
