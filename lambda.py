# def power(num):
#     return lambda x: x ** num

# sq = power(2)
# print(sq(5))

from functools import reduce

def factorial(n):
    return reduce(lambda x,y : x*y, range(1,n+1))

n = 5
print(factorial(n))