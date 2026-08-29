from datetime import datetime

now = datetime.now()

formatted = now.strftime("%A, %d-%B-%Y %I:%M %p")

print(formatted)
