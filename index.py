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
    def getHighestRightWardNumber (self, numberArray: List[int]):

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
                
