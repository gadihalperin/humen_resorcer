"""

def display_employee(emp_dict):
    print(f"Employee Name: {emp_dict['name']}\nEmployee Role: {emp_dict['role']}\nEmployee Salary: {emp_dict['base_salary']}")



employee_one = {"name": "Dany", "employee_id": "157345", "role" : "Portfolio Manager", "base_salary" : 2000}
display_employee(employee_one)

"""



class Employee:
    def __init__ (self, name, employee_id, role, base_salary):
        self.name = name
        self.employee_id = employee_id
        self.role = role
        self.base_salary = base_salary
       

employee_one = Employee("Dany", "157345", "Portfolio Manager", 2000)
print(f"{employee_one.name} Salary is {employee_one.base_salary}")
    