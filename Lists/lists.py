grades = [5, 2, 4, 1, 4, 3, 2, 5, 2, 3, 5,]


average = sum(grades) / len(grades)
print(f"average: {average}")

passed = [grade for grade in grades if grade > 1]
print(f"passed:", passed)

numbers = [2, 3, 4, 4, 1, 1, 4, 5]
remove_duplicate = []

for numb in numbers:
    if numb not in remove_duplicate:
        remove_duplicate.append(numb)
print(remove_duplicate)


fruits = ["apple", "banana", "pineapple", "lemon", "orange", "kiwi"]

list_fruit = []

for fruit in fruits:
    if len(fruit) > 5:
        list_fruit.append(fruit)
print(list_fruit)