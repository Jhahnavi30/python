# write the function to calculate 2nd power of a number
# return the result from the function and print the result

base = 3
exponent = 4

result = 1

for exponent in range(exponent, 0, -1):
    result *= base

print("Answer = " + str(result))


def power_2(a: int):
    return a ** 2

print(power_2(6))

# write a function to calculate a**n
def exponentiate(a, n):
    result = 1
    for _ in range(n):
        result *= a
    return result
base = 2
power = 5
result = exponentiate(base, power)
print(result)

