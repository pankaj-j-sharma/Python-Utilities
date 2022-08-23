from abc import ABC, abstractmethod

class ISingleLinkedList(ABC):

    @abstractmethod
    def insert_values(self,lst):
        pass 

    @abstractmethod
    def insert_at(self,idx,data):
        pass 

    @abstractmethod
    def insert_at_beginning(self,data):
        pass 

    @abstractmethod
    def insert_at_end(self,data):
        pass 

    @abstractmethod
    def remove_at(self,idx):
        pass 

    @abstractmethod
    def get_index_by_value(self,value):
        pass 

    @abstractmethod
    def remove_by_value(self,value):
        pass 

    @abstractmethod
    def insert_after_value(self,value,data):
        pass 

    @abstractmethod
    def get_length(self):
        pass 

    @abstractmethod
    def display_linked_list(self):
        pass 

class Node:
    
    def __init__(self,data,next=None,last=None):
        self.data = data
        self.next = next
        self.last = last

# 12 -> 21 -> 29 -> 

class SingleLinkedList(ISingleLinkedList):

    def __init__(self):
        self.head=None

    def get_length(self):
        count=0
        node = self.head
        while node:
            node = node.next
            count+=1
        return count


    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node 


    def insert_at_end(self,data):
        if not self.head:
            self.head = Node(data,next=None)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data,next=None)
    

    def insert_at(self,idx,data):
        if idx<0 or idx>self.get_length():
            print('Invalid index')
        elif idx==0:
            self.insert_at_beginning(data)
        else:
            count=0
            node = self.head
            while node:
                if count==idx-1:
                    node1 = Node(data,node.next)
                    node.next = node1
                    break
                node = node.next
                count+=1
    

    def remove_at(self,idx):
        if idx<0 or idx>self.get_length():
            print('Invalid index')
        elif idx==0:
            self.head=self.head.next
        else:
            count=0
            node = self.head
            while node:
                if count==idx-1:
                    node.next = node.next.next
                    break
                node=node.next
                count+=1

    def get_index_by_value(self, value):
        count=0
        node=self.head
        while node:
            if node.data == value:
                return count
            node = node.next
            count+=1
        return -1


    def insert_after_value(self, value, data):
        idx = self.get_index_by_value(value)
        self.insert_at(idx,data)


    def remove_by_value(self, value):
        idx = self.get_index_by_value(value)
        self.remove_at(idx)                


    def insert_values(self, lst):
        for data in lst:
            self.insert_at_beginning(data)
                

    def display_linked_list(self):
        node = self.head
        lstr=''
        while node:
            lstr+=str(node.data)+' -> '
            node = node.next
        print(lstr)


if __name__ == '__main__':
    ll = SingleLinkedList()
    ll.insert_at_end(12)
    ll.insert_at_end(34)
    ll.insert_at_end(90)
    ll.insert_at_end(19)
    # ll.insert_values(["banana","mango","grapes","orange"])
    ll.display_linked_list()
    ll.insert_at(1,"blueberry")
    ll.remove_at(2)
    print('length 3',ll.get_length())
    
    ll.insert_values([45,7,12,567,99])
    ll.insert_at_end(67)
    print('index',ll.get_index_by_value(671))
    ll.insert_after_value(67,1111)
    ll.remove_by_value(67)
    ll.display_linked_list() 
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.display_linked_list()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.display_linked_list()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.display_linked_list()
    ll.remove_by_value("figs")
    ll.display_linked_list()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.display_linked_list()                       