import os
from importlib.metadata import entry_points
from linecache import clearcache

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

exercise = 0
while exercise != 99:
    exercise = eval(input('Inform the exercise number [1,2,3,4,5,6,7,8,9,10,11,12]  99-Exit: '))
    if exercise==1:
        clear()
        print('****** BEGIN *******')
        nome = input('Entry your name: ')
        for letra in nome:
            print(letra)
        print('******  END  *******')

    elif exercise==2:
        clear()
        print('****** BEGIN *******')
        for item in range(4):
            print(item)
        print('*****************')
        for item in range(2,5):
            print(item)
        print('*****************')
        for item in range (2, 9, 3):
            print(item)
        print('******  END  *******')

    elif exercise==3:
        clear()
        print('****** BEGIN *******')
        for number in range(1,11):
            if (number%2 == 0):
                print(f'The number {number} is even')
            else:
                print(f'The number {number} is odd')
        print('******  END  *******')

    elif exercise==4:
        clear()
        print('****** BEGIN *******')
        sum = 0
        elements = 0
        entryNumber = 0
        while entryNumber <= 0:
            entryNumber = eval(input('Entry with the positive number: '))

        for number in range(1,entryNumber+1):
            sum += number
            elements += 1
        print(f'The sum of the integers between 1 and {entryNumber} is: {sum}/{elements} elements')
        print(f'The average of  integers between 1 and {entryNumber} is {sum/len(range(1,entryNumber+1))} ')
        print('******  END  *******')

    elif exercise==5:
        clear()
        print('****** BEGIN *******')
        names = ['Laura', 'Lis', 'Guilherme', 'Enzo', 'Arthur']
        for name in names:
            print(name)
        print('******  END  *******')

    elif exercise==6:
        clear()
        print('****** BEGIN *******')
        a = 1
        b = 2
        for i in range(3):
            a = a + b
            b = a + b
            print(b)
        print('******  END  *******')

    elif exercise==7:
        clear()
        print('****** BEGIN *******')
        s = 0
        for i in range(5):
            s += 3 * i
        print(s)
        print('******  END  *******')

    elif exercise == 8:
        clear()
        print('****** BEGIN *******')
        print('How many years will be necessarry to increase in 50% the value?')
        factor     = 1
        counter    = 0
        annualRate = eval(input('Inform the annual rate: '))
        while factor < 1.5:
            factor  += factor*annualRate/100
            counter += 1
        print(f'Will be necessary {counter} years to touch 50% of rentability wtih rate of {annualRate} per year')
        print('******  END  *******')

    elif exercise == 9:
        clear()
        print('****** BEGIN *******')
        factor = 1
        sum    = 1
        counter= 1
        while factor >= 0.01:
            factor  = factor * 0.5
            sum     = sum + factor
            counter+= 1
        print(f'The sum of the {counter} termos vale {sum}.')
        print(f'The {counter+1}º factor is {factor} and was below 0.01.')
        print('******  END  *******')

    elif exercise == 10:
        clear()
        print('****** BEGIN *******')
        a = 1
        escolha = input('Você deseja sair? S / N')
        while escolha != 'S':
            print(a)
            a += 1
            escolha = input('Você deseja sair? S / N')
        print('******  END  *******')

    elif exercise == 11:
        clear()
        print('****** BEGIN *******')
        print('******  END  *******')

    elif exercise == 12:
        clear()
        print('****** BEGIN *******')
        print('******  END  *******')