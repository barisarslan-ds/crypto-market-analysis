# Crypto Market Analysis

Simple BTC/SOL market-analysis workspace using Binance US daily price data.

## Summary

This repository currently contains a reproducible data download script and prepared BTC/SOL relative-spread analysis files. The active vectorized backtesting framework is not included yet; this repo is the data and analysis foundation for that next step.

## Dataset

- Source: Binance US public klines API
- Symbols: `BTCUSDT`, `SOLUSDT`
- Interval: 1 day
- Date range: `2025-05-15` through `2026-05-14`
- Raw rows: 366 daily observations per symbol

Included CSV files:

- `data/raw/BTCUSDT_1d_binance_us_2025-05-15_2026-05-15.csv`
- `data/raw/SOLUSDT_1d_binance_us_2025-05-15_2026-05-15.csv`
- `data/processed/btc_sol_relative_spread_analysis_dataonly.csv`

Generated workbook outputs are intentionally excluded from git.

## Project Files

- `scripts/download_binance_us_klines.py`: downloads BTC and SOL daily klines from Binance US and writes raw CSV files.
- `data/raw/`: raw OHLCV data exported by symbol.
- `data/processed/`: processed BTC/SOL relative-spread analysis data.

## Analysis Purpose

The processed dataset supports BTC/SOL relative-value research, including the BTC/SOL close-price ratio, a 30-day moving average, rolling standard deviation, and 30-day Z-score. The next planned project step is a clean, vectorized Python backtesting framework comparing:

- BTC directional mean-reversion wallet
- BTC/SOL market-neutral pairs wallet
- SOL directional mean-reversion wallet
- BTC buy-and-hold benchmark
- SOL buy-and-hold benchmark

## Reproducibility

Run the downloader from the repository root:

```bash
python3 scripts/download_binance_us_klines.py
```

The script writes raw CSV files to `data/raw/`.

## Current Status

This is an initial repository upload containing the data source script, raw CSV exports, and data-only processed analysis output. The production-grade backtesting modules, risk metrics, and visualization layer are planned but not yet implemented.
