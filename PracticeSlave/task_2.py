from prettytable import PrettyTable, ALL


table = PrettyTable()
table.title = 'Задача_2'
table.field_names = ("Единицы продукции (в неделю)", "FC", "VC", "TC", "АТС", "MC")
table.padding_width = 3
table.align = 'l'
table.align["Единицы продукции (в неделю)"] = 'c'
table.hrules = ALL

Q: list[int] = [i for i in range(9)]
FC: int = 1000
VC: list[int] = [0, 350, 560, 740, 1000, 1400, 2000, 2800, 3960]
TC: list[int] = []
ATC: list[int] = [0] # ATC = TC/Q
MC: list[int] = [0]

for i in range(9):
    TC.append(FC + VC[i])

for i in range(1, 9):
    ATC.append(int((TC[i] - TC[i - 1]) / Q[i]))

for i in range(1, 9):
    MC.append(int((TC[i] - TC[i - 1]) / (Q[i] - Q[i - 1])))

for i in range(9):
    table.add_row([Q[i], FC, VC[i], TC[i], ATC[i], MC[i]])

print(table)
