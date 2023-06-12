class stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop an item.")
        else:
            return self.stack.pop()
        
    def peek(self):
        if self.is_empty():
            print("Stack is empty. Cannot peek.")
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)

    def clear(self):
        self.stack = []
        
    def __str__(self) :
        res = ""
        for s in self.stack:
            res += str(s) + " "

        return res
    
# stack = stack()

# stack.push(10)
# stack.push(20)
# stack.push(30)
# stack.pop()
# print(stack)


bracs = input("enter bracs to check : ")

# def check(s):
#     for i in s:
#         if i == "(":
#             stack.push(i)
#         else:
#             if stack.is_empty():
#                 return False
#             else:s
#                 stack.pop()
#     return stack.is_empty()

# print(check(bracs))

multistack = stack()

def check_multi(s):
    for i in s :
        if i in "({[":
            multistack.push(i)
        else:
            if multistack.is_empty():
                return False
            elif i=="]" and multistack.peek =="[":
                multistack.pop()
            elif i==")" and multistack.peek =="(":
                multistack.pop()
            elif i=="}" and multistack.peek =="{":
                multistack.pop()
            
    return multistack.is_empty()

print(check_multi(bracs))