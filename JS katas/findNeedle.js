haystack = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] 

function findNeedle(haystack) {
    return "found the needle at position " + haystack.indexOf('needle');
  }
console.log(findNeedle(haystack));


function findNeedle(haystack) {
    return `found the needle at position ${haystack.indexOf('needle')}`;
  }

  const findNeedle = haystack => `found the needle at position ${haystack.indexOf('needle')}`;