O ato de desempacotar requer que transfira todos os n elementos da pilha primária para a pilha secundária,
o que requer n operações O(n). Mas após o desempacotamento, até a pilha secundária se esgotar, as operações serão O(1)
pois só é necessário acessar o elemento na pilha secundária, não fazer o desempacotamento completo.