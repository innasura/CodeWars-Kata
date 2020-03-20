# https://www.codewars.com/kata/59ab0ca4243eae9fec000088
# The sum of the primes below or equal to 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below or equal to the number passed in.

def summationOfPrimes(primes):
    p = 2
    prime = [True] * (primes + 1)
    while p * p <= primes:
        if prime[p] == True:
            i = p * 2
            while i <= primes:
                prime[i] = False
                i += p
        p += 1

    return sum([i for i in range(2, primes + 1) if prime[i]])

print(summationOfPrimes(10))

# ------------ Best Practice -------------------

def summationOfPrimes2(primes):
    return sum(i for i in range(2,primes+1) if all(i%j for j in range(2,int(i**.5)+1)))

print(summationOfPrimes2(100))


# ------------ Best Practice -------------------

def summationOfPrimes3(n):
    numbers = [x for x in range(2, n+1)]
    for i, j in enumerate(numbers):
        if j != 'x':
            index = i + j
            while index < len(numbers):
                numbers[index] = 'x'
                index += j
    return sum(list(filter(lambda a: a != 'x', numbers)))

print(summationOfPrimes3(50))