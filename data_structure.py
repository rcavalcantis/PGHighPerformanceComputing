from numpy import array

from selection import selecionador

cadeiras = array([["Português", "Matemática" , "Química" ], ["História", "Geografia" , "Física"]], dtype=str)
print(cadeiras[0][0])
print(cadeiras[1][2])
semestre = 1
for row in cadeiras:
    print(f'Semestre {semestre}')
    for col in row:
        print(col)
    print(' ***** ')
    semestre += 1


