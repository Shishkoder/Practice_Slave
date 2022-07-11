from prettytable import PrettyTable, ALL


table = PrettyTable()
table.hrules = ALL
table.title = 'Задача_1'
table.header = False
table.padding_width = 5
table.align = 'l'

Q: list[int] = [i for i in range(5)]
TC: list[int] = [60, 100, 130, 155, 190]
FC: int = TC[0]
VC: list[int] = []
AC: list[int] = [0]
MC: list[int] = [0]

for i in range(5):
    VC.append(TC[i] - FC)

for i in range(1, 5):
    AC.append(int(TC[i] / Q[i]))

for i in range(1, 5):
    MC.append(int((TC[i] - TC[i - 1]) / (Q[i] - Q[i - 1])))

table.add_rows([
        ["Выпуск продукции Q", *Q],
        ["Валовые издержки TC", *TC],
        ["Постоянные издержки FC", *[FC for _ in range(5)]],
        ["Переменные издержки VC", *VC],
        ["Средние издержки AC", *AC],
        ["Предельные издержки MC", *MC]
    ])

print(table)
