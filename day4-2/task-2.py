def make_greeting(language):
    def greet(name):
        if language == "English":
            print(f"Hello {name}")
        elif language == "Spanish":
            print(f"Hola {name}")
        else:
            print("Language not supported")

    return greet


english_greeting = make_greeting("English")
spanish_greeting = make_greeting("Spanish")

english_greeting("Aristotle")
spanish_greeting("Jaquel")