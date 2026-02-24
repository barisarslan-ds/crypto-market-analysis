"""
Configuration settings for the Crypto Market Analysis project.
"""

# CoinGecko API Base URL
# Documentation: https://www.coingecko.com/en/api/documentation
COINGECKO_BASE_URL = "https://api.coingecko.com/api/v3"

# List of cons we want to analyze
COINS = ["bitcoin", "ethereum", "solana", "ripple", "cardano"]

# Timeframe for analysis
DAYS = "365"  # 1 year of data
CURRENCY = "usd"
