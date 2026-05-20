import argparse

from bot.client import BinanceFuturesClient
from bot.orders import OrderService
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)



def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading symbol, e.g. BTCUSDT"
    )

    parser.add_argument(
        "--side",
        required=True,
        help="BUY or SELL"
    )

    parser.add_argument(
        "--type",
        required=True,
        help="MARKET or LIMIT"
    )

    parser.add_argument(
        "--quantity",
        required=True,
        type=float,
        help="Order quantity"
    )

    parser.add_argument(
        "--price",
        type=float,
        help="Required for LIMIT orders"
    )

    return parser.parse_args()



def main():
    try:
        args = parse_arguments()

        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price, order_type)

        print("\n=== ORDER REQUEST SUMMARY ===")
        print(f"Symbol     : {args.symbol.upper()}")
        print(f"Side       : {side}")
        print(f"Order Type : {order_type}")
        print(f"Quantity   : {quantity}")

        if price:
            print(f"Price      : {price}")

        client = BinanceFuturesClient().get_client()

        order_service = OrderService(client)

        response = order_service.place_order(
            symbol=args.symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        print("\n=== ORDER RESPONSE ===")
        print(f"Order ID     : {response.get('orderId')}")
        print(f"Status       : {response.get('status')}")
        print(f"Executed Qty : {response.get('executedQty')}")
        print(f"Avg Price    : {response.get('avgPrice')}")

        print("\nOrder placed successfully.")

    except Exception as e:
        print(f"\nError: {str(e)}")


if __name__ == "__main__":
    main()