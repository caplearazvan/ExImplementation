

#6.Given a two list of numbers create a new list such that new list should contain only odd numbers from the first list and even numbers from the second list.


list1=[1,2,5,4,8,9,213,254,568]
list2=[3,6,9,10,20,25,269,512,1324]

list3=[]
for i in range(len(list1)):
    if(list1[i]%2==0):
        list3.append(list1[i])
for i in range(len(list2)):
    if (list2[i] % 2 != 0):
        list3.append(list2[i])
print(list3)



