class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    def increment_login_attempts(self):
        self.login_attempts +=1
    def reset_login_attempts(self):
        self.login_attempts = 0
user1 = User('shadow', 'lawler')
print(user1.first_name + ' ' + user1.last_name)
for i in range(1,10):
    user1.increment_login_attempts()
    print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)
