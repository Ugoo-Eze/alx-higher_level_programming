#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    i = 0
    for num in range(1, len(argv)):
        i = i + int(argv[num])
    print('{}'.format(i))
