from store_tools import get_net_payout

order_amount = 120.00
cogs = 45.00

payout = get_net_payout(order_amount, cogs)
print(f"Shopify Net Payout: ${payout}")