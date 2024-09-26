def swap_case(s):
    s2 = ""
    for l in s:
        if l.isupper() == True:
            s2+=l.lower()
        else:
            s2+=l.upper()
    return s2

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
