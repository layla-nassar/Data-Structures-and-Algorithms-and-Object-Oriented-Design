"""Design for the Person Class:
- Required instance variables: first_name, last_name, age
- Additional variable: phone_number (a list to store phone numbers)

Person Class Methods:
1. `add_phone(phone_number)`: Adds a phone number to the list.
2. `get_name()`: Returns the full name of the person.
3. `__lt__`: Compares the age of two objects; raises a TypeError if any age is not an integer.

Design for the Student Class (inherits from Person):
- Required instance variables: student_id

Student Class Methods:
1. `get_id()`: Returns the student ID."""

import unittest
from mod2code import Person

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person1 = Person('John', 'Smith', 18)
        self.person2 = Person('Amy', 'Rogers', '22')

    def test_init(self):
        self.assertEqual(self.person1.fname, 'John')
        self.assertEqual(self.person1.lname, 'Smith')
        self.assertEqual(self.person1.age, 18)
        self.assertEqual(self.person1.phone_number, [])

    def test_add_phone(self): 
        self.person1.add_phone('2039118765')
        self.assertEqual(self.person1.phone_number, ['2039118765'])

    def test_get_name(self):
        self.assertEqual(self.person1.get_name(), 'John Smith')

    def test_compare_age(self):
        invalid = self.person1 < self.person2



unittest.main()
    
