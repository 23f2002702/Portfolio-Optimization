# 📊 Portfolio Optimization using Modern Portfolio Theory (MPT)

This project uses **Modern Portfolio Theory (MPT)** to construct, analyze, and optimize stock portfolios using real stock data. It includes enhancements such as Monte Carlo simulation, Sharpe Ratio maximization, log returns, risk metrics (VaR, CVaR), rebalancing strategies, and Capital Market Line (CML) analysis.

---

## 🚀 Features

- ✅ Historical data download via `yfinance`
- ✅ Random portfolio generation
- ✅ Sharpe Ratio maximization using `scipy.optimize`
- ✅ Efficient Frontier visualization
- ✅ Monte Carlo simulation with 5000+ portfolios
- ✅ Capital Market Line (CML) and Tangency Portfolio
- ✅ Real-world risk metrics:  
  - Alpha, Beta  
  - Max Drawdown  
  - Sortino Ratio  
  - VaR (Value at Risk)  
  - CVaR (Expected Shortfall)
- ✅ Monthly rebalancing vs. buy-and-hold strategy comparison
- ✅ Covariance shrinkage using Ledoit-Wolf estimator
- ✅ Benchmarking vs. S&P 500 (SPY)

---

## 🧪 Requirements

Install the required Python libraries:

```bash
pip install -r requirements.txt
