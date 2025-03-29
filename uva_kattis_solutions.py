import sys

"""Those that don't have uva or kattis ID aren't uva, kattis problems"""

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

def jollyjumpers():
    #kattis jollyjumpers
    inputs = iter(sys.stdin.readlines())
    line = next(inputs, None)
    while line is not None:
        values = list(map(int,line.split(" "))) 
        jolly = "Jolly"
        if len(values) > 2:
            max = values.pop(0) - 1
            array = [0]*max
            i = 1
            while i < len(values):
                diff = abs(values[i] - values[i-1])
                if diff <= max and array[diff-1] == 0:
                    array[diff-1] = 1
                    i += 1
                    continue
                jolly = "Not Jolly"
                break
        print(jolly)
        line = next(inputs, None)


def polePosition():
    #UVa 12150   
    input = iter(sys.stdin.readlines())
    size = next(input, None)
    while int(size) != 0:
        array = [None]*int(size)
        for position in range(int(size)):
            x = (next(input, None)).rstrip().split(" ")
            car, gain = x
            if array is not None:
                initial = position + int(gain)
                if int(gain) in range(-int(size)+1,int(size)) and initial in range(0,int(size)) :
                    if array[initial] is None:
                        array[initial] = car
                        continue
                array = None

        #printResult
        result = ""
        if array is not None:
            for elem in array :
                result += elem + " "
            print(result[:-1])
        else: print("-1")

        size = next(input, None)

def onlyISolvedIt(key, i, solved):
    for x in range(len(solved)):
        if x != i:
            if key in solved[x]: return False
    return True

def onlyIDidIt():
    #UVa 11222
    inputs = iter(sys.stdin.readlines())
    test = int(next(inputs,"0"))
    for case in range(test):
        solved = [None]*3
        sorted = [None]*3
        for x in range(3):
            solved[x]={}
            line = next(inputs).rstrip().split(" ")
            line.pop(0)
            for elem in line:
                solved[x][elem] = True
        winner = []
        max = 0
        for i in range(3):
            current = 0
            sorted[i] = []
            for key in solved[i]:
                if onlyISolvedIt(key,i,solved):
                    current += 1
                    sorted[i].append(int(key))
            if current >= max:
                if current > max:
                    winner.clear()
                    max = current
                    winner.append(i)
                else: winner.append(i)
    
        print(f"Case #{case+1}:")
        for elem in winner:
            sortedString = f"{str(elem+1)} {len(sorted[elem])} "
            sorted[elem].sort()
            for elem in sorted[elem]:
                sortedString += str(elem) + " "
            print(sortedString.rstrip())
    return

def main():
    onlyIDidIt()

if __name__ == "__main__":
    main()

