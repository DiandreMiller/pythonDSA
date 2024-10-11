// # Given an integer array X[] of size n, write a program to find all the leaders in the array X[]. 
// # An element is a leader if it is strictly greater than all the elements to its right side.



// # Input: X[] = [16, 17, 4, 3, 5, 2], Output: [17, 5, 2]
// # Input: X[] = [6, 5, 4, 3, 2, 1], Output: [6, 5, 4, 3, 2, 1]
// # Input: X[] = [1, 2, 3, 4, 5, 6], Output: [6]

//Time complexity O(n^2)
//Space complexity 0(n)


// const largestRightNumber = (numberArray) => {

//     const largestRightNumberArray = []

//     while(numberArray.length > 0) {
//         const maximumNumber = Math.max(...numberArray);
//         const indexOfMaximumNumber = numberArray.indexOf(maximumNumber);
//         largestRightNumberArray.push(maximumNumber);
//         numberArray.splice(0, indexOfMaximumNumber + 1);
//         // console.log('numberArray:', numberArray);
//     }

   
//     // console.log('largestRightNumberArray:', largestRightNumberArray);

//     return largestRightNumberArray;

// }

// console.log(largestRightNumber([16, 17, 4, 3, 5, 2]));
// console.log(largestRightNumber([6, 5, 4, 3, 2, 1]));
// console.log(largestRightNumber([1, 2, 3, 4, 5, 6]));
// console.log(largestRightNumber([1,1,1,1]));


const largestRightNumberOptimized = (numberArray) => {
    const largestRightNumberArray = [];
    let maximumNumber = -Infinity; 
    
    for (let i = numberArray.length - 1; i >= 0; i--) {
        if (numberArray[i] > maximumNumber) {
            maximumNumber = numberArray[i];  
            largestRightNumberArray.push(maximumNumber); 
        }
    }
    
    return largestRightNumberArray.reverse();
}



console.log(largestRightNumberOptimized([16, 17, 4, 3, 5, 2]));
console.log(largestRightNumberOptimized([6, 5, 4, 3, 2, 1]));
console.log(largestRightNumberOptimized([1, 2, 3, 4, 5, 6]));
console.log(largestRightNumberOptimized([1,1,1,1]));