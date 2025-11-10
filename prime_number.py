#game prime not prime
def num_prime(number):
    is_prime=True
    for i in range(2,number - 1):
        if number % i==0:
            is_prime=False
    if is_prime:
        print(f"the number:{number} is prime")
    else:
        print(f"the number {number} is not prime")
num=int(input("check the number if is prime: "))
num_prime(number=num)
