// Usar destructuring como parametro de uma função

// min e maximo já têm valores padrão na função
function rand( { min = 0, max = 1000 }) { // Operador destructuring
    const valor = Math.random() * (max - min) + min;
    return Math.floor(valor);
};

// Criando um objeto
const obj = { max: 50, min: 40 };
console.log(rand(obj));
console.log(rand({ min: 955 }));
console.log(rand({ }));
