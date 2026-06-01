class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating          # задание 13.3

    def describe_restaurant(self):
        print(f"Ресторан '{self.restaurant_name}' | Кухня: {self.cuisine_type} | Рейтинг: {self.rating}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} открыт!")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Рейтинг ресторана '{self.restaurant_name}' обновлён до {self.rating}")


# ---------- 13.1 Демонстрация ----------
print("=== 13.1 ===")
newRestaurant = Restaurant("Уют", "Русская")
print(newRestaurant.restaurant_name)
print(newRestaurant.cuisine_type)
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()

# ---------- 13.2 Три экземпляра ----------
print("\n=== 13.2 ===")
rest1 = Restaurant("Итальянский дворик", "Итальянская", 4.5)
rest2 = Restaurant("Суши-мастер", "Японская", 4.7)
rest3 = Restaurant("Бургер Кинг", "Фастфуд", 4.2)
rest1.describe_restaurant()
rest2.describe_restaurant()
rest3.describe_restaurant()

# ---------- 13.3 Обновление рейтинга ----------
print("\n=== 13.3 ===")
rest1.update_rating(4.8)
rest1.describe_restaurant()
