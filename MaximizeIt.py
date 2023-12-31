# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

def find_max(k_lists, M):
    f = lambda x: x*x 
    combinations = product(*k_lists)
    results = [(sum([f(a) for a in x]) % M) for x in combinations]
    # Return the maximum value
    return max(results)


K, M = tuple(map(int, input().split(" ")))
k_lists = [list(map(int, input().split(" ")))[1:] for _ in range(K)]
print(find_max(k_lists, M))
