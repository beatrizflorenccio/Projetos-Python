Maria Beatriz Ramos Florencio - 2020 - Fonte: Curso online de IaC do ITA
# INTRODUÇÃO AO CONTROLE DE SISTEMAS

## **O QUE É UM SISTEMA?**

Sistema é uma parte do universo de interesse para estudo.

## **QUAL O OBJETIVO DO CONTROLE DE SISTEMAS?**

Modificar o comportamento de um sistema de forma eficiente. Modificar o comportamento quer dizer alterar a relação entre a entrada e a saída de um sistema de modo a atender requisitos de desempenho. De forma eficiente quer dizer com a menor complexidade, custo e intervenção humana possível.

### **REQUISITOS DE DESEMPENHO**

Rquisitos de desempenho são características desejáveis da relação entrada saída e da resposta a uma determinada entrada. De maneira mais simples, os requisitos do sistema são o que você deseja que o sistema faça e como você deseja que ele faça.

Normalmente eles estão associados à velocidade de resposta do sistema, à presença ou não de oscilações e ao quão bem a saída acompanha o valor desejado (referência). Porém, cada sistema possui suas peculiaridades. 

Pense em um evelevador como exemplo. Você deseja que ele chegue rapidamente ao andar desejado, mas não deseja que ele fique oscilando em torno do andar desejado, pois seria desconfortável. E você também não deseja que o elevador pare nem muito acima nem muito abaixo do nível do andar desejado. 

### **O QUE É O ERRO?**

De maneira bem genérica, o erro é a diferença entre a referência (valor da saída desejado) e a saída (valor real da saída). 

Podem existir entradas do nosso sistema que não podemos manipular (perturbações). 

> Como exemplo, pense num forno a gás, em que a temperatura é a saída e a entrada é o fluxo de gás. Digamos que a referência seja de 180°C. A partir dela, definimos a entrada (fluxo de gás) através do botão do fogão. O ângulo do botão afeta o fluxo de gás que será queimado, produzindo calor e aumentando a temperatura do forno. A saída do sistema é a temperatura real do forno. O erro é a diferença entre a temperatura desejada e a temperatura real, uma vez que existem entradas do nosso sistema que não podemos manipular (perturbações).

### Representação

| Termo | Representação 
:--------:|:--------------:
| Saída | y
| Entrada | u
| Referência | r

No domínio do tempo, o erro pode ser denotado como:
- e(t) = r(t) - y(t)

## **ANÁLISE E PROJETO**

### **ANÁLISE**

Consiste em verificar se um sistema atende ou não aos requisitos do sistema. Essa verificação pode ser feita através de testes, mas demandaria muito tempo.

#### **SISTEMA APROVADO NA ANÁLISE**
 
 Foi constatado que o sistema atende aos requisitos do sistema. Dessa forma, nada mais precisa ser feito.

#### **SISTEMA REPROVADO NA ANÁLISE**

Foi constatado que o sistema não atende aos requisitos. Dessa forma, precisamos alterar a relação entre a sua entrada e a sua saída. Fazemos isso através do controle. O processo de definição do controle é o projeto.

### **PROJETO**

Processo de definição do controle. Como já vimos, o controle consiste na modificação do desempenho do sistema ou na relação entrada-saída, de modo que a nova relação passe a atender requisitos de desempenho que o sistema não atenderia normalmente.

O controle pode ser realizado em malha aberta ou em malha fechada.

#### **CONTROLE EM MALHA ABERTA**

No controle em malha aberta, ajustamos o valor da entrada com base exclusivamente na referência. Não nos preocupamos em verificar se a saída está realmente indo para o valor desejado. Confia-se cegamente no projeto.

A entrada depende diretamente da referência, mas não da saída.

Desse modo, se tudo ocorre perfeitamente bem, temos a saída desejada. Mas caso algo não seja exatamente como previmos, temos problemas.


> Como exemplo, imagine que você está saindo de casa encima da hora para ir à escola. Alguns imprevistos, como pegar um trânsito tenso, obras no caminho ou atraso do ônibus podem te causar problemas. 

#### **CONTROLE EM MALHA FECHADA**

No controle em malha fechada, realimentamos o sinal de saída e subtraímos esse sinal da referência, gerando um sinal de erro. Esse sinal de erro é então usado para ajustar a entrada do sistema. 

A entrada depende tanto da referência quanto do sinal de saída através do sinal de erro.

## **RESUMINDO**

Sendo assim, agora sabemos que o controle de sistemas consiste da análise e do projeto, com o objetivo de verificar e adequar o desempenho/comportamento de um sistema aos requisitos de desempenho. Na análise, verificamos se ele atende aos requisitos. No projeto, ajustamos o desempenho para que ele atenda aos requisitos e fazemos isso projetando o controle do sistema. 







