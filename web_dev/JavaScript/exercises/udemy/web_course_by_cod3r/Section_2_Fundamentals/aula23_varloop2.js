// Exemplo mais dificil

const funcs = [];

for (var i = 0; i < 10; i++) {
    funcs.push(function() {
        console.log(i);
    });
};

funcs[2](); // var não tem escopo de função
funcs[8]();
