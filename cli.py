import argparse

from rich.console import Console
from rich.table import Table

from bot.client import BinanceFuturesClient
from bot.orders import OrderService
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

console = Console()


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument(
        "--quantity",
        required=True,
        type=float
    )
    parser.add_argument(
        "--price",
        type=float
    )

    return parser.parse_args()


def print_order_summary(
    symbol,
    side,
    order_type,
    quantity,
    price
):
    print("\n")
    table = Table(title="ORDER REQUEST SUMMARY")

    table.add_column("Field")
    table.add_column("Value")

    table.add_row("Symbol", symbol.upper())
    table.add_row("Side", side)
    table.add_row("Order Type", order_type)
    table.add_row("Quantity", str(quantity))

    if price is not None:
        table.add_row("Price", str(price))

    console.print(table)


def print_order_response(response):
    print("\n")
    table = Table(title=" === ORDER RESPONSE === ")

    table.add_column("Field")
    table.add_column("Value")

    table.add_row(
        "Order ID",
        str(response.get("orderId"))
    )

    table.add_row(
        "Status",
        str(response.get("status"))
    )

    table.add_row(
        "Executed Qty",
        str(response.get("executedQty"))
    )

    table.add_row(
        "Avg Price",
        str(response.get("avgPrice"))
    )

    console.print(table)


def main():
    try:
        args = parse_arguments()

        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(
            args.price,
            order_type
        )

        print_order_summary(
            args.symbol,
            side,
            order_type,
            quantity,
            price
        )

        client = BinanceFuturesClient().get_client()

        order_service = OrderService(client)

        response = order_service.place_order(
            symbol=args.symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        print_order_response(response)

        console.print(
            "\n[bold green]✓ Order placed successfully[/bold green]"
        )

    except ValueError as e:
        console.print(
            f"\n[bold red]Validation Error:[/bold red] {e}"
        )

    except Exception as e:
        console.print(
            f"\n[bold red]Error:[/bold red] {e}"
        )


if __name__ == "__main__":
    main()