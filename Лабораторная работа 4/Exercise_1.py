# TODO решите задачу
import json


def task() -> float:
    with open('input.json', 'r') as file:
        f = json.load(file)
    summa = 0
    for dict_ in f:
        summa += dict_["score"] * dict_["weight"]
    return round(summa, 3)


print(task())
