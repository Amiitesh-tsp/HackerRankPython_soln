def split_and_join(line):
    l = line.split(" ")
    line2 = "-".join(l)
    return line2

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
