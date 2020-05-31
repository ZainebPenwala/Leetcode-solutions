''' Given a 32-bit signed integer, reverse digits of an integer.
Example 1:
  Input: 123     Output: 321
Example 2:
  Input: -123    Output: -321
Example 3:
  Input: 120     Output: 21 '''
 
  
# Solution: 
class Reverse:
  def reverse(self, num):
      string = str(num)
      if '-' in string:
          t = string.strip('-')
          mid = t[::-1]
          ans = int('-' + mid)
      else:
          mid = string[::-1]
          ans = int(mid)
      return ans
    
obj = Reverse()
obj.reverse(120)
