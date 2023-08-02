# Método utilizado para resolução:
 O próprio desafio deixou uma base do código para introdução sendo ele a estrutura principal.

 O que foi estudado antes de inicar o código foram quais as particularidades de cada método: depósito, saque e extrato.

 Depósito teria que ser com valores positvos, armazenar em uma váriavel os valores depositados e gerar relátorios na base de extratos em cada operação realizada.
 
 Saque teria que ser com valores positvos, menores ou igual ao valor do saldo, também teria a particularidade de ter no máximo três saques diários, configurado para sacar
 no máximo R$500,00 por saque e também deveria gerar um relátorio que deveria ser armazenado no extrato.

 Extrato deveria exibir os valores no formato " R$ 000,00 e também notificar caso não tenha sido efetuado nenhuma operação.

 # Método de funcionamento do código
 Existe uma mensagem de boas vindas ao usuário e aparece um menu onde o mesmo deve fazer a seleção das opções [(Depositar), (Sacar), (Extrato), (Sair)].

 Caso o usuário faça um acesso e logo em seguida saia do sistema bancário será exibido uma mensagem de agradecimento por utilizar o sistema.

 Caso o usuário faça um deposito será verificado se está dentro dos critérios acima relatados para assim prosseguir para que seja informado o valor
 informado ou uma mensagem de erro caso não atenda os requisitos para o depósito.

Caso o usuário faça um saque será verificado se está dentro dos critérios acima relatados para assim prosseguir para que seja informado o valor
 informado ou uma mensagem de erro caso não atenda os requisitos para o depósito. No caso do cliente exceder o limite diário de valor de saque ou exceda a quantidade de vezes permitido para sacar
 será exibido mensagem personalizada informando o devido problema.

A opção de extrato exibe as informações de valor de depósito e saque em ordens as quais foram efetuadas. No caso do cliente não ter feito nenhuma operação será exibido uma mensagem informando ao memsmo.

Toda estrutura foi configurada dentro um comando while para sempre repetir o menu até o cliente desejar sair da conta.
 
 
