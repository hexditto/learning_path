/* 
 * Operadores relacionais dão resultado verdadeiro ou falso
 * Como JS é fracamente tipado, caso precise comparar
 * dois valores, há a possibilidade de precisar que além do
 * valor ser igual, o tipo também precise ser!!!
 */

// Dica: usar o estritamente igual ===
console.log('01)', '1' == 1); // apenas o valor
console.log('02)', '1' === 1); // valor e o tipo
console.log('03)', '3' != 3); // valor não é diferente
console.log('04)', '3' !== 3); // valor e tipo são diferentes
console.log('05)', 3 < 2); 
console.log('06)', 3 > 2); 
console.log('07)', 3 <= 2); 
console.log('08)', 3 >= 2); 

// Data do início na memória da linguagem
const d1 = new Date(0);
const d2 = new Date(0);
console.log('09)', d1 === d2);
console.log('10)', d1 == d2);
console.log('11)', d1.getTime() === d2.getTime());
console.log('12)', d1.getTime() == d2.getTime());

// undefined e null
console.log('13)', undefined == null);
console.log('14)', undefined === null);
