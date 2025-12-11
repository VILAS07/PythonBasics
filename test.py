import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
from supabase import create_client

# ---------------- Supabase Setup ----------------
SUPABASE_URL = "https://uobulncmptvgsprjuqky.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVvYnVsbmNtcHR2Z3Nwcmp1cWt5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjUyMjYyMTcsImV4cCI6MjA4MDgwMjIxN30.sthTRFsP9lNn9niVNvDgxPTw_NQfx9Aw9DeAwyMNDhU"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# ---------------- Page Config ----------------
st.set_page_config(page_title="Expense Tracker", page_icon="💰", layout="wide")
st.title("💰 Personal Expense Tracker")
st.markdown("---")

# ---------------- Categories & Payment Methods ----------------
CATEGORIES = [
    "Food & Dining", "Transportation", "Shopping", "Entertainment",
    "Bills & Utilities", "Healthcare", "Education", "Travel",
    "Groceries", "Others"
]
PAYMENT_METHODS = ["Cash", "Credit Card", "Debit Card", "UPI", "Net Banking"]

def fetch_expences():
    response=supabase.table('Expence').select('*').execute()
    if response.data:
        st.session_state.expences=response.data
    else:
        st.session_state.expences=[]

def add_expences(date, category, amount, description, payment_method):
    if category and amount>0 and payment_method!=0:
        data={
            "Date": date.isoformat(),
            "Category": category,
            "Amount": amount,
            "Description": description,
            "Payment_Method": payment_method
        }
        responce=supabase.table('Expence').insert(data).execute()
        if responce.data:
            st.success("Expense Added Successfully :)")
            fetch_expences()
        else:
            st.error("Failed To Add Expence :(")
    else:
        st.error("Fill All The Fiedls :|")

if 'expenses' not in st.session_state:
    fetch_expences()