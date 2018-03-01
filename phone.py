class Phone:
    count = 1
    def __init__(self):
        self.contacts= []
        self.id =Phone.count 
        Phone.count +=1

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    #test add new number
    def add_new(self,name,number):
        add =dict(number=number,name=name)
        self.contacts.append(add)
        return {"message":"Business added succesfully"}

    #delete contact
    def delete(self,name):
        found=[name for name in  self.contacts if name==name][0]
        self.contacts.remove(found)
        return {"message":"Contact deleted succesfully"}

    #view contacts
    def view_contacts(self):
        for numbers in self.contacts:
            return numbers

    #update contacts
    def update_contacts(self,name,number):
        found=[name for name in  self.contacts if name==name][0]
        self.contacts[name] = name 
        self.contacts[number] = number
        return {"message":"Contact updated succesfully"}


        

    


x=Phone()
x.add_new('james',444)
#print(x)
#x.delete('james')
#x.view_contacts()
#x.update_contacts('james',888)
#p.delete_no('linda',555)
#x.delete_no('james',555)

#x.view_numbers()

print (x)