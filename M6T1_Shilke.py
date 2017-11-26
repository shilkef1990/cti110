# M6T1_Shilke.py
# Kilometer Converter
# Frederick Shilke
# 23 Sept 2017

CONVERSION_FACTOR = 0.6214

def main():
     #Get the distance of kilometers. 
     kilometers = float(input('Enter the number of kilometers to be converted? '))

     #Display the distance converted to miles.
     show_miles(kilometers)
     
def show_miles(km):
     # Calculate miles
     miles = km * CONVERSION_FACTOR
     
     # Display the miles. 
     print (km, 'kilometer equeals', miles, 'miles.')
# Call the main function.
main()






