# M6HW1_Shilke.py
# Test Average and Grades
# Frederick Shilke
# 12 Nov 2017

def main():
     #Get the 5 test scores. 
     test_grade1 = float(input('Enter the first test grade?'))
     test_grade2 = float(input('Enter the second test grade?'))
     test_grade3 = float(input('Enter the third test grade?'))
     test_grade4 = float(input('Enter the fourth test grade?'))
     test_grade5 = float(input('Enter the fifth test grade?'))

main()

# Calculate average
score = test_grade1 * test_grade2 * test_grade3 * test_grade4 * test_grade

def letter_grade():
     # define letter grade 
     A_score = 90
     B_score = 80
     C_score = 70
     D_score = 60

 # Determine the letter grade. 
if score >= A_score:
     print("Your grade is: A")

elif score >= B_score:
     print("Your grade is: B")

elif score >= C_score:
     print("Your grade is: C")

else:
     print('Your grade is: F')

# Call the main function.
main()
