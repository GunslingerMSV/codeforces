"""
UFBA - DSU Training Contest
https://codeforces.com/gym/102078
"""

def ProblemA():
    """
    https://codeforces.com/gym/102078/problem/A
    я пока не вижу какого то хитрого алгоритма решения. Попробуем брутфорс
    """
    
    def GCD(a, b):
        """
        Нахождение наибольшего общего делителя алгоритмом Евклида
        """
        a, b = max(a, b), min(a, b)
        a, b = b, a % b
        if b == 0:
            return a
        else: 
            return GCD(a, b)
        
    
    #ввод данных
    #n, m, q = (int(el) for el in input().split())
    #games = [0] * q
    #for i in range(q):        
    #    games[i] = [0] * 2
    #    games[i][0], games[i][1] = (int(el) for el in input().split())
    
    n, m, q = 25, 6, 1
    games = [[20, 9]]
    #расчет
    for i in range(q):
        a = max(games[i][0], games[i][1])
        b = min(games[i][0], games[i][1])
        setTotal = list()
        for j in range(m, 0, -1):
            setCurr = set()
            for k in range(1, n // j + 1, 1):
                setCurr.add(k * j)
            
            if len(setCurr) > 1:
                setTotal.append(setCurr.copy())
            if len(setTotal) >= 2:
                for k in range(len(setTotal) - 2, 0, -1):
                    for l in range(len(setTotal) - 1, k, -1):                        
                        if setTotal[k].intersection(setTotal[l]) != set():
                            setTotal[k].union(setTotal[l])
                            setTotal.pop(l)
            
            flag = False
            for k in range(len(setTotal)):
                if (a in setTotal[k]) and (b in setTotal[k]):
                    flag = True
                    break
            if flag:                
                break
        print(m - j + 1)

if __name__ == '__main__':
    ProblemA()
