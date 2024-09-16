import pytest

if __name__ == '__main__':
    pytest.main()


#a = [21,21,67,90,56,90]
#n = len(a)
## i in range(n) :
#    print(i,a[i])
#    a[i]+=5
#print(a)

#s = 'heLLo'
#for i in s:
#    if i> 'a' and i<'z':
# ##elif "A" <=i<="Z":
# #       print(i,"big")
#    else:
#        print(i)

vowejs ='aeiou'
s = 'eadfiuqey'
n =len(s)
for i in range(n-1):
    if s[i] in vowejs and s[i+1] in vowejs:
        print(s[i] , s[i+1])


text = input()
a = set()
while text != '':
    slova = text.split()
    a.update(slova)
    print(a)
    text = input()
    print(len(a))