#Program to check whether the input received from user is prime or not.💻🚀

num = int(input(">> "))


def isPrime(num):
    for i in range(2,num):
        if num%i==0:
            return "Number is Not prime"
    return "Number is Prime"


print(isPrime(num))