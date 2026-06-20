def display_employee(emp_dict):
    print(f"Employee Name: {emp_dict['name']}\nEmployee Role: {emp_dict['role']}\nEmployee Salary: {emp_dict['base_salary']}")



employee_one = {"name": "Dany", "employee_id": "157345", "role" : "Portfolio Manager", "base_salary" : 2000}
display_employee(employee_one)