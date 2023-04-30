def pnum():
    while True:
        try:
            num = int(input('Input a number: '))
            print(f'The string representation of the number you entered is {str(num)}')
            break
        except:
            print('This is not a number!!! Please Try again')
print(pnum())