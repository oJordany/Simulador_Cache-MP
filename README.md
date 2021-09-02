# Simulador_Cache-MP

Simulador da interação entre cache e MP feito em Python

Universida Federeal do Pará - Ciência da Computação

Trabalho de Sistemas de Computação

Discente: Luiz Jordany de Sousa Silva

Prof. : Claudomiro Sales

# Funcionamento do projeto: 

-Capacidade da  MP: 32 bytes

-BE da MP: 5 bits

-Capacidade da cache: 8 bytes

-Largura dos blocos/linhas: 2 bytes

-Quantidade de linhas da cache: 4 linhas

-Quantidade de blocos da MP: 16 blocos 

A simulção dessa interação entre cache e MP é feita através de dois métodos de mapeamento: o direto e o associativo completo.

No começo do programa o usuário insere o método de mapeamento desejado e então o programa passa a rodar todo através dele.

Em seguida é apresentada uma mensagem contendo as informações da MP - 32 bytes, com BE de 5 bits e a disposição dos 32 bytes

Posteriormente, a UC insere o sinal de leitura(1) ou escrita(0).

A partir disso, o programa pode fazer uma operação de escrita utilizando a política de write through ou fazer uma leitura.

Na operação de leitura a substituição das informações contidas nas linhas da cache é feita em sua respectiva linha no caso do mapeamento direto. Já no caso do mapeamento associativo, a substituição é feita de maneira aleatória dentro da cache, isto é, as informações podem ir para qualquer linha da cache
