#slicing for Lists
name = ["Ethio", "Banana", "china", "Apple"]
print(name[-1:-5:-2])      #prints:  Apple, Banana
print(name[::])            #prints All lists
print(name[0:4:3])         #prints: Ethio, Apple

#slicing for string
name = "Sol The Great"
print(name[0:4:1])       #prints:  Sol
print(name[8:12:1])      #prints: Grea
print(name[8:13:1])      #prints: Great
print(name[8::3])        #prints: Ga
print(name[-2:-6:-1])    #prints: aerG
print(name[-1:-6:1])     #prints nothing. b/c, the order is reversing but the step is positive.
