import sys

print(f'My arguments are {sys.argv}')

()

print(f'A python program that prints it command line arguments, one to a line:')
for arg in sys.argv:
    print(f'\t{arg}')
print(f'This Python program has {len(sys.argv)} command line arguments')

for i in range(len(sys.argv)):
    print(f'\t{i}. {sys.argv[i]}')

def sumOfSysargv():
    accum = 0
    for arg in sys.argv:
        if arg.isnumeric():
            accum += int(arg)
    print(f'The sum of my arguments is: {accum}')

def productOfSysargv():
    accum = 1
    for arg in sys.argv:
        if arg.isnumeric():
            accum *= int(arg)
    print(f'The sum of my arguments is: {accum}')

def main():
    if '-product' in sys.argv and '-sum' in sys.argv:
        print("Error! One of '-sum' or '-product' is required as an argument")
    elif '-product' in sys.argv:
        productOfSysargv()
    elif '-sum' in sys.argv:
        sumOfSysargv()
    else:
        print("Error! One of '-sum' or '-product' is required as an argument")

main()
