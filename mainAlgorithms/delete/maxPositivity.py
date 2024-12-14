from math import inf
def solve(self, A):
        ansi = inf
        ansl = 0
        n = len(A)
        temp = 0
        for i in range(n):
            if A[i] > 0:
                temp += 1
            else:
                if ansl < temp:
                    ansi = i-temp
                    ansl = temp
                temp = 0
        print(ansl , temp)
        if ansl < temp:
             ansi = (n) - temp
             ansl = temp
        print(ansi , ansi+ansl)


        return A[ansi:ansi+ansl]

A = [1, 2, -1, 3, 4]
A = [1,2,3,4]
print(solve('s' ,A ))