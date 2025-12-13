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

st.set_page_config(page_title="Expense Tracker", page_icon="💰", layout="wide")
st.title("💰 Personal Expense Tracker")
st.markdown("---")
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
st.header(f"Welcome Back {st.session_state.username}")

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

# ---------------- Initialize Data ----------------
if 'expenses' not in st.session_state:
    fetch_expenses()

df = get_expenses_df()
tab3, tab4, tab5 = st.tabs(["Add Expence", "Table View", "Analytics"])


with tab3:
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
with tab4:
    # Ensure filtered_df exists
    if not df.empty:
        filtered_df = df.copy()  # fallback if no filters yet
    else:
        filtered_df = pd.DataFrame()


    if not filtered_df.empty:
        st.subheader("📝 Recent Transactions")
        display_df = filtered_df.sort_values("date", ascending=False).copy()
        display_df["date"] = display_df["date"].dt.strftime("%Y-%m-%d")
        display_df["Amount"] = display_df["Amount"].apply(lambda x: f"₹{x:,.2f}")

        st.dataframe(
            display_df[["date", "Category", "Amount", "Description", "Payment_Method"]],
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info("No recent transactions to display.")




with tab5:
    if df.empty:
        st.info("👋 Welcome! Start by adding your first expense using the form on the left.")
    else:
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Expenses", f"₹{df['Amount'].sum():,.2f}")
        col2.metric("Average Expense", f"₹{df['Amount'].mean():,.2f}")
        col3.metric("Total Transactions", len(df))
        top_category = df.groupby('Category')['Amount'].sum().idxmax()
        col4.metric("Top Category", top_category)

        st.markdown("---")

        st.subheader("📊 Expense Analytics")
        col1, col2 = st.columns(2)
        date_range = st.date_input("Select Date Range", value=(df['date'].min(), df['date'].max()))
        selected_categories = st.multiselect("Filter by Category", options=CATEGORIES, default=CATEGORIES)
        if len(date_range) == 2:
            mask = (df['date'] >= pd.Timestamp(date_range[0])) & (df['date'] <= pd.Timestamp(date_range[1]))
            filtered_df = df[mask]
        else:
            filtered_df = df
        filtered_df = filtered_df[filtered_df['Category'].isin(selected_categories)]

        if filtered_df.empty:
            st.warning("No data available for the selected filters.")
        else:
            # Pie chart: Category-wise
            category_totals = filtered_df.groupby('Category')['Amount'].sum().reset_index()
            fig_pie = px.pie(category_totals, values='Amount', names='Category', title='Expenses by Category', hole=0.4)
            fig_pie.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig_pie, use_container_width=True)

            # Bar chart: Payment Method
            payment_totals = filtered_df.groupby('Payment_Method')['Amount'].sum().reset_index()
            fig_payment = px.bar(payment_totals, x='Payment_Method', y='Amount', title='Expenses by Payment Method',
                                 color='Amount', color_continuous_scale='Blues')
            st.plotly_chart(fig_payment, use_container_width=True)

            # Daily Trend
            daily_expenses = filtered_df.groupby('date')['Amount'].sum().reset_index()
            fig_line = px.line(daily_expenses, x='date', y='Amount', title='Daily Expense Trend', markers=True)
            st.plotly_chart(fig_line, use_container_width=True)



            # Monthly Summary
            st.subheader("📅 Monthly Summary")
            filtered_df['month'] = filtered_df['date'].dt.to_period('M')
            monthly_summary = filtered_df.groupby('month')['Amount'].agg(['sum', 'count', 'mean']).reset_index()
            monthly_summary['month'] = monthly_summary['month'].astype(str)
            monthly_summary.columns = ['Month', 'Total Spent', 'Transactions', 'Average']

            col1, col2 = st.columns(2)
            col1.dataframe(monthly_summary.style.format({'Total Spent': '₹{:,.2f}', 'Average': '₹{:,.2f}'}),
                           use_container_width=True, hide_index=True)

            fig_monthly = px.bar(monthly_summary, x='Month', y='Total Spent', title='Monthly Spending',
                                 text='Total Spent')
            fig_monthly.update_traces(texttemplate='₹%{text:,.0f}', textposition='outside')
            col2.plotly_chart(fig_monthly, use_container_width=True)

    # ---------------- Footer ----------------
    st.markdown("---")
