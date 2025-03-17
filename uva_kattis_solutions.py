import sys

"""Those that don't have uva or kattis ID aren't uva, kattis problems"""

def main():
    #modulo
    #print(modulo(15,4))
    #print(bin(39),bin(turnOnConsec0(39)))
    greyCode()

#######tasks with bit manipulation

def modulo(dvd, dvs):
    #Obtain the remainder (modulo) of S when it is divided by N (N is a power of 2)
    return ((dvd) & (dvs-1))

def isPower2(n):
    #Determine if S is a power of 2.
    return (not(n & (n - 1)))
    #return (n & -n) == n


def turnOffConsec1(n):
    # Turn o, the last consecutive run of ones in S
    return (n & (n+1))


def turnOnConsec0(n):
    # Turn o, the last consecutive run of ones in S
    return (n | (n-1))


def greyCode():
    #UVa 11173
    """
    pattern 1 : active the first nonzero (from the left) bit of the number
    looks like xor
    """
    inputs = iter(sys.stdin.readlines())
    n = int(next(inputs))
    while n > 0 :
        _, kth = (next(inputs)).split(" ")
        kth = int(kth)
        print(kth^(kth>>1))
        n -= 1

if __name__ == "__main__":
    main()

