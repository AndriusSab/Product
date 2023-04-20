# Create a dataclass named "Product" that has the following attributes:
#     product_id: int
#     name: str
#     price: float
#     quantity: int
# The class should also have a method named "total_cost" that calculates and returns the total cost of the product, which is the price multiplied by the quantity.
# Create a list of Product objects and write a function that takes this list as input and returns the product with the highest total cost.
# Write a program that creates a list of 5 Product objects, prints out their attributes, and then calls the function to find the product with the highest total cost.


from dataclasses import dataclass


@dataclass
class Product:
    product_id: int
    name: str
    price: float
    quantity: int

    def total_cost(self):
        total_cost = self.price * self.quantity
        return total_cost


products = products = [
    Product(product_id=1, name="Cepelinai", price=10.0, quantity=5),
    Product(product_id=2, name="Ceburekai", price=2.0, quantity=10),
    Product(product_id=3, name="Alutis", price=2.5, quantity=20),
]


def find_highest_cost_product(products):
    max_cost_product = max(products, key=lambda p: p.total_cost())

    return max_cost_product


highest_cost_product = find_highest_cost_product(products)

print(highest_cost_product)
