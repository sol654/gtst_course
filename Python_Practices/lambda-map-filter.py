nums = [14, 2, 3, 4, 5, 8, 10, 12]
def is_even(n):
    return n%2==0
even_nos = list(filter(is_even, nums))
print(even_nos)     #filters and prints even numbers
#OR
nums = [14, 2, 3, 4, 5, 8, 10, 12]
evens = list(filter(lambda n: n%2==0, nums))   #filters and prints the evens
double_evens = list(map(lambda n: n*2, evens))  #doubles the evens only
print(evens)
print(double_evens)