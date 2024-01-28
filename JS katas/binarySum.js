// https://www.codewars.com/kata/551f37452ff852b7bd000139/train/javascript
// Décimal 13 en binaire :
// 13 / 2 = 6 reste 1
// 6 / 2 = 3 reste 0
// 3 / 2 = 1 reste 1
// 1 / 2 = 0 reste 1
// En lisant les restes dans l'ordre inverse : 1101.
// Binaire 1011 en décimal :
// (1 * 2^3) + (0 * 2^2) + (1 * 2^1) + (1 * 2^0) = 8 + 0 + 2 + 1 = 11.

function addBinary(a,b) {
    let sum = a + b;
    let resultArray = [];
    
    while ( sum >= 1){
        resultArray.push(sum % 2);
        sum = Math.floor(sum / 2);
     }
     if (sum > 0) {
        resultArray.push(1);
      }
    return(resultArray.reverse().join(''));  
     }
    console.log(addBinary(10,3));

    // ---best practice---
    // function addBinary(a,b){
    //     return (a+b).toString(2)
    //   }