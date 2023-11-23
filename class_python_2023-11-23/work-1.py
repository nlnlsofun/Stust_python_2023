# 定義 Employee 類別
class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department
    # 計算員工薪水的方法，根據工作小時數計算可能的加班薪水
    def calculate_emp_salary(self, hours_worked):
        base_salary = self.emp_salary
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = overtime * (base_salary / 50)
            total_salary = base_salary + overtime_amount
        else:
            total_salary = base_salary
        return total_salary
    # 分配員工部門的方法
    def emp_assign_department(self, new_department):
        self.emp_department = new_department
    # 印出員工詳細資訊的方法
    def print_employee_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Salary: {self.emp_salary}")
        print(f"Employee Department: {self.emp_department}")
# 樣本員工資料
employees_data = [
    ("ADAMS", "E7876", 50000, "ACCOUNTING"),
    ("JONES", "E7499", 45000, "RESEARCH"),
    ("MARTIN", "E7900", 50000, "SALES"),
    ("SMITH", "E7698", 55000, "OPERATIONS"),
]
# 創建 Employee 實例
employees = [Employee(*data) for data in employees_data]
# 使用方法
for emp in employees:
    emp.print_employee_details()
    new_department = "IT"  # 更改部門為 "IT"
    emp.emp_assign_department(new_department)
    emp.print_employee_details()
    hours_worked = 55  # 例子中的工作小時
    total_salary = emp.calculate_emp_salary(hours_worked)
    print(f"Total Salary (including overtime): {total_salary}")
    print("\n")
