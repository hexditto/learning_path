/* Função é uma ação
 * , executando um processo
 * baseado na sentença de código
 * Função é um bloco de código nomeado
 * para chamar o código em qualquer momento
 */

// função sem retorno
function imprimirSoma(a, b) {
    console.log(a + b);
}

imprimirSoma(2, 3);
imprimirSoma(2); // Caso falte um parametro, o outro valor torna undefined
imprimirSoma(2, 10, 4, 5, 6, 7, 8);
imprimirSoma();

// função com retorno
function soma(a, b = 1) {
    return a + b;
}

console.log(soma(2, 3)); // necessita do console.log para mostrar valor return
console.log(soma(2));
console.log(soma());
