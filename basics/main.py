# user = input("type your name: ")
# age = int(input("type your age: "))

# print(f"Hello {user} you are {age} years old.")


# num1 = int(input("type first number: "))
# num2 = int(input("type second number: "))

# print(f"sum: {num1 + num2}")
# print(f"difference: {num1 - num2}")
# print(f"product: {num1 * num2}")

# if num2 == 0:
#     print("quotient: error, cannot divide by zero")
# else:
#     print(f"quotient: {num1 / num2}")


number = int(input("type number:"))

if number % 2 == 0:
    print("number is even")
else:
    print("odd")



age = int(input("type your age: "))

if age < 0:
    print("age cannot be negative")
elif age < 13:
    print("child")
elif age < 18:
    print("teenager")
else:
    print("adult")