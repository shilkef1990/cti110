# M5T2_Shilke
# Bug Collector
# Frederick Shilke
# 16 Oct 2017

# Initialize the accumulator.
total = 0

# Get the bugs collected for each day.
for day in range (1, 8):
        print ('Enter the bugs collected on day', day)
        bugs = int(input())
        total += bugs

# Display the total bugs.
print('You collected a total of', total, 'bugs.')

	

