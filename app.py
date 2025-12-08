import streamlit as st
import pandas as pd
import datetime
import os

st.set_page_config(page_title="Expense Tracker", layout="wide")

# -------------------------------
# Load or create CSV file
# -------------------------------
FILE_PATH = "expenses.csv"

if not os.path.exists(FILE_PATH):
    df = pd.DataFrame(columns=["date", "title", "amount", "category"])
    df.to_csv(FILE_PATH, index=False)

df = pd.read_csv(FILE_PATH)

# -------------------------------
# Add New Expense
# -------------------------------
st.title("💰 Expense Tracker")

with st.form("expense_form"):
    date = st.date_input("Date", datetime.date.today())
    title = st.text_input("Expense Title")
    amount = st.number_input("Amount (₹)", min_value=1.0, step=1.0)
    category = st.selectbox("Category", ["Food", "Travel", "Bills", "Shopping", "Other"])
    submitted = st.form_submit_button("Add Expense")

if submitted:
    new_entry = {"date": date, "title": title, "amount": amount, "category": category}

    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(FILE_PATH, index=False)

    st.success("Expense added successfully!")

# -------------------------------
# Dashboard
# -------------------------------
st.header("📊 Dashboard")

# Total expense
total = df["amount"].sum()
st.metric("Total Spent (₹)", f"{total:.2f}")

col1, col2 = st.columns(2)

# Pie chart - spend per category
with col1:
    st.subheader("🧾 Spending by Category")
    if not df.empty:
        st.bar_chart(df.groupby("category")["amount"].sum())

# Line chart - expenses over time
with col2:
    st.subheader("📅 Expenses Over Time")
    if not df.empty:
        df["date"] = pd.to_datetime(df["date"])
        time_series = df.groupby("date")["amount"].sum()
        st.line_chart(time_series)

# -------------------------------
# Show Full Table
# -------------------------------
st.header("📘 All Expenses")
st.dataframe(df)
