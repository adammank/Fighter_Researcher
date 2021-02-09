from tkinter import Tk

from app.home_page import HomePage
from app.utilities.utilities import center_window


if __name__ == '__main__':
    window = Tk()
    width, height = center_window(
        screen_width=window.winfo_screenwidth(),
        screen_height=window.winfo_screenheight(),
        tk_window_width=626, tk_window_height=915,
    )
    window.geometry(f"626x900+{width}+{height}")
    window.title("Fighter Researcher - Home Page")
    window.iconbitmap("app/static/project_photos/red-fist-icon.ico")
    window.resizable(False, False)
    HomePage(window)