import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime
from scipy.optimize import minimize

st.set_page_config(page_title="Portfolio Optimizer", layout="wide")

# ----------------------------
# Sidebar Inputs
# ----------------------------
st.sidebar.header("Portfolio Configuration")

stock_list = ['AAPL', 'GOOGL', 'META', 'AMZN', 'MSFT', 'TSLA', 'NFLX', 'NVDA', 'JPM', 'UNH']
selected_stocks = st.sidebar.multiselect("Select Stocks", stock_list, default=['AAPL', 'GOOGL', 'META', 'AMZN', 'MSFT'])
start_date = st.sidebar.date_input("Start Date", datetime(2020, 1, 1))
end_date = st.sidebar.date_input("End Date", datetime.today())
num_random = st.sidebar.slider("Number of Random Portfolios", 2, 10000, 500)

# ----------------------------
# Load Data
# ----------------------------
@st.cache_data
def load_data(tickers, start, end):
    data = yf.download(tickers, start=start, end=end,auto_adjust=False)['Adj Close']
    return data

if len(selected_stocks) < 2:
    st.warning("Please select at least two stocks.")
    st.stop()

data = load_data(selected_stocks, start_date, end_date)
returns = data.pct_change().dropna()

# ----------------------------
# Portfolio Performance
# ----------------------------
def portfolio_perf(weights, mean_returns, cov_matrix):
    ret = np.dot(weights, mean_returns) * 252
    vol = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))) * np.sqrt(252)
    sharpe = ret / vol
    return ret, vol, sharpe

# ----------------------------
# Generate Random Portfolios
# ----------------------------
mean_returns = returns.mean()
cov_matrix = returns.cov()
results = {'Return': [], 'Volatility': [], 'Sharpe': [], 'Weights': []}

for i in range(num_random):
    w = np.random.random(len(selected_stocks))
    w /= np.sum(w)
    ret, vol, sharpe = portfolio_perf(w, mean_returns, cov_matrix)
    results['Return'].append(ret)
    results['Volatility'].append(vol)
    results['Sharpe'].append(sharpe)
    results['Weights'].append(w)

df_results = pd.DataFrame(results)

# ----------------------------
# Optimize Portfolio (Max Sharpe)
# ----------------------------
def neg_sharpe(weights, mean_returns, cov_matrix):
    return -portfolio_perf(weights, mean_returns, cov_matrix)[2]

bounds = tuple((0, 1) for _ in range(len(selected_stocks)))
constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
init_guess = len(selected_stocks) * [1. / len(selected_stocks)]

opt_result = minimize(neg_sharpe, init_guess, args=(mean_returns, cov_matrix),
                      method='SLSQP', bounds=bounds, constraints=constraints)

opt_weights = opt_result.x
opt_ret, opt_vol, opt_sharpe = portfolio_perf(opt_weights, mean_returns, cov_matrix)

# ----------------------------
# Display Output
# ----------------------------
st.title("📈 Portfolio Optimization App")

col1, col2 = st.columns(2)
col1.metric("Optimized Return", f"{opt_ret:.2%}")
col2.metric("Optimized Volatility", f"{opt_vol:.2%}")
st.metric("Optimized Sharpe Ratio", f"{opt_sharpe:.2f}")

st.subheader("Optimized Portfolio Weights")
opt_df = pd.DataFrame({'Stock': selected_stocks, 'Weight': np.round(opt_weights, 4)})
st.dataframe(opt_df)

# ----------------------------
# Plot Efficient Frontier
# ----------------------------
st.subheader("Efficient Frontier")

fig, ax = plt.subplots(figsize=(10, 6))
sc = ax.scatter(df_results['Volatility'], df_results['Return'], c=df_results['Sharpe'], cmap='viridis', alpha=0.5)
ax.scatter(opt_vol, opt_ret, color='red', marker='*', s=200, label='Optimized')
plt.colorbar(sc, label='Sharpe Ratio')
ax.set_xlabel('Volatility (Risk)')
ax.set_ylabel('Expected Return')
ax.set_title('Portfolio Efficient Frontier')
ax.legend()
st.pyplot(fig)
