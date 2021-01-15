class Node:
    def __init__(self, value):
        # La referencia el siguiente
        self.next = None
        # Valor del nodo
        self.value = value

    def __str__(self) -> str:
        # Si hacemos un print al nodo nos devuelve el valor
        return f"{self.value}"


class Stack:
    def __init__(self, max_size):
        # El primer nodo comienza como None
        self.top = None
        # Size es la cantidad de elementos en el stack
        self.size = 0
        # Si el tamaño del stack es igual al tamaño del stack entonces el stack esta lleno
        self.max_size = max_size

    def push(self, value):
        # If not top
        if self.top == None:
            # Si no hay nodo superior entonces se asigna el valor superior al primer nodo
            self.top = Node(value)
        elif self.size < self.max_size:
            # Si hay un nodo superior creamos un nuevo nodo con el valor que le pasamos al metodo como argumento
            new_node = Node(value)
            # Extaemos el nodo superior
            top = self.top
            # Decimos que el siguiente nodo luego del superior sera el nuevo nodo asi el ultimo valor en entrar es el primero en salir
            new_node.next = top
            # Ponemos el siguiente nodo arriba
            self.top = new_node
        else:
            # Si el stack sta completo lanzamos un error
            raise ValueError("The Stack is full")
        # Si no aumentamos el tamaño en 1
        self.size += 1

    def pop(self):
        if self.size == 0:
            # Si no hay elementos en el stack
            raise Exception("The Stack is empty")
        else:
            # Si no asignamos el valor a una variable temporal
            top = self.top
            # Asignamos al nodo superior el siguiente nodo
            self.top = top.next
            # Decrementamos el tamaño del stack
            self.size -= 1
            # Retornamos el valor
            return top.value

    def is_empty(self):
        # Si no hay elementos en el Stack decimos que el stack esta vacio
        return self.top == None

    def is_full(self):
        # Si el tamaño del stack es igual al tamaño maximo decimos que esta lleno
        return self.size == self.max_size
