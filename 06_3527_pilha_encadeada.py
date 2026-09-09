class PilhaEncadeada:
    class _Node:
        def __init__(self,v,next):
            self.value = v
            self._next = next

    def __init__(self):
        self._size = 0
        self._head = None

    def push(self, item):
        '''
        Insere um elemento na pilha encadeada - O(1)
        '''
        self._size += 1
        self._head = self._Node(item, self._head)

    def pop(self):
        '''
            Remove e retorna o último elemento inserido na pilha - O(1)
        '''
        if self._size == 0:
            raise IndexError()

        v = self._head.value
        self._head = self._head._next
        self._size -= 1
        return v

    def topo(self):
        '''
            Retorna o último elemento insero na pilha - O(1)
        '''
        if self._size == 0:
            raise IndexError()

        return self._head.value

    def esta_vazia(self):
        '''
        Retorna True se a pilha é vazia e False se não é vazia - O(1)
        '''
        return self._size == 0

    def __len__(self):
        return self._size
    def len(self):
        '''
        Retorna a quantidade de elementos na pilha - O(1)
        '''
        return self._size

    def repr(self):
            '''
            Retorna uma string de exibição da fila - O(n)
            '''
            return self.__repr__()
    def __repr__(self):
        if self.len() == 0:
            return "[ ]"
        
        node = self._head
        texto = "[ "
        while node != None:
            texto += f'{node.value} {"<- " if node._next != None else "]"}'
            node = node._next

        return texto