a  
#!/usr/bin/python

"""
Linked Lists, Stacks and Queues
"""

"""
QUESTION 1: 
========================================================================================================
Write a Python function to implement a recursive algorithm which counts the number of nodes in a 
singly linked list. The input of the function should be a reference pointing to the first node of the
linked list. The output of the function should be the number of nodes in that linked list. 
Your function should be robust enough to handle possible inappropriate inputs.
linkedList.add(1)
linkedList.add(2)
linkedList.add(3)
linkedList.add(4)
linkedList.add(5)
Outpot :  5
"""
class Node (object): 
    def __init__(self, data=None, next_node=None): 
        self.data = data 
        self.next = None
class LinkedList:
  
    def __init__(self):
        self.head = None
  
    def add(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
  
    def getCount(self):
        temp=self.head
        count=0
        while (temp):
            count +=1
            temp=temp.next
        return count
  
if __name__=='__main__':
    llist = LinkedList()
    llist.add(1)
    llist.add(2)
    llist.add(3)
    llist.add(4)
    llist.add(5)
    print ("number of nodes in linked list is:",llist.getCount())


    
"""
QUESTION 2: 
========================================================================================================
Write a function evalPostfix that takes a string with space as delimiter and evaluates the value of postfix. Assume we have only two operators: * and +.
	
Evaluate the value for "55 44 + 3 *"
Outpot : 297 


===========================
"""
class  Evalpostfix:
   def evalRPN(self, tokens):
        givenOp = {"+": lambda a, b: a + b, "*": lambda a, b: a *b}
       
        stack = []
       
        for token in tokens:
            if token in givenOp:
                num2 = stack.pop()
                num1 = stack.pop()
               
                op = givenOp[token]
                stack.append(op(num1, num2))
            else:
                stack.append(int(token))
       
        return stack.pop()

eval = Evalpostfix()
inp = input("Enter Expression: ")
inp = inp.strip().split()
print(eval.evalRPN(inp))



