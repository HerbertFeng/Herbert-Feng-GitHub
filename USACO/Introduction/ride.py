'''
ID: herbert4
LANG: PYTHON2
TASK: ride
'''
def helper(name):
    res = 1
    for letter in name:
        res*= (ord(letter)-ord('A')+1)
    return res%47

def main():
    with open('ride.in','r') as fr, open('ride.out','w') as fw:
        lines = [line.rstrip('\n') for line in fr]
        for i in range(0,len(lines),2):
            w1 = lines[i]
            w2 = lines[i+1]

            if helper(w2)==helper(w1):
                fw.write('GO' + '\n')
            else:
                fw.write('STAY' + '\n')
main()

