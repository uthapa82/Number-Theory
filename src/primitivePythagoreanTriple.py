# python program for  Pythagorean Triples Theorem

# Pythagorean Triples Theorem: We will get primitive pythagorean triples(a, b, c)
#  of the solutions of pythagorean equation a^2 + b^2 = c^2 satisfying coditions gcd(a, b, c) = 1 
#   , 2|a, a > 0, b > 0, c > 0 by the given formulas 
#                    a = 2st, b = (s^2 - t^2 ), c = (s^2 + t^2 )
#      where s > t > 0 any odd integers with no common factors i.e gcd(s, t) = 1 and s not congurent to t mod 2.
#
# Triplets less than the given number by user 

# Euclidean Algorithm to determine gcd
def gcd(a, b):
    '''Greatest Common divisor of a and b '''
    while b:
        a , b = b , a % b
    return a

def pythagoreanTriple(endNumber):
#primitive pythagorean triplets (PPT) list 
    pptList = []
    for s in range(1 , endNumber):
        for t in range(s + 1, endNumber + 1):
            if (s**2 + t**2) > endNumber:
                break
            if s % 2 == 1 and t % 2 == 1:
                continue
            if gcd(s, t) != 1:
                continue

            pptList.append([t**2 - s**2, 2*s*t,t**2 + s**2])
            
    return pptList
lessThan = int(input("Enter the number until which you want the PPT: "))
for i, j in enumerate(pythagoreanTriple(lessThan) ,1 ):
    print(i, j)