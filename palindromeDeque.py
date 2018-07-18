class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

n = "abbsabasabba"
p = Deque()
k=0
for i in range(len(n)):
    p.addFront(n[i])
while p.size() > 1:
    if p.removeRear() == p.removeFront():
        k=1
    else:
        k=0
        break;
if k == 1:
    print("Yes it is palindrome")
else:
    print("No it is not palindrome")
