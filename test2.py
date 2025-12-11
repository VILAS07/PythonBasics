from datetime import datetime
import streamlit as st
from supabase import create_client

SUPABASE_URL = "https://uobulncmptvgsprjuqky.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVvYnVsbmNtcHR2Z3Nwcmp1cWt5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjUyMjYyMTcsImV4cCI6MjA4MDgwMjIxN30.sthTRFsP9lNn9niVNvDgxPTw_NQfx9Aw9DeAwyMNDhU"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

category = st.text_input("Category")
amount = st.number_input("Amount", min_value=0.0)
description = st.text_input("Description")
payment_method = st.selectbox("Payment Method", ["Cash", "Credit Card", "Debit Card", "UPI", "Net Banking"])

if st.button("Add Expense"):
    if category and amount > 0 and payment_method:
        data = {
            "Date": datetime.now().isoformat(),  # matches column 'Date'
            "Category": category,
            "Amount": amount,
            "Description": description,
            "Payment_Method": payment_method
        }
        response = supabase.table("Expence").insert(data).execute()
        st.write("Inserted:", response.data)
    else:
        st.error("Please fill all required fields")
