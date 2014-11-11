import linked_list

mylist = linked_list.LinkedList()
mylist.insert_head_element(2)
mylist.insert_head_element(1)
mylist.insert_tail_element(3)
mylist.insert_tail_element(5)
mylist.insert_tail_element(6)
mylist.insert_tail_element(7)

def my_own_print(element):
    print('element is: ' + str(element.data))

def my_list_processor(element,params):
    if element.data == params[0]:
        #add a new element
        el = linked_list.Element(params[1])
        element.add_successor(el)
    
    if element.data == params[2]:
        element.delete_successor()

mylist.process_list_elements(my_own_print)
mylist.process_list_elements(my_list_processor,[3,4,6])
mylist.print_list()
