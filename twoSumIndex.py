#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.



#Example 1:

#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

#Example 2:

#Input: nums = [3,2,4], target = 6
#Output: [1,2]

#Example 3:

#Input: nums = [3,3], target = 6
#Output: [0,1]

# my first try
class Solution: 
    def twoSum(self,nums:list[int], target:int) ->list[int]:
        self.answerList = []
        self.nums = nums
        self.target = target
        self.want = 0
        for i in self.nums:
            self.want = self.target - i
            for j in self.nums:
                if self.want == j:
                    self.answerList.append(self.nums.index(i))
                    self.answerList.append(self.nums.index(j))
                    return self.answerList


aList = [7,3,1,1,1,2,3,4]
aList.pop(1)
print(aList) 
#so = Solution()
#print(so.twoSum([2,7,11,15],9))


#sample solution

class Solution: 
    def twoSum(self,nums:list[int], target:int) ->list[int]:
        seen = {}
        for i,value in enumerate(nums):    # i is the index, value is value
            remaining = target - nums[i]   # quite similar as my self.want
            if remaining in seen:
                return [i,seen[remaining]]  #so that it is a pair
            seen[value] = i        #seen is a dicitonary, key is VALUE, value is i, the index
            


#review:
# the use of enumerate
#seq = ['one', 'two', 'three']
#>>> for i, element in enumerate(seq):
#...     print i, element
#...
#0 one
#1 two
#2 three   so that we can get the index directly, and avoid the duplicate like [0,0]

#newSet = set(nums)
#nums = list(newSet)
#return len(nums)
