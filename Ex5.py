# 5. Reverse a given number and return true if it is the same as the original number.

num=int(input("Enter a number:\n"))
list1=list()
list_reversed=list()

for i  in range(num):
    digit=num%10
    list_reversed.append(digit)
    num = num // 10
    if num==0:
        break

decrement=0
lenght=len(list_reversed)-1

for i in range(len(list_reversed)):
    list1.append(list_reversed[lenght])
    lenght-=1
    decrement+=1
    if i==len(list_reversed):
        break

if list1==list_reversed:
    print("the reverse of the number is the same as the number")
else:
    print("the reverse of the number is different as the number")
