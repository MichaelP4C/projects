try:
    numenator = int(input('Enter numenator: '))
    
    
    choices = ['/', '*', '-', '+']
    devider = input('What do you want to devide by?: (+, -, *, /) ')
    
    show_result = '='

    denumenator = int(input('Enter denumenator: '))
    
    if devider == '/':
          result = (numenator/denumenator)
    elif devider == '*':
          result = (numenator*denumenator)
    elif devider == '-':
          result = (numenator-denumenator)
    elif devider == '+':
          result = (numenator+denumenator)
    print(result)
      

    if devider not in choices:
          print('You can only devide by +,-,*,/')
    

except ZeroDivisionError:
        print('You cant devide by zero!')
except ValueError:
      print('You can only enter numbers!')


