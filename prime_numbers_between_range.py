start = int(input("Enter starting number (>1): "))
end = int(input("Enter ending number: "))

# Print prime numbers
print("Prime numbers are:")

for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
