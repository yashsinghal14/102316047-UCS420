#1.1
print("Yash")
print("Yash")
print("Yash")

#2.1
print(3 + 5 + 7)

#2.2
print("Yash" + " " + "Singhal")

#4.1
for i in range(1, 11):
    print("7 x", i, "=", 7 * i)
for i in range(1, 11):
    print("9 x", i, "=", 9 * i)

#4.2
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)

#4.3
n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    total += i
print(total)

#5.1
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b and a > c:
    print(a)
elif b > c:
    print(b)
else:
    print(c)

#5.2
n = int(input("Enter a number: "))
total = 0
for x in range(1, n + 1):
    if x % 7 == 0 and x % 9 == 0:
        total += x
print(total)

#5.3
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
n = int(input("Enter a number: "))
total = 0
for x in range(1, n + 1):
    if is_prime(x):
        total += x
print(total)

#6.1
def sum_of_odds(n):
    total = 0
    for x in range(1, n + 1):
        if x % 2 != 0:
            total += x
    return total
n = int(input("Enter a number: "))
print(sum_of_odds(n))

#6.2
def sum_of_primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    total = 0
    for x in range(1, n + 1):
        if is_prime(x):
            total += x
    return total
n = int(input("Enter a number: "))
print(sum_of_primes(n))