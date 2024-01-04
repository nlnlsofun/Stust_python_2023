class FriedChickenShop:
    def __init__(self, name, location, chicken_type, price_per_piece, opening_hours):
        # 建構子，初始化屬性
        self.name = name #店名
        self.location = location #開在哪
        self.chicken_type = chicken_type #口味
        self.price_per_piece = price_per_piece #價格
        self.opening_hours = opening_hours #開店時間

    def display_info(self):
        # 顯示炸雞店資訊
        print(f"歡迎光臨 {self.name}，位於 {self.location}。我們提供 {self.chicken_type} 雞，每塊售價 {self.price_per_piece} 元。")

    def calculate_total_price(self, num_pieces):
        # 計算指定數量的總價格
        return num_pieces * self.price_per_piece

    def is_open(self, current_time):
        # 檢查店家是否在指定時間開放
        return current_time in self.opening_hours


# 建立四個物件
shop1 = FriedChickenShop("胖老爹", "永康", "辣味", 2.5, ["12:00 PM", "9:00 PM"])
shop2 = FriedChickenShop("麥當勞", "安南", "燒烤", 3.0, ["11:00 AM", "8:00 PM"])
shop3 = FriedChickenShop("肯德基", "東區", "原味", 2.0, ["10:00 AM", "7:00 PM"])
shop4 = FriedChickenShop("丹丹漢堡", "歸仁", "特辣", 3.5, ["1:00 PM", "10:00 PM"])

# 呼叫三個函式共計12次
shop1.display_info()
print(f"購買 5 塊的總價格: ${shop1.calculate_total_price(5)}")
print(f"店家在下午2點是否開放？ {'是的' if shop1.is_open('2:00 PM') else '否'}\n")

shop2.display_info()
print(f"購買 3 塊的總價格: ${shop2.calculate_total_price(3)}")
print(f"店家在中午12點30分是否開放？ {'是的' if shop2.is_open('12:30 PM') else '否'}\n")

shop3.display_info()
print(f"購買 8 塊的總價格: ${shop3.calculate_total_price(8)}")
print(f"店家在下午5點30分是否開放？ {'是的' if shop3.is_open('5:30 PM') else '否'}\n")

shop4.display_info()
print(f"購買 4 塊的總價格: ${shop4.calculate_total_price(4)}")
print(f"店家在晚上9點是否開放？ {'是的' if shop4.is_open('10:00 PM') else '否'}")
