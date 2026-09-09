# Questão 1.
- Pessoa
    - Funcionário
        - Garçom
        - Chefe de Cozinha
        - Gerente

- Iguaria (Comida)
    - Bolo
    - Pizza

- Restaurante
    - Pizzaria

As subclasses herdam os respectivos atributos e métodos de suas classes pai e "avô". Como no caso onde Gerente herda os atributos e métodos
de Funcionário, onde Funcionário herda os métodos e atributos de Pessoa. O mesmo equivale para Bolo a Iguaria (Comida) e Pizzaria com Restaurante.

# Questão 2
A classe iguaria não precisa herdar os atributos de restaurante. Mas restaurante poderia ter algo relacionado como cardápio como atributo ou "Cozinhar" como método e receberia como argumento algum objeto da classe Iguaria.

Iguarias também poderia conter informações como ingredientes, preço, tempo de preparo, complexidade na cozinha, que seriam passadas pelo método "Cozinhar" de Restaurante.

# Questão 3
Argumento 1:
Poderia a priori ser um par ordenado onde o primeiro elemento é o nome do cliente ou a mesa em que foi feito o pedido e o segundo elemento ser uma outra lista com todas iguarias (strings) requisitadas por esse(a) cliente/mesa.

Argumento 2:
Preparar poderia ser um tipo lista (string) que representa o nome do alimento a ser preparado agora. Poderia ser semelhante ao argumento 1 e conter um par ordenado onde fica a mesa em que o pedido foi feito e também o pedido em si.

Argumento 3:
Deve ser uma instância de classe, em especial a classe funcionário, pois o gerente pode demitir um funcionário, não uma iguaria por exemplo.