# Lambda
# UNa lambda function is a small anonymous function
# A lambda function can take any number of arguments, but can only have one expression
x = lambda a : a + 10
print(x(5))

numeros = [1,2,3,4,5,6,7]
square = lambda num : num ** 2
# print(square(5))

print(list(map(lambda num: num ** 2, numeros)))
