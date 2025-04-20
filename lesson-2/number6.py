
num = input("Enter a number: ")


cleaned_num = num.replace(".",'').lstrip("-")
print(cleaned_num)

if cleaned_num.isdigit():
    last_digit = num[-1]
    print(f"The last digit of {num} is: {last_digit}")
else:
    print("Invalid input. Please enter a valid number.")