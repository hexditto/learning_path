// let é uma variável que tem escopo global, de função e de bloco

let numero = 1;
{
    let numero = 2;
    console.log('dentro =', numero);
}
console.log('fora =', numero); // diferenças de escopos

