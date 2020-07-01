''' Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Example 1:
Input: [2,2,1]   Output: 1
Example 2:
Input: [4,1,2,1,2]   Output: 4 '''

#Solution 1:
class Single:
    def single_no (self,num):
        num1 = []
        for elem in num:
            if elem not in num1:
                num1.append(elem)
            else:
                num1.remove(elem)
        return num1[0]   
num_li = Single()
num_li.single_no([4,1,2,1,2])

#Solution 2: uding count()
class Single:
    def single_no (self,num):
        for elem in num:
            if num.count(elem)== 1:
                print(elem)
            else:
                pass
num = Single()
num.single_no([4,1,2,1,2])
