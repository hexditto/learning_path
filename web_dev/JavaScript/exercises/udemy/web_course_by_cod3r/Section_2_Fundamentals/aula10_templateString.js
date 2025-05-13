/* Template String
 * concatenação mais elegante
 * utiliza-se crase para manipular o template
 * 
 * pode colocar quebras de linhas
 */

const nome = 'Rebeca';
const concatenacao = 'Olá' + nome + '!';
const template = `
    Olá
    ${nome}!` //interpolação

console.log(concatenacao, template);

// expressões

console.log(`1 + 1 = ${1 + 1}`); // o que está dentro do sifrão é interpretado

const up = texto => texto.toUpperCase();

console.log(`Ei... ${up('cuidado')}!`);
