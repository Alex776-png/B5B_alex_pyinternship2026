library = {
    "B101": {
        "title": "Python Basics",
        "author": "John Smith",
        "copies": 5
    },
    "B102": {
        "title": "Data Structures",
        "author": "Alice Brown",
        "copies": 3
    },
    "B103": {
        "title": "Machine Learning",
        "author": "David Lee",
        "copies": 2
    }
}

# Issue book B102
book_id = "B102"

if library[book_id]["copies"] > 0:
    library[book_id]["copies"] -= 1
    print("Book issued successfully.")
else:
    print("Book is not available.")

print(library)