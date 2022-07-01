import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    

    def setUp(self):
        self.e = Employee('Yesheb',23,67000,'0324-4348321',15000)
        self.e.get_name()
        self.e.get_age()
        self.e.get_salary()
        self.e.update_salary()
        self.e.get_bonus()
    
        
    #test_case_1
    def test_get_name(self):
        print('test_name')
        self.assertEqual(self.e.get_name(), 'Yesheb')
    
    #test_case_2
    def test_get_age(self):
        print('test_age')
        self.assertEqual(self.e.get_age(),23)

    #test_case_3
    def test_get_salary(self):
        print('test_salary')
        self.assertEqual(self.e.get_salary(), 67000)
    
    #test_case_4
    def test_update_salary(self):
        print('test_update_salary')
        self.assertEqual(self.e.update_salary(), 82000)
    
    #test_case_5
    def test_get_bonus(self):
        print('test_bonus')
        self.assertEqual(self.e.get_bonus(), 15000)
    
    
if __name__ == '__main__':
    unittest.main()  