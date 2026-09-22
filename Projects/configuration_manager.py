def add_setting(settings, pair):
    key = pair[0].lower()
    val = pair[1].lower()
    if key in settings:
        return (f"Setting '{key}' already exists! Cannot add a new setting with this name.")
    else:
        settings[key] = val
        return (f"Setting '{key}' added with value '{val}' successfully!")

def update_setting(settings, pair):
    key = pair[0].lower()
    val = pair[1].lower()
    if key in settings:
        settings[key] = val
        return (f"Setting '{key}' updated to '{val}' successfully!")
    else:
        return (f"Setting '{key}' does not exist! Cannot update a non-existing setting.")

def delete_setting(settings, nkey):
    key = nkey.lower()
    if key in settings:
        del settings[key]
        return (f"Setting '{key}' deleted successfully!")
    else:
        return ("Setting not found!")

def view_settings(settings):
    if not settings:
        return("No settings available.")

    result = 'Current User Settings:\n'
    for key, value in settings.items():
        result += f"{key.capitalize()}: {value}\n"
    return result

test_settings = {
    'theme': 'bolas',
    'volume': 'bajo'
}
