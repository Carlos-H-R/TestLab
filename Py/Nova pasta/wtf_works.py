file = open('base.txt','r+')
text = file.readlines()
for i in text:
    print(str(i))
line = str(input('escreva: ')) + "\n"
file.write(line)
file.close()
