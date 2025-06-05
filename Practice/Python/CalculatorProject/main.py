# CALCULATOR PROJECT
# CREATED: 03/21/2025
# LAST UPDATE: 03/26/2025
# ESTIMATED COMPLETION TIME: 2.5 HOURS OF ACTIVE WORK

# Four basic operation functions
def op_add(a, b):
    return a + b

def op_sub(a, b):
    return a - b

def op_mult(a, b):
    return a * b

def op_div(a, b):
    return a / b

# Menu choice function
def menu_display():
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('0. Exit Calculator')

# IF statements
def answer_calc():
    while True:
        user_choice = input('Choose an operation from the above options:')
        if user_choice in ('1','2','3','4'):
            try:
                number1 = float(input('Enter a number here: '))
                number2 = float(input('Enter another number here: '))
            except ValueError:
                print('INVALID INPUT. ENTER NUMBERS/DIGITS ONLY.')
            if user_choice == '1':
                print(number1, '+' ,number2, '=' ,op_add(number1,number2))
            elif user_choice == '2':
                print(number1, '-', number2, '=', op_sub(number1, number2))
            elif user_choice == '3':
                print(number1, '*', number2, '=', op_mult(number1, number2))
            elif user_choice == '4':
                print(number1, '/', number2, '=', op_div(number1, number2))

            # Check for new calculation request
            new_calc = input('Would you like to do another calculation (Y or N): ')
            if new_calc == 'N':
                break
            else:
                print("INVALID INPUT")
# Defining the main program function
def main():
    menu_display()
    answer_calc()
main()


