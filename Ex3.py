# 3. Given a list of numbers, Iterate it and print only those numbers which are divisible by 5.
my_list=[5,10,23,27,30,50,51,98,125,137]

for index in range(len(my_list)):
    remainder= my_list[index] % 5
    if remainder==0:
        print(my_list[index])

