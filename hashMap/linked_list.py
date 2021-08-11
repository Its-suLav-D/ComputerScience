class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def get_value(self):
        return self.data

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node


class LinkedList:
    def __init__(self):
        self.head_node = None

    def insert(self, value):
        new_node = Node(value)
        current_head = self.head_node

        if current_head is None:
            self.current_head = new_node

        while current_head != None:
            if current_head.next_node is None:
                current_head.set_next_node(new_node)

            current_head = current_head.get_next_node()

    def __iter__(self):
        current_node = self.head_node
        while(current_node):
            yield current_node.get_value()
            current_node = current_node.get_next_node()
