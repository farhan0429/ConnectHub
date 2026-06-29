from themes.dark import DARK_THEME
from themes.light import LIGHT_THEME


class ThemeManager:
    """
    Handles application themes.
    """

    _themes = {
        "dark": DARK_THEME,
        "light": LIGHT_THEME,
    }

    _current = "dark"

    @classmethod
    def get(cls):
        return cls._themes[cls._current]

    @classmethod
    def set_theme(cls, name: str):
        if name in cls._themes:
            cls._current = name

    @classmethod
    def current_name(cls):
        return cls._current