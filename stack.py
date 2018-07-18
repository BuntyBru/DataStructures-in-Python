# implementation of Stack
class Stack:
    def __init__(self):
         self.items = []

    def isEmpty(self):
         return self.items == []

    def push(self, item):
         self.items.append(item)

    def pop(self):
         return self.items.pop()

    def peek(self):
         return self.items[len(self.items)-1]

    def size(self):
         return len(self.items)

    def __str__(self):
        return str(self.items)


#the Calculating function
def tea(a,b):
    if a < b:
        m1 = a
        m2 = b
    if b < a:
        m1 = b
        m2 = a
    return  (((m1 & m2) ^ (m1 | m2)) & (m1 ^ m2))

Stack2 = Stack()
Stack1 = Stack()



#Stack2function where the stack2 is loaded everytime with indexes
def stack2Function(length):
    for i in range(length):
        Stack2.push(i)
    return Stack2
    

#n = 10
#l = [76969694 ,71698884,32888447,31877010 ,65564584 ,87864180 ,7850891,1505323,17879621,15722446]
#n=5
#l = [5, 2, 1, 4, 3]
n = 5
l = [9,8,3,5,7]

arr_rev =l[::-1]
ans = []
final = -1

while len(arr_rev) > 0:
    item = arr_rev.pop()
    print("The item which is popped from the arr_rev is below")
    print(item)
    Stack1.push(item)
    print("The stack1 is printed below")
    print(Stack1)
    #stack2Function(len(arr_rev))
    for i in range(len(arr_rev)):
        Stack2.push(i)

    print("Stack2 is printed below")
    print(Stack2)
    #print(Stack2.peek())
    print("----------------------------")
    while not Stack2.isEmpty():
        a = Stack1.peek()
        b = arr_rev[Stack2.peek()]
        ans.append(tea(a,b))
        print("The answer for")
        print(ans)
        Stack2.pop()


print(max(ans))
    