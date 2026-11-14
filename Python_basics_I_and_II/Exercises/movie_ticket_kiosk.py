# Imagine you are running a small cinema booking app. Here is what your code needs to do step-by-step:

# The Menu: You have a dictionary of available movies and their ticket prices:
movies = {"Action": 500, "Comedy": 300, "Drama": 400, "Horror": 350}

total = 0
for movie, price in movies.items():
    print(f"{movie} Ticket - Rs. {price}")
while True:
    item = input("Enter your Movie (or 'done' to stop): ").strip().title()
    if item.lower() == "done":
        break
    elif item in movies:
        total += movies[item]
        print(f"Added {item} ticket (Rs. {movies[item]}). Current total: Rs. {total}")
    else:
        print("Sorry, that movie is not available. Please choose from the list.")

print("\n--- Your Cinema Receipt ---")
print(f"Total: Rs. {total}")
print("Enjoy your movie!")