import sys

"""Those that don't have uva or kattis ID aren't uva, kattis problems"""

def main():
    #modulo
    print(modulo(15,4))

#######tasks with bit manipulation

#Obtain the remainder (modulo) of S when it is divided by N (N is a power of 2)
def modulo(dvd, dvs):
    return ((dvd) & (dvs-1))


if __name__ == "__main__":
    main()

