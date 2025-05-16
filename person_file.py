class Person:
    def __init__(self, first_name, last_name, age):
        self.fname = first_name
        self.lname = last_name
        self.age = age
        self.phone_number = [] 
    
    def add_phone(self, pnumber):
        """Add phone number"""
        self.phone_number.append(pnumber)
    
    def get_name(self):
        """Return the first and the last name"""
        return f"{self.fname} {self.lname}"
    
    def __lt__(self,other):
        """Compare the age of two objects"""
        if not (isinstance(self.age, int) and isinstance(other.age, int)):
            raise TypeError("One of the ages is not int")
        return self.age < other.age

class Student(Person):
    def __init__(self, first_name, last_name, age, student_id):
        super().__init__(first_name, last_name, age)
        self.student_id = student_id

    def get_id(self):
        """Return student id"""
        return self.student_id
            
if __name__ == "__main__":
    p1 = Person('h', 'r', 1)
    p2= Person('e', 't', 33)
    assert (p1 < p2) == True # <-- print(p1 < p2)