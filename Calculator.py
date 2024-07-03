logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1, n2):
    return n1 + n2;

def subtract(n1, n2):
    return n1 - n2;

def multiply(n1, n2):
    return n1 * n2;

def divide(n1, n2):
    return n1 / n2;

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
    }

print(logo)
n1 = float(input('Enter the first number: '))
for symbol in operations:
    print(symbol)
    
choice = 'y'
while choice == 'y':
    op = input("Select An Operation to perform: ")
    n2 = float(input('Enter Next number: '))
    calc = operations[op]
    result = calc(n1, n2)
    print(f"{n1} {op} {n2} = {result}")
    choice = input(f"Type 'y' to continue with calculating with {result}, or type 'n' to exit: ")
    if(choice == 'y'):
        n1 = result
    
    