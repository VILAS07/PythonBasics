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

# ---------------- CSS: Tab Spacing ----------------
st.markdown("""
<style>
.stTabs [data-baseweb="tab-list"] {
    gap: 200px !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Categories ----------------
CATEGORIES = [
    "Food & Dining", "Transportation", "Shopping", "Entertainment",
    "Bills & Utilities", "Healthcare", "Education", "Travel",
    "Groceries", "Others"
]
PAYMENT_METHODS = ["Cash", "Credit Card", "Debit Card", "UPI", "Net Banking"]

# ---------------- User Authentication ----------------
if "user" not in st.session_state:
    st.session_state.user = None

if "username" not in st.session_state:
    st.session_state.username = "User"

if st.session_state.user is None:
    st.title("Login / Signup")
    login_tab, signup_tab = st.tabs(["Login", "Signup"])

    # ---------------- LOGIN ----------------
    with login_tab:
        login_email = st.text_input("Email")
        login_pass = st.text_input("Password", type="password")

        if st.button("Login"):
            resp = supabase.auth.sign_in_with_password(
                {"email": login_email, "password": login_pass}
            )

            if resp.user:
                st.session_state.user = resp.user

                # Fetch username
                prof = supabase.table("profiles") \
                    .select("username") \
                    .eq("user_id", resp.user.id) \
                    .execute()

                if prof.data and len(prof.data) > 0:
                    st.session_state.username = prof.data[0]["username"]
                else:
                    st.session_state.username = "User"

                st.success("Logged in successfully!")
                st.rerun()
            else:
                st.error("Login failed. Check email/password.")

    # ---------------- SIGNUP ----------------
    with signup_tab:
        username = st.text_input("Name")
        signup_email = st.text_input("New Email")
        signup_pass = st.text_input("New Password", type="password")

        if st.button("Signup"):
            resp = supabase.auth.sign_up(
                {"email": signup_email, "password": signup_pass}
            )

            if resp.user:
                # Insert username + user_id
                supabase.table("profiles").insert({
                    "user_id": resp.user.id,
                    "username": username
                }).execute()

                st.success("Account created! Please login.")
            else:
                st.error("Signup failed.")

    st.stop()  # Prevent loading app before login


# ---------------- Fetch Expenses ----------------
def fetch_expenses():
    response = supabase.table("Expence") \
        .select("*") \
        .eq("user_id", st.session_state.user.id) \
        .execute()

    st.session_state.expenses = response.data if response.data else []


# ---------------- Add Expense ----------------
def add_expense(date, category, amount, description, payment_method):
    data = {
        "user_id": st.session_state.user.id,
        "Date": date.isoformat(),
        "Category": category,
        "Amount": amount,
        "Description": description,
        "Payment_Method": payment_method,
    }

    response = supabase.table("Expence").insert(data).execute()
    if response.data:
        st.success("Expense added successfully!")
        fetch_expenses()
    else:
        st.error("Failed to add expense.")


# ---------------- Convert to DataFrame ----------------
def get_expenses_df():
    if "expenses" in st.session_state and st.session_state.expenses:
        df = pd.DataFrame(st.session_state.expenses)

        # Use correct column name from Supabase: "Date"
        df["date"] = pd.to_datetime(df["Date"], utc=True, errors="coerce").dt.tz_convert(None)
        return df
    return pd.DataFrame()



# ---------------- Load data ----------------
if "expenses" not in st.session_state:
    fetch_expenses()

df = get_expenses_df()

# ---------------- Sidebar ----------------
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
    if not df.empty:
        csv = df.to_csv(index=False)
        st.download_button("Download CSV", csv, "expenses.csv", "text/csv")

# ---------------- Main Page ----------------
st.title(f"💰 Welcome, {st.session_state.username}!")

if df.empty:
    st.info("👋 You have no expenses yet. Add some using the sidebar!")
else:
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Expenses", f"₹{df['amount'].sum():,.2f}")
    col2.metric("Avg Expense", f"₹{df['amount'].mean():,.2f}")
    col3.metric("Transactions", len(df))
    top_category = df.groupby('category')['amount'].sum().idxmax()
    col4.metric("Top Category", top_category)

    st.markdown("---")
    st.subheader("📊 Expense Analytics")

    # ----- Filters -----
    date_range = st.date_input(
        "Select Date Range", (df["date"].min(), df["date"].max())
    )
    selected_categories = st.multiselect(
        "Filter by Category", CATEGORIES, default=CATEGORIES
    )

    mask = (df["date"] >= pd.Timestamp(date_range[0])) & \
           (df["date"] <= pd.Timestamp(date_range[1]))

    filtered_df = df[mask]
    filtered_df = filtered_df[filtered_df["category"].isin(selected_categories)]

    if filtered_df.empty:
        st.warning("No data available for selected filters.")
    else:
        # Pie Chart
        fig_pie = px.pie(
            filtered_df.groupby("category")["amount"].sum().reset_index(),
            values="amount",
            names="category",
            title="Expenses by Category"
        )
        st.plotly_chart(fig_pie, use_container_width=True)

        # Payment Method Bar
        fig_bar = px.bar(
            filtered_df.groupby("payment_method")["amount"].sum().reset_index(),
            x="payment_method",
            y="amount",
            title="Expenses by Payment Method"
        )
        st.plotly_chart(fig_bar, use_container_width=True)

        # Daily Trend
        fig_line = px.line(
            filtered_df.groupby("date")["amount"].sum().reset_index(),
            x="date",
            y="amount",
            title="Daily Expense Trend",
            markers=True
        )
        st.plotly_chart(fig_line, use_container_width=True)

        # Recent Transactions
        st.subheader("📝 Recent Transactions")
        st.dataframe(
            filtered_df.sort_values("date", ascending=False)[
                ["date", "category", "amount", "description", "payment_method"]
            ],
            use_container_width=True
        )

st.markdown("---")
st.caption("💡 Tip: Add expenses through the sidebar!")

