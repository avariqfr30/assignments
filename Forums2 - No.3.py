## No. 3 ##
f = open('/Users/avariqfrr30/pg66691.txt', 'r')

w = [len(word) for line in f for word in line.rstrip().split(" ")]
w_avg = float(sum(w))/float(len(w))

print ('Average word length: ', w_avg)
f.close()

