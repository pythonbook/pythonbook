class Element:
    def __init__(self,data,prev=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next
        
    def add_successor(self,element):
        element.next = self.next
        if self.next != None:
            self.next.prev = element
        self.next = element
        element.prev = self
        
    def add_predecessor(self,element):
        element.next = self
        if self.prev != None:
            self.prev.next = element
        element.prev = self.prev
        self.prev = element
        
    def delete_element(self):
        if self.prev != None:
            self.prev.next = self.next
        if self.next != None:
            self.next.prev = self.prev
        self.next = None
        self.prev = None
        return self.data
    
    
class DoublyLinkedList:
    def __init__(self,element=None):
        self.head = element
        self.tail = element
        
    def insert_tail_element(self,data):
        if self.tail != None:
            self.tail.next = Element(data,self.tail)
            self.tail = self.tail.next
        else:
            self.head = Element(data)
            self.tail = self.head
        
    def insert_head_element(self, data):
        if self.head != None:
            self.head.prev = Element(data,None,self.head)
            self.head = self.head.prev
        else:
            self.head = Element(data)
            self.tail = self.head
        
    def delete_head_element(self):
        current = self.head
        if self.head != None:
            self.head = current.next
            if self.head != None:
                self.head.prev = None
            else:
                self.tail = None
        if current != None:
            current.next = None
            current.prev = None
            return current.data
        else:
            return None
    
    def delete_tail_element(self):
        current = self.tail
        if self.tail != None:
            self.tail = self.tail.prev
            if self.tail != None:
                self.tail.next = None
            else:
                self.head = None
        if current != None:
            current.next = None
            current.prev = None
            return current.data
        else:
            return None
            
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
	
