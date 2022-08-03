
import sys

def fibonacci(number):
    try:
        number = int(number)
    except:
        print ("Not a Number")
        return

    if number == 0:
        print(0)
        return 0

    if number == 1:
        print(1)
        return 1


    n1 = 0
    n2 = 1
    count = 1

    while count < number:
        count += 1
        fibo = n1 + n2
        n1 = n2
        n2 = fibo

    print (fibo)

fibonacci(sys.argv[1])