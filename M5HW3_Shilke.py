# M5HW3
# Factortial
# Frederick Shilke
# 22 OCT 2017

userInteger = int( input("Enter a nonnegative integer?: " ) )

while userInteger < 1:
    userInteger = int( input("Enter a nonnegative integer? :" ) )

factorial = 1

for currentNumber in range( 1, userInteger + 1 ): 
    factorial = factorial * currentNumber

print("The factorial of", userInteger, "is", factorial )






