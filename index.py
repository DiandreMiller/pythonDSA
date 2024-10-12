#STACK

# Given an array of intergers, remove all occurence of neighboring elements that add up to 8. If the 
# removal of two integers creates a new pair that adds up to 8, remove those elements as well. 

NUM_ARRAY = [1,2,3,5,6,9]

from typing import List

class Solution:
    def removeNeighboringEights (self, numberArray: List[int]) -> List[int]:

        CHECK_FOR_EIGHT = []

        for i in range(len(numberArray)):
            if CHECK_FOR_EIGHT and CHECK_FOR_EIGHT[-1] + numberArray[i] == 8:
                CHECK_FOR_EIGHT.pop()
                print('CHECK_FOR_EIGHT1:', CHECK_FOR_EIGHT)
            else:
                CHECK_FOR_EIGHT.append(numberArray[i])
                print('CHECK_FOR_EIGHT2:', CHECK_FOR_EIGHT)

    
        return CHECK_FOR_EIGHT
    

solution = Solution()

print('removeNeighboringEights:',solution.removeNeighboringEights(NUM_ARRAY))

# Given an integer array X[] of size n, write a program to find all the leaders in the array X[]. 
# An element is a leader if it is strictly greater than all the elements to its right side.



# Input: X[] = [16, 17, 4, 3, 5, 2], Output: [17, 5, 2]
# Input: X[] = [6, 5, 4, 3, 2, 1], Output: [6, 5, 4, 3, 2, 1]
# Input: X[] = [1, 2, 3, 4, 5, 6], Output: [6]

class Answer:
    def getHighestRightWardNumber (self, numberArray: List[int]) -> List[int]:

        LARGEST_RIGHT_NUMBER = []
        smallest_number = float('-inf') 
    
        for i in numberArray[::-1]:
            if i > smallest_number:
                smallest_number = i
                LARGEST_RIGHT_NUMBER.append(i)

        
        return LARGEST_RIGHT_NUMBER[::-1]
            




answer = Answer()

print('getHighestRightWardNumber:', answer.getHighestRightWardNumber([16, 17, 4, 3, 5, 2]))
print('getHighestRightWardNumber:', answer.getHighestRightWardNumber([1, 2, 3, 4, 5, 6]))
print('getHighestRightWardNumber:', answer.getHighestRightWardNumber([6, 5, 4, 3, 2, 1]))

class Answer2:
    def stictlyIncreasing(self, numberArray) -> bool:

        true_or_false = True
        increasing_or_decreasing = 1
        pointer = 1

        for i in range(len(numberArray)):
            if numberArray[i] < numberArray[pointer]:
                pointer += 1
                continue
            elif numberArray[i] > numberArray[pointer]:
                true_or_false = False
                if not true_or_false:
                    increasing_or_decreasing += 1



        return increasing_or_decreasing == 2
    
answer2 = Answer2()
print('stictlyIncreasing:', answer2.stictlyIncreasing([1,2,6,5,3]))
print('stictlyIncreasing:', answer2.stictlyIncreasing([5,8,8]))
print('stictlyIncreasing:', answer2.stictlyIncreasing([5,2,1,4]))


# Given an integer array nums sorted in non-decreasing order, return an array of the squares of 
# each number sorted in non-decreasing order.

 

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
                
class SortedSquaredNumbers:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        SORTED_SQUARED_NUMBERS_ARRAY = [None] * len(nums)

        left = 0
        right = len(nums) - 1
        position_in_array = len(nums) - 1

        while(left <= right):

            LEFT_SQUARED_NUMBERS = nums[left] ** 2
            RIGHT_SQUARED_NUMBERS = nums[right] ** 2

            if LEFT_SQUARED_NUMBERS > RIGHT_SQUARED_NUMBERS:
                SORTED_SQUARED_NUMBERS_ARRAY[position_in_array] = LEFT_SQUARED_NUMBERS
                left += 1
            else:
                SORTED_SQUARED_NUMBERS_ARRAY[position_in_array] = RIGHT_SQUARED_NUMBERS
                right -= 1
            position_in_array -= 1

        return SORTED_SQUARED_NUMBERS_ARRAY
    
sortedSquaredNumbers = SortedSquaredNumbers()
print('sortedSquares:', sortedSquaredNumbers.sortedSquares([-4,-1,0,3,10]))
print('sortedSquares:', sortedSquaredNumbers.sortedSquares([-7,-3,2,3,11]))
            


