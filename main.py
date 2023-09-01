"""

Alunos:
Bruno Assis Miglioretto
Vitor Solieri do Vale

Desenvolvido em 01/09/2023 para a matéria de Matemática Discreta

"""


operation_alias = {
    "U": "União",
    "I": "Interseção",
    "D": "Diferença",
    "C": "Produto cartesiano",
}

input_file = "input3.txt"


def build_print(operation, first_set, second_set, result):
    first_set_print = ", ".join(first_set)
    second_set_print = ", ".join(second_set)
    operation_result = f"{operation_alias[operation]}: conjunto 1: "
    operation_result += "{"
    operation_result += first_set_print
    operation_result += "}, "
    operation_result += "conjunto 2: {"
    operation_result += second_set_print
    operation_result += "}. Resultado: {"
    operation_result += ", ".join(result)
    operation_result += "}"
    return operation_result


with open(input_file, "r") as f:
    lines = f.readlines()

    operation_count = lines.pop(0)[:-1]

    while lines:
        operation = lines.pop(0)[:-1].strip()
        first_set = [line.strip() for line in lines.pop(0)[:-1].split(",")]
        first_set = [number for number in first_set if number]
        second_set = [line.strip() for line in lines.pop(0)[:-1].split(",")]
        second_set = [number for number in second_set if number]

        if operation == "U":
            result = first_set + second_set
        elif operation == "I":
            result = [number for number in first_set if number in second_set]
        elif operation == "D":
            result = [number for number in first_set if number not in second_set]
        elif operation == "C":
            result = []
            for i in first_set:
                for j in second_set:
                    item_result = f"({i}, {j})"
                    result.append(item_result)

        print(build_print(operation, first_set, second_set, result))
