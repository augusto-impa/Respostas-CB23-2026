import importlib.util
import sys

caminho = "06_3527_pilha_encadeada.py"
nome_modulo = "pilha_encadeada"

spec = importlib.util.spec_from_file_location(nome_modulo, caminho)
pilha_encadeada = importlib.util.module_from_spec(spec)
sys.modules[nome_modulo] = pilha_encadeada
spec.loader.exec_module(pilha_encadeada)
##

class FilaEncadeada:
    def __init__(self):
        self.input = pilha_encadeada.PilhaEncadeada()
        self.output = pilha_encadeada.PilhaEncadeada()

    def enfileirar(self, item):
        '''
        Insere um elemento na lista - O(1)
        '''
        self.input.push(item)

    def desenfileirar(self):
        '''
        Remove e retorna o último elemento - O(1) até O(n)
        '''
        if self.len() == 0:
            raise IndexError()

        if self.output.len() == 0:
            while self.input.len() > 0:
                self.output.push(self.input.pop())

        return self.output.pop()

    def frente(self):
        '''
        Retorna o último elemento - O(1) até O(n)
        '''
        if self.output.len() == 0:
            while self.input.len() > 0:
                self.output.push(self.input.pop())

        if self.output.len() == 0:
            raise IndexError()

        return self.output.topo()

    def esta_vazia(self):
        '''
        Retorna True se a pilha é vazia e False se não é vazia - O(1)
        '''
        return self.len() == 0
    def len(self):
        '''
        Retorna a quantidade de elementos na pilha - O(1)
        '''
        return self.output.len() + self.input.len()
    def __len__(self):
        return self.output.len() + self.input.len()
    def repr(self):
        '''
        Retorna uma string de exibição da fila - O(n)
        '''
        return self.__repr__()
    def __repr__(self):
        if self.len() == 0:
            return "[ ]"

        texto = "[ "

        node = self.output._head
        while node != None:
            texto += str(node.value)
            if node._next != None:
                texto += " -> "
            node = node._next

        valores = ""
        node = self.input._head

        while node != None:
            valores = f"{node.value}" + (" -> " if valores else "") + valores
            node = node._next

        if self.output.len() > 0 and valores:
            texto += " -> "

        texto += valores

        return texto + " ]"

