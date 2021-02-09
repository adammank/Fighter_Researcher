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


def center_value(obj, stat_or_name):
    """Add spaces in order to center a text within an entry."""

    obj_length = len(str(obj))
    amount_of_maxium_spaces = 21 if stat_or_name != 'stat' else 4
    amount_of_avaliable_spaces = amount_of_maxium_spaces - obj_length
    centered_obj = f"{amount_of_avaliable_spaces * ' '}{obj}"

    return centered_obj


def colors_dict(theme, file) -> dict:
    """Based on selected by user theme & on file on which he actually is,
    returns dictionary containing object names as keys and their colors as values.
    Used for adjusting page theme (colors)."""

    if theme == 'Default':
        colors_list = [
            'bisque', 'black', 'white',
            'black', 'bisque', 'chocolate',
            'seaborn-darkgrid'
        ] if file == 'SEARCH_PAGE' else [
            'bisque', 'black', 'white',
            'black', 'chocolate', 'bisque',
            'seaborn-darkgrid']

    elif theme == 'Dracula':
        colors_list = [
            'black', 'white', 'black',
            'white', 'black', 'black',
            'Solarize_Light2'
        ] if file == 'SEARCH_PAGE' else [
            'black', 'white', 'black',
            'white', 'black', 'black',
            'Solarize_Light2']

    elif theme == 'Navy':
        colors_list = [
            'midnightblue', 'yellow', 'darkslategray',
            'yellow', 'midnightblue', 'darkslategray',
            'dark_background'
        ] if file == 'SEARCH_PAGE' else [
            'midnightblue', 'yellow', 'darkslategray',
            'yellow', 'darkslategray', 'midnightblue',
            'dark_background']

    elif theme == 'Dark grey':
        colors_list = [
            'darkslategray', 'deepskyblue', 'bisque4',
            'lawn green', 'darkslategray', 'darkolivegreen',
            'grayscale'
        ] if file == 'SEARCH_PAGE' else [
            'darkslategray', 'deepskyblue', 'bisque4',
            'lawn green', 'darkolivegreen', 'darkslategray',
            'grayscale']


    objects_parts = [
        'lbl_bg_color', 'lbl_fg_color',
        'entry_bg_color', 'entry_fg_color',
        'right_frame', 'left_frame',
        'graph',
    ]

    return {
        obj_part: color for obj_part, color in zip(objects_parts, colors_list)
    }

def db_command_return_fighter_stats_for_comparing(fighter_name):
    return f"""
        SELECT   
            NAME, AGE, FIGHTNING_YEARS, WEIGHT, HEIGHT, AMOUNT_OF_FIGHTS, 
            PRO_MMA_RECORD, LAST_STREAK, RECENT_FIGHT, 
            WIN_KO, WIN_KO_PERC, WIN_SUB, WIN_SUB_PERC, WIN_DEC, WIN_DEC_PERC, 
            LOSS_KO, LOSS_KO_PERC, LOSS_SUB, LOSS_SUB_PERC, LOSS_DEC, LOSS_DEC_PERC
        FROM 
            fighters_table 
        WHERE 
            NAME ='{fighter_name}'
    """


def db_command_return_fighter_stats_for_comparing_graph(fighter_name):
    return f"""
        SELECT
            WIN_KO, WIN_SUB, WIN_DEC, 
            LOSS_KO, LOSS_SUB, LOSS_DEC
        FROM 
            fighters_table 
        WHERE 
            NAME ='{fighter_name}'
    """


def db_command_return_fighter_last_streak(fighter_name):
    return f"""
        SELECT 
            LAST_STREAK
        FROM 
            fighters_table 
        WHERE 
            NAME ='{fighter_name}'
    """


def db_command_create_fighter_career_history_table(table_name):
    return f"""
        CREATE TABLE IF NOT EXISTS {table_name}
            (NUMBER INTEGER, 
             VERDICT TEXT, 
             OPPONENT TEXT, 
             EVENT TEXT,
             DATE TEXT, 
             METHOD TEXT, 
             ROUND INTEGER, 
             TIME TEXT)
        """


def db_command_update_fighter_stats(fighter_stat_list):
    return f"""
        UPDATE fighters_table SET

            ALIAS='{fighter_stat_list[1]}',
            NATIONALITY='{fighter_stat_list[2]}',
            AFFILIATION='{fighter_stat_list[3]}',
            HEIGHT='{fighter_stat_list[4]}',
            WEIGHT='{fighter_stat_list[5]}',
            AGE='{fighter_stat_list[6]}',
            BORN='{fighter_stat_list[7]}',
            RECENT_FIGHT='{fighter_stat_list[8]}',
            FIRST_FIGHT='{fighter_stat_list[9]}',
            FIGHTNING_YEARS='{fighter_stat_list[10]}',
            AMOUNT_OF_FIGHTS='{fighter_stat_list[11]}',
            PRO_MMA_RECORD='{fighter_stat_list[12]}',
            LAST_STREAK='{fighter_stat_list[13]}',
            WIN_KO='{fighter_stat_list[14]}',
            WIN_KO_PERC='{fighter_stat_list[15]}',    
            WIN_SUB='{fighter_stat_list[16]}',
            WIN_SUB_PERC='{fighter_stat_list[17]}',    
            WIN_DEC='{fighter_stat_list[18]}',
            WIN_DEC_PERC='{fighter_stat_list[19]}',       
            LOSS_KO='{fighter_stat_list[20]}',
            LOSS_KO_PERC='{fighter_stat_list[21]}',
            LOSS_SUB='{fighter_stat_list[22]}',
            LOSS_SUB_PERC='{fighter_stat_list[23]}',
            LOSS_DEC='{fighter_stat_list[24]}',
            LOSS_DEC_PERC='{fighter_stat_list[25]}',
            DRAWS='{fighter_stat_list[26]}',
            U_F_I_EVENT='{fighter_stat_list[27]}',           
            U_F_I_PLACE='{fighter_stat_list[28]}',
            U_F_I_DATE='{fighter_stat_list[29]}',
            U_F_I_FIGHTERS='{fighter_stat_list[30]}',
            FIGHTER_URL='{fighter_stat_list[31]}'

        WHERE
            NAME='{fighter_stat_list[0]}'
        """


def db_command_add_career_history_fight(table_name, fight, index):
    return f"""
    INSERT INTO {table_name} (
        NUMBER, VERDICT, 
        OPPONENT, EVENT, 
        DATE, METHOD, 
        ROUND, TIME
    )
    VALUES (
        {index}, "{fight[0]}", 
        "{fight[1]}", "{fight[2]}", 
        "{fight[3]}", "{fight[4]}",
        {fight[5]}, "{fight[6]}"
    )
    """