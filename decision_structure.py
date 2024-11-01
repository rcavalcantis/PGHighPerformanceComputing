"""
EXERCISE 1
"""
age = eval(input('Inform the child age: '))
if age < 5:
    print('The child should be vaccinated against the flu.')
    print('Look for the Medical Post more close')
elif age == 5:
    print('The vaccine will be available as soon')
    print('Wait by the next information')
else:
    print('The vaccination will be available only 3 months ahead')
    print('Get more information into this period')
print('Take care your health. See you!')

"""
EXERCISE 2
"""
lado1 = eval(input('Entre com o maior lado do triângulo: '))
lado2 = eval(input('Entre com o segundo lado do triângulo: '))
lado3 = eval(input('Entre com o terceiro lado do triângulo: '))
if (lado1**2 == lado2**2 + lado3**2):      #condição1
    print('O triângulo é retângulo')
elif (lado1**2 < lado2**2 + lado3**2):   #condição2
    print('O triângulo é acutângulo')
else:
    print('O triângulo é obtusângulo')