// // "https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/javascript"

function createPhoneNumber(numbers) {
    return "(" + numbers.slice(0, 3).toString().replace(/,/g, '') + ") " +
           numbers.slice(3, 6).toString().replace(/,/g, '') + "-" +
           numbers.slice(6, 10).toString().replace(/,/g, '');
}

let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0];
console.log(createPhoneNumber(numbers));

// // ---best practice------
// function createPhoneNumber(numbers){
//     var format = "(xxx) xxx-xxxx";
    
//     for(var i = 0; i < numbers.length; i++)
//     {
//       format = format.replace('x', numbers[i]);
//     }
    
//     return format;
//   }
  
// //   ---other options----
// function createPhoneNumber(numbers){
//     numbers = numbers.join('');
//     return '(' + numbers.substring(0, 3) + ') ' 
//         + numbers.substring(3, 6) 
//         + '-' 
//         + numbers.substring(6);
//   }

//   function createPhoneNumber(numbers){
//     return numbers.join('').replace(/(...)(...)(.*)/, '($1) $2-$3');
//   }

//   function createPhoneNumber(numbers){
//     return numbers.reduce((p,c) => p.replace('x',c), "(xxx) xxx-xxxx");
//  }

//  function createPhoneNumber(numbers){
//     return '(' + numbers.slice(0,3).join('') + ') ' + numbers.slice(3,6).join('') + '-' + numbers.slice(6).join('');
//   }