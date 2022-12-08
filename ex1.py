try:
    begin = int(input('Begin:'))
    end= int(input('End:'))
    for item in range (begin, end + 1): 
        print(item, end= '\t') 
        if item % 7 == 0:
           print('There are multiples of 7 here!') 
        else:
           print('There are no multiples of 7 here!')
except Exception as ex: print(f'Error: {ex}')