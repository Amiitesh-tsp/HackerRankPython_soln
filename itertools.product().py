from itertools import product
l1 = map(int, input().split())
l2 = map(int, input().split())
l3 = [l1, l2]
l4 = (list(product(*l3)))
for i in l4:
    print(i, end = " ")
