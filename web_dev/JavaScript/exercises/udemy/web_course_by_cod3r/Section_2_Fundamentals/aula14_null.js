/*
 * atribuição por referência = endereço na memoria
 *
 *
 */

const a = {};
a.name = 'Teste';

console.log(a);
const b = a; // b está apontando para o local na memória que tem a

console.log(b);
 b.name = 'Opa';
console.log(a); // por esse motivo mudar valor de b muda o de a

let c = 3;
let d = c;

d++;
console.log(c, d); // há uma copia por valor e nao referencias

// não inicializada
let valor
console.log(valor);

valor = null; //ausência de valor
console.log(valor); // não aponta para nenhum local na memória

// console.log(valor.toString()) // Erro!

const produto = {};
console.log(produto.preco); //não está definido
console.log(produto);

produto.preco = 3.50;
console.log(produto);

produto.preco = undefined // evite atribuir undefined
console.log(!!produto.preco);
// delete produto.preco
console.log(produto);

produto.preco = null // sem preço
console.log(!!produto.preco);
console.log(produto);