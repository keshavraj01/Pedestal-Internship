import json
import os
import datetime
import pandas as pd

DATA_FILE = 'inventory.json'
LOG_FILE = 'stock_log.csv'

class Product:
    def __init__(self, name, id, quantity, price, category):
        self.name = name
        self.product_id = id  # Internally still using product_id
        self.quantity = quantity
        self.price = price
        self.category = category

    def to_dict(self):
        return {
            'name': self.name,
            'id': self.product_id,  # Match this with JSON key 'id'
            'quantity': self.quantity,
            'price': self.price,
            'category': self.category
        }

class Inventory:
    def __init__(self):
        self.products = []
        self.load_data()

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                try:
                    data = json.load(f)
                    self.products = [Product(**prod) for prod in data]
                except json.JSONDecodeError:
                    self.products = []
        else:
            self.products = []

    def save_data(self):
        with open(DATA_FILE, 'w') as f:
            json.dump([p.to_dict() for p in self.products], f, indent=4)

    def log_update(self, product, action):
        with open(LOG_FILE, 'a') as f:
            timestamp = datetime.datetime.now().isoformat()
            f.write(f"{timestamp},{product.product_id},{product.name},{action},{product.quantity}\n")

    def add_product(self):
        try:
            name = input("Name: ").strip()
            product_id = input("ID: ").strip()
            if any(p.product_id == product_id for p in self.products):
                print("❌ Product with this ID already exists.")
                return
            quantity = int(input("Quantity: "))
            price = float(input("Price: "))
            category = input("Category: ").strip()
            new_product = Product(name, product_id, quantity, price, category)
            self.products.append(new_product)
            self.save_data()
            self.log_update(new_product, "ADD")
            print("✅ Product added.")
        except Exception as e:
            print(f"❌ Error adding product: {e}")

    def view_products(self):
        if not self.products:
            print("No products found.")
            return
        print("\n📦 All Products:")
        for p in self.products:
            print(f"ID: {p.product_id} | Name: {p.name} | Qty: {p.quantity} | Price: {p.price} | Category: {p.category}")

    def search_product(self):
        key = input("Search by Name or ID: ").strip().lower()
        results = [p for p in self.products if p.product_id.lower() == key or p.name.lower() == key]
        if results:
            for p in results:
                print(f"ID: {p.product_id} | Name: {p.name} | Qty: {p.quantity} | Price: {p.price} | Category: {p.category}")
        else:
            print("🔍 Product not found.")

    def update_product(self):
        product_id = input("Enter Product ID to update: ").strip()
        for p in self.products:
            if p.product_id == product_id:
                try:
                    print("Leave blank to keep current value.")
                    name = input(f"Name ({p.name}): ").strip() or p.name
                    quantity = input(f"Quantity ({p.quantity}): ").strip()
                    price = input(f"Price ({p.price}): ").strip()
                    category = input(f"Category ({p.category}): ").strip() or p.category
                    p.name = name
                    p.quantity = int(quantity) if quantity else p.quantity
                    p.price = float(price) if price else p.price
                    p.category = category
                    self.save_data()
                    self.log_update(p, "UPDATE")
                    print("✅ Product updated.")
                    return
                except Exception as e:
                    print(f"❌ Error updating product: {e}")
                    return
        print("❌ Product ID not found.")

    def delete_product(self):
        product_id = input("Enter Product ID to delete: ").strip()
        for p in self.products:
            if p.product_id == product_id:
                self.products.remove(p)
                self.save_data()
                self.log_update(p, "DELETE")
                print("✅ Product deleted.")
                return
        print("❌ Product ID not found.")

    def generate_report(self):
        if not self.products:
            print("No products to report.")
            return
        df = pd.DataFrame([p.to_dict() for p in self.products])
        print("\n📊 Inventory Report")
        print("Total Inventory Value: ₹", (df['quantity'] * df['price']).sum())
        print("\n🔻 Low Stock Items (Qty < 10):")
        low_stock = df[df['quantity'] < 10]
        if low_stock.empty:
            print("All items sufficiently stocked.")
        else:
            print(low_stock[['id', 'name', 'quantity', 'category']].to_string(index=False))

def menu():
    inv = Inventory()
    while True:
        print("\n=== Inventory Management Menu ===")
        print("1. Add Product")
        print("2. View All Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Generate Report")
        print("7. Exit")

        choice = input("Enter choice (1-7): ")
        match choice:
            case '1': inv.add_product()
            case '2': inv.view_products()
            case '3': inv.search_product()
            case '4': inv.update_product()
            case '5': inv.delete_product()
            case '6': inv.generate_report()
            case '7':
                print("Exiting Inventory System.")
                break
            case _: print("Invalid choice. Please enter 1-7.")

if __name__ == "__main__":
    menu()
