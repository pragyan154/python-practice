# a shop application to add products and display products.
# check if product and name is valid or not , used custom exception
import re
class InvalidProductError(Exception): # Custom Exception 
    def __init__(self, product_name):
        self.product_name = product_name

    def __str__(self):
        return f"Invalid product: {self.product_name}"

class Product:
    def __init__(self, name, price):
        self.name = self.validate_product_name(name)
        self.price = price

    def validate_product_name(self, name):
        pattern = r"^[a-zA-Z0-9\s]+$"
        if not re.match(pattern, name):
            raise InvalidProductError(name)
        return name

class Shop:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        print(f"Products available in {self.name}:")
        for product in self.products:
            print(f"- {product.name}: ${product.price}")


# shop will be initilized, then asked about the opreation.
def main():
    try:
        shop_name = input("Enter shop name: ")
        shop = Shop(shop_name)

        while True:
            print("Select an option:")
            print("1. Add product")
            print("2. Display products")
            print("3. Exit")

            option = input("Enter option: ")

            if option == "1":
                product_name = input("Enter product name: ")
                product_price = float(input("Enter product price: "))

                product = Product(product_name, product_price)
                shop.add_product(product)
                print("Product added successfully!")

            elif option == "2":
                shop.display_products()

            elif option == "3":
                break

            else:
                print("Invalid option. Please try again.")

    except InvalidProductError as e:
        print("Error:", e)

    except Exception as e:
        print("An error occurred:", e)


# Run the Application
if __name__ == "__main__":
    main()
