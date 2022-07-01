class Employee:
    
    def __init__(self,name,age,salary,phone_number,bonus):
        self.name = name
        self.age = age
        self.salary = salary
        self.phone_number = phone_number
        self.bonus = bonus
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_salary(self):
        return self.salary
    
    def get_phone_number(self):
        return self.phone_number
    
    def update_salary(self):
        updated_salary = self.get_salary() + self.bonus
        return updated_salary
    
    def get_bonus(self):
        return self.bonus
    
    

            
    