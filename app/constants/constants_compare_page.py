#################################################################
RIGHT_DB_BOX_TITLE = "------------- Choose 2 Fighters -------------"
RIGHT_SORT_BOX_TITLE = "-------------------- Sort by --------------------"

#################################################################
RIGHT_FIGHTER_NAME_ENTRIES = [
    'first_fighter_choose_entry', 'second_fighter_choose_entry'
]

#################################################################
INFO_TEXT_NAMES = [
    f"{18*' '}Age", f"{9*' '}Fightning For",
    f"{7*' '}Weight / Height", f"{15*' '}Fights",
    f"{6*' '}Pro MMA Record", f"{11*' '}Last Streak",
    f"{10*' '}Recent Fight"
]

#################################################################
FIRST_FIGHTER_INFO_ENTRY_NAMES = [
    'first_age', 'first_age_2', 'first_we_he', 'first_fights',
    'first_mma_record', 'first_last_streak', 'first_recent_fight',
]
SECOND_FIGHTER_INFO_ENTRY_NAMES = [
    'second_age', 'second_age_2', 'second_we_he', 'second_fights',
    'second_mma_record', 'second_last_streak', 'second_recent_fight',
]
INFO_ENTRY_NAMES = [
    *FIRST_FIGHTER_INFO_ENTRY_NAMES,
    *SECOND_FIGHTER_INFO_ENTRY_NAMES,
]
INFO_ENTRY_NAMES_X_VALUES = (
    215, 215, 215, 215, 215, 215, 215,
    642, 642, 642, 642, 642, 642, 642,
)
INFO_ENTRY_NAMES_Y_VALUES = (
    110, 150, 190, 230, 270, 310, 350,
    110, 150, 190, 230, 270, 310, 350,
)

#################################################################
STAT_TITLE_TEXT_NAMES = (
    'LOSSES', 'WINS', 'WINS ', 'LOSSES ',
)
STAT_TITLE_TEXT_X_VALUES = (
    70, 317, 703, 917,
)

#################################################################
STAT_TEXT_NAMES = {
    'f_l_ko': 'KO/TKO', 'f_l_sub': 'SUB', 'f_l_dec': 'DEC',
    'f_w_ko': 'KO/TKO', 'f_w_sub': 'SUB', 'f_w_dec': 'DEC',

    's_l_ko':'KO/TKO', 's_l_sub':'SUB', 's_l_dec':'DEC',
    's_w_ko':'KO/TKO', 's_w_sub':'SUB', 's_w_dec':'DEC',
}
STAT_TEXT_X_VALUES = (
    25, 100, 160, 260, 335, 395,
    640, 715, 775, 875, 950, 1010,
)

#################################################################
STAT_ENTRY_NAMES = [
    'first_l_ko', 'first_l_sub', 'first_l_dec',                   # UPPER
    'first_w_ko', 'first_w_sub', 'first_w_dec',
    'second_w_ko', 'second_w_sub', 'second_w_dec',
    'second_l_ko', 'second_l_sub', 'second_l_dec',

    'first_l_ko_perc', 'first_l_sub_perc', 'first_l_dec_perc',     # LOWER
    'first_w_ko_perc', 'first_w_sub_perc', 'first_w_dec_perc',
    'second_w_ko_perc', 'second_w_sub_perc', 'second_w_dec_perc',
    'second_l_ko_perc', 'second_l_sub_perc', 'second_l_dec_perc'
]
STAT_ENTRY_NAMES_X_VALUES = (
    40, 100, 160, 275, 335, 395, 655, 715,
    775, 890, 950, 1010, 40, 100, 160, 275,
    335, 395, 655, 715, 775, 890, 950, 1010
)
STAT_ENTRY_NAMES_Y_VALUES = (
    471, 471, 471, 471, 471, 471, 471, 471,
    471, 471, 471, 471, 646, 646, 646, 646,
    646, 646, 646, 646, 646, 646, 646, 646,
)
FIRST_FIGHTER_ENTRY_NAMES_FOR_DISPLAYING = (
    *FIRST_FIGHTER_INFO_ENTRY_NAMES,
    'first_w_ko', 'first_w_ko_perc', 'first_w_sub', 'first_w_sub_perc',
    'first_w_dec', 'first_w_dec_perc', 'first_l_ko', 'first_l_ko_perc',
    'first_l_sub', 'first_l_sub_perc', 'first_l_dec', 'first_l_dec_perc',
)
SECOND_FIGHTER_ENTRY_NAMES_FOR_DISPLAYING = (
    *SECOND_FIGHTER_INFO_ENTRY_NAMES,
    'second_w_ko', 'second_w_ko_perc', 'second_w_sub', 'second_w_sub_perc',
    'second_w_dec', 'second_w_dec_perc', 'second_l_ko', 'second_l_ko_perc',
    'second_l_sub', 'second_l_sub_perc', 'second_l_dec', 'second_l_dec_perc'
)
ENTRY_ABBREVIATIONS = (
    '', ' years', '', '', '', '', '', '', '%',
    '', '%', '', '%', '', '%', '', '%', '', '%',
)

#################################################################
BAR_LIST = [
    'first_l_ko_bar', 'first_l_ko_bar2', 'first_l_sub_bar',            # FIRST FIGHTER
    'first_l_sub_bar2', 'first_l_dec_bar', 'first_l_dec_bar2',
    'first_w_ko_bar', 'first_w_ko_bar2', 'first_w_sub_bar',
    'first_w_sub_bar2', 'first_w_dec_bar', 'first_w_dec_bar2',

    'second_w_ko_bar', 'second_w_ko_bar2', 'second_w_sub_bar',         # SECOND FIGHTER
    'second_w_sub_bar2', 'second_w_dec_bar', 'second_w_dec_bar2',
    'second_l_ko_bar', 'second_l_ko_bar2', 'second_l_sub_bar',
    'second_l_sub_bar2', 'second_l_dec_bar', 'second_l_dec_bar2'
]
BAR_X_VALUES = (
    42, 62, 102, 122, 162, 182, 277, 297,
    337, 357, 397, 417, 657, 677, 717, 737,
    777, 797, 892, 912, 952, 972, 1012, 1032
)

#################################################################
GRAPH_X_VALUES = (
    'W_KO/TKO', 'W_SUB', 'W_DEC', 'L_KO/TKO', 'L_SUB', 'L_DEC'
)

###############################################################################
SORT_BOX_VARIANTS = [
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
