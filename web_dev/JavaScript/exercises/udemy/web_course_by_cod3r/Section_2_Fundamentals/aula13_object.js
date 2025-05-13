/* JSON - JavaScript object notation
 * JSON != objeto em javascript
 * JSON é um formato textual
 */

const prod1 = {}; //objeto usa chave
prod1.nome = 'Celular Ultra Mega';
prod1.preco = 4998.90;
prod1 ['Desconto Legal'] = 0.40; // evitar atributos com espaço

// objeto é uma coleção de chave <-> valor

console.log(prod1);
console.log(typeof prod1);

const prod2 = {
    nome: 'Camisa Polo',
    preco: 79.90
}

console.log(prod2);

// transformando em JSON

'{"nome": "Camisa Polo", "preco": 79.90}' // formato textual

