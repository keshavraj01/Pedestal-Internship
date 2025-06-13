# 📒 Contact Book CLI – Python Project

A simple command-line based **Contact Book** built in Python that allows users to manage contacts efficiently with persistent storage using JSON.

---

## 📌 Features

- ➕ Add new contacts  
- 📋 View all saved contacts  
- 🔍 Search contacts by name or phone  
- ✏️ Edit existing contact details  
- ❌ Delete contacts  
- 💾 Data persistence using JSON file  
- ✅ Input validation for phone numbers and email addresses  
- 📤 **Bonus**: Export contacts to a CSV file  

---

## 📂 Contact Fields

Each contact stores the following information:

- **Name**
- **Phone Number**
- **Email Address**
- **Address**

---

## ✅ Validations

- **Phone Number**: Must be 10 digits.
- **Email Address**: Must follow valid email format (e.g., `example@gmail.com`).
- If input is invalid, the program will prompt the user to re-enter instead of exiting.

---

## 🛠 How to Run

1. **Clone this repository** or download the `contact_book.py` file.
2. Make sure Python 3 is installed.
3. Run the script:
   ```bash
   python contact_book.py
