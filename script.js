let string = 'Je veux manger';

function myFunction(s) {
    const words = s.split(' '); 
    let shortestLength = words[0].length; 
    for (let i = 1; i < words.length; i++) {
        if (words[i].length < shortestLength) {
            shortestLength = words[i].length;
      }
    }
    return shortestLength; 
}

best 
function findShort(s){
    return Math.min(...s.split(" ").map (s => s.length));
}

function findShort(s){
    return Math.min.apply(null, s.split(' ').map(w => w.length));
  }
