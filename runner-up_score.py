if __name__ == '__main__':
    n = int(input())
    l = map(int, input().split())
    l1 = set(l)
    l2 = sorted(l1)
    print(l2[-2])
