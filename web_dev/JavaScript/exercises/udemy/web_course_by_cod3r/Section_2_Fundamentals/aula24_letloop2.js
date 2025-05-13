// Exemplo mais difícil

const funcs = [];

for (let i = 0; i < 10; i++) {
    funcs.push(function() {
        console.log(i);
    });
};

funcs[2](); // existe a memória do escopo de bloco
funcs[8]();

// uma função tem consciência do local que ela foi defiinida
