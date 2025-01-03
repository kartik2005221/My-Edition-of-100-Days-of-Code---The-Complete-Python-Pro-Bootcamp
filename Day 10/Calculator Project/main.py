from art import logo

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

opera = {
    '+' : add,
    '-' : substract,
    '*' : multiply,
    '/' : divide
}

# print(opera['*'](4, 8))
def calc():
    """For Calculator"""
    print(logo)
    n1 = int(input("Enter 1st Number : "))
    cont = True
    while cont:
        sy = input("Enter symbol \n + \n - \n * \n / \n\t::: ")
        n2 = int(input("Enter 2nd Number : "))
        result = opera[sy](n1, n2)
        print(f"the result of operation {sy} bw {n1} and {n2} is {result}")
        k = input("contd? y for yes, n for new calculation, q for quit : ")
        n1= result
        if k=='n':
            print('\n'*100)
            calc()

calc()