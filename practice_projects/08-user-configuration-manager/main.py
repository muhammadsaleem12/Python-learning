# Test Data
test_settings = {
    "theme": "dark",
    "language": "english",
    "brightness": "medium",
}

def add_setting(settings, setting):
    key = setting[0].lower()
    value = setting[1].lower()
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    elif key != settings:
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, setting):
    key = setting[0].lower()
    value = setting[1].lower()
    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    elif key != settings:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(settings, setting):
    key = setting.lower()
    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    elif key != settings:
        return f"Setting not found!"


def view_settings(settings):
    if not settings:
        return "No settings available."
    else:
        result = "Current User Settings:\n"

        for key, value in settings.items():
            if key in settings:
                result += f"{key.capitalize()}: {value}\n"

        return result


# Testing all of the functions.

# added new key, value
print(add_setting(test_settings, ("volume", "high")))
# updated the existing
print(update_setting(test_settings, ("theme", "light")))
# deleted language
print(delete_setting(test_settings, "language"))
# printed the result by calling view_settings functions.
print(view_settings(test_settings))

