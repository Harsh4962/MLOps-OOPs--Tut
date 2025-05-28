from oops_proj import chatbook

user1 = chatbook()
print(user1.__name) #-> error
print(user1._chatbook__name) #-> use class name to access hidden atri

user1.set_name("harsh")
print(user1.get_name)

chatbook.set_id(10) #--> setter of static var