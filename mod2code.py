class Person:
    def __init__(self, first_name, last_name, age):
        self.fname = first_name
        self.lname = last_name
        self.age = age
        self.phone_number = []
    
    def add_phone(self, pnumber):
        self.phone_number.append(pnumber)
    
    def get_name(self):
        return f"{self.fname}, {self.lname}"

    def __lt__(self, other):
        if not isinstance(self.age, int) and isinstance(other.age, int):
            raise TypeError("One of the ages is not int")
        
    if __name__ == "__main__":
        p1 = Person('h','r', 12)
        p2 = Person('e', 't', '44')
        p1 < p2



