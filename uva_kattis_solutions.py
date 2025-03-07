import sys

"""Those that don't have uva or kattis ID aren't uva, kattis problems"""

def main():
    #modulo
    #print(modulo(15,4))
    print(lsb(1))

#######tasks with bit manipulation

#Obtain the remainder (modulo) of S when it is divided by N (N is a power of 2)
def modulo(dvd, dvs):
    return ((dvd) & (dvs-1))

#Determine if S is a power of 2.
def isPower2(n):
    return (not(n & (n - 1)))
    #return (n & -n) == n

def lsb(x):
    n = 0
    while (x | (1 << n)) != x: 
        n += 1
    return n

if __name__ == "__main__":
    main()

