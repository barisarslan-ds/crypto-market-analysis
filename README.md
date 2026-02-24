# 🦅 Crypto Market Analysis Dashboard

## 📌 Project Overview
The **Crypto Market Analysis Dashboard** is an end-to-end data science project built from scratch to analyze the historical market behavior of major cryptocurrencies (Bitcoin, Ethereum, Solana, Ripple, Cardano). 

This project demonstrates the complete data pipeline: from fetching raw data via REST APIs, to performing complex data wrangling, and executing statistical financial analysis.

## 💼 Skills & Technologies Demonstrated
- **Languages:** Python
- **Libraries:** Pandas, NumPy, Requests, Matplotlib, Seaborn
- **Data Engineering:** REST API integrations (CoinGecko), JSON parsing, automated data pipelines.
- **Data Wrangling (ETL):** Time-series alignment, handling missing data (NaN) via forward-fill techniques, resampling frequencies (Daily to Weekly), and feature engineering (calculating absolute/percentage price changes).
- **Statistical Analysis:** Volatility calculation (Standard Deviation), moving averages (Rolling Windows), and Correlation Matrix generation to identify asset interdependencies.

## 📂 Project Structure
```text
├── data/
│   ├── raw/               # Raw JSON/CSV data fetched from APIs
│   ├── processed/         # Cleaned, merged, and wrangled datasets
├── notebooks/             # Jupyter notebooks for Exploratory Data Analysis (EDA)
├── src/                   # Core Python scripts
│   ├── config.py             # Project configuration and constants
│   ├── data_loader.py        # API interaction and data loading
│   ├── fetch_data.py         # Automated data ingestion script
│   ├── process_data.py       # Multi-asset data merging and alignment
│   ├── clean_data.py         # Missing data handling and imputation
│   ├── feature_engineering.py# New feature creation (e.g., price differences)
│   ├── resample_data.py      # Time-series resampling (Daily to Weekly)
│   ├── correlation.py        # Statistical correlation analysis and heatmaps
│   └── analysis.py           # Returns and volatility calculations
├── roadmap.md             # Detailed 4-week project learning roadmap
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

## 🚀 Key Insights (In Progress)
- **High Market Correlation:** Initial correlation analysis reveals a strong positive correlation (>0.80) between Bitcoin, Ethereum, and Solana, indicating highly coupled market movements.
- **Volatility Tracking:** Calculated historical daily percentage returns to dynamically track asset volatility.

## ⚙️ How to Run
1. Clone the repository: `git clone https://github.com/your-username/crypto-market-analysis.git`
2. Create a virtual environment: `python -m venv .venv`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the data pipeline:
   ```bash
   python -m src.fetch_data
   python -m src.process_data
   python -m src.clean_data
   python -m src.feature_engineering
   python -m src.resample_data
   python -m src.analysis
   python -m src.correlation
   ```

*Note: This project is currently in Week 3 of a 4-week development roadmap.*
