def a():
    print(f'a is selected')

def s():
    print(f's is selected')

match input ('select some inputs '):
    case 'q':
        a()
    case 'w':
        s()
    case _:
        print('invalid input')
