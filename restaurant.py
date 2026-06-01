# restaurant.py
class Restaurant:
    def __init__(self, name, cuisine, rating=0):
        self.name = name
        self.cuisine = cuisine
        self.rating = rating
    def describe(self):
        print(f"{self.name}, {self.cuisine}, рейтинг {self.rating}")
# и т.д. (вставьте полный код из предыдущего сообщения)
