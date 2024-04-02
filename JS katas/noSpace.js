let x = "8 j 8   mBliB8g  imjB8B8  jl  B";
function noSpace(x){
   return x.replace(/\s/g, "");  
}
console.log(noSpace(x));

// En JavaScript, la méthode replace() est une méthode de chaîne (string) qui permet de rechercher et de remplacer des sous-chaînes dans une chaîne de caractères. Elle prend deux arguments :

// Le premier argument est la sous-chaîne à rechercher (ou une expression régulière).

// / : Le premier / est le délimiteur indiquant le début de l'expression régulière.
// \s : C'est le motif de l'expression régulière qui correspond à n'importe quel caractère d'espacement (comme expliqué précédemment).
// / : Le deuxième / est le délimiteur indiquant la fin de l'expression régulière.
// g : C'est un modificateur qui indique à la méthode replace() de rechercher toutes les occurrences du motif (pattern) dans la chaîne. Sans ce modificateur, replace() ne remplacerait que la première occurrence trouvée.



// Le deuxième argument est la chaîne de remplacement qui remplacera les occurrences trouvées.