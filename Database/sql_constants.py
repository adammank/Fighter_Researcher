
db_command_create_table = """
    CREATE TABLE IF NOT EXISTS 
        fighters_table(
                    NAME TEXT PRIMARY KEY,      ALIAS TEXT,
                    NATIONALITY TEXT,           AFFILIATION TEXT,
                    HEIGHT INTEGER,             WEIGHT INTEGER,
                    AGE INTEGER,                BORN TEXT,
                    RECENT_FIGHT TEXT,          FIRST_FIGHT TEXT,
                    FIGHTNING_YEARS INTEGER,    AMOUNT_OF_FIGHTS INTEGER,
                    PRO_MMA_RECORD TEXT,        LAST_STREAK TEXT,
                    WIN_KO INTEGER,             WIN_KO_PERC INTEGER,       
                    WIN_SUB INTEGER,            WIN_SUB_PERC INTEGER,      
                    WIN_DEC INTEGER,            WIN_DEC_PERC INTEGER,       
                    LOSS_KO INTEGER,            LOSS_KO_PERC INTEGER,
                    LOSS_SUB INTEGER,           LOSS_SUB_PERC INTEGER,
                    LOSS_DEC INTEGER,           LOSS_DEC_PERC INTEGER,
                    DRAWS INTEGER,              U_F_I_EVENT TEXT,           
                    U_F_I_PLACE TEXT,           U_F_I_DATE TEXT,
                    U_F_I_FIGHTERS TEXT,        FIGHTER_URL TEXT
                    )
    """

db_table_column_list = [
    'ALIAS', 'NATIONALITY', 'AFFILIATION', 'HEIGHT', 'WEIGHT',
    'AGE', 'BORN', 'RECENT_FIGHT', 'FIRST_FIGHT', 'FIGHTNING_YEARS',
    'AMOUNT_OF_FIGHTS', 'PRO_MMA_RECORD', 'LAST_STREAK',
    'WIN_KO', 'WIN_KO_PERC', 'WIN_SUB', 'WIN_SUB_PERC', 'WIN_DEC', 'WIN_DEC_PERC',
    'LOSS_KO', 'LOSS_KO_PERC', 'LOSS_SUB', 'LOSS_SUB_PERC', 'LOSS_DEC', 'LOSS_DEC_PERC',
    'DRAWS', 'U_F_I_EVENT', 'U_F_I_PLACE', 'U_F_I_DATE', 'U_F_I_FIGHTERS', 'FIGHTER_URL'
]

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

db_command_preface = "SELECT NAME, ALIAS, LAST_STREAK FROM fighters_table"


db_command_conditions_dict = {

    ###### AGE
    "AGE:    Young-old":            "ORDER BY AGE",
    "AGE:    Old-young":            "ORDER BY AGE DESC",
    "AGE:    <=20":                 "WHERE AGE <= 20 ORDER BY AGE",
    "AGE:    20-30":                "WHERE AGE BETWEEN 20 and 30 ORDER BY AGE",
    "AGE:    30-40":                "WHERE AGE BETWEEN 30 and 40 ORDER BY AGE",
    "AGE:    40+":                  "WHERE AGE >= 40 ORDER BY AGE",

    ###### HEIGHT
    "HEIGHT:    Small-high":        "ORDER BY HEIGHT",
    "HEIGHT:    High-small":        "ORDER BY HEIGHT DESC",
    "HEIGHT:    <=170":             "WHERE HEIGHT <= 170 ORDER BY HEIGHT",
    "HEIGHT:    171-180":           "WHERE HEIGHT BETWEEN 171 and 180 ORDER BY HEIGHT",
    "HEIGHT:    181-190":           "WHERE HEIGHT BETWEEN 181 and 190 ORDER BY HEIGHT",
    "HEIGHT:    190+":              "WHERE HEIGHT >= 190 ORDER BY HEIGHT",

    ###### WEIGHT
    "WEIGHT:    Light-heavy":       "ORDER BY WEIGHT",
    "WEIGHT:    Heavy-light":       "ORDER BY WEIGHT DESC",
    "WEIGHT:    <=70":              "WHERE WEIGHT <= 70 ORDER BY WEIGHT",
    "WEIGHT:    71-80":             "WHERE WEIGHT BETWEEN 71 and 80 ORDER BY WEIGHT",
    "WEIGHT:    80-99":             "WHERE WEIGHT BETWEEN 81 and 99 ORDER BY WEIGHT",
    "WEIGHT:    100+":              "WHERE WEIGHT >= 100 ORDER BY WEIGHT",

    ###### AMOUNT OF FIGHTS
    "AMOUNT:    Low-high":          "ORDER BY AMOUNT_OF_FIGHTS",
    "AMOUNT:    High-low":          "ORDER BY AMOUNT_OF_FIGHTS DESC",
    "AMOUNT:    <=10":              "WHERE AMOUNT_OF_FIGHTS <= 10 ORDER BY AMOUNT_OF_FIGHTS",
    "AMOUNT:    11-25":             "WHERE AMOUNT_OF_FIGHTS BETWEEN 11 and 25 ORDER BY AMOUNT_OF_FIGHTS",
    "AMOUNT:    26+":               "WHERE AMOUNT_OF_FIGHTS >=26 ORDER BY AMOUNT_OF_FIGHTS",

    ###### FIGHTNING YEARS
    "YEARS:    Low-high":           "ORDER BY FIGHTNING_YEARS",
    "YEARS:    High-low":           "ORDER BY FIGHTNING_YEARS DESC",
    "YEARS:    <=4":                "WHERE FIGHTNING_YEARS <= 4 ORDER BY FIGHTNING_YEARS",
    "YEARS:    5-14":               "WHERE FIGHTNING_YEARS BETWEEN 5 and 14 ORDER BY FIGHTNING_YEARS",
    "YEARS:    15+":                "WHERE FIGHTNING_YEARS >= 15 ORDER BY FIGHTNING_YEARS",

    ###### LAST STREAK (WIN/LOSSES)
    "STREAK:    WIN":               "WHERE LAST_STREAK LIKE '%WIN%' ORDER BY LAST_STREAK DESC",
    "STREAK:    LOSS":              "WHERE LAST_STREAK LIKE '%LOSS%' ORDER BY LAST_STREAK DESC",

    ###### WINS/LOSSES DETAILS
    "WINS:    KO/TKO":              "ORDER BY WIN_KO_PERC DESC",
    "WINS:    SUB":                 "ORDER BY WIN_SUB_PERC DESC",
    "WINS:    DEC":                 "ORDER BY WIN_DEC_PERC DESC",
    "LOSSES:    KO/TKO":            "ORDER BY LOSS_KO_PERC DESC",
    "LOSSES:    SUB":               "ORDER BY LOSS_SUB_PERC DESC",
    "LOSSES:    DEC":               "ORDER BY LOSS_DEC_PERC DESC",

    ###### NATIONALITY
    "NAT:    Poland":               "WHERE NATIONALITY LIKE 'POLAND%' ORDER BY AGE",
    "NAT:    USA":                  "WHERE NATIONALITY LIKE 'UNITED STATES%' ORDER BY AGE",
    "NAT:    Brazil":               "WHERE NATIONALITY LIKE 'BRAZIL%' ORDER BY AGE",
    "NAT:    France":               "WHERE NATIONALITY LIKE 'FRANCE%' ORDER BY AGE",
    "NAT:    England":              "WHERE NATIONALITY LIKE 'ENGLAND%' ORDER BY AGE",
    "NAT:    Russia":               "WHERE NATIONALITY LIKE 'RUSSIA%' ORDER BY AGE",
}