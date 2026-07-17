def validate_side(side):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Invalid side")

def validate_order_type(order_type):
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Invalid type")

def validate_quantity(qty):
    if qty <= 0:
        raise ValueError("Invalid quantity")

def validate_price(price, order_type):
    if order_type == "LIMIT" and price is None:
        raise ValueError("Price required")