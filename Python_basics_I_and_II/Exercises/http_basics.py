# import json
# def save_order_to_json(order_dict, filename):
#     try:
#         with open(filename, 'w', encoding='utf-8') as f:
#             json.dump(order_dict, f, indent=4)
#             print("file saved successfully!")
#     except IOError as e:
#         print(f"File I/o Error: {e}")

# save_order_to_json(order_dict={"order_id": 501, "customer": "Adil", "amount": 250.0}, filename="files_save_test/order_dict.json")
# print("done")


import requests
import json
def analyze_tool(user_id):
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/todos", params = {"userId": user_id})
        if response.status_code == 200:
            list_todos = response.json()
            completed_count = 0
            uncompleted_count = 0
            for todo in list_todos:
                if todo['completed']:
                    completed_count += 1
                else:
                    uncompleted_count += 1
            print(f"Number of Completed Orders: {(completed_count)}")
            print(f"Number of uncompleted or pending: {uncompleted_count}")
    except requests.exceptions.RequestException as e:
        print(f"API network Failed: {e}")

analyze_tool(user_id=5)

