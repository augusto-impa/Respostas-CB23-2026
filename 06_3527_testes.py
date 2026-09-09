import importlib.util
import sys


# Importa a pilha encadeada
caminho_pilha = "06_3527_pilha_encadeada.py"
nome_pilha = "pilha_encadeada"

spec_pilha = importlib.util.spec_from_file_location(nome_pilha, caminho_pilha)
pilha = importlib.util.module_from_spec(spec_pilha)
sys.modules[nome_pilha] = pilha
spec_pilha.loader.exec_module(pilha)


# Importa a fila encadeada
caminho_fila = "06_3527_fila_encadeada.py"
nome_fila = "fila_encadeada"

spec_fila = importlib.util.spec_from_file_location(nome_fila, caminho_fila)
fila = importlib.util.module_from_spec(spec_fila)
sys.modules[nome_fila] = fila
spec_fila.loader.exec_module(fila)


if __name__ == "__main__":
    pilha_encadeada = pilha.PilhaEncadeada()
    pilha_encadeada.push(5)
    pilha_encadeada.push("Bom dia")

    print("Pilha:")
    print(repr(pilha_encadeada))

    print("Topo da pilha:", pilha_encadeada.topo())
    print("Tamanho da pilha:", pilha_encadeada.len())

    ultimo = pilha_encadeada.pop()

    print("Elemento removido da pilha:", ultimo)
    print("Topo da pilha após remoção:", pilha_encadeada.topo())
    print("Tamanho da pilha após remoção:", pilha_encadeada.len())


    # Teste da fila

    fila_encadeada = fila.FilaEncadeada()

    fila_encadeada.enfileirar(123)
    fila_encadeada.enfileirar("arroz")
    fila_encadeada.enfileirar(5 * 2)

    print("\nFila:")
    print(repr(fila_encadeada))

    print("Tamanho da fila:", fila_encadeada.len())

    primeiro = fila_encadeada.desenfileirar()

    print("Primeiro Elemento da fila (removido):", primeiro)
    print("Fila após remoção:", repr(fila_encadeada))
    print("Tamanho da fila após remoção:", fila_encadeada.len())
