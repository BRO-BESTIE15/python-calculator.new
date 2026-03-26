import time

print("Starting Calculator...")
for i in range(3, 0, -1):
    print(i)
    time.sleep(1)
while True:
    try:
        x = float(input("Enter first value: "))
        y = float(input("Enter second value: "))

        op = input("Choose (+, -, *, /, //): ")
        print("Calculating...")
        time.sleep(1)
        print("Processing...")
        time.sleep(1)

        match op:
            case "+":
                print("Answer:", x + y)

            case "-":
                print("Answer:", x - y)

            case "*":
                print("Answer:", x * y)

            case "/":
                if y == 0:
                    print("Cannot divide by zero 💀")
                else:
                    print("Answer:", x / y)

            case "//":
                if y == 0:
                    print("Cannot divide by zero 💀")
                else:
                    print("Answer:", x // y)

            case _:
                print("Invalid operation 😤")

    except ValueError:
        print("Invalid input 💀, try again")

    again = input("Again? (y/n): ")
    if again != "y":
        break
print("Closing...")
for i in range(3):
    print(".")
    time.sleep(0.5)
print("\n THANKS TO USE IT \n")   
print("TTYL")    
