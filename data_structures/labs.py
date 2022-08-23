# implementing a Single Linked List 
  
class NodeSL:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next


class SingleLinkedList:


    def __init__(self):
        self.head = None


    def get_length(self):
        count=0
        node = self.head
        while node:
            node = node.next
            count+=1
        return count


    def insert_at_beginning(self,data):
        self.head = NodeSL(data,self.head)


    def insert_at_end(self,data):
        if not self.head:
            self.head=NodeSL(data,None)
        else:
            next_node = self.head
            while next_node.next:
                next_node=next_node.next
            next_node.next = NodeSL(data,None)


    def insert_at(self,idx,data):
        if idx < 0 or idx > self.get_length():
            raise Exception("Invalid index")
        elif idx==0:
            self.insert_at_beginning(data)
        else:
            count=0
            itr = self.head
            while itr:
                if count == idx - 1:
                    node = NodeSL(data, itr.next)
                    itr.next = node
                    break
                itr = itr.next
                count += 1


    def remove_at(self,idx):
        if idx < 0 or idx > self.get_length():
            raise Exception("Invalid index")
        elif idx==0:
            self.head=self.head.next
        else:
            count=0
            node = self.head
            while node:
                if count==idx-1:
                    node.next = node.next.next
                    break
                node = node.next
                count+=1


    def print(self):
        if not self.head:
            print('Linked List is empty')
        else:
            listr=''
            head = self.head
            while head:
                listr+=str(head.data)+'-->'
                head = head.next
            print(listr)


    def insert_values(self,values):
        for data in values:
            self.insert_at_end(data)


    def get_index_by_value(self,data):
        count=0
        node = self.head
        while node:
            if node.data == data:
                return count
            node = node.next
            count+=1        
        return -1

    def insert_after_value(self, data_after, data_to_insert):
        idx = self.get_index_by_value(data_after)
        if idx<0:
            print('data doesnt exist')
        else:
            self.insert_at(idx+1,data_to_insert)


    def remove_by_value(self, data):
        idx = self.get_index_by_value(data)
        if idx<0:
            print('data doesnt exist')
        else:
            self.remove_at(idx)        


if __name__ == '__main__':
    ll = SingleLinkedList()
    ll.insert_at_end(12)
    ll.insert_at_end(34)
    ll.insert_at_end(90)
    ll.insert_at_end(19)
    # ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_at(1,"blueberry")
    ll.remove_at(2)
    print('length 3',ll.get_length())
    
    ll.insert_values([45,7,12,567,99])
    ll.insert_at_end(67)
    print('index',ll.get_index_by_value(671))
    ll.insert_after_value(67,1111)
    ll.remove_by_value(67)
    ll.print() 
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()               