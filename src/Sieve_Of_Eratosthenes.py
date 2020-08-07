# Theorem: If n is a composite integer, then n has a prime 
# factor not exceeding square root n, so to find all the 
# prime less than a given positive integer we use same procedure
# where we find the square root of n ans take multiples of primes
# we get 
# function to caluclate prime less than n
def sieve_of_Eratosthenes(n):
    prime_numbers = [True for i in range(n + 1)]
    prime = 2
    # multiples of prime 
    while(prime * prime <= n):
        if(prime_numbers[prime] == True):
            for number in range(prime * prime, n + 1 , prime):
                prime_numbers[number] = False
        prime += 1
    #printing the remaining number which are just primes without multiples 
    for prime in range(2, n + 1):
        if prime_numbers[prime]:
            print(prime)

user_input = int(input("Find Prime numbers less than: "))
print(f"Prime number less than {user_input} are: ")
print(sieve_of_Eratosthenes(user_input))
