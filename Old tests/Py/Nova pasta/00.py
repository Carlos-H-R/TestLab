import string

def print_rangoli(size):
    base = list(str(string.ascii_lowercase))
    width = (size*4)-3
    tr = '-'
    rangoli = ''
    for i in range(1,size+1):
        letras = size - i + 1
        sample = list(base[(size-i):size])
        sample.reverse()
        sample += base[(size-i+1):size]
        st = tr.join(sample)
        rangoli += (tr*((width - len(st))//2)) + st + (tr*((width - len(st))//2)) + '\n'
    for i in range(size-1,0,-1):
        letras = size - i + 1
        sample = list(base[(size-i):size])
        sample.reverse()
        sample += base[(size-i+1):size]
        st = tr.join(sample)
        rangoli += (tr*((width - len(st))//2)) + st + (tr*((width - len(st))//2)) + '\n'
    return(rangoli)
        
file = open('D:/Code Test/Nova pasta/memo.txt','a')
n = int(input())
r = print_rangoli(n)
file.write(r)
file.close()
