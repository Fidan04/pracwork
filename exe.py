''' The program that finds perfect and friendly numbers till the given number '''
import math

def isPerfect(n): 
    '''
    It finds if n is perfect number or not
    If it is perfect number, It is True, else False
    
    '''
    sum=0
    m=math.ceil(n/2)+1

    for i in range(1, m):
        if n%i==0:
            sum+=i

    if sum==n:
        return True
    else:
        return False


def sumDiv(n):
    '''
    this function finds the sum and the keyword return gives us the answer
    
    '''
    sum=0
    m=math.ceil(n/2)+1

    for i in range(1, m):
        if n%i==0:
            sum+=i

    return sum



def isFriend(a,b):
    '''
    if a and b are friendly numbers, the keyword return gives us true, else false
    
    '''
    if sumDiv(a)==b and sumDiv(b)==a:
        return True
    else:
        return False


MAX=int(input("Enter MAX: "))

for N in range(2,MAX+1):
    if isPerfect(N):
        print("{0} is perfect number".format(N))
    else:
        M=sumDiv(N)
        if M<=MAX and N<M:
            if isFriend(N,M):
                print("{0} and {1} are friendly numbers".format(N,M))
    