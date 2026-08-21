library = {
    "A10": {
        "title": "Python",
        "author": "Johan Libert",
        "copies": 5
    },
    "A11": {
        "title": "Java",
        "author": "Chris Norington",
        "copies": 3
    },
    "A12": {
        "title": "Devops",
        "author": "Bruce Lee",
        "copies": 2
    }
}

# Issue book B102
issued_id = "A12"

if library[issued_id]["copies"] > 0:
    library[issued_id]["copies"] -= 1
    print("Book issued successfully.")
else:
    print("Book is not available.")

print(library)