# crypto market analysis

a compact research workspace for studying the btc/sol relationship with daily binance us market data.

the repo currently holds the data layer and the first relative-spread analysis output. the next build step is a vectorized python backtesting framework for comparing directional, pairs, and buy-and-hold wallets.

## what's inside

| area | contents |
| --- | --- |
| `scripts/` | reproducible data download script |
| `data/raw/` | daily btc and sol ohlcv csv exports |
| `data/processed/` | data-only btc/sol relative-spread analysis |

## data

| field | value |
| --- | --- |
| source | binance us public klines api |
| symbols | `BTCUSDT`, `SOLUSDT` |
| interval | 1 day |
| range | `2025-05-15` to `2026-05-14` |
| observations | 366 rows per symbol |

tracked csv files:

- `data/raw/BTCUSDT_1d_binance_us_2025-05-15_2026-05-15.csv`
- `data/raw/SOLUSDT_1d_binance_us_2025-05-15_2026-05-15.csv`
- `data/processed/btc_sol_relative_spread_analysis_dataonly.csv`

generated workbook files are intentionally excluded from git.

## current analysis

the processed dataset is focused on btc/sol relative value:

- btc close
- sol close
- btc/sol ratio
- 30-day ratio moving average
- 30-day rolling standard deviation
- 30-day z-score
- simple signal column

## planned backtest

the next stage is a clean, vectorized backtester comparing five wallets:

- wallet_a: btc directional mean reversion
- wallet_b: btc/sol market-neutral pairs trading
- wallet_c: sol directional mean reversion
- wallet_hodl_btc: btc buy and hold
- wallet_hodl_sol: sol buy and hold

the strategy design will use next-day execution, shifted positions, transaction costs, equity curves, drawdowns, sharpe ratio, win rate, and matplotlib diagnostics.

## reproduce the raw data

from the repository root:

```bash
python3 scripts/download_binance_us_klines.py
```

the script writes symbol-level csv files into `data/raw/`.
