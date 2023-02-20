class User:

    def __init__(self, first_name, last_name):

        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0


    def greeting(self):
        print(f'Hello {self.first_name} {self.last_name}!')


    def increment_login_attempts(self, attempts):
        self.login_attempts += attempts
        print(f'Number of log in attempts increased to {self.login_attempts}')

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f'Log in attempts reset to {self.login_attempts}')


class Privledges:
    def __init__(self,privledges):
        self.privledges = privledges

    def show_privledges(self):
        print(f'Privledges are: {self.privledges}')

class Admin(User):

    def __init__(self, first_name, last_name, privledges):
        super().__init__(first_name, last_name)
        self.privledges = Privledges(privledges)

jonny = Admin("Jonny", "Jamison", ["can delete post", "can ban user"]) #List of strings as input

jonny.privledges.show_privledges()

