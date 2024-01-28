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


// const camelCased = words.map((word, index) => {
//     // La méthode map() est utilisée pour itérer sur chaque élément du tableau "words".

//     if (index !== 0) {
//         // Si l'index n'est pas égal à zéro (c'est-à-dire, si ce n'est pas le premier mot),
//         // alors appliquer la conversion CamelCase.

//         return word.charAt(0).toUpperCase() + word.slice(1);
//         // La méthode charAt(0) renvoie le premier caractère de la chaîne (le premier caractère du mot).
//         // La méthode toUpperCase() convertit ce premier caractère en majuscule.
//         // Ensuite, la méthode slice(1) renvoie le reste de la chaîne à partir du deuxième caractère.
//         // Enfin, les deux parties sont concaténées pour former le mot en CamelCase.
//     }

//     // Si l'index est égal à zéro (c'est le premier mot), ne pas modifier le mot.
//     return word;

// }).join('');
// // La méthode join('') est utilisée pour concaténer tous les éléments du tableau en une seule chaîne.
// // Cela crée la version finale en CamelCase de tous les mots du tableau "words".

// // Le résultat final est stocké dans la variable camelCased.




