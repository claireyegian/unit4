#Claire Yegian
#10/27/17
#warmup12.py - finds GCF of two numbers

def GCF(num1,num2):
    i == min(num1,num2)
    while i>=0:
        if num1%i==0:
            if num2%i==0:
                return(i)
                break
        elif num1%i!=0:
            break
    i = i - 1

print(GCF(10,15))
