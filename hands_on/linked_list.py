class Node:
    def __init__(self, name):
        self.name = name
        self.next = None
        self.last = None
        # print(f'({name}) node created')


class SingleLinkedList:
    def __init__(self):
        self.nodes = None

    def add_node(self, node):
        if not self.nodes:
            self.nodes = node
        else:
            last_node = self.nodes

            #---------------*******************----------#
            # traverse until the last node
            while last_node.next:
                last_node = last_node.next
            last_node.next = node

    def print_linked_list(self):
        nodes = self.nodes
        while nodes:
            print(nodes.name, '->', end=' ')
            nodes = nodes.next
        print('\n', '-'*100, '\n', end='\n')


class DoubleLinkedList:
    def __init__(self):
        self.nodes = None

    def add_node_at_end(self, node):
        if not self.nodes:
            self.nodes = node
        else:
            last_node = self.nodes
            #---------------*******************----------#
            # traverse until the last node
            while last_node.next:
                last_node = last_node.next
            last_node.next = node

    def add_node_at_start(self, node):
        if not self.nodes:
            self.nodes = node
        else:
            first_node = self.nodes
            #---------------*******************----------#
            # traverse until the first node
            while first_node.last:
                first_node = first_node.last
            first_node.last = node

    def print_linked_list(self):

        backward_nodes = self.nodes
        while backward_nodes:
            print(backward_nodes.name, '<-', end=' ')
            backward_nodes = backward_nodes.last

        forward_nodes = self.nodes
        while forward_nodes:
            print(forward_nodes.name, '->', end=' ')
            forward_nodes = forward_nodes.next

        print('\n', '-'*100, '\n')


if __name__ == '__main__':

    linkedList = SingleLinkedList()
    linkedList.add_node(Node(1))
    linkedList.add_node(Node(9))
    linkedList.add_node(Node(5))
    linkedList.add_node(Node(3))
    linkedList.add_node(Node(6))
    linkedList.print_linked_list()

    dblLinkedList = DoubleLinkedList()
    dblLinkedList.add_node_at_end(Node(4))
    dblLinkedList.add_node_at_end(Node(3))
    dblLinkedList.add_node_at_end(Node(1))
    dblLinkedList.add_node_at_end(Node(6))

    dblLinkedList.add_node_at_start(Node(5))
    dblLinkedList.add_node_at_start(Node(2))
    dblLinkedList.add_node_at_start(Node(7))
    dblLinkedList.add_node_at_start(Node(8))

    dblLinkedList.print_linked_list()
