import os


def get_config():
    if os.name == "nt":
        return {"name": "Windows"}
    elif os.name == "linux":
        return {"name": "Linux"}
    elif os.name == "posix":
        return {"name": "Macos"}
    else:
        return {"name": "Unknown"}
