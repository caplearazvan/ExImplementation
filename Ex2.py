
# 2.1. Given a string, display only those characters which are present at an prime index number.
value = input("Please enter a string:\n")
for index in range(2, len(value)):
    for i in range(2, index):
        remainder = index % i
        if remainder != 0:
            print("Value at even index {} is {}".format(index, value[index]))
            break
        else:
            break
            
 # 2.2 Given a string, display only those characters which are present at an odd index number.
value = input("Please enter a string:\n")
for index in range(2, len(value)):
    remainder = index % 2
    if remainder != 0:
        print("Value at odd index {} is {}".format(index, value[index]))
    else:
        continue

