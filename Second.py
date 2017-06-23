def main():
    mystring = input("enter your string")
    required=mystring.__len__()
    count=0
    for i in range(0, required):
        if(mystring[required-i-1]==mystring[i]):
            count=count+1
    if(count==required):
        print(mystring)
main()
