again="yes"
while again=="yes":
    num1 = int(input("Enter the fisrt number:"))
    operator= input("Enter the operator(+,-,*,/:)")
    num2 = int(input("Enter the second number:"))

    if operator == "+":
        result=num1+num2
        print(result)

    elif operator == "-":
        result= num1-num2
        print(result)

    elif operator == "*":
        result= num1*num2
        print(result)

    elif operator == "/":
        if num2 == 0:
            print("can not divide by zero..")
        else:
            result=num1/num2
            print(result)

    else:
        print("invalid operator!!..")
    again=input("can you calculate again(yes/no:)").lower()