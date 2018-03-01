class Phone:
    def __init__(self):
        self.contacts= []

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    #test add new number
    def add_new(self,name,number):
        add =dict(number=number,name=name)
        self.contacts.append(add)
        return {"message":"Business added succesfully"}
    #delete contact
    def delete(self,name):
        if name in self.contacts:
            self.contacts.remove(name)
            return {"message":"Contact deleted succesfully"}
    #view contacts
    def view_contacts(self):
        for numbers in self.contacts:
            return numbers

    def update_contacts(self,name,number):
        for number in self.contacts:
            if name == self.name and number == self.number:
                self.name['']

        

    


x=Phone()
x.add_new('james',444)
print(x)

#p.delete_no('linda',555)
#x.delete_no('james',555)

#x.view_numbers()

print 