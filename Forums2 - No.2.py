import os
os.chdir('/Users/avariqfrr30')

f=open('pg66691.txt', 'r')
n=open('new_text.txt', 'x')

sentences=f.read().split('\n')
counter=1
for sentence in sentences:
    n.write(str(counter) + '. ' + sentence + '\n')
    counter += 1