## basic lambda function : used for anosymus function
doSum = lambda x, y: x + y
print(doSum(10, 20)) # Output: 30

## list filter with lambda function
## Syntax: result = filter(function, sequence) fumction defines the condition to filter the sequence, result is a filter object


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8]


# ## list map with lambda function
# squared_numbers = list(map(lambda x: x ** 2, numbers))
# print(squared_numbers)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81] 