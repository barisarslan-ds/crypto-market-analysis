# crypto market analysis

a compact btc/sol market analysis project using daily binance us data.

the project packages the raw market data, processed relative-spread dataset, spreadsheet analysis outputs, and a reproducible downloader for rebuilding the source csv files.

## what's inside

| area | contents |
| --- | --- |
| `scripts/` | reproducible data download script |
| `data/raw/` | daily btc and sol ohlcv csv exports |
| `data/processed/` | btc/sol relative-spread csv and workbook outputs |

## data

| field | value |
| --- | --- |
| source | binance us public klines api |
| symbols | `BTCUSDT`, `SOLUSDT` |
| interval | 1 day |
| range | `2025-05-15` to `2026-05-14` |
| observations | 366 rows per symbol |

tracked data files:

- `data/raw/BTCUSDT_1d_binance_us_2025-05-15_2026-05-15.csv`
- `data/raw/SOLUSDT_1d_binance_us_2025-05-15_2026-05-15.csv`
- `data/processed/btc_sol_relative_spread_analysis_dataonly.csv`
- `data/processed/btc_sol_relative_spread_analysis.xlsx`
- `data/processed/btc_sol_relative_spread_analysis_dataonly.xlsx`

## analysis output

the processed files contain the completed btc/sol relative-value analysis:

- btc close
- sol close
- btc/sol ratio
- 30-day ratio moving average
- 30-day rolling standard deviation
- 30-day z-score
- simple signal column

## strategy scope

the research setup compares five wallet profiles:

- wallet_a: btc directional mean reversion
- wallet_b: btc/sol market-neutral pairs trading
- wallet_c: sol directional mean reversion
- wallet_hodl_btc: btc buy and hold
- wallet_hodl_sol: sol buy and hold

the strategy specification uses 30-day z-scores, t+1 execution, shifted positions, transaction costs, equity curves, drawdowns, sharpe ratio, win rate, and matplotlib diagnostics.

## reproduce the raw data

from the repository root:

```bash
python3 scripts/download_binance_us_klines.py
```

the script writes symbol-level csv files into `data/raw/`.
