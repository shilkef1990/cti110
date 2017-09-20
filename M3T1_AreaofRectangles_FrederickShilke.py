# M3T1_AreaofRectangles_FrederickShilke.py
# Hello World
# Frederick Shilke
# 20 Sept 2017

# Get the length and width of rectangle 1 and 2.
rectangle1 = int(input('Enter the length of your first rectangle: '))
rectangle2 = int(input('Enter the width of your first rectangle: '))
rectangle1a = int(input('Enter the length of your second rectangle: '))
rectangle2a = int(input('Enter the width of your second rectangle: '))

# Calculate the area of Rectangle1.
rectangle1area = (rectangle1 * rectangle2)

# Calculate the area of Rectangle2.
rectangle2area = (rectangle1a * rectangle2a)

# Is Rectangle1 bigger than Rectangle2.
if rectangle1area > rectangle2area:
     print ("The first rectangle has the larger area!")

# Is Rectangle2 bigger than Rectangle1.
if rectangle1area < rectangle2area:
    print ("The second rectangle has the larger area!")

# Are the rectangles equal.
if rectangle1area == rectangle2area:
    print ("Both rectangles have equal area!")
    









