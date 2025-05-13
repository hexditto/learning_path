// Desestruturação - tira da estrutura alguma coisa
// exemplo - tirar elementos de um OBJETO
// novo recurso do ES2015

const pessoa = {
    nome: 'Ana',
    idade: 5,
    endereco: {
        logradouro: 'Rua ABC',
        numero: 1000
    }
}

const { nome, idade } = pessoa; // usar const + chaves abertas { }
console.log(nome, idade);

const { nome: n, idade: i } = pessoa; // retire da estrutura nome e idade e atribua variaveis
console.log(n, i);


// Caso não tenha um atributo dentro do objeto: undefined
const { sobrenome, bemHumorada = true } = pessoa;
console.log(sobrenome, bemHumorada);

// Tira um elemento dentro de um elemento:
const { endereco: { logradouro, numero, cep } } = pessoa;
console.log(logradouro, numero, cep);

// Cuidado para não acessar atributos que não existem de forma aninhada
//const { conta: { ag, num } } = pessoa;
//console.log(ag, num);