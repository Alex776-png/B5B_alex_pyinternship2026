default_settings = {
    "theme": "light",
    "language": "Russian",
    "notifications": True,
    "font_size": 14
}

user_settings = {
    "theme": "dark",
    "font_size": 16
}

final_settings = default_settings.copy()
final_settings.update(user_settings)

print(final_settings)