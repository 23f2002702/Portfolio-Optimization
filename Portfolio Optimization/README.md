# 📈 Portfolio Optimization App

This Streamlit app allows you to construct and optimize a stock portfolio using historical price data. It finds the **Sharpe-optimal portfolio** using **random sampling** and **numerical optimization**, and provides interactive charts and performance metrics.

---

## 🚀 Features

- 📅 Select any combination of stocks (AAPL, GOOGL, META, etc.)
- 📈 Optimize based on **Sharpe Ratio** using historical data
- 📊 Visualize the **Efficient Frontier**
- 🔁 Choose **log returns** or **simple % returns**
- 🔐 Set a custom **risk-free rate**
- 🧮 View **optimized weights**, **cumulative return**, and **metrics**
- 📥 Export portfolio weights as CSV
- ℹ️ Full in-app explanation of logic, assumptions, and methodology

---

## 🧠 How It Works

1. Historical stock prices are pulled using `yfinance`.
2. Returns are calculated (log or percent).
3. Thousands of random portfolios are generated.
4. Sharpe Ratios are calculated for each.
5. The portfolio with the highest Sharpe Ratio is optimized using `scipy.optimize`.

---

## 📦 Installation

```bash
# Step 1: Clone the repo
git clone https://github.com/your-username/portfolio-optimizer.git
cd portfolio-optimizer

# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Run the app
streamlit run your_app_file.py
