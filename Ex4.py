#4. Given a number count the total number of digits in a number.

num=123456
sum_of_digits=0
for i  in range(num):
    digit=num%10
    num=num//10
    sum_of_digits+=digit
    if num==0:
        print("the sum of no {} is {}".format(num, sum_of_digits))
        break


