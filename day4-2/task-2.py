def make_greeting(language):
    def greet(name):
        if language == "english":
            print(f"Hello, {name}")
        elif language == "hindi":
            print(f"Namaste, {name}")
        else:
            print("Language not supported")

    return greet


english_greeting = make_greeting("english")
hindi_greeting = make_greeting("hindi")

english_greeting("Rahul")
hindi_greeting("Amit")