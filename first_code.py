
import datetime

s = 'Hello World'
print(s)
print('*********************')
print('NEXT PROGRAM')
print('*********************')
name = input('Entry with your name: ')
print(name)
print('*********************')
print('CALCULATOR imc')
print('*********************')
weigth = eval(input('Entry with your weigth: '))
heigth = eval(input('Entry with your heigth: '))
imc    = weigth / (heigth ** 2)
print(' your IMC is ', imc)
time = datetime.datetime.now()
hour   = time.hour
minute = time.minute
seconds= time.second
print(f'{time.day:2}/{time.month:2}/{time.year:4}')
print(f'Hour {hour} : Minutes {minute} : Seconds {seconds}')