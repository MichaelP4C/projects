try:
    numenator = int(input('Enter numenator: '))
    
    
    choices = ['/', '*', '-', '+']
    devider = input('What do you want to devide by?: (+, -, *, /) ')

    denumenator = int(input('Enter denumenator: '))

    if devider == '/':
          print(numenator/denumenator)
    elif devider == '*':
          print(numenator*denumenator)
    elif devider == '-':
          print(numenator-denumenator)
    elif devider == '+':
          print(numenator+denumenator)

    if devider not in choices:
          print('Something went wrong!')
    

except ZeroDivisionError:
        print('You cant devide by zero!')
except ValueError:
      print('You can only enter numbers!')


