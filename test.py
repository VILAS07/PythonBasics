import streamlit as st

import streamlit as st

import streamlit as st

# Configure Streamlit page
st.set_page_config(page_title="Expense Tracker", layout="wide")

# Glassmorphic Expense Tracker UI
html_code = """
<!DOCTYPE html>
<html>
<head>
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

.expense-tracker-container {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #4facfe 75%, #00f2fe 100%);
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite;
    padding: 40px 20px;
    min-height: 100vh;
    position: relative;
    overflow: hidden;
}

.expense-tracker-container::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320"><path fill="%23ffffff" fill-opacity="0.05" d="M0,96L48,112C96,128,192,160,288,160C384,160,480,128,576,112C672,96,768,96,864,112C960,128,1056,160,1152,160C1248,160,1344,128,1392,112L1440,96L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"></path></svg>');
    background-size: cover;
    pointer-events: none;
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.header {
    text-align: center;
    color: white;
    margin-bottom: 40px;
    animation: fadeInUp 0.8s ease;
}

.header h1 {
    font-size: 3em;
    font-weight: 700;
    text-shadow: 0 4px 15px rgba(0,0,0,0.2);
    margin-bottom: 10px;
}

.header p {
    font-size: 1.2em;
    font-weight: 300;
    opacity: 0.9;
}

.glass-card {
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.3);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    padding: 25px;
    margin-bottom: 20px;
    transition: all 0.3s ease-in-out;
    animation: fadeInUp 0.8s ease;
    position: relative;
    overflow: hidden;
}

.glass-card::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
    opacity: 0;
    transition: opacity 0.3s ease;
}

.glass-card:hover::before {
    opacity: 1;
}

.glass-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.2);
    border-color: rgba(255, 255, 255, 0.5);
}

.float-card {
    animation: float 3s ease-in-out infinite;
}

.dashboard-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
    margin-bottom: 30px;
}

.stat-card {
    text-align: center;
    color: white;
    animation-delay: 0.2s;
}

.stat-card:nth-child(2) {
    animation-delay: 0.4s;
}

.stat-card:nth-child(3) {
    animation-delay: 0.6s;
}

.stat-icon {
    font-size: 2.5em;
    margin-bottom: 15px;
    filter: drop-shadow(0 4px 8px rgba(0,0,0,0.2));
}

.stat-value {
    font-size: 2.5em;
    font-weight: 700;
    margin: 10px 0;
    text-shadow: 0 2px 10px rgba(0,0,0,0.2);
}

.stat-label {
    font-size: 1em;
    font-weight: 400;
    opacity: 0.9;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.form-container {
    animation-delay: 0.8s;
}

.form-group {
    margin-bottom: 20px;
}

.form-label {
    display: block;
    color: white;
    font-weight: 500;
    margin-bottom: 8px;
    font-size: 0.95em;
    text-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.glass-input {
    width: 100%;
    padding: 14px 18px;
    background: rgba(255, 255, 255, 0.2);
    border: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: 12px;
    color: white;
    font-size: 1em;
    font-family: 'Poppins', sans-serif;
    transition: all 0.3s ease;
    outline: none;
}

.glass-input::placeholder {
    color: rgba(255, 255, 255, 0.6);
}

.glass-input:focus {
    background: rgba(255, 255, 255, 0.25);
    box-shadow: 0 0 15px rgba(255, 255, 255, 0.6);
    border-color: rgba(255, 255, 255, 0.6);
    transform: scale(1.02);
}

.glass-input:hover {
    border-color: rgba(255, 255, 255, 0.5);
}

.glass-button {
    width: 100%;
    padding: 16px;
    background: rgba(255, 255, 255, 0.25);
    border: 1px solid rgba(255, 255, 255, 0.4);
    border-radius: 12px;
    color: white;
    font-size: 1.1em;
    font-weight: 600;
    font-family: 'Poppins', sans-serif;
    cursor: pointer;
    transition: all 0.3s ease;
    text-transform: uppercase;
    letter-spacing: 1px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.glass-button:hover {
    transform: scale(1.05);
    background: rgba(255, 255, 255, 0.35);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
    border-color: rgba(255, 255, 255, 0.6);
}

.glass-button:active {
    transform: scale(0.98);
}

.table-container {
    animation-delay: 1s;
    overflow-x: auto;
}

.glass-table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0 10px;
}

.glass-table thead th {
    color: white;
    font-weight: 600;
    text-align: left;
    padding: 15px;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-size: 0.9em;
    text-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.glass-table tbody tr {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    transition: all 0.3s ease;
}

.glass-table tbody tr:hover {
    background: rgba(255, 255, 255, 0.2);
    transform: scale(1.02);
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
}

.glass-table tbody td {
    padding: 18px 15px;
    color: white;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.glass-table tbody td:first-child {
    border-left: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px 0 0 12px;
}

.glass-table tbody td:last-child {
    border-right: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 0 12px 12px 0;
}

.category-badge {
    display: inline-block;
    padding: 6px 14px;
    background: rgba(255, 255, 255, 0.2);
    border-radius: 20px;
    font-size: 0.85em;
    font-weight: 500;
    backdrop-filter: blur(5px);
}

.delete-btn {
    padding: 8px 16px;
    background: rgba(255, 100, 100, 0.3);
    border: 1px solid rgba(255, 100, 100, 0.5);
    border-radius: 8px;
    color: white;
    font-size: 0.9em;
    cursor: pointer;
    transition: all 0.3s ease;
    font-family: 'Poppins', sans-serif;
}

.delete-btn:hover {
    background: rgba(255, 100, 100, 0.5);
    transform: scale(1.1);
    box-shadow: 0 4px 12px rgba(255, 100, 100, 0.4);
}

@media (max-width: 768px) {
    .header h1 {
        font-size: 2em;
    }

    .dashboard-grid {
        grid-template-columns: 1fr;
    }

    .stat-value {
        font-size: 2em;
    }
}
</style>
</head>
<body>
<div class="expense-tracker-container">
    <div class="header">
        <h1>💸 Expense Tracker</h1>
        <p>Track your spending with style</p>
    </div>

    <div class="dashboard-grid">
        <div class="glass-card stat-card float-card">
            <div class="stat-icon">💰</div>
            <div class="stat-value">$2,450</div>
            <div class="stat-label">Total Expenses</div>
        </div>

        <div class="glass-card stat-card float-card">
            <div class="stat-icon">📊</div>
            <div class="stat-value">$5,000</div>
            <div class="stat-label">Monthly Budget</div>
        </div>

        <div class="glass-card stat-card float-card">
            <div class="stat-icon">🎯</div>
            <div class="stat-value">$2,550</div>
            <div class="stat-label">Savings</div>
        </div>
    </div>

    <div class="glass-card form-container">
        <h2 style="color: white; margin-bottom: 25px; font-size: 1.8em;">Add New Expense</h2>

        <div class="form-group">
            <label class="form-label">Expense Name</label>
            <input type="text" class="glass-input" placeholder="e.g., Grocery Shopping">
        </div>

        <div class="form-group">
            <label class="form-label">Amount ($)</label>
            <input type="number" class="glass-input" placeholder="0.00">
        </div>

        <div class="form-group">
            <label class="form-label">Category</label>
            <input type="text" class="glass-input" placeholder="e.g., Food, Transport, Entertainment">
        </div>

        <div class="form-group">
            <label class="form-label">Date</label>
            <input type="date" class="glass-input">
        </div>

        <button class="glass-button">Add Expense</button>
    </div>

    <div class="glass-card table-container">
        <h2 style="color: white; margin-bottom: 25px; font-size: 1.8em;">Recent Transactions</h2>

        <table class="glass-table">
            <thead>
                <tr>
                    <th>Date</th>
                    <th>Description</th>
                    <th>Category</th>
                    <th>Amount</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Nov 30</td>
                    <td>Grocery Shopping</td>
                    <td><span class="category-badge">🍕 Food</span></td>
                    <td>$125.50</td>
                    <td><button class="delete-btn">Delete</button></td>
                </tr>
                <tr>
                    <td>Nov 29</td>
                    <td>Gas Station</td>
                    <td><span class="category-badge">🚗 Transport</span></td>
                    <td>$45.00</td>
                    <td><button class="delete-btn">Delete</button></td>
                </tr>
                <tr>
                    <td>Nov 28</td>
                    <td>Netflix Subscription</td>
                    <td><span class="category-badge">🎬 Entertainment</span></td>
                    <td>$15.99</td>
                    <td><button class="delete-btn">Delete</button></td>
                </tr>
                <tr>
                    <td>Nov 27</td>
                    <td>Coffee Shop</td>
                    <td><span class="category-badge">☕ Food</span></td>
                    <td>$8.50</td>
                    <td><button class="delete-btn">Delete</button></td>
                </tr>
            </tbody>
        </table>
    </div>
</body>
</html>
"""

# Display using components.html for better rendering
import streamlit.components.v1 as components

components.html(html_code, height=1400, scrolling=True)