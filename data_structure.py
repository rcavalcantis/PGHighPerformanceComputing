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

str = 'Sou programador Python'
print(str[5:0:-1])

for k in range(0, 4, -1):
    print(k)
