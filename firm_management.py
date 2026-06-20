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
    number_of_pms = 0
    pms = []
    def __init__ (self,name, employee_id, role, base_salary, aum):
        super().__init__(name, employee_id, role, base_salary)
        self.aum = aum
        PortfolioManager.number_of_pms +=1
        PortfolioManager.pms.append(self)

    def __str__(self) -> str:
        return f"{self.name} Salary is {self.base_salary} and he manages {self.aum}"

    @staticmethod
    def display_status():
        for portfoliomanageremployee in PortfolioManager.pms:
            print(portfoliomanageremployee)

class Administrative(Employee):
    def __init__ (self,name, employee_id, role, base_salary, responsibilities):
        super().__init__(name, employee_id, role, base_salary)
        self.responsibilities = responsibilities

pm_dany = PortfolioManager("Dany", "157345", "Portfolio Manager", 2000, 50000000)
pm_rami = PortfolioManager("Rami", "167333", "Portfolio Manager", 2000, 45000000)
pm_elis = PortfolioManager("Elis", "294300", "Portfolio Manager", 2800, 65000000)

PortfolioManager.display_status()

#ad_yael = Administrative("Yael", "963114", "Manage Front Desk", 1650, ["Front desk's employees", "Bank's connections"])
#ad_yaron = Administrative("Yaron", "593169", "IT", 3650, ["Data Accuracy", "Computers", "Bookkeeping"])
#print(f"{ad_yaron.name} Salary is {ad_yaron.base_salary} and his responsibilities are:\n{ad_yaron.responsibilities}")    