from binance.exceptions import BinanceAPIException
from bot.logging_config import setup_logger

logger = setup_logger()


class OrderService:
    def __init__(self, client):
        self.client = client

    def place_order(
        self,
        symbol,
        side,
        order_type,
        quantity,
        price=None
    ):
        try:
            logger.info(
                f"Sending order | "
                f"symbol={symbol} "
                f"side={side} "
                f"type={order_type} "
                f"quantity={quantity} "
                f"price={price}"
            )

            params = {
                "symbol": symbol.upper(),
                "side": side,
                "type": order_type,
                "quantity": quantity
            }

            if order_type == "LIMIT":
                params["price"] = price
                params["timeInForce"] = "GTC"

            response = self.client.futures_create_order(**params)

            logger.info(f"Order response: {response}")

            order_id = response["orderId"]

            final_response = self.client.futures_get_order(
                symbol=symbol.upper(),
                orderId=order_id
            )

            logger.info(f"Final order status: {final_response}")

            return final_response

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e.message}")
            raise

        except Exception as e:
            logger.exception(f"Unexpected error: {str(e)}")
            raise