class StartCookie:
    #Global variable that will be applied for all objects
    milk = 0.1
    #__init__ is the initializer method — it runs automatically when you create an object and is used to set up attributes.
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight
        
    
    
    
my_cookie = StartCookie('Red', 16)
print(my_cookie.color)
print(my_cookie.weight)
print(my_cookie.milk)
#all the information about the object
print(my_cookie.__dict__)


my_cookie2 = StartCookie('Blue', 16)
print(my_cookie2.color)
print(my_cookie2.weight)
print(my_cookie2.milk)
#all the information about the object
print(my_cookie2.__dict__)
print(StartCookie.__dict__)

# #Variables can be already innitialized with a default value
# class Youtube:
#     def __init__(self,username, subscribers=0):
#         self.username = username
#         self.subscribers = subscribers
        
        
# user = Youtube('Vitor')        
# print(user.username)
# print(user.subscribers)