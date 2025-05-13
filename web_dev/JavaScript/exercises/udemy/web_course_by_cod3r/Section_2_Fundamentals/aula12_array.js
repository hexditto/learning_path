/* Vetor unidimensional
 *
 * Acessa os valores através de índices
 * em JavaScript:
 * array heterogêneo = varios tipos dentro do array
 * array flexivel = cresce e diminui livremente
 * push = adiciona
 * pop / delete = retira
 */

const valores = [7.7, 8.9, 6.3, 9.2];
console.log(valores[0], valores[3]);
console.log(valores[4]); // daria erro, mas em JS não dá

valores[4] = 10;
console.log(valores);

valores[8] = 12;
console.log(valores);

console.log(valores.length); // tamanho do array

valores.push({id: 3}, false, null, 'teste'); //aceitar valores
console.log(valores);

console.log(valores.pop());
delete valores[0];
console.log(valores);

console.log(typeof valores); // tipo object