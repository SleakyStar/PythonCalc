print("Welcome to Simple Python Calculator")
while True:
    print("Ask some math")
    num1 = int(input("First number: "))
    todo = input("Sign: ")
    num2 = int(input("Second number: "))
    if todo == "+":
        print(num1+num2)
    if todo == "*":
        print(num1*num2)
    if todo == "/":
        print(num1/num2)
    if todo == "-":
        print(num1-num2)
