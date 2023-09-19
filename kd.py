num1 = int(input("Enter the 1st num: "))
num2 = int(input("Enter the 2nd num: "))

print("Choose the operation: \n"
      "1. Add \n"
      "2. Multiply \n"
      "3. Divide \n"
      "4. Subtract ")

choice = input()

if choice == '1':
    result = num1 + num2
    operation = "+"
elif choice == '2':
    result = num1 * num2
    operation = "*"
elif choice == '3':
    result = num1 / num2
    operation = "/"
elif choice == '4':
    result = num1 - num2
    operation = "-"
else:
    print("Invalid choice")
    exit()

print(f"{num1} {operation} {num2} = {result}")
