import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
from supabase import create_client, Client

# ---------------- Supabase Setup ----------------
SUPABASE_URL = "https://uobulncmptvgsprjuqky.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVvYnVsbmNtcHR2Z3Nwcmp1cWt5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjUyMjYyMTcsImV4cCI6MjA4MDgwMjIxN30.sthTRFsP9lNn9niVNvDgxPTw_NQfx9Aw9DeAwyMNDhU"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# ---------------- Page Config ----------------
st.set_page_config(page_title="Expense Tracker", page_icon="💰", layout="wide")

# ---------------- Categories & Payment Methods ----------------
CATEGORIES = [
    "Food & Dining", "Transportation", "Shopping", "Entertainment",
    "Bills & Utilities", "Healthcare", "Education", "Travel",
    "Groceries", "Others"
]
PAYMENT_METHODS = ["Cash", "Credit Card", "Debit Card", "UPI", "Net Banking"]

# ---------------- User Authentication ----------------
if "user" not in st.session_state:
    st.session_state.user = None

if st.session_state.user is None:
    st.title("Login / Signup")
    tab1, tab2 = st.tabs(["Login", "Signup"])

    # Login tab
    with tab1:
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_pass")
        if st.button("Login"):
            resp = supabase.auth.sign_in_with_password({"email": email, "password": password})
            if resp.user:
                st.session_state.user = resp.user
                st.success("Logged in successfully!")

            else:
                st.error("Login failed. Check email/password.")

    # Signup tab
    with tab2:
            username = st.text_input("Name", key="signup_username")
            email = st.text_input("New Email", key="signup_email")
            password = st.text_input("New Password", type="password", key="signup_pass")

            if st.button("Signup"):
                resp = supabase.auth.sign_up({"email": email, "password": password})

                if resp.user:
                    # Insert username into profiles table
                    supabase.table("profiles").insert({
                        "id": resp.user.id,
                        "username": username
                    }).execute()

                    st.success("Account created! Please login.")
                else:
                    st.error("Signup failed.")


# ---------------- Helper Functions ----------------
def fetch_expenses():
    """Fetch expenses of the logged-in user from Supabase"""
    if st.session_state.user:
        response = supabase.table("Expence").select("*").eq("user_id", st.session_state.user.id).execute()
        if response.data:
            st.session_state.expenses = response.data
        else:
            st.session_state.expenses = []

def fetch_user_profile():
    user_id = st.session_state.user.id
    resp = supabase.table("profiles").select("username").eq("user_id", user_id).execute()

    if resp.data:
        st.session_state.username = resp.data[0]["username"]
    else:
        st.session_state.username = "User"



def add_expense(date, category, amount, description, payment_method):
    """Insert a new expense into Supabase"""
    if category and amount > 0 and payment_method:
        data = {
            "user_id": st.session_state.user.id,
            "Date": date.isoformat(),
            "Category": category,
            "Amount": amount,
            "Description": description,
            "Payment_Method": payment_method
        }
        response = supabase.table("Expence").insert(data).execute()
        if response.data:
            st.success("Expense added successfully!")
            fetch_expenses()
        else:
            st.error("Failed to add expense.")
    else:
        st.error("Please fill all required fields.")

def get_expenses_df():
    """Convert session_state expenses to DataFrame"""
    if 'expenses' in st.session_state and st.session_state.expenses:
        df = pd.DataFrame(st.session_state.expenses)
        df['date'] = pd.to_datetime(df['date'], utc=True, errors='coerce').dt.tz_convert(None)
        return df
    return pd.DataFrame()

# ---------------- Initialize Data ----------------
if 'expenses' not in st.session_state:
    fetch_expenses()

df = get_expenses_df()

# ---------------- Sidebar: Add Expense ----------------
with st.sidebar:
    st.header("Add New Expense")
    with st.form("expense_form"):
        exp_date = st.date_input("Date", datetime.now())
        exp_category = st.selectbox("Category", CATEGORIES)
        exp_amount = st.number_input("Amount (₹)", min_value=0.0, step=10.0)
        exp_description = st.text_input("Description")
        exp_payment = st.selectbox("Payment Method", PAYMENT_METHODS)
        submitted = st.form_submit_button("Add Expense")
        if submitted:
            add_expense(exp_date, exp_category, exp_amount, exp_description, exp_payment)

    st.markdown("---")
    st.subheader("Data Management")
    if st.button("Clear Local Data"):
        st.session_state.expenses = []
        df = pd.DataFrame()

    if not df.empty:
        csv = df.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name=f"expenses_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )

# ---------------- Main Content ----------------
st.title(f"💰 {st.session_state.user.email}'s Expense Tracker")

if df.empty:
    st.info("👋 Start by adding your first expense using the form on the left.")
else:
    # Summary Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Expenses", f"₹{df['amount'].sum():,.2f}")
    col2.metric("Average Expense", f"₹{df['amount'].mean():,.2f}")
    col3.metric("Total Transactions", len(df))
    top_category = df.groupby('category')['amount'].sum().idxmax()
    col4.metric("Top Category", top_category)

    st.markdown("---")
    st.subheader("📊 Expense Analytics")

    col1, col2 = st.columns(2)
    date_range = st.date_input("Select Date Range", value=(df['date'].min(), df['date'].max()))
    selected_categories = st.multiselect("Filter by Category", options=CATEGORIES, default=CATEGORIES)

    # Filter data
    if len(date_range) == 2:
        mask = (df['date'] >= pd.Timestamp(date_range[0])) & (df['date'] <= pd.Timestamp(date_range[1]))
        filtered_df = df[mask]
    else:
        filtered_df = df
    filtered_df = filtered_df[filtered_df['category'].isin(selected_categories)]

    if filtered_df.empty:
        st.warning("No data available for the selected filters.")
    else:
        # Pie chart
        category_totals = filtered_df.groupby('category')['amount'].sum().reset_index()
        fig_pie = px.pie(category_totals, values='amount', names='category', title='Expenses by Category', hole=0.4)
        st.plotly_chart(fig_pie, use_container_width=True)

        # Bar chart
        payment_totals = filtered_df.groupby('payment_method')['amount'].sum().reset_index()
        fig_payment = px.bar(payment_totals, x='payment_method', y='amount', title='Expenses by Payment Method',
                             color='amount', color_continuous_scale='Blues')
        st.plotly_chart(fig_payment, use_container_width=True)

        # Daily trend
        daily_expenses = filtered_df.groupby('date')['amount'].sum().reset_index()
        fig_line = px.line(daily_expenses, x='date', y='amount', title='Daily Expense Trend', markers=True)
        st.plotly_chart(fig_line, use_container_width=True)

        # Recent Transactions
        st.subheader("📝 Recent Transactions")
        display_df = filtered_df.sort_values('date', ascending=False).copy()
        display_df['date'] = display_df['date'].dt.strftime('%Y-%m-%d')
        display_df['amount'] = display_df['amount'].apply(lambda x: f"₹{x:,.2f}")
        st.dataframe(display_df[['date', 'category', 'amount', 'description', 'payment_method']],
                     use_container_width=True, hide_index=True)

        # Monthly Summary
        st.subheader("📅 Monthly Summary")
        filtered_df['month'] = filtered_df['date'].dt.to_period('M')
        monthly_summary = filtered_df.groupby('month')['amount'].agg(['sum', 'count', 'mean']).reset_index()
        monthly_summary['month'] = monthly_summary['month'].astype(str)
        monthly_summary.columns = ['Month', 'Total Spent', 'Transactions', 'Average']

        col1, col2 = st.columns(2)
        col1.dataframe(monthly_summary.style.format({'Total Spent': '₹{:,.2f}', 'Average': '₹{:,.2f}'}),
                       use_container_width=True, hide_index=True)
        fig_monthly = px.bar(monthly_summary, x='Month', y='Total Spent', title='Monthly Spending', text='Total Spent')
        fig_monthly.update_traces(texttemplate='₹%{text:,.0f}', textposition='outside')
        col2.plotly_chart(fig_monthly, use_container_width=True)

# ---------------- Footer ----------------
st.markdown("---")
st.markdown("💡 **Tip:** Use the sidebar to add expenses and manage your data!")
