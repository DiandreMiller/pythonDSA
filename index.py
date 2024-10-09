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
            else:
                CHECK_FOR_EIGHT.append(numberArray[i])

        print('CHECK_FOR_EIGHT:', CHECK_FOR_EIGHT)
    
        return CHECK_FOR_EIGHT
    

solution = Solution()

print('removeNeighboringEights:',solution.removeNeighboringEights(NUM_ARRAY))
