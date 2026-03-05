# Prime Numbers Finder

num = int(input("Enter a number: "))

print("Prime numbers up to", num, "are:")

for n in range(2, num + 1):
    is_prime = True
    
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(n)