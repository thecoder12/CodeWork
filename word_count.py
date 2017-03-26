import sys
from collections import defaultdict

with open("big.txt") as f:
    data = f.read().lower().split(' ')
print(type(data))


from collections import Counter
counts = Counter(data)
search = 'Gutenberg'
search = search.lower()
print(counts[search])



#d = defaultdict(dict)
d = {}
d = defaultdict(lambda :0,d)

for word in data:
#    print(word)
    d[word] += 1
    #print('>>>' + word + '<<<')
    #sys.exit() 


print(data.count(search))



print(d[search])

for k,v in d.iteritems():
    if v == 1:
        print("key %s" %k)


