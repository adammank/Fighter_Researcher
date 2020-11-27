#################################################################
right_db_box_title = "------------- Choose 2 Fighters -------------"
right_sort_box_title = "-------------------- Sort by --------------------"

#################################################################
right_fighter_name_entries = [
    'first_fighter_choose_entry', 'second_fighter_choose_entry'
]

#################################################################
info_text_names= [
    f"{18*' '}Age", f"{9*' '}Fightning For",
    f"{7*' '}Weight / Height", f"{15*' '}Fights",
    f"{6*' '}Pro MMA Record", f"{11*' '}Last Streak",
    f"{10*' '}Recent Fight"
]

#################################################################
first_fighter_info_entry_names = [
    'first_age', 'first_age_2', 'first_we_he', 'first_fights',
    'first_mma_record', 'first_last_streak', 'first_recent_fight',
]
second_fighter_info_entry_names = [
    'second_age', 'second_age_2', 'second_we_he', 'second_fights',
    'second_mma_record', 'second_last_streak', 'second_recent_fight',
]
info_entry_names = [
    *first_fighter_info_entry_names,
    *second_fighter_info_entry_names,
]
info_entry_names_x_values = (
    215, 215, 215, 215, 215, 215, 215,
    642, 642, 642, 642, 642, 642, 642,
)
info_entry_names_y_values = (
    110, 150, 190, 230, 270, 310, 350,
    110, 150, 190, 230, 270, 310, 350,
)

#################################################################
stat_title_text_names = (
    'LOSSES', 'WINS', 'WINS ', 'LOSSES ',
)
stat_title_text_x_values = (
    70, 317, 703, 917,
)

#################################################################
stat_text_names = {
    'f_l_ko': 'KO/TKO', 'f_l_sub': 'SUB', 'f_l_dec': 'DEC',
    'f_w_ko': 'KO/TKO', 'f_w_sub': 'SUB', 'f_w_dec': 'DEC',

    's_l_ko':'KO/TKO', 's_l_sub':'SUB', 's_l_dec':'DEC',
    's_w_ko':'KO/TKO', 's_w_sub':'SUB', 's_w_dec':'DEC',
}
stat_text_x_values = (
    25, 100, 160, 260, 335, 395,
    640, 715, 775, 875, 950, 1010,
)

#################################################################
stat_entry_names = [
    'first_l_ko', 'first_l_sub', 'first_l_dec',                   # UPPER
    'first_w_ko', 'first_w_sub', 'first_w_dec',
    'second_w_ko', 'second_w_sub', 'second_w_dec',
    'second_l_ko', 'second_l_sub', 'second_l_dec',

    'first_l_ko_perc', 'first_l_sub_perc', 'first_l_dec_perc',     # LOWER
    'first_w_ko_perc', 'first_w_sub_perc', 'first_w_dec_perc',
    'second_w_ko_perc', 'second_w_sub_perc', 'second_w_dec_perc',
    'second_l_ko_perc', 'second_l_sub_perc', 'second_l_dec_perc'
]
stat_entry_names_x_values = (
    40, 100, 160, 275, 335, 395, 655, 715,
    775, 890, 950, 1010, 40, 100, 160, 275,
    335, 395, 655, 715, 775, 890, 950, 1010
)
stat_entry_names_y_values = (
    471, 471, 471, 471, 471, 471, 471, 471,
    471, 471, 471, 471, 646, 646, 646, 646,
    646, 646, 646, 646, 646, 646, 646, 646,
)
first_fighter_entry_names_for_displaying = (
    *first_fighter_info_entry_names,
    'first_w_ko', 'first_w_ko_perc', 'first_w_sub', 'first_w_sub_perc',
    'first_w_dec', 'first_w_dec_perc', 'first_l_ko', 'first_l_ko_perc',
    'first_l_sub', 'first_l_sub_perc', 'first_l_dec', 'first_l_dec_perc',
)
second_fighter_entry_names_for_displaying = (
    *second_fighter_info_entry_names,
    'second_w_ko', 'second_w_ko_perc', 'second_w_sub', 'second_w_sub_perc',
    'second_w_dec', 'second_w_dec_perc', 'second_l_ko', 'second_l_ko_perc',
    'second_l_sub', 'second_l_sub_perc', 'second_l_dec', 'second_l_dec_perc'
)
entry_abbreviations = (
    '', ' years', '', '', '', '', '', '', '%',
    '', '%', '', '%', '', '%', '', '%', '', '%',
)

#################################################################
bar_list = [
    'first_l_ko_bar', 'first_l_ko_bar2', 'first_l_sub_bar',            # FIRST FIGHTER
    'first_l_sub_bar2', 'first_l_dec_bar', 'first_l_dec_bar2',
    'first_w_ko_bar', 'first_w_ko_bar2', 'first_w_sub_bar',
    'first_w_sub_bar2', 'first_w_dec_bar', 'first_w_dec_bar2',

    'second_w_ko_bar', 'second_w_ko_bar2', 'second_w_sub_bar',         # SECOND FIGHTER
    'second_w_sub_bar2', 'second_w_dec_bar', 'second_w_dec_bar2',
    'second_l_ko_bar', 'second_l_ko_bar2', 'second_l_sub_bar',
    'second_l_sub_bar2', 'second_l_dec_bar', 'second_l_dec_bar2'
]
bar_x_values = (
    42, 62, 102, 122, 162, 182, 277, 297,
    337, 357, 397, 417, 657, 677, 717, 737,
    777, 797, 892, 912, 952, 972, 1012, 1032
)

#################################################################
graph_x_values = (
    'W_KO/TKO', 'W_SUB', 'W_DEC', 'L_KO/TKO', 'L_SUB', 'L_DEC'
)

###############################################################################
sort_box_variants = [
    f"{28*'*'}  AGE  {28*'*'}",
    "AGE:    Young-old", "AGE:    Old-young",
    "AGE:    <=20", "AGE:    20-30", "AGE:    30-40", "AGE:    40+",

    f"{26*'*'}  HEIGHT  {26*'*'}",
    "HEIGHT:    Small-high", "HEIGHT:    High-small",
    "HEIGHT:    <=170", "HEIGHT:    171-180", "HEIGHT:    181-190", "HEIGHT:    190+",

    f"{26*'*'}  WEIGHT  {25*'*'}",
    "WEIGHT:    Light-heavy", "WEIGHT:    Heavy-light",
    "WEIGHT:    <=70", "WEIGHT:    71-80", "WEIGHT:    80-99", "WEIGHT:    100+",

    f"{26*'*'}  FIGHTS  {26*'*'}",
    "AMOUNT:    Low-high", "AMOUNT:    High-low",
    "AMOUNT:    <=10", "AMOUNT:    11-25", "AMOUNT:    26+",

    f"{21*'*'}  YEARS OF FIGHT  {21*'*'}",
    "YEARS:    Low-high", "YEARS:    High-low",
    "YEARS:    <=4", "YEARS:    5-14", "YEARS:    15+",

    f"{25*'*'}  STREAK  {26*'*'}",
    "STREAK:    WIN", "STREAK:    LOSS",

    f"{18*'*'}  WINS/LOSSES DETAILS  {17*'*'}",
    "WINS:    KO/TKO", "WINS:    SUB", "WINS:    DEC",
    "LOSSES:    KO/TKO", "LOSSES:    SUB", "LOSSES:    DEC",

    f"{23*'*'}  NATIONALITY  {23*'*'}",
    "NAT:    Poland", "NAT:    USA", "NAT:    Brazil",
    "NAT:    France", "NAT:    England", "NAT:    Russia",
]

#################################################################
def compare_colors_dict(theme):
    """Returns dictionary containing objects as keys and
        their colors as values based on passed argument."""

    if theme == 'Default':
        colors_list = [
            'bisque', 'black', 'white',
            'black', 'chocolate', 'bisque',
            'seaborn-darkgrid',
        ]
    elif theme == 'Dracula':
        colors_list = [
            'black', 'white', 'black',
            'white', 'black', 'black',
            'Solarize_Light2',
        ]
    elif theme == 'Navy':
        colors_list = [
            'midnightblue', 'yellow', 'darkslategray',
            'yellow', 'darkslategray', 'midnightblue',
            'dark_background',
        ]
    elif theme == 'Dark grey':
        colors_list = [
            'darkslategray', 'deepskyblue', 'bisque4',
            'lawn green', 'darkolivegreen', 'darkslategray',
            'grayscale',
        ]

    objects_parts = [
        'lbl_bg_color', 'lbl_fg_color',
        'entry_bg_color', 'entry_fg_color',
        'right_frame', 'left_frame',
        'graph'
    ]

    return {
        obj_part: color for obj_part, color in zip(objects_parts, colors_list)
    }
