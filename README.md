# Bill Book Management System

This is a Python-based **Bill Book Management System**, which allows users to create and view customer bills with detailed information. The application is designed for small businesses to manage billing in a simple and efficient way using a console-based interface.

## Features
1. **Create Bill**:
   - Input customer details (name, mobile number).
   - Add multiple items with their name, rate, and quantity.
   - Automatically calculates the total amount for the bill.
   - Generates a unique bill number.
2. **View All Bills**:
   - Display all previously generated bills.
   - Shows detailed information, including:
     - Bill number
     - Date
     - Customer details
     - Itemized list with rate, quantity, and price
     - Total amount
3. **Persistent Data**:
   - Bills are stored in a dictionary within the program.

## How It Works
1. When the program starts, the user is presented with a menu:
   - Press `1` to create a new bill.
   - Press `2` to view all bills.
   - Press `0` to exit.
2. For creating a bill:
   - Enter customer details (name and mobile number).
   - Specify the number of items and input details for each item (name, rate, and quantity).
   - A bill is generated and displayed in a formatted layout.
3. For viewing all bills:
   - The program loops through all stored bills and displays them one by one.
4. Exit the application by selecting `0`.

## Requirements
- Python 3.x
- `datetime` library (built-in)

## How to Run
1. Clone the repository or download the script file.
2. Open a terminal or command prompt in the script's directory.
3. Run the script using:
   ```bash
   python bill_book.py
