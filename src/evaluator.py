from src.stack import Stack
from src.const import OPERATORS
from src.infix_to_postfix import InfixToPostFix
from src.utils import operate, check_string


class Evaluator:
    def __init__(self, expression: str):
        # Obtenemos el resultado postfijo de la cadena de entrada
        self.postfix = InfixToPostFix(expression).final_expression

        # self.postfix = [i for i in self.postfix if i != ""]
        # for term in self.postfix:
        #     if term.isdigit():
        #         self.final.append(term)
        #     for operator in ["*", "/", "-", "+"]:
        #         if operator in term:
        #             self.final.append(term.replace(operator, ""))
        #             self.final.append(operator)
        # self.postfix = [i for i in self.final if i != ""]

        # Preparamos el stack para la expresion
        self.result = Stack(len(expression))
        # Preparamos una lista para pasar la expresión a su forma final
        # EJ:
        #   Input: (10+10)*15
        #   Postfix: 10 10 + 15 *
        #   Expected Format: ["10", "10", "+", "15", "*"]
        self.final = []
        # Preparamos el contador
        self.counter: int = 0
        # Inicializamos la expresion que retiene el resultado
        self.final_expression: int = 0

        # self.actual_expresion = Stack(len(self.postfix) / 2)
        # Parseamos los terminos para almacenarlos en la lista final
        self.parse_terms()
        # Convertirmos el postfix en el formato esperado
        # Ademas filtramos los espacios
        self.postfix = list(filter(lambda x: x != "", self.final))
        # Reiniciamos el countr
        self.counter = 0
        # Parseamos y evaluamos el resultado
        self.parse()

    def EOS(self):
        # End Of String
        return self.counter >= len(self.postfix)

    def peek(self):
        # String Peeker
        char = self.postfix[self.counter]
        self.counter += 1
        return char

    def parse_terms(self, string=""):
        # Para parsear los terminos primero obtenemos un caracter
        char = self.peek()
        # Si el caracter es un espacio
        if char == " ":
            # Y el string tampoco es un espacio
            if string != "" or string != " ":
                # La incluimos dentro de la lista

                self.final.append(string)
            # Hacemos una llamada recursiva con el string en blannco
            return self.parse_terms()

        # Si el caracter no es un operador
        if char not in OPERATORS.keys():
            # Lo concatenamos al string
            string += char

        # Si el caracter es un operador
        elif char in OPERATORS.keys():
            # Vamos a guardar nuestra cadena completa dentro de la lista de la expresión final
            self.final.append(string)
            # Reiniciamos el String
            string = ""
            # Ponemos el operador en la lista
            self.final.append(char)

        if self.EOS():
            # Si la cadena postfija termino retornamos la cadena
            return string
        # Si no hacemos una llamada recursiva
        return self.parse_terms(string)

    def parse(self):
        # Tomamos el caracter
        char = self.peek()
        # Si no es un operador
        if char not in OPERATORS.keys():
            # Lo convertimos a un numero
            char = check_string(char)
            # Ponemos el numero en el stack
            self.result.push(char)

        # Si el caracter es un operador
        if char in OPERATORS.keys():
            # Obtenemos los operandos
            operand1 = self.result.pop()
            operand2 = self.result.pop()
            # Los operamos
            res = operate(operand1, operand2, char)
            # Ponemos el resultado en el stack
            self.result.push(res)

        # Si la cadena termina
        if self.EOS():
            # Pasamos lo que quedo en el Stack que el resultado a la expresion final
            self.final_expression = self.result.pop()
            # Salimos de la función
            return
        # Si no volvemos a llamar a parse recursivamente
        return self.parse()
