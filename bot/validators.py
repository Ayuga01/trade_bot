VALID_SIDES = {"BUY", "SELL"}
VALID_ORDER_TYPES = {"MARKET", "LIMIT"}


def validate_side(side: str):
    side = side.upper()

    if side not in VALID_SIDES:
        raise ValueError(
            f"Invalid side: {side}. Use BUY or SELL"
        )

    return side



def validate_order_type(order_type: str):
    order_type = order_type.upper()

    if order_type not in VALID_ORDER_TYPES:
        raise ValueError(
            f"Invalid order type: {order_type}. "
            f"Use MARKET or LIMIT"
        )

    return order_type



def validate_quantity(quantity: float):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    return quantity



def validate_price(price, order_type):
    if order_type == "LIMIT":
        if price is None:
            raise ValueError(
                "Price is required for LIMIT orders"
            )

        if float(price) <= 0:
            raise ValueError("Price must be greater than 0")

    return price