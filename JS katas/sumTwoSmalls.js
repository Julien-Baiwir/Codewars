let numbers = [19, 5, 42, 2, 77];
function sumTwoSmallestNumbers(numbers) {  
  let sortNumbers = numbers.sort(function(a , b){return a - b;});
  return sortNumbers[0] + sortNumbers[1];
}
console.log (sumTwoSmallestNumbers(numbers));