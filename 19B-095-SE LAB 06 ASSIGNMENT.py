#!/usr/bin/env python
# coding: utf-8

# In[17]:


class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.previous=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def InsertatFirst(self,value):
        newnode = Node(value)
        x=self.head
        if x is None:
            self.head = newnode
            self.tail = newnode
        else:
            self.head.previous = newnode
            newnode.next=self.head
            self.head = newnode
    def InsertatEnd(self,value):
        newnode= Node(value)
        x=self.tail
        if x==None:
            self.head= newnode
            self.tail= newnode
        else:
            self.tail.next= newnode
            newnode.previous= self.tail
            self.tail= newnode
            newnode.next= None
    def DeleteatFirst(self):
        x= self.head
        if x is None:
            raise("There is No item in the list")
        self.head= self.head.next
        y=None

    def DeleteatEnd(self):
        y= self.head
        x= self.tail
        if y is None:
            raise("There is No Item in the list")
        while y.next.next is not None:
            y= y.next
        y.next= None
    def InsertAfter(self,item,value):
        x = self.head
        while x.next !=None:
            if x.value == item:
                newnode= Node(value)
                newnode.next = x.next
                newnode.previous=x.previous
                x.next = newnode
                break
            else:
                x = x.next
    def DeleteByValue(self,value):
        x=self.head
        while x.next != None:
                if x.value == value:
                    x.previous.next = x.next
                    x.next.previous = x.previous 
                    x.next = None
                    x.previous = None
                    break
                x = x.next
                
    def Print(self):
        x= self.head
        while x!=None:
            print(x.value)
            x=x.next
            
            
obj=DoublyLinkedList()
obj.InsertatFirst(1)
obj.InsertatFirst(10)
obj.InsertatFirst(3)
obj.InsertatFirst(4)
obj.InsertatEnd(2)
obj.InsertatEnd(7)
obj.InsertAfter(7,8)
obj.DeleteatFirst()
obj.DeleteByValue(10)
obj.DeleteatEnd()
obj.Print()


# In[ ]:




