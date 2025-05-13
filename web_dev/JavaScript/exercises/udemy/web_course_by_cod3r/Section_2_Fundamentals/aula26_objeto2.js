// Diferenças entre objeto e função
console.log(typeof Object);
console.log(typeof new Object); // instanciar

const Cliente = function() {};
console.log(typeof Cliente);
console.log(typeof new Cliente);

// classe = atalho de sintaxe
class Produto {} // ES 2015 (ES6) EchScript
console.log(typeof Produto);
console.log(typeof new Produto);

// Cria-se objetos em JS a partir de funções
// Funções podem ser instanciadas para gerar objetos
