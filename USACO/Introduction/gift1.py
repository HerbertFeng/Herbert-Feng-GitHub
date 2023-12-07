'''
ID: herbert4
LANG: PYTHON2
TASK: gift1
'''


def main():
    with open('gift1.in', 'r') as fr, open('gift1.out', 'w') as fw:
        lines = [line.rstrip('\n') for line in fr]

        for line in lines:
            fw.write(line+ '\n' )
    '''
    for i in range(time):
        lines[i+1]=0
    '''
main()