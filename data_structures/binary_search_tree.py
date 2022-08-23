from dataclasses import dataclass
from logging import root


class BinarySearchTreeNode:
    
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


    def add_child(self,data):
        # node already exists
        if data==self.data:
            return
            
        # node in left subtree 
        if data < self.data:
            if self.left:
                return self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        # node in right subtree
        if data > self.data:
            if self.right:
                return self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def search(self,value):
        
        # value matched
        if self.data==value:
            return True

        # value in left subtree 
        if value < self.data :
            if self.left:
                return self.left.search(value)
            else:
                return False

        # value in right subtree         
        if value > self.data :
            if self.right:
                return self.right.search(value)
            else:
                return False


    def in_order_traversal(self):
        # visit all the left nodes first then root and then right node
        elements=[]

        # visting all left nodes
        if self.left:
            elements+=self.left.in_order_traversal()

        # visintg root node 
        elements.append(self.data)

        # vising right nodes
        if self.right:
            elements+=self.right.in_order_traversal()

        return elements



    def pre_order_traversal(self):
        # visit all the root nodes first then left and then right node
        elements=[]

        # visintg root node 
        elements.append(self.data)

        # visting all left nodes
        if self.left:
            elements+=self.left.in_order_traversal()

        # vising right nodes
        if self.right:
            elements+=self.right.in_order_traversal()

        return elements


    def post_order_traversal(self):
        # visit all the left nodes first then right and then root node
        elements=[]

        # visting all left nodes
        if self.left:
            elements+=self.left.in_order_traversal()

        # vising right nodes
        if self.right:
            elements+=self.right.in_order_traversal()

        # visintg root node 
        elements.append(self.data)

        return elements


    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data 

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data 

    def delete(self,value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            # case when this is the only node and no children
            if not self.right and not self.left:
                return None
            # case when right subtree present
            if not self.left :
                return self.right

            if not self.right:
                return None

            # min_val = self.right.find_min()
            # self.data = min_val
            # self.right=self.right.delete(min_val)            

            max_val = self.left.find_max()
            self.data = max_val
            self.right=self.left.delete(max_val)            

        return self


    def display_binary_search_tree(self,level=0,dir=None):
        # to be implemented
        pass 


def build_binary_search_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for ele in elements[1:]:
        root.add_child(ele)
    return root
    

if __name__=='__main__':
    countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    country_tree = build_binary_search_tree(countries)

    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))

    numbers_tree = build_binary_search_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())    
    # print("Pre order traversal gives this sorted list:",numbers_tree.pre_order_traversal())  
    # print("Post order traversal gives this sorted list:",numbers_tree.post_order_traversal())  
    # print("minimum of this sorted list:",numbers_tree.find_min()) 
    # print("maximum of this sorted list:",numbers_tree.find_max()) 
    print("delete node 18",numbers_tree.delete(18))
    print("In order traversal after delete :",numbers_tree.in_order_traversal())   
