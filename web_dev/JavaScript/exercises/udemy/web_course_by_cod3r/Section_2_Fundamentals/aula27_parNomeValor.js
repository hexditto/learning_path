// Objeto é uma coleção de chave/valor

const saudacao = 'Opa'; // Contexto léxico 1 - local que sua variável foi definida no código

function exec() {
    const saudacao = 'Falaaa'; // Contexto léxico 2
    return saudacao;
}

// Objetos são grupos aninhados de pares nome/valor
const cliente = {
    nome: 'Pedro',
    idade: 32,
    peso: 90,
    endereco: {
        logradouro: 'Rua Muito Legal',
        numero: 123
    }
}

console.log(saudacao);
console.log(exec());
console.log(cliente);
