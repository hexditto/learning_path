// valores verdadeiros e falsos

let isAtivo = false;
console.log(isAtivo);

isAtivo = true;
console.log(isAtivo);

isAtivo = 1;
console.log(!true); // ! funciona como negação
console.log(!!isAtivo); // ! funciona como negação


// os verdadeiros
console.log('os verdadeiros...');
console.log(!!3);
console.log(!!-1);
console.log(!!' ');
console.log(!![]);
console.log(!!{});
console.log(!!Infinity);
console.log(!!(isAtivo = true));

// os falsos
console.log('os falsos...');
console.log(!!0);
console.log(!!'');
console.log(!!null);
console.log(!!NaN);
console.log(!!undefined);
console.log(!!(isAtivo = false));

console.log('pra finalizar...');
console.log(!!('' || null || 0 || ' ')); // || representa OU

// valor padrão
let nome = '';
console.log(nome || 'Desconhecido');

nome = 'Lucas';
console.log(nome || 'Desconhecido');
