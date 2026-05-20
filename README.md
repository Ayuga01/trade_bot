# Binance Futures Testnet Trading Bot

A simple Python CLI bot for placing `MARKET` and `LIMIT` orders on Binance
Futures Testnet.

It uses `python-binance`, keeps the code split into small modules, and writes
order activity to log files.

## What It Does

- Places `MARKET` and `LIMIT` orders
- Supports `BUY` and `SELL`
- Takes input from the command line
- Validates basic inputs before sending an order
- Prints the order summary and response
- Logs requests, responses, and errors

## Setup

Install dependencies with `uv`:

```bash
uv sync
```

Create a `.env` file in the project root:

```env
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
```

Use API keys from Binance Futures Testnet, not a live Binance account.

## Run

Market order:

```bash
uv run cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

Limit order:

```bash
uv run cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 150000
```

## CLI Options

| Option | Description |
| --- | --- |
| `--symbol` | Trading pair, like `BTCUSDT` |
| `--side` | `BUY` or `SELL` |
| `--type` | `MARKET` or `LIMIT` |
| `--quantity` | Order quantity |
| `--price` | Required for `LIMIT` orders |

## Example Output

```text
=== ORDER REQUEST SUMMARY ===
Symbol     : BTCUSDT
Side       : BUY
Order Type : MARKET
Quantity   : 0.001

=== ORDER RESPONSE ===
Order ID     : 13167300006
Status       : FILLED
Executed Qty : 0.0010
Avg Price    : 77539.500000

Order placed successfully.
```

## Logs

Logs are saved in the `logs/` folder:

- `logs/market_orders.log`
- `logs/limit_orders.log`

## Project Structure

```text
bot/
  client.py          # Binance client setup
  orders.py          # order placement logic
  validators.py      # input validation
  logging_config.py  # log file setup
cli.py               # command line entry point
```

## Notes

- This project is only for Binance Futures Testnet.
- Market orders usually fill right away.
- Limit orders may stay open if the price is not reached.
- This is a demo/assignment project, not a production trading bot.
