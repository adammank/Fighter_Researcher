import random


def center_window(
        screen_width, screen_height,
        tk_window_width, tk_window_height
):
    """Return two values (width & height) for better
        positioning center of the application."""

    avaliable_width = round(screen_width - tk_window_width)
    avaliable_height = round(screen_height - tk_window_height)

    screen_width_center = str(avaliable_width // 2)
    screen_height_top = str(avaliable_height // 4)

    return screen_width_center, screen_height_top


def compare_page_center_name_or_stat(obj, stat_or_name):
    """Add spaces to center a text within an entry."""

    obj_length = len(str(obj))
    amount_of_maxium_spaces = 21 if stat_or_name != 'stat' else 4
    amount_of_avaliable_spaces = amount_of_maxium_spaces - obj_length
    centered_obj = f"{amount_of_avaliable_spaces * ' '}{obj}"

    return centered_obj
