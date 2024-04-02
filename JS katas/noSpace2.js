let x = "8 j 8   mBliB8g  imjB8B8         jl  B";
function noSpace(x){
  return x.split('').join('')
}
console.log(noSpace(x));

// .split(' ')
// il avec seulement un écartement entre les parenthèses 
// avec un espace .split divise la chaîne x en un tableau de sous-chaînes en utilisant un espace comme séparateur, puis réassemble ces sous-chaînes en une seule chaîne en les joignant sans séparateur. Cela signifie que tous les espaces dans la chaîne d'origine sont supprimés.

// .join('')
// sans aucunes parentheses il y a des virgules dans le nouveau String
// avec des parentheses tous les simples espaces disparaissent


// Dans le premier cas (x.split('').join('')), chaque caractère est considéré comme un élément distinct, donc aucun caractère n'est supprimé, y compris les espaces.
// Dans le deuxième cas (x.split(' ').join('')), la chaîne est divisée en sous-chaînes à chaque espace, et ensuite ces sous-chaînes sont réassemblées sans espace, ce qui supprime tous les espaces de la chaîne d'origine.

function noSpace(x) {
  return x.replaceAll(' ', '');
}