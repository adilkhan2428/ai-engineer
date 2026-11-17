# The dot (.) means "look inside my current package folder"
from .fees import calculate_gateway_fee

def get_net_payout(order_total, product_cost):
    fee = calculate_gateway_fee(order_total)
    net = order_total - product_cost - fee
    return round(net, 2)
