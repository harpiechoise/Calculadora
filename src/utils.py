from src.const import OPERATORS
from src.errors import Error


# La funcion que ejecuta la operación
def operate(a, b, operator):
    if operator == "+":
        return b + a
    if operator == "*":
        return b * a
    if operator == "-":
        return b - a
    if operator == "/":
        return b / a


# Una función para comprobar si un numero es un string
def check_string(a):
    if isinstance(a, str):
        return float(a)
    if isinstance(a, float):
        return a


# Error handling (prevent crashing)
def check_expression(expression: str):
    for i in expression:
        if not i.isdigit() and i not in OPERATORS.keys():
            if i in ["^", "sqrt"]:
                Error("Not Implemented",
                      f"The operator {i} isnt't implemented").show_meeesage()
                return False
            Error("Invalid Syntax",
                  f"Symbol {i} isn't number or operator").show_meeesage()
            return False
    if expression[0] in OPERATORS.keys():
        Error("Expression Malformed",
              "The expression couldn't start with an operator").show_meeesage()
        return False
    if expression[-1] in OPERATORS.keys():
        Error("Expression Malformed",
              "The expression couldn't end with an operator").show_meeesage()
        return False
    return True
