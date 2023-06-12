# class Review:
#     def __init__(self, user_name, review, rating):
#         self.user_name = user_name
#         self.review = review
#         self.rating = rating
#         self.reviews = [self]

#     def __str__(self):
#         return f"Review by {self.user_name}: {self.review} (Rating: {self.rating})"

#     def add_review(self, review, rating):
#         new_review = Review(self.user_name, review, rating)
#         self.reviews.append(new_review)

#     def calculate_average_rating(self):
#         if not self.reviews:
#             return 0

#         total_rating = sum(review.rating for review in self.reviews)
#         average_rating = total_rating / len(self.reviews)
#         return average_rating


# review1 = Review("John", "Great food and excellent service!", 4)
# review1.add_review("Delicious dishes and friendly staff!", 5)
# review1.add_review("Average experience, but good food.", 3)

# for review in review1.reviews:
#     print(review)

class Menu:
    def __init__(self):
        self.items = {}

    def add_menuitem(self, item, price):
        self.items[item] = price

    def remove_menuitem(self, item):
        if item in self.items:
            del self.items[item]
            print(f"Removed {item} from the menu")
        else:
            print(f"{item} is not in the menu")

    def display_menu(self):
        if self.items:
            print("Menu:")
            for item, price in self.items.items():
                print(f"{item} - Rs.{price}")
        else:
            print("No items found in the menu")


class OrderFood:
    def __init__(self, menu):
        self.menu = menu
        self.order = {}

    def add_item(self, item, quantity):
        if item in self.menu.items:
            if item in self.order:
                self.order[item] += quantity
            else:
                self.order[item] = quantity
            print(f"Added {quantity} {item}(s) to the order")
        else:
            print(f"{item} is not available in the menu")

    def remove_item(self, item, quantity):
        if item in self.order:
            if self.order[item] >= quantity:
                self.order[item] -= quantity
                if self.order[item] == 0:
                    del self.order[item]
                print(f"Removed {quantity} {item}(s) from the order")
            else:
                print(f"Not enough {item}(s) in the order")
        else:
            print(f"{item} is not in the order")

    def calculate_bill(self):
        total = 0
        for item, quantity in self.order.items():
            if item in self.menu.items:
                price = self.menu.items[item]
                total += price * quantity
        return total


# Creating an instance of Menu
menu = Menu()

# Adding menu items
menu.add_menuitem("Pizza", 200)
menu.add_menuitem("Burger", 150)
menu.add_menuitem("Pasta", 180)
menu.add_menuitem("Salad", 100)

# Displaying the menu
menu.display_menu()

# Creating an instance of OrderFood
order = OrderFood(menu)

# Adding items to the order
order.add_item("Pizza", 2)
order.add_item("Burger", 1)
order.add_item("Salad", 3)

# Removing items from the order
order.remove_item("Pizza", 1)

# Calculating the bill
bill = order.calculate_bill()
print(f"Total Bill: Rs.{bill}")
