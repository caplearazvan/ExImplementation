# 1. Given two integer numbers return their product. If the product is greater than 1000, then return their sum.
int1=10
int2=12
def Func(int1, int2):
    product=int2*int2
    if product > 1000:
        return int1+int2
    else:
        return product
int3 = Func(int1, int2)
print(int3)







