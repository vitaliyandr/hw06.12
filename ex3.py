try:
    begin = int(input('begin->'))
    end= int(input('end->'))
    counter = int(0)

    for item in range(begin+1, end):
        print(item, end=" ")
        if item % 3 == 0:
            print('fizz', end=' ')
        if item % 5 == 0:
            print('buzz', end=' ')
        print()
except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')