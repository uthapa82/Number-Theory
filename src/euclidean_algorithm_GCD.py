# ---------------------------------------------------
# Greatest common divisor for any given two numbers
# using Euclidean Algorithm, divisions until the 
# remainder is zero 
#----------------------------------------------------
#       General formula is : A = Q * B + R where Q and R 
#         are quotient and Remainder respectively.
#--------------------------------------------------------

# function to calculate the gcd of A, B
def euclidean_GCD(A, B):
    while B:
        A, B = B, A % B
    return A

# user input for the number
first_number = int(input("Enter first number \'A\' : "))
second_number = int(input("Enter second number \'B\': "))

# printing out the result 
print("The GCD of (" + str(first_number) + ", " + str(second_number) +") is :")
print(euclidean_GCD(first_number, second_number))



