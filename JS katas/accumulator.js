// https://www.codewars.com/kata/541c8630095125aba6000c00/train/javascript
function digitalRoot(n) {
    let nArray = Math.abs(n).toString().split('');

    while (nArray.length > 1) {
    let sum = nArray.reduce((accumulator, currentValue) => accumulator + parseInt(currentValue), 0);
    nArray = sum.toString().split('');
}

   return parseInt(nArray[0]);
}
console.log(digitalRoot(1));

// la plus concise
// function digital_root(n) {
//     return (n - 1) % 9 + 1;
//   }

// clever
// function digital_root(n) {
//     if (n < 10) return n;
    
//     return digital_root(
//       n.toString().split('').reduce(function(acc, d) { return acc + +d; }, 0));
//   }

// -----------------------other solution------------------------
// function digitalRoot(n) {
//     const nArray = Math.abs(n).toString().split('');

//     if (nArray.length === 1) {
//         return parseInt(nArray[0]);
//     } else {
//         const sum = nArray.reduce((accumulator, currentValue) => accumulator + parseInt(currentValue), 0);
//         return digitalRoot(sum);
//     }
// }

// console.log(digitalRoot(2568));

// ----------CHAT GPT--------
// function digitalRoot(n) {
//     // Base case: If n is a single-digit number, return n
//     if (n < 10) {
//       return n;
//     }
  
//     // Convert the number to a string to easily iterate over its digits
//     const digits = n.toString().split('').map(Number);
  
//     // Sum the digits
//     const sum = digits.reduce((acc, digit) => acc + digit, 0);
  
//     // Recursively call digitalRoot with the sum
//     return digitalRoot(sum);
//   }
  
//   // Example usage:
//   const result = digitalRoot(942);
//   console.log(result); // Output: 6 (because 9 + 4 + 2 = 15, and 1 + 5 = 6)