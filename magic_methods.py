class Employee:
    def __new__(cls):
        print("__new__ magic method is called")
        inst = object.__new__(cls)
        return inst
    
    def __init__(self):
        print("__init__ magic method is called")
        self.name = 'Jordin'
        self.salary = 100000
        
    def __str__(self):
        return f'name={self.name}, salary=${str(self.salary)}'
        
    

if __name__ == "__main__":
    employee_one = Employee()
    print(employee_one)