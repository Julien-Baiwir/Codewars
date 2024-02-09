let name = "Sam Harris";

function splitName(name) {
  return name.split(' ').map(word => word[0].toUpperCase()).join('.');
}
 console.log(splitName(name));



 function abbrevName(name){

    return name.split(' ').map(i => i[0].toUpperCase()).join('.')

}

function abbrevName(name){
    return name.split(' ').map(x => x.substr(0, 1).toUpperCase()).join('.');
  }
