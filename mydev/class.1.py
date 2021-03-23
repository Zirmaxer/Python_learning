class Name():
    def __init__ (self, f_name, l_name):
        self.f_name = f_name.capitalize()
        self.l_name = l_name.capitalize()
    
    def first_name (self):
        return f'{self.f_name}'
    
    def last_name (self):
        return f'{self.l_name}'

    def full_name (self):
        return f'{self.f_name} {self.l_name}'
    
    def initials (self):
        return  f'{self.f_name[0]}.{self.l_name[0]}'