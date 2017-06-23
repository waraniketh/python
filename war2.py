def main():
    first = int(input("enter first number"))
    second = int(input("enter second number"))
    mystring = int(input("enter length of series"))
    third = 0
    print(first)
    print(second)
    for i in range(0, mystring-2):
        third = first + second
        print(third)
        first = second
        second = third
main()
