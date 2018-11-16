class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
class Adimin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = privileges()
class privileges():
    def __init__(self):
        self.privileges=['can add post', 'can delete post', 'can ban user']
    def show_privileges(self):
        for item in self.privileges:
            print(item)
    
adimin1 = Adimin('shadow', 'lawler')
adimin1.privileges.show_privileges()
