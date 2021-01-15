from src.stack import Stack
from src.const import OPERATORS


class InfixToPostFix:
    def __init__(self, expression: str):
        # Borramos los espacios del input
        self.expression: str = expression.replace(" ", "")
        # Asignamos el cursor a cero
        self.cursor: int = 0
        # Asignamos la expresión final como una cadena vacia
        self.final_expression: str = ""
        # Asignamos el stack temporal como la mitad del largo de nuestra expresion
        self.result: Stack = Stack(len(expression) / 2)
        # Llamamos a la función parse
        self.parse()

    def peek(self):
        # Tomamos un caracter de la cadena
        char = self.expression[self.cursor]
        # Aumentamos le cursor en 1
        self.cursor += 1
        # Retornamos el caracter
        return char

    def EOS(self):
        # Si el cursor es mayor o igual al tamaño de la cadena significa que
        # Hemos terminado de parsear
        return self.cursor >= len(self.expression)

    def flush(self):
        # Toma todo lo que hay en el stack y lo concatena a la cadena
        while not self.result.is_empty():
            self.final_expression += " "+self.result.pop()

    def parse(self):
        # Pedimos el char
        char = self.peek()
        # Si el Char no es un operador o es un parentesis lo incluimos dentro de la cadena
        # Final
        if char not in OPERATORS.keys() and char != ")" and char != "(":
            self.final_expression += char
        # Si el caracter es un parentesis de apertura lo incluimos en el Stack
        if char == "(":
            self.result.push(char)
        # Si el caracter es un operador
        elif char in OPERATORS.keys():
            # Agregamos un espacio en la expresión final
            self.final_expression += " "
            # Si el stack sta vacio o tiene un parentesis
            if self.result.top == None or self.result.top.value == "(":
                # Incluimos el caracter
                self.result.push(char)
                # Hacemos una llamada recursiva de la función
                return self.parse()

            # Si no vemos la presedencia de los operadores
            operator_precedence = OPERATORS[char]
            top_precedence = OPERATORS[self.result.top.value]

            # Si el operador actual tiene mayor precedencia que el superior
            if operator_precedence > top_precedence:
                # Ponemos el caracter dentro del Stack
                self.result.push(char)
            else:
                # Si no, obtenemos un operador del Stack
                popped = self.result.pop()
                # Ponemos el operador actual
                self.result.push(char)
                # Ponemos el operador que sacamos del stack en la cadena final
                self.final_expression += popped

            # Agregamos un espacio al final
            self.final_expression += " "

        # Si el caracter es un cierre de parentesis
        elif char == ")":
            # Sacamos todo lo que hay dentro del stack hasta obtener un parentesis de apertura
            # Concatenamos el resultado a la expresión final con espacios
            while True:
                pop = self.result.pop()
                if pop == "(":
                    break
                self.final_expression += pop

        # Si no hay mas caracteres en la cadena
        if self.EOS():
            # Vaciamos el stack
            while not self.result.is_empty():
                self.final_expression += self.result.pop()
            # Terminamos la función
            return
        # Si no llamamos a la funcion parse con el siguiente caracter
        return self.parse()
