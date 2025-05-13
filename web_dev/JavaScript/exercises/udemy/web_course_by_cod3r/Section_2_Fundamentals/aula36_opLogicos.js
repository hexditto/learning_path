// Tabelas-Verdade e Condicionais

function compras(trabalho1, trabalho2) {
    const comprarSorvete = trabalho1 || trabalho2; // || é OU
    const comprarTV50 = trabalho1 && trabalho2; // && é E
    // const comprarTV32 = !!(trabalho1 ^ trabalho2) // bitwise xor
    const comprarTV32 = trabalho1 != trabalho2; // outra forma do OU exclusivo
    const manterSaudavel = !comprarSorvete; // operador unário

    return { comprarSorvete, comprarTV50, comprarTV32, manterSaudavel }; // vai criar o nome automaticamente
}

console.log(compras(true, true));
console.log(compras(true, false));
console.log(compras(false, true));
console.log(compras(false, false));
