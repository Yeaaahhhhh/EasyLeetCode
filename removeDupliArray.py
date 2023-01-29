#Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

#Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

#Return k after placing the final result in the first k slots of nums.

#Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

#Custom Judge:

#The judge will test your solution with the following code:

#int[] nums = [...]; // Input array
#int[] expectedNums = [...]; // The expected answer with correct length

#int k = removeDuplicates(nums); // Calls your implementation

#assert k == expectedNums.length;
#for (int i = 0; i < k; i++) {
    #assert nums[i] == expectedNums[i];
#}

#If all assertions pass, then your solution will be accepted.

#add comments

# my solution
class Solution(object):
    def removeduplicates(self,nums):
        #newSet = set(nums)
        #nums = list(newSet)
        #print(nums)
        #return len(nums)
        pass
        #pass
#sample solution
class Solution:
    def removeDuplicates(self, nums) -> int:
        n=len(nums)
        if n == 0 or n == 1:
            return n
        j = 1
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        return j

#so = Solution()
#aList = [1,1,2,2,2,3,3,4]
#print(so.removeDuplicates(aList))


# Review
# It consider the most simple cases when length == 0 or 1, then j is the j th index
# Here j starts at '1', nums[i] compare with previous, if not equal, then change


class Solution:
    def removeDuplicates(self,nums) -> int:
        print(set(nums))
        nums[:] = sorted(set(nums))
        print(set(nums))
        return len(nums) 
    
    #set is not in sorted
so = Solution()
aList = [7,2,3,1,1,2,2,2,3,3,4]
print(so.removeDuplicates(aList))