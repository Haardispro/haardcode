import platform
import os
from json import loads, dumps

# Theme schema
THEME_SCHEMA = {
    "foreground": str,
    "background": str,
    "font": str,
    "font_size": int
}

# Default theme
DEFAULT_FOREGROUND = "#f8f8f2"
DEFAULT_BACKGROUND = "#282828"
DEFAULT_FONT = "Cascadia Code"
DEFAULT_FONT_SIZE = 14
DEFAULT_THEME_DICT = {
    "foreground": DEFAULT_FOREGROUND,
    "background": DEFAULT_BACKGROUND,
    "font": DEFAULT_FONT,
    "font_size": DEFAULT_FONT_SIZE
}


class Theme:
    def __init__(self, bg, fg, font, font_size):
        self.background = bg
        self.foreground = fg
        self.font = font
        self.font_size = font_size

    def as_dict(self) -> dict:
        return {
            "background": self.background,
            "foreground": self.foreground,
            "font": self.font,
            "font_size": self.font_size
        }

    def as_json(self):
        return dumps(self.as_dict())


def get_themes_folder_path():
    """
    Returns the path to the themes folder (this can depend on the platform)
    (HOMEFOLDER)/.haarded_themes
    """
    os_platform = platform.system()
    if os_platform == "Windows":
        return f"{os.environ['USERPROFILE']}/.haarded_themes"

    elif os_platform == "Linux" or os_platform == "Darwin":
        return f"{os.environ['HOME']}/.haarded_themes"


def get_theme_from_dict(theme: dict) -> Theme:
    """
    Returns an instance of `Theme` created from a dictionary
    """

    # Compare `theme` with `THEME_SCHEMA`
    # (Make sure the dictionary contains all the necessary properties)
    for k in THEME_SCHEMA:
        if not k in theme:
            raise KeyError(f"The theme supplied its missing the following property: '{k}'")
        elif not isinstance(theme[k], THEME_SCHEMA[k]):
            raise TypeError(f"The theme supplied contains an invalid type of property for '{k}', (expected '{THEME_SCHEMA[k]}', got '{type(theme[k])}')")
        else:
            pass

    return Theme(
        theme['background'],
        theme['foreground'],
        theme['font'],
        theme['font_size'])


def save_theme_to_themes_folder(theme_name: str, theme: Theme):
    """
    Saves the theme supplied to the themes folder in a json
    file with the name `{theme_name}.json`
    """
    target_path = os.path.join(get_themes_folder_path(), f"{theme_name}.json")
    print(f"Saving theme {theme_name} in {target_path}")
    open(target_path, "w").write(theme.as_json())


def load_theme(theme_name: str="default") -> Theme:
    """
    Looks for a file named `{theme_name}.json`, reads it, and returns a `Theme`
    *If no `theme_name` its supplied, it will return the default theme saved in 
    the themes folder.*
    This can fail if the theme file doesn't exist (`FileNotFoundError`), or if
    the theme file its corrupted / doesn't follow the `THEME_SCHEMA`.
    """
    target_path = os.path.join(get_themes_folder_path(), f"{theme_name}.json")
    content = loads(open(target_path, "r").read())

    return get_theme_from_dict(content)


def initialize_themes_folder():
    """
    If the themes folder its not created already, it gets created by using the
    path provided by `get_themes_folder_path()` and saves the default theme as
    `default.json`
    """
    themes_path = get_themes_folder_path()
    if not os.path.isdir(themes_path):
        print(f"Creating themes folder in {themes_path}")
        os.mkdir(themes_path)
        save_theme_to_themes_folder(
                "default",
                get_theme_from_dict(DEFAULT_THEME_DICT))

    else:
        pass


def list_themes():
    """
    Returns a list containing all the available themes in the themes folder.
    """
    files = os.listdir(get_themes_folder_path())
    themes = []

    for f in files:
        if f.endswith(".json"):
            themes.append(f.replace(".json", ""))

        else:
            pass

    return themes
