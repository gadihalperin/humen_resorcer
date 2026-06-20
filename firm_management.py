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
    
class PortfolioManager(Employee):
    def __init__ (self,name, employee_id, role, base_salary, aum):
        super().__init__(name, employee_id, role, base_salary)
        self.aum = aum
       

pm_dany = PortfolioManager("Dany", "157345", "Portfolio Manager", 2000, 50000000)
print(f"{pm_dany.name} Salary is {pm_dany.base_salary} and he manage {pm_dany.aum}")
    