# function
def add(num1, num2):
    return num1 + num2


print(add(2, 3))

# same as above however using lambdas
addition = lambda num1, num2: num1 + num2

print(addition(2, 3))

# another example
# function

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8]


print(numbers_list)


def square_func(num):
    return num ** 2


# squared_numbers = map(square_func, numbers_list)

# using lambdas
squared_numbers = map(lambda x: x**2, numbers_list)

print(list(squared_numbers))

# another example of lambdas
salary = [230, 350, 540, 430]

ten_per_cent_bonus = map(lambda x: x * 1.1, salary)
print(list(ten_per_cent_bonus))
