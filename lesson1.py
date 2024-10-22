'''
Name:
Date: 10/22/24
Description: Unit 4 Lesson 1 - while loops
'''
# while loops run while a condition is true
# we usually don't know how many times
# this scenario is when they are most often used

'''
some_condition

while some_condition is true:
  code to esecute
  update variable (if forgotten -> infinite loop)
  
'''

start_number = 10
while -1 < start_number <= 10:
  print(start_number)
  start_number = start_number - 1
print("Blastoff!") # this will always print 

# change the code so it prints 10 9... 0 Blastoff!

# making a loop run to get user input 

While True:
  user_age = int(input("Enter age or -1 to quit: "))
  if user_age == -1:
    break # exits the loop
  else:
    continue # return to top of loop 

