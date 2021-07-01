
#7.Given a number from user, calculate the sum of all number from 1 to a given number.

num=int(input("Please choose a number to calculate\n"))
index=0
for index in range(num+1):
    index+=index

print("the sum of all numbers is: {}".format(index))
