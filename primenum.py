n = int(input("enter a num: "))

for i in range(2, n):
    if n % i == 0:
        print(n, "is not a prime number")
        break
    if n%i != 0:
        print(n, "is a prime number")
        break