# 🏷️ Mini Inventory Management System – Python Project

A command-line based **Inventory Management System** built using **Object-Oriented Programming (OOP)** in Python. It enables adding, updating, deleting, and reporting on products with data stored in a persistent CSV or JSON format.

---

## 📌 Features

- ➕ Add new products (Name, ID, Quantity, Price, Category)  
- 📋 View all products in the inventory  
- 🔍 Search products by ID or Name  
- ✏️ Update product information  
- ❌ Delete products from inventory  
- 📊 Generate Reports:
  - Total Inventory Value
  - List of Low-Stock Items (quantity < 10)
- 💾 Store and update inventory data in JSON or CSV format  
- 🧪 Robust exception handling throughout the program  

---

## 🎯 Bonus Features

- 🧭 CLI Menu-based user interface  
- 🧮 Use of `pandas` for filtering and reporting  
- 🕒 Maintain a **date-wise stock update log**

---

## 📂 Product Fields

Each product includes the following details:

- **Product Name**
- **Product ID**
- **Quantity**
- **Price**
- **Category**

---

## 🛠 How to Run

1. Ensure Python 3 is installed.
2. (Optional) Install `pandas`:
   ```bash
   pip install pandas
