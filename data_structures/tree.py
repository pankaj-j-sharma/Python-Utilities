from memory_profiler import profile

class TreeNode:
    def __init__(self,data):
        self.data=data
        self.chilren=[]
        self.parent=None

    def add_child(self,child):
        child.parent=self
        self.chilren.append(child)

    def get_level(self):
        level=0
        parent = self.parent
        while parent:
            level+=1
            parent = parent.parent
        return level


    def display_tree(self):
        prefix = ' '*self.get_level()*2+'|__ ' if self.parent else '' 
        print(prefix+self.data)
        for child in self.chilren:
            child.display_tree()

@profile
def build_product_tree():
    root = TreeNode("electronics")

    laptop = TreeNode("Laptop")
    cellphone = TreeNode("Cell Phone")
    tv = TreeNode("TV")

    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("thinkpad"))

    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("One Plus"))
    cellphone.add_child(TreeNode("Vivo"))

    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root

if __name__=='__main__':
    root = build_product_tree()
    root.display_tree()
