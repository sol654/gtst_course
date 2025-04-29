#filter
nums = [3, 2, 6, 8, 4, 2, 9]
evens = list(filter(lambda n: n%2==0, nums))
print(evens)

#or 
def is_even(n):
    return n%2==0
nums = [3, 2, 6, 8, 4, 2, 9]
evens = list(filter(is_even, nums))
print(evens)

#map
nums = [3, 2, 6, 8, 4, 2, 9]
doubles = list(map(lambda n: n*2, nums))
print(doubles)

#or
nums = [3, 2, 6, 8, 4, 2, 9]
def doub(n):
     return n*2
doubles = list(map(doub, nums))
print(doubles)
