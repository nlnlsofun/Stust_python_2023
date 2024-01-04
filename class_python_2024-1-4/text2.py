class Employee:
    def __init__(self, name, years_of_service, working_hours):
        # 員工屬性
        self.name = name
        self.years_of_service = years_of_service
        self.working_hours = working_hours

    def query_name(self):
        # 查詢員工姓名
        return self.name

    def query_years_of_service(self):
        # 查詢員工年資
        return self.years_of_service

    def query_working_hours(self):
        # 查詢員工工作時數
        return self.working_hours

    def calculate_monthly_salary(self, hourly_wage):
        # 計算員工月薪
        return self.working_hours * hourly_wage * 30  # 假設一個月有30天

    def increase_working_hours(self, additional_hours):
        # 增加員工工作時數
        self.working_hours += additional_hours

    def increase_years_of_service(self, additional_years):
        # 增加員工年資
        self.years_of_service += additional_years


class ColdBeverage:
    def __init__(self, name, ice_amount, sweetness_level, price):
        # 冷飲屬性
        self.name = name
        self.ice_amount = ice_amount
        self.sweetness_level = sweetness_level
        self.price = price


class HotBeverage:
    def __init__(self, name, ice_amount, sweetness_level, price):
        # 熱飲屬性
        self.name = name
        self.ice_amount = ice_amount
        self.sweetness_level = sweetness_level
        self.price = price


# 建立一個飲料店員工物件
employee1 = Employee("小明", 2, 160)

# 查詢員工資訊
print(f"員工姓名: {employee1.query_name()}")
print(f"員工年資: {employee1.query_years_of_service()} 年")
print(f"員工工作時數: {employee1.query_working_hours()} 小時")

# 計算月薪
hourly_wage = 150  # 假設時薪為150元
print(f"員工月薪: {employee1.calculate_monthly_salary(hourly_wage)} 元")

# 增加工作時數和年資
employee1.increase_working_hours(10)
employee1.increase_years_of_service(1)

# 查詢增加後的資訊
print(f"員工工作時數增加後: {employee1.query_working_hours()} 小時")
print(f"員工年資增加後: {employee1.query_years_of_service()} 年")

# 建立一個冷飲物件
cold_drink = ColdBeverage("檸檬紅茶", "半冰", "正常甜", 50)

# 顯示冷飲資訊
print(f"冷飲名稱: {cold_drink.name}")
print(f"冰量: {cold_drink.ice_amount}")
print(f"甜度: {cold_drink.sweetness_level}")
print(f"價格: {cold_drink.price} 元")
