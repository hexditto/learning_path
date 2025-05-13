/* String é uma cadeia de caracteres
 * delimitado por "" ou '' ou `´
 *
 */

const escola = "Cod3r";

console.log(escola.charAt(4));
console.log(escola.charAt(5)); // não retorna erro, e sim um vazio
console.log(escola.charCodeAt(3)); //usa tabela ASCII para dar o índice
console.log(escola.indexOf('3'));

console.log(escola.substring(1)); // a partir desse ponto até o final
console.log(escola.substring(0, 3)); // do início até o 3

console.log('Escola '.concat(escola).concat('!')); //'Escola ' -> literal
console.log(escola.replace(3, 'e')); //substituir
console.log(escola.replace(/\d/, 'e')); // /\d/ -> expressão regular -> substitua todos os digitos
console.log(escola.replace(/\w/g, 'e')); // /\w/g -> expressão regular -> global

console.log('Ana,Maria,Pedro'.split(',')); // criar arrays
console.log('Ana,Maria,Pedro'.split(/,/));
