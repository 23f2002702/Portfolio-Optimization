# 📈 Portfolio Optimization App

This interactive Streamlit app helps you **optimize a stock portfolio** using historical data from Yahoo Finance.  
It uses **Sharpe Ratio maximization** and **Monte Carlo simulation** to find the optimal asset allocation for your selected stocks.

---

## 🚀 Features

- ✅ Select stocks from **S&P 500, Indian, UK, German, Japanese, and Global ETFs**
- 📅 Set custom **date ranges**
- 🧪 Choose between **log returns** or **percentage returns**
- 🧮 Generate thousands of **random portfolios**
- 🏆 Optimize the portfolio for **maximum Sharpe Ratio**
- 📊 Visualize:
  - Efficient Frontier
  - Cumulative Return of optimized portfolio
- 📥 Download optimized portfolio weights as **CSV**
- 🧠 Learn the concepts with tooltips and explanations

---

## 🧠 How It Works

### 📘 Step 1: Data Collection
- Historical **adjusted close prices** are downloaded via [Yahoo Finance](https://finance.yahoo.com/).
- Returns are computed (either **log** or **% change** based on user selection).

### 📘 Step 2: Random Portfolio Simulation
- `n` portfolios are randomly generated with different weights (normalized to sum to 1).
- For each portfolio, the following are computed:
  - **Expected annual return**
  - **Annualized volatility**
  - **Sharpe Ratio** (risk-adjusted return)

### 📘 Step 3: Optimization
- The portfolio with the **maximum Sharpe Ratio** is identified using:
  - **SciPy’s `minimize` function** with Sequential Least Squares (SLSQP) optimization.
  - **Constraints**: weights sum to 1; each weight between 0 and 1.

---

## 📊 Sample Visuals

- Efficient Frontier with color-coded Sharpe ratios
- Optimized portfolio location marked with 🔴 red star
- Cumulative returns of optimized portfolio over time

---

## 📦 Dependencies

Make sure to install the following Python packages:

```bash
pip install streamlit numpy pandas yfinance matplotlib scipy
```

---

## ⚠️ Disclaimer 
- This app is for educational and demonstration purposes only.
- Past performance is not indicative of future results.
- No financial advice is being given.

---
