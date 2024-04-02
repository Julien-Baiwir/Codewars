let numbers0= [];
let numbers = [ 1, 5.2 , 4 , 0 ];

function sum (numbers) {
 "use strict";
 if (numbers.length === 0) {
  return 0; 
}
let addition = 0;
for (let i = 0; i < numbers.length; i++) {
  addition += numbers[i];
}
return addition; 
}
console.log(sum(numbers)); 

function sum(numbers) {
  return numbers.reduce((a, b) => a + b, 0);
}