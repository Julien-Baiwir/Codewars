// "https://www.codewars.com/kata/517abf86da9663f1d2000003/train/javascript"

function toCamelCase(str) {
    const words = str.split(/[-_]/);

    const camelCased = words.map((word, index) => {
     
        if (index !== 0) {
            return word.charAt(0).toUpperCase() 
            + word.slice(1);
        }
        return word;

    }).join('');

    return camelCased;
}
console.log(toCamelCase("the-stealth-warrior"));  
console.log(toCamelCase("The_Stealth_Warrior"));    
console.log(toCamelCase("The_Stealth-Warrior"));    


// quelques variations:
// function toCamelCase(str){
//     var regExp=/[-_]\w/ig;
//     return str.replace(regExp,function(match){
//           return match.charAt(1).toUpperCase();
//      });
// }
// ----------------
// function toCamelCase(str){
//     return str.replace(/[-_](.)/g, (_, c) => c.toUpperCase());
//   }
//   -----------------
//   function toCamelCase(str){
//     return str.split(/-|_/g).map((w, i) => (i > 0 ? w.charAt(0).toUpperCase() : w.charAt(0)) + w.slice(1)).join('');
//   }
//   -------------

