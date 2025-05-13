// Aprender as diferenças de var e let

/* 
 * Conceito de escopo em linguagem de 
 * programação: a visibilidade do código 
 * dentro do programa
 * var usa uma variável global
 */

{
    {
        {
            var sera = 'Será???' // escopo
            console.log(sera);

        }
    }
}

console.log(sera);

function teste() {
    var local = 123;
    console.log(local);
}

teste();
console.log(local); // está fora do escopo

/* 
 * "A variável var dentro de um bloco de código que não seja uma 
 * função continuará 'visível' durante o programa"
 */