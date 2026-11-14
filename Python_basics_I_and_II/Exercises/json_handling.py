
# order_text = '''{
#     "id": 1001,
#     "order_number": 1001,
#     "financial_status": "paid",
#     "total_price": "249.90",
#     "email": "buyer@test.com",
#     "customer": {"id": 77, "orders_count": 1},
#     "shipping_address": {"country_code": "PK"},
#     "line_items": [
#     {"sku": "TSH-BLU-M", "quantity": 2, "price": "59.95"},
#     {"sku": "JNS-BLK-32", "quantity": 1, "price": "130.00"}
#     ],
#     "tags": "gift, first-order"
# }'''

# order_dict = json.loads(order_text)
# print(order_dict['email'])

# order_json = json.dumps(order_dict, indent=2)
# print(order_json)

# # .loads --> convert the text into python dict, so we can use it, and then .dumps() --> convert back the dict into json text. 

# import json

# raw = '{"id": 1002, "status": "paid", "tags": ["vip", "gift"]}'
# order = json.loads(raw)               # 1: string -> dictionary
# print(order["tags"][0])           # 2: print "vip"
# text = json.dumps(order, indent=2)     # 3 and 4: dictionary -> pretty text
# with open("out.json", "w") as f:  # 5: write mode
#     f.write(text)

import json
def parse_and_update_order(json_string, new_status):
    python_object = json.loads(json_string)
    python_object['status'] = new_status

    updated_json_string = json.dumps(python_object)
    return updated_json_string
order_1 = parse_and_update_order(json_string='{"order_id": 1001, "status": "pending", "total": 150.0}', new_status="Cencelled")

print(order_1)



