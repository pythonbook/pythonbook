import linked_list_tail

class Queue:
    def __init__(self,data=None):
        self.elements = linked_list_tail.LinkedList()
        if data != None:
            self.elements.insert_tail_element(data)

    def enqueue(self,data):
        self.elements.insert_tail_element(data)
    
    def dequeue(self):
        return self.elements.delete_head_element()
    
    def is_empty(self):
        return self.elements.head == None
