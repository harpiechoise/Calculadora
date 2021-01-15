from src.evaluator import Evaluator
from src.utils import check_expression


def menu():
    # En el menu se espera una entrada de texto
    string = input("Ingrese una expresion matematica: ")
    # Si es exit
    if string == "exit":
        # Se rompe la funcion
        return
    is_valid = check_expression(string)
    if not is_valid:
        return menu()
    # Si no se evalua la expresión
    e = Evaluator(string)
    # Se muestra la expresión final
    print(e.final_expression)
    return menu()  # Se llama al menu de forma recursiva


if __name__ == "__main__":
    # [] <- 10
    # [10] <- 20
    # [10, 20] -> 20
    # [10] -> 10

    menu()
