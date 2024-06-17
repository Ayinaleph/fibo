from argparse import ArgumentParser, Namespace
print('Hello World, I\'m Felix')

def main():
    print('Main method')
    
if __name__ =='__main__':
    main()

parser = ArgumentParser()
parser.add_argument('nth_term', help='The nth term of a fibonacci sequence', type=int)
args: Namespace = parser.parse_args()

fib = 1
fib1 = 1
fib2 = 1
if args.nth_term == 1 or args.nth_term == 2:
    print('1')
else:
    print('1')
    for n in range(2,args.nth_term):
        print(f'{fib}')
        fib = fib1 + fib2
        fib1 = fib2
        fib2 = fib
    print(f'{fib}')
    fib1 = 0
    fib2 = 1
    fib = 0