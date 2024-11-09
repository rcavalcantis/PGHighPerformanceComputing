import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

exercise = 0
while exercise != 99:
    exercise = eval(input('Inform the exercise number [1,2,3,4,5,6,7,8,9,10,11,12]  99-Exit: '))
    if exercise==1:
        while True:
            print('You are into first loop.')
            option1 = input('Do you desire get out of first loop? Write YES to that. ')
            if option1 == 'YES':
                break # Out of first loop
            else:
                while True:
                    print('You are into second loop.')
                    option2 = input('Do you desire get out of second loop? Write YES to that. ')
                    if option2 == 'YES':
                        break # Out of second loop
                print('You out from second loop. ')
        print('You out from first loop. ')

    if exercise==2:
        for num in range(1,11):
            if num == 5:
                break
            else:
                print(num)
        print('Loop end')

    if exercise==3:
        a = 0
        for i in range(30):
            if a % 2 == 0:
                a += 1
                continue
            else:
                if a % 5 == 0:
                    break
                else:
                    a += 3
        print(a)