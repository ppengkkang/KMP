class Stack():
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

# s=Stack()
# print(s.isEmpty())
# s.push(4)
# s.push('dog')
# print(s.peek())
# s.push(True)
# print(s.isEmpty())
# s.push(8.4)
# print(s.pop())
# print(s.pop())
# print(s.size())
def reverstring(mystr):
    s=Stack()
    outputstr=''
    for c in mystr:
        s.push(c)
    while not s.isEmpty():
        outputstr+=s.pop()
    return outputstr
# print(reverstring('apple'))
def Dec2Bin(decNumber):
    s=Stack()
    while decNumber>0:
        temp=decNumber%2
        s.push(temp)
        decNumber=decNumber//2
    binString=''
    while not s.isEmpty():
        binString+=str(s.pop())
    return binString
# print(Dec2Bin(42))
def baseConverter(decNumber,base):
    digits='0123456789ABCDEF'
    s=Stack()
    while decNumber>0:
        temp=decNumber%base
        s.push(temp)
        decNumber=decNumber//base

    newString=''
    while not s.isEmpty():
        newString=newString+digits[s.pop()]
    return newString
print(baseConverter(59,16))