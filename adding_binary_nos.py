print('Adding binary numbers from right to left')
a = '1001'
b = '1010'
aa = list(a)
carry = 0
b = ((b[::-1]))

r = list()

for count,i in enumerate(a[::-1]):
    res = 0
    # print(type(i),count)
    c = int(a[count]) + int(b[count])
    # print(repr(c))
    if c == 2 and carry == 0:
        carry = 1
        c = 0
    if c == 2 and carry == 1:
        carry = 1 
        c = 1
    r.append(c) 
    print('a=> %s b=> %s , c=> %s' %(int(a[count]), int(b[count]), c) )
    print(r)
if carry == 1:
    r.append(carry)
# print(''. join(r[::-1]))        
    
final = ''    
for i in r[::-1]:
    final += str(i)
    
print(final)    
    
fina = ''. join((str(i)) for i in r[::-1])
print(fina)
    
    
aaaa = (''.join(map(str, r[::-1])))
print(aaaa)
    
