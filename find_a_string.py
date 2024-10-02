def count_substring(string, sub_string):
    t = 0
    for i in range(0, len(string)):
        if string[i:len(string)].startswith(sub_string):
            t += 1
    return t

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
