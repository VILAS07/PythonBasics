import streamlit as st
import csv
import os
from datetime import datetime

# Units dictionary
UNITS = {
    "Piece": "piece",
    "Kg": "kg",
    "Gram": "gram",
    "Litre": "litre",
    "ML": "ml",
    "Packet": "packet"
}

st.set_page_config(page_title="Daily Expense Tracker", layout="centered")

st.title("🧾 Daily Expense Tracker")
st.write("Enter your daily expense items here.")

# Input form
with st.form("expense_form"):
    category = st.selectbox("Category", ["Grocery", "Food", "Travel", "Shopping", "Bills", "Other"])
    item = st.text_input("Item Name")

    unit = st.selectbox("Unit", list(UNITS.keys()))
    quantity = st.number_input("Quantity", min_value=0.0, format="%.2f")
    unit_price = st.number_input("Unit Price", min_value=0.0, format="%.2f")

    payment_mode = st.selectbox("Payment Mode", ["Cash", "UPI", "Card"])

    submitted = st.form_submit_button("➕ Add Expense")

# When form is submitted
if submitted:
    if item == "" or quantity == 0 or unit_price == 0:
        st.error("Please fill all fields correctly.")
    else:
        date = datetime.now().strftime("%Y-%m-%d")
        total_price = quantity * unit_price

        # Check CSV
        file_exists = os.path.isfile("expenses.csv")

        with open("expenses.csv", "a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(
                    ["date", "category", "item", "quantity", "unit", "unit_price", "total_price", "payment_mode"])
            writer.writerow([date, category, item, quantity, UNITS[unit], unit_price, total_price, payment_mode])

        st.success(f"Added: {item} - ₹{total_price:.2f}")

# Show existing expenses
st.subheader("📊 Today's Expenses")

if os.path.isfile("expenses.csv"):
    import pandas as pd

    df = pd.read_csv("expenses.csv")

    # Filter by today's date
    today = datetime.now().strftime("%Y-%m-%d")
    today_data = df[df["date"] == today]

    if not today_data.empty:
        st.dataframe(today_data)
        st.write(f"### 💰 Total Spent Today: ₹{today_data['total_price'].sum():.2f}")
    else:
        st.info("No expenses added today yet.")
else:
    st.info("No data found yet.")
