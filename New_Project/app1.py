import streamlit as st
import pandas as pd
from datetime import datetime
from supabase import create_client
import plotly.express as px
import logging
logging.basicConfig(level=logging.INFO)


st.markdown("""
<style>
/* container holding the tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 250px !important;    /* space between tabs */
}

/* tab text size (optional) */
.stTabs [data-baseweb="tab"] {
    font-size: 20px;
}
</style>
""", unsafe_allow_html=True)

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

st.set_page_config(
    page_title="Expense Tracker",
    page_icon="💰",
    layout="wide"
)

st.markdown("## 💰 Expense Tracker")
st.caption("Track • Analyze • Control your spending")
st.divider()
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
            st.rerun()
        else:
            st.error("Failed to add expense.")
    else:
        st.error("Please fill all required fields.")


def get_expenses_df():
    """Convert session_state expenses to DataFrame"""
    if 'expenses' in st.session_state and st.session_state.expenses:
        df = pd.DataFrame(st.session_state.expenses)
        df['date'] = pd.to_datetime(df['Date'], utc=True, errors='coerce').dt.tz_convert(None)
        return df
    return pd.DataFrame()

def update_expense(expense_id, date, category, amount, description, payment):
    supabase.table("Expence") \
        .update({
            "Date": date.isoformat(),
            "Category": category,
            "Amount": amount,
            "Description": description,
            "Payment_Method": payment
        }) \
        .eq("id", expense_id) \
        .execute()

    st.success("Expense updated successfully ✨")
    fetch_expenses()
    st.rerun()


# ---------------- Initialize Data ----------------
if 'expenses' not in st.session_state:
    fetch_expenses()

df = get_expenses_df()
tab_add, tab_table, tab_analytics = st.tabs(
    ["➕ Add", "📋 Transactions", "📊 Insights"]
)

with tab_add:
    st.subheader("➕ Add Expense")

    with st.form("add_expense_form"):
        col1, col2 = st.columns(2)

        with col1:
            amount = st.number_input("Amount (₹)", min_value=0.0, step=10.0)
            category = st.selectbox("Category", CATEGORIES)

        with col2:
            payment = st.selectbox("Payment Method", PAYMENT_METHODS)
            date = st.date_input("Date")

        description = st.text_input("Description (optional)")

        submit = st.form_submit_button("➕ Add Expense", use_container_width=True)

        if submit:
            add_expense(date, category, amount, description, payment)


with tab_table:
    st.subheader("📋 Recent Transactions")

    if df.empty:
        st.info("No expenses yet. Add your first expense ➕")
    else:
        display_df = df.sort_values("date", ascending=False).head(10)

        st.dataframe(
            display_df[["date", "Category", "Amount", "Payment_Method", "Description"]],
            use_container_width=True,
            hide_index=True
        )


with tab_analytics:
    if df.empty:
        st.info("📊 Analytics will appear once you add expenses.")
    else:
        # KPI CARDS
        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Total Spent", f"₹{df['Amount'].sum():,.2f}")
        col2.metric("Avg / Expense", f"₹{df['Amount'].mean():,.2f}")
        col3.metric("Transactions", len(df))
        col4.metric(
            "Top Category",
            df.groupby("Category")["Amount"].sum().idxmax()
        )

        st.divider()

        # FILTERS
        with st.expander("🔍 Filters"):
            date_range = st.date_input(
                "Date Range",
                value=(df["date"].min(), df["date"].max())
            )
            categories = st.multiselect(
                "Categories",
                options=CATEGORIES,
                default=CATEGORIES
            )

        filtered_df = df[
            (df["Category"].isin(categories)) &
            (df["date"] >= pd.Timestamp(date_range[0])) &
            (df["date"] <= pd.Timestamp(date_range[1]))
        ]

        if filtered_df.empty:
            st.warning("No data for selected filters.")
        else:
            # CHARTS
            col1, col2 = st.columns(2)

            with col1:
                fig_pie = px.pie(
                    filtered_df,
                    names="Category",
                    values="Amount",
                    title="Expenses by Category",
                    hole=0.4
                )
                st.plotly_chart(fig_pie, use_container_width=True)

            with col2:
                fig_bar = px.bar(
                    filtered_df,
                    x="Payment_Method",
                    y="Amount",
                    title="Payment Method Usage"
                )
                st.plotly_chart(fig_bar, use_container_width=True)

            st.divider()

            fig_line = px.line(
                filtered_df.groupby("date")["Amount"].sum().reset_index(),
                x="date",
                y="Amount",
                title="Daily Spending Trend",
                markers=True
            )
            st.plotly_chart(fig_line, use_container_width=True)



