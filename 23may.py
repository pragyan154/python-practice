class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
#can also use while
# def add_end(self, val):
#         # creating a new node
#         new_node = Node(val)
#         # if the new_node is the first node, 
#         # in that case, both head and tail will point towards it
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         # if its not, then, iterate to the end of list and add
#         else:
#             curr = self.head
#             while curr.next:
#                 curr = curr.next
#             curr.next = new_node
    def insert_at_tail(self, data):
        new_node = Node(data)
 
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = None

    def add_begin(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def __str__(self):
        res = ""
        current = self.head

        while current is not None:
            res += str(current.data)+"->"
            # print(current.data, end=" -> ")
            current = current.next
        res += "nones"
        return res
        print("None")

    def remove_end(self):
        if self.head is None:
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            cur = self.head
            while cur.next.next :
                cur = cur.next
            cur.next = None

    def remove_begin(self):
        if self.head is None:
            return
        elif self.head ==  self.tail:
            self.head = None
            self.tail = None
        else:
            curr = self.head
            self.head = self.head.next
            curr.next = None


linked_list = LinkedList()

linked_list.insert_at_tail(10)
linked_list.insert_at_tail(20)
linked_list.insert_at_tail(30)
linked_list.add_begin(1)
# linked_list.remove_end()
linked_list.remove_begin()
print(linked_list)


#----------------------------------------------------------------------
# class array(object):
#     def __init__(self,sizeofarr, arraytype=int):
#         self.sizeofarr = len(list(map(arraytype,range(sizeofarr))))
#         self.arrayitems = [0,1,2,3,4,5,6,7,8,9]

#     def __str__(self):
#         return str(self.arrayitems)

#     def __len__(self):
#         return len(self.arrayitems)
    
#     def insert(self, keytoinsert, position):
#         if self.sizeofarr > position:
#             for i in range(self.sizeofarr-2 , position-1,-1):
#                 self.arrayitems[i+1] = self.arrayitems[i]
#             self.arrayitems[position] = keytoinsert

#         else:
#             print("size limit exceeded")

# # print(array(10,int))
# a = array(10,int)
# a.insert(1,1)
# print(a)






# class saaaman:
#     def __init__(self):
#         self.items = []

#     def insert_item(self, item):
#         self.items.append(item)

#     def delete_item(self, item):
#         if item in self.items:
#             self.items.remove(item)
#         else:
#             print(f"{item} is not found in the list.")

#     def display_items(self):
#         print("Current items in the list:")
#         for item in self.items:
#             print(item)

# m = saaaman()

# m.insert_item("Apple")
# m.insert_item("Banana")
# m.insert_item("Orange")

# m.display_items()

# m.delete_item("Banana")
# m.delete_item("Grape")

# m.display_items()





# num1 = 10
# num2 = 5

# # Addition
# print("Addition:", num1 + num2)

# # Subtraction
# print("Subtraction:", num1 - num2)

# # Multiplication
# print("Multiplication:", num1 - num2)

# # Division
# if num2 != 0:
#     print("Division:", num1 / num2)
# else:
#     print("Error: Division by zero is not allowed.")


# import numpy
# arr = numpy.array([1,2])
# print(arr)



# print(datetime.date.today())
# Function to take attendance and save in nested dictionary

# {'23': {'x': 'present', 'y'}}








