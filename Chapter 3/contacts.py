class Contacts(object):

    def __init__(self):
        self.data = dict()
        
    def add_contact(self,first,last,phone,email):
        self.data[first + ' ' + last] = (first,last,
                                         phone,email)

    def delete_contact(self,first,last):
        del self.data[first + ' ' + last]

    def print_names(self):
        for key, (first,last,phone,email) in \
            self.data.items():
            
            self.print_contact(first,last,
                               phone,email)
            print('--')

    def search_by_name(self,name):
        count = 0
        for key, (first,last,phone,email) in \
            self.data.items():
            
            if (first.find(name) != -1 or
                last.find(name) != -1):
                
                self.print_contact(first,last,
                                   phone,email)
                print('--')
                count = count+1

        if count == 0:
            print("No results found")
        else:
            print("Found " + str(count) + " result(s)")

    def get_contact_by_full_name(self,name):
        key = name
        if key in self.data:
            (first, last, phone, email) = self.data[key]
            self.print_contact(first,last,phone,email)
        else:
            print("Contact does not exist")

    def print_contact(self,first,last,phone,email):
            print('Name:   ' + first + ' ' + last)
            print('Phone:  ' + phone)
            print('E-mail: ' + email)
 

 


                  
        
