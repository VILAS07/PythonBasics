import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json

# Page configuration
st.set_page_config(page_title="Expense Tracker", page_icon="💰", layout="wide")

# Initialize session state for expenses
if 'expenses' not in st.session_state:
    st.session_state.expenses = []

# Categories for expenses
CATEGORIES = [
    "Food & Dining", "Transportation", "Shopping", "Entertainment",
    "Bills & Utilities", "Healthcare", "Education", "Travel",
    "Groceries", "Others"
]

# Payment methods
PAYMENT_METHODS = ["Cash", "Credit Card", "Debit Card", "UPI", "Net Banking"]


# Helper functions
def add_expense(date, category, amount, description, payment_method):
    expense = {
        "date": date.strftime("%Y-%m-%d"),
        "category": category,
        "amount": float(amount),
        "description": description,
        "payment_method": payment_method
    }
    st.session_state.expenses.append(expense)


def get_expenses_df():
    if st.session_state.expenses:
        df = pd.DataFrame(st.session_state.expenses)
        df['date'] = pd.to_datetime(df['date'])
        return df
    return pd.DataFrame()


# App title
st.title("💰 Personal Expense Tracker")
st.markdown("---")

# Sidebar for adding expenses
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
            if exp_amount > 0:
                add_expense(exp_date, exp_category, exp_amount, exp_description, exp_payment)
                st.success("Expense added successfully!")
                st.rerun()
            else:
                st.error("Please enter a valid amount")

    st.markdown("---")

    # Data management
    st.subheader("Data Management")

    if st.button("Clear All Data"):
        st.session_state.expenses = []
        st.rerun()

    # Download data
    if st.session_state.expenses:
        df = get_expenses_df()
        csv = df.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name=f"expenses_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )

# Main content
df = get_expenses_df()

if df.empty:
    st.info("👋 Welcome! Start by adding your first expense using the form on the left.")
else:
    # Summary metrics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Expenses", f"₹{df['amount'].sum():,.2f}")

    with col2:
        st.metric("Average Expense", f"₹{df['amount'].mean():,.2f}")

    with col3:
        st.metric("Total Transactions", len(df))

    with col4:
        top_category = df.groupby('category')['amount'].sum().idxmax()
        st.metric("Top Category", top_category)

    st.markdown("---")

    # Filters
    st.subheader("📊 Expense Analytics")

    col1, col2 = st.columns(2)
    with col1:
        date_range = st.date_input(
            "Select Date Range",
            value=(df['date'].min(), df['date'].max()),
            key="date_range"
        )

    with col2:
        selected_categories = st.multiselect(
            "Filter by Category",
            options=CATEGORIES,
            default=CATEGORIES
        )

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
        # Visualizations
        col1, col2 = st.columns(2)

        with col1:
            # Category-wise expenses (Pie chart)
            category_totals = filtered_df.groupby('category')['amount'].sum().reset_index()
            fig_pie = px.pie(
                category_totals,
                values='amount',
                names='category',
                title='Expenses by Category',
                hole=0.4
            )
            fig_pie.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig_pie, use_container_width=True)

        with col2:
            # Payment method distribution
            payment_totals = filtered_df.groupby('payment_method')['amount'].sum().reset_index()
            fig_payment = px.bar(
                payment_totals,
                x='payment_method',
                y='amount',
                title='Expenses by Payment Method',
                color='amount',
                color_continuous_scale='Blues'
            )
            st.plotly_chart(fig_payment, use_container_width=True)

        # Daily expenses trend
        daily_expenses = filtered_df.groupby('date')['amount'].sum().reset_index()
        fig_line = px.line(
            daily_expenses,
            x='date',
            y='amount',
            title='Daily Expense Trend',
            markers=True
        )
        fig_line.update_layout(xaxis_title="Date", yaxis_title="Amount (₹)")
        st.plotly_chart(fig_line, use_container_width=True)

        # Category breakdown over time
        category_timeline = filtered_df.groupby(['date', 'category'])['amount'].sum().reset_index()
        fig_area = px.area(
            category_timeline,
            x='date',
            y='amount',
            color='category',
            title='Category-wise Expense Timeline'
        )
        st.plotly_chart(fig_area, use_container_width=True)

        st.markdown("---")

        # Recent transactions table
        st.subheader("📝 Recent Transactions")

        display_df = filtered_df.sort_values('date', ascending=False).copy()
        display_df['date'] = display_df['date'].dt.strftime('%Y-%m-%d')
        display_df['amount'] = display_df['amount'].apply(lambda x: f"₹{x:,.2f}")

        st.dataframe(
            display_df[['date', 'category', 'amount', 'description', 'payment_method']],
            use_container_width=True,
            hide_index=True
        )

        # Monthly summary
        st.markdown("---")
        st.subheader("📅 Monthly Summary")

        filtered_df['month'] = filtered_df['date'].dt.to_period('M')
        monthly_summary = filtered_df.groupby('month')['amount'].agg(['sum', 'count', 'mean']).reset_index()
        monthly_summary['month'] = monthly_summary['month'].astype(str)
        monthly_summary.columns = ['Month', 'Total Spent', 'Transactions', 'Average']

        col1, col2 = st.columns(2)

        with col1:
            st.dataframe(
                monthly_summary.style.format({
                    'Total Spent': '₹{:,.2f}',
                    'Average': '₹{:,.2f}'
                }),
                use_container_width=True,
                hide_index=True
            )

        with col2:
            fig_monthly = px.bar(
                monthly_summary,
                x='Month',
                y='Total Spent',
                title='Monthly Spending',
                text='Total Spent'
            )
            fig_monthly.update_traces(texttemplate='₹%{text:,.0f}', textposition='outside')
            st.plotly_chart(fig_monthly, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("💡 **Tip:** Use the sidebar to add expenses and manage your data!")