class Element(object):
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
        
    def add_successor(self,element):
        element.next = self.next
        self.next = element
        
    def delete_successor(self):
        element = self.next
        if element != None:
            self.next = element.next
            element.next = None
        return element.data
    
class LinkedList(object):
    def __init__(self,element=None):
        self.head = element
        self.tail = element
        
    def insert_tail_element(self,data):
        current = self.tail
        if current == None:
            self.head = Element(data)
            self.tail = self.head
            return
        current.next = Element(data)
        self.tail = current.next
        
    def insert_head_element(self,data):
        el = Element(data)
        el.next = self.head
        self.head = el
        
    def delete_head_element(self):
        current = self.head
        self.head = current.next
        if self.head == None:
            self.tail = None
        return current.data
    
    def delete_tail_element(self):
        current = self.head
        if current == None:
            return None
        prev = None
        while current.next != None:
            prev = current
            current = current.next
        if prev != None:
            prev.next = None
            self.tail = prev
        return current.data
            
    def print_list(self):
        current = self.head
        while current != None:
            print('element: ' + str(current.data))
            current = current.next
            
    def process_list_elements(self,
                              process_function,
                              other_process_params=None):
        current = self.head
        while current != None:
            if other_process_params == None:
                process_function(current)
            else:
                process_function(current,other_process_params)
            current = current.next
	
