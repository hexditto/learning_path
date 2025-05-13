// hoisting = içar para cima / mover para o topo

console.log('a =', a); // em outras linguagens daria erro
var a = 2; // declaração de variável posterior
console.log('a =', a);

function teste() {
    console.log('b =', b);
    var b = 3
    console.log('b =', b);
}

teste();

console.log('c =', c);
let c = 2; // variável let não sustenta hoisting
console.log('c =', c);
