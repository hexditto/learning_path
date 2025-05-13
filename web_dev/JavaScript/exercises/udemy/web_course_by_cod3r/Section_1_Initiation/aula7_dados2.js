/*
 *
 *A criação de variável por  var  gera 
 uma variável global em toda a sua linha de código, 
 enquanto criar uma variável por let limita o 
 seu alcance apenas para sua sentença ou bloco, 
 portanto mais recomendável
 * 
 * var é um identificador 
 */ 

 // var + identificador = valor

 var idade = 3;
 
 let preco = 19.90;
 let desconto = 0.4;
 let precoComDesconto = preco * (1 - desconto);
 console.log(precoComDesconto);
 console.log(19.9 * 0.6);
 console.log(preco * (1 - desconto));

 // textos
 let nome = "Caderno";
 let categoria = "Papelaria";
 console.log("Produto: " + nome
     + " " + ", Categoria: " + categoria
     + ", Preço: " + preco
     + ", Desconto: " + desconto);

     console.log(1 + 1);
     console.log("1" + 1);