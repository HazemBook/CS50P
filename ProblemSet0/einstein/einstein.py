# ask user for mass as an integer in kilograms
mass = int(input("m: "))

# mass to Joules
# E = mass * 300000000 ** 2

# mass to Joules using pow function
E = mass * pow(300000000, 2)

# output the result
print("E = ", E)