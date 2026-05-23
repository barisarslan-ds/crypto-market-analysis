from __future__ import annotations

import csv
import json
import logging
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import UTC, date, datetime
from pathlib import Path
from typing import Any, TypedDict, cast


class DownloadError(RuntimeError):
    pass


class KlineRow(TypedDict):
    Date: str
    Symbol: str
    OpenTimeUTC: str
    Open: str
    High: str
    Low: str
    Close: str
    Volume: str
    CloseTimeUTC: str
    QuoteVolume: str
    NumberOfTrades: int


LOGGER: logging.Logger = logging.getLogger("download_binance_us_klines")
API_BASE_URL: str = "https://api.binance.us/api/v3/klines"
OUTPUT_DIR: Path = Path("data/raw")
START_DATE: date = date(2025, 5, 15)
END_DATE_EXCLUSIVE: date = date(2026, 5, 15)
SYMBOLS: tuple[str, ...] = ("BTCUSDT", "SOLUSDT")
CSV_FIELDS: tuple[str, ...] = (
    "Date",
    "Symbol",
    "OpenTimeUTC",
    "Open",
    "High",
    "Low",
    "Close",
    "Volume",
    "CloseTimeUTC",
    "QuoteVolume",
    "NumberOfTrades",
)


def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s %(name)s %(message)s",
    )


def to_epoch_milliseconds(value: date) -> int:
    midnight_utc: datetime = datetime(value.year, value.month, value.day, tzinfo=UTC)
    return int(midnight_utc.timestamp() * 1000)


def build_url(symbol: str, start_date: date, end_date_exclusive: date) -> str:
    params: dict[str, str] = {
        "symbol": symbol,
        "interval": "1d",
        "startTime": str(to_epoch_milliseconds(start_date)),
        "endTime": str(to_epoch_milliseconds(end_date_exclusive)),
        "limit": "1000",
    }
    return f"{API_BASE_URL}?{urllib.parse.urlencode(params)}"


def read_url(url: str) -> bytes:
    request: urllib.request.Request = urllib.request.Request(
        url,
        headers={"User-Agent": "excel-analysis-learning-project/1.0"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        status_code: int = response.status
        response_body: bytes = response.read()
    if status_code != 200:
        raise DownloadError(f"Unexpected status code {status_code} for url={url}")
    return response_body


def fetch_with_retries(url: str, attempt_count: int, wait_seconds: float) -> list[list[Any]]:
    last_error: urllib.error.URLError | urllib.error.HTTPError | json.JSONDecodeError | DownloadError | None = None
    for attempt_index in range(1, attempt_count + 1):
        try:
            response_body: bytes = read_url(url)
            parsed_json: Any = json.loads(response_body.decode("utf-8"))
            if not isinstance(parsed_json, list):
                raise DownloadError(f"Expected list response for url={url}; response_body={response_body[:500]!r}")
            return cast(list[list[Any]], parsed_json)
        except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError, DownloadError) as error:
            last_error = error
            LOGGER.warning(
                "download_attempt_failed",
                extra={"attempt": attempt_index, "attempt_count": attempt_count, "url": url, "error": repr(error)},
            )
            if attempt_index < attempt_count:
                time.sleep(wait_seconds)
    raise DownloadError(f"Download failed after {attempt_count} attempts for url={url}") from last_error


def milliseconds_to_iso(value: int) -> str:
    return datetime.fromtimestamp(value / 1000, tz=UTC).isoformat().replace("+00:00", "Z")


def kline_to_row(symbol: str, kline: list[Any]) -> KlineRow:
    if len(kline) < 9:
        raise DownloadError(f"Malformed kline for symbol={symbol}; kline={kline!r}")

    open_time_ms: int = int(kline[0])
    close_time_ms: int = int(kline[6])
    open_time: datetime = datetime.fromtimestamp(open_time_ms / 1000, tz=UTC)

    return {
        "Date": open_time.date().isoformat(),
        "Symbol": symbol,
        "OpenTimeUTC": milliseconds_to_iso(open_time_ms),
        "Open": str(kline[1]),
        "High": str(kline[2]),
        "Low": str(kline[3]),
        "Close": str(kline[4]),
        "Volume": str(kline[5]),
        "CloseTimeUTC": milliseconds_to_iso(close_time_ms),
        "QuoteVolume": str(kline[7]),
        "NumberOfTrades": int(kline[8]),
    }


def fetch_symbol_rows(symbol: str, start_date: date, end_date_exclusive: date) -> list[KlineRow]:
    url: str = build_url(symbol, start_date, end_date_exclusive)
    klines: list[list[Any]] = fetch_with_retries(url, 3, 2.0)
    rows: list[KlineRow] = [kline_to_row(symbol, kline) for kline in klines]
    if not rows:
        raise DownloadError(f"No kline rows returned for symbol={symbol}; url={url}")
    return rows


def write_csv(output_path: Path, rows: list[KlineRow]) -> None:
    with output_path.open("w", newline="", encoding="utf-8") as output_file:
        writer: csv.DictWriter[str] = csv.DictWriter(output_file, fieldnames=list(CSV_FIELDS))
        writer.writeheader()
        writer.writerows(rows)


def download_symbol(symbol: str, start_date: date, end_date_exclusive: date, output_dir: Path) -> Path:
    rows: list[KlineRow] = fetch_symbol_rows(symbol, start_date, end_date_exclusive)
    output_path: Path = output_dir / f"{symbol}_1d_binance_us_{start_date.isoformat()}_{end_date_exclusive.isoformat()}.csv"
    write_csv(output_path, rows)
    LOGGER.info(
        "csv_written",
        extra={"symbol": symbol, "row_count": len(rows), "output_path": str(output_path)},
    )
    return output_path


def main() -> None:
    configure_logging()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for symbol in SYMBOLS:
        download_symbol(symbol, START_DATE, END_DATE_EXCLUSIVE, OUTPUT_DIR)


if __name__ == "__main__":
    main()
