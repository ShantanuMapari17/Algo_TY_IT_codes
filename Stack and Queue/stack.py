#Program to implement Stack
class Stack(object):
    def __init__(self,limit=10):
        self.stk=[]
        self.limit=limit
    
    def isEmpty(self):
        return len(self.stk)<=0
    
    def push(self,item):
        if len(self.stk)>=self.limit:
            print("Stack Overflow!!")
        else:
            self.stk.append(item)
            print(f"{item} pushed successfully")
    
    def pop(self):
        if len(self.stk)<=0:
            print("Stack Underflow!!")
            return 0
        else:
            return self.stk.pop()
    
    def peek(self):
        if len(self.stk)<=0:
            print("stack UNderflow")
            return 0
        else:
            return self.stk[-1]
        
    def size(self):
        return len(self.stk)
    

    #----------Dry Run of Stack----------

St = Stack(5)
St.push("1")
St.push("21")
St.push("14")
St.push("31")
St.push("19")
St.push("3")
St.push("99")
St.push("9")
print(f"Size of the Stack is: {St.size()}")
print("Elements in the Stack: ",end=" ")
print(St.stk)
print(f"ELemet at the top is: {St.peek()}")
print(f"{St.pop()} #poped element from the stack ")
print(f"{St.pop()} #poped element from the stack ")
print(f"Stack is: {St.stk}")
print(f"{St.pop()} #poped element from the stack ")
print(f"{St.pop()} #poped element from the stack ")
print(f"{St.pop()} #poped element from the stack ")
print(f"{St.pop()} #poped element from the stack ")


