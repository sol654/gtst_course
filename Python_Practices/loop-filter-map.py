i = 0
nums=[]
while i < 10:
    i = i+1
    try:
        num = int(input(f"Enter number {i} of 10 numbers: "))
        nums.append(num)
    except ValueError:
        print("Enter integer only!!")
        i = i-1     #if mistake happens, it won't jump some indexs
evens = list(filter(lambda n: n%2==0, nums))
evens_plus_15 = list(map(lambda n: n+15, evens))
print(f"The list is: {nums}\n The evens: {evens}\n Evens + 15: {evens_plus_15}")
