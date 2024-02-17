'''
ID: herbert4
LANG: PYTHON2
TASK: gift1
'''


def main():
    with open('gift1.in', 'r') as fr, open('gift1.out', 'w') as fw:
        lines = [line.rstrip('\n') for line in fr]
        times = lines[0]
        for name in range(1,times+1):
            name = 0


main()