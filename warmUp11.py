#Claire Yegian
#10/23/17
#warmUp11.y - determines if a number is prime

def isPrime(n):
    i = 2
    while i<=n:
        if n%i==0:
            return False
        i += 1
    return True

print(isPrime(17))