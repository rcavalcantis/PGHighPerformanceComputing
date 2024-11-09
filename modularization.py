from typing import overload, override



def categorizing(imc):
    if imc < 18.5:
        print("Low weigth")
    elif imc < 25:
        print("Rigth weigth")
    elif imc <= 30:
        print("Over weigth")
    else:
        print("Fat")

def imc(weigth, heigth):
    print('Parameter Weight: ', weigth)
    print('Parameter Heigth: ', heigth)
    imc = weigth / heigth**2
    print('IMC: ', imc)
    return imc
# TEST
# list = [0,2,4,6,7,8,9]
# for number in list:
#     assert number % 2 == 0, 'Number odd founded ->' + str(number)

data = [118, 1.85]
categorizing(imc(110, 1.85))