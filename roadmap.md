# 🦅 Crypto Market Analysis Dashboard - Mentorship Roadmap

**Objective:** Master Python for Data Science (EDA, Pandas, Visualization) by building a real-world Crypto Dashboard.
**Timeline:** 4 Weeks
**Role:** Data Scientist (You) & Lead Mentor (Me)

---

## 📅 Week 1: The Data Pipeline & Pandas Basics
**Goal:** Build a robust data ingestion engine. Learn to handle APIs, JSON, and creates clean DataFrames.

### 🧠 Key Concepts to Master
- **APIs:** Requesting data, handling rate limits, understanding status codes (200 vs 429).
- **Pandas Core:** `DataFrame` vs `Series`, `read_json`, `to_csv`.
- **Data Types:** `datetime` objects vs strings, converting types.
- **Clean Code:** Writing functions with docstrings, not just scripts.

### 📝 Tasks
- [x] **Setup:** Initialize `venv`, install `pandas`, `requests`, `jupyter`.
- [x] **API Analysis:** Read CoinGecko API documentation. Identify endpoints for "Historical Data".
- [x] **Raw Data Fetcher:** Write a function `fetch_coin_data(coin_id, days)` that returns a list of prices.
- [x] **DataFrame Creation:** Convert that list into a Pandas DataFrame with proper columns (`timestamp`, `price`, `market_cap`).
- [x] **Data Validation:** Check for duplicates or missing timestamps immediately after fetching.
- [x] **Storage:** Save raw data to `data/raw/{coin}_raw.csv`.

---

## 📅 Week 2: Data Wrangling & Cleaning
**Goal:** Transform raw data into analytical gold. Master merging, resampling, and handling real-world messiness.

### 🧠 Key Concepts to Master
- **Indexing:** Setting `DatetimeIndex`. Why is it crucial for time-series?
- **Resampling:** Changing frequency (Daily -> Weekly) using `.resample()`. Aggregation methods (`mean` vs `last`).
- **Merging:** `pd.merge()` vs `pd.concat()`. Inner vs Outer joins. Aligining dates.
- **Missing Data:** Forward fill (`ffill`), backward fill, or interpolation.

### 📝 Tasks
- [x] **Loader Function:** Write `load_data(filepath)` that reads CSVs and parses dates automatically.
- [x] **Multi-Asset Merge:** Create a single DataFrame containing close prices for BTC, ETH, and SOL side-by-side.
- [x] **Sanity Check:** Detect outliers (e.g., price = 0 or sudden 500% spikes).
- [x] **Resampling:** Create a separate DataFrame for "Weekly Average Price".
- [x] **Feature Engineering:** Create simple new columns: `price_change` (difference from yesterday).

---

## 📅 Week 3: Statistical Analysis & Numpy
**Goal:** Uncover hidden patterns. Understand financial metrics and vectorization.

### 🧠 Key Concepts to Master
- **Returns:** Simple Returns vs Log Returns. Why do financial analysts prefer Log Returns?
- **Volatility:** Standard Deviation (`std`) and Rolling Windows.
- **Correlation:** Pearson correlation coefficient. What does 0.8 correlation mean?
- **Vectorization:** Avoiding `for` loops. Using columns operations for speed.

### 📝 Tasks
- [x] **Daily Returns:** Calculate `pct_change()` for all coins.
- [ ] **Rolling Stats:** Calculate the 30-day Moving Average (SMA) and Rolling Volatility.
- [x] **Correlation Matrix:** Compute how much ETH moves when BTC moves.
- [ ] **Aggregate Metrics:** Calculate "Max Drawdown" (largest drop from peak) for each coin.

---

## 📅 Week 4: Visualization & Storytelling
**Goal:** Present findings professionally. Don't just show data; tell a story.

### 🧠 Key Concepts to Master
- **Matplotlib vs Seaborn:** When to use which? (Customization vs Aesthetics).
- **Plot Components:** Titles, Labels, Legends, Gridlines.
- **Types of Plots:** Line (trends), Histogram (distributions/risk), Heatmap (correlations).
- **Subplots:** showing multiple charts in one figure.

### 📝 Tasks
- [ ] **Trend Analysis:** Plot Price vs. 30-day SMA. Highlight "Golden Cross" events.
- [ ] **Risk Analysis:** Plot the distribution of Daily Returns. Is it Normal (Gaussian)?
- [ ] **Market structure:** Create a Heatmap of the Correlation Matrix.
- [ ] **Final Dashboard:** Combine these into a clean Jupyter Notebook report with markdown commentary explaining the market state.

---

## 🛠 Project Structure Rules
1. **No Hardcoding:** Paths should be relative or defined in a config.
2. **Modular Functions:** Code goes in `src/`, Notebooks import from `src/`.
3. **Commit Often:** Use meaningful commit messages.

## 🚀 Ready to start?
Your first assignment is in **Week 1: Setup**.
Let me know when you have created your virtual environment!
