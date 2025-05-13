/* 
 * try é um bloco que pode gerar erro
 * o fluxo do problema é direcionado para o catch
 * o finally envia a mensagem mesmo com erro
 */

function tratarErroLancar(erro) {
    // throw new Error('...')
    // throw 10
    // throw true
    // throw 'mensagem'
    throw {
        nome: erro.name,
        msg: erro.messagem,
        date: new Date
    };
};


function imprimirNomeGritado(obj) {
    try {
        console.log(obj.name.toUpperCase() + '!!!');
    } catch (e) {
        tratarErroLancar(e)
    } finally {
        console.log('final');
    }
}

const obj = { name: 'Roberto' };
imprimirNomeGritado(obj);
