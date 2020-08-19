"""
https://codeforces.com/gym/100092
2012-2013 Тренировка СПбГУ С #3. Язык C++.
но делать будем на Python ))))
"""

def problemA():
    """
    https://codeforces.com/gym/100092/problem/A
    полное решение
    """
    with open("sum.in", "r") as inFile:        
        a, b = (int(el) for el in inFile.readline().split())        
    with open("sum.out", "w") as outFile:
        outFile.write(str(a + b))
  

def problemB():
    """
    https://codeforces.com/gym/100092/problem/B    
    полное решение
    """
    with open("product.in", "r") as inFile:        
        a, b = (int(el) for el in inFile.readline().split())        
    with open("product.out", "w") as outFile:
        outFile.write(str(a * b))


def problemD():
    """
    https://codeforces.com/gym/100092/problem/D  
    полное решение
    """
    
    with open("gcd.in", "r") as inFile:        
        a, b = (int(el) for el in inFile.readline().split())        
    
    a, b = min(a, b), max(a, b) # всегда считаем, что a - меньшее из двух чисел
    GCD = 1
    if b % a == 0 : #сразу проверим, не является ли меньшее из наших чисел общим делителм
        GCD = a
    else : 
        # задача нахождения НОД связана с задачей получения последовательности простых чисел
        simple = [2] # массив простых чисел - потенциальных делителей наших числе, 1 -  в него не включаем
        aDivisor = [1]
        bDivisor = [1]
        #проверим, делятся ли наши числа на 2
        while True :
            if a % 2 == 0 : 
                aDivisor.append(2)
                a //= 2
            else : break
        while True : 
            if b % 2 == 0 : 
                bDivisor.append(2)
                b //= 2
            else : break
        c = 3
        flagTotal = True
        while flagTotal :
            if c ** 2 > min(a, b) : 
                c = min(a, b)
                if c == 1 : break
                flagTotal = False
            flag = True
            for i in simple :
                if i ** 2 > c : break
                if c % i == 0 :
                    flag = False
                    break
            if flag : 
                simple.append(c)
                while True :
                    if a % c == 0 : 
                        aDivisor.append(c) 
                        a //= c
                    else : break
                while True :
                    if b % c == 0 : 
                        bDivisor.append(c) 
                        b //= c
                    else : break
            c += 2
        i = j = 0
        while i < len(aDivisor) and j < len(bDivisor) :
            if aDivisor[i] == bDivisor[j] :
                GCD *= aDivisor[i]
                i += 1
                j += 1
            elif aDivisor[i] > bDivisor[j] : j += 1
            elif aDivisor[i] < bDivisor[j] : i += 1
    with open("gcd.out", "w") as outFile:
        outFile.write(str(GCD))


def problemE() :
    """
    https://codeforces.com/gym/100092/problem/E
    полное решение
    """
    with open("fib.in", "r") as inFile:        
        n = int(inFile.readline())

    a = b = 1
    if n > 1 :        
        for i in range(n - 1) :
            a, b = a + b, a
    
    with open("fib.out", "w") as outFile:
        outFile.write(str(a))


def problemC() :
    """
    https://codeforces.com/gym/100092/problem/C    
    полное решение
    """
    with open("apbtest.in", "r") as inFile:        
        a = int(inFile.readline())
    
    if a > 0 : b = (10 ** 9)
    else : b = - (10 ** 9)
    a -= b
    
    with open("apbtest.out", "w") as outFile:
        outFile.write(str(a) + ' ' + str(b))


def problemF() :
    """
    https://codeforces.com/gym/100092/problem/F
    полное решение
    """    
    with open("skateboard.in", "r") as inFile:        
        n = int(inFile.readline())
        a = [int(el) for el in inFile.readline().split()]

    k = 0
    if n > 2 :
        for i in range(n - 1) :
            if a[i] > a[i - 1] and a[i] > a[i + 1] : k += 1

    with open("skateboard.out", "w") as outFile:
        outFile.write(str(k))
 

def problemG() :
    """
    https://codeforces.com/gym/100092/problem/F
    полное решение
    """    
    with open("numbers.in", "r") as inFile:                
        a, b = (int(el) for el in inFile.readline().split())

    x = -10000
    flag = True
    
    while x <= 10000 :
        y = (1 - a * x) / b
        if y == int(y) and abs(y) <= 10000 :
            flag = False
            y = int(y)
            break
        x += 1

    if flag : x = y = 0    
    with open("numbers.out", "w") as outFile:
        outFile.write(str(x) + ' ' + str(y))
    

def problemH() :
    """
    https://codeforces.com/gym/100092/problem/F
    полное решение
    """
    with open("symposium.in", "r") as inFile:        
        n = int(inFile.readline())
        a = [int(el) for el in inFile.readline().split()]
    
    a.sort()
    cnt1 = cnt2 = 1
    if n > 1 :
        for i in range(1, n) :
            if a[i] < 2 * a[i - 1] : cnt1 += 1
            else :
                cnt2 = max(cnt1, cnt2)
                cnt1 = 1
        cnt2 = max(cnt1, cnt2)

    with open("symposium.out", "w") as outFile:
        outFile.write(str(cnt2))

if __name__ == "__main__" :
    problemH()