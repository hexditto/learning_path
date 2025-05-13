// Teste de um código sem criar bloco if:

function teste1(num) {;
    if(num > 7)
        console.log(num);
        
    console.log('Final'); 
}

teste1(6);
teste1(8);

// Cuidado com a posição do ; ponto e virgula
function teste2(num) {
    if(num > 7); { // nessa posição
        console.log(num);
    }
}

teste2(6);
teste2(8);

function teste3(num) {
    if(num > 7) {
        console.log(num);
    }
}

teste3(6);
teste3(8);