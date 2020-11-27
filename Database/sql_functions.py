
##### sql_functions.py
#####   This file contains all used functions cooligated with database in entire project.

import os
import random
from sqlite3 import *
from .sql_constants import *
from Selenium.selenium_functions import run_driver, grab_fighter_info


class DatabaseManager:
    def __init__(self):
        self.connection = connect(
            "Database/fighters_database.db")

    ###### OPENING / CLOSING METHODS
    def create_main_db_table(self):
        return self.connection.cursor().execute(
            db_command_create_table)

    def close_connection_with_db(self):
        return self.connection.close()


    ###### DOING SMTH TO THE DB METHODS
    def add_fighter(self, fighter_stat_list, fighter_career_history):
        """Add a fighter to db."""

        # add person's row
        self.add_fighter_row(fighter_name=fighter_stat_list[0])

        # fulfill this row with his stats
        self.update_fighter_row(fighter_stat_list=fighter_stat_list)

        # create fighter's career history table
        table_name = fighter_stat_list[0].replace(' ', '_', 1).split()[0]
        self.career_history_create_table(table_name=table_name)

        # add his fights (rows) to this table
        self.career_history_add_fights(
            table_name=table_name, fighter_career_history=fighter_career_history)


    def update_fighter(self, url):
        """Update fighter by passing his url."""

        # grab all necessary informations
        run_driver(url, headless=1)
        fighter_stat_list, fighter_career_history = grab_fighter_info()
        table_name = fighter_stat_list[0].replace(' ', '_', 1).split()[0]

        # update fighter's stats
        self.update_fighter_row(
            fighter_stat_list=fighter_stat_list)

        # remove rows (fights) from fighter's career history table
        self.career_history_remove_fights(table_name=table_name)

        # add rows (fights) to fighter's career history table
        self.career_history_add_fights(
            table_name=table_name, fighter_career_history=fighter_career_history)


    def add_fighter_row(self, fighter_name):
        """Add fighter's row to fighters table."""

        self.connection.cursor().execute(
            f"INSERT INTO fighters_table (NAME) VALUES ('{fighter_name}')")
        self.connection.commit()


    def update_fighter_row(self, fighter_stat_list):
        """Update certain row (fighter's stats) in fighters table."""

        self.connection.cursor().execute(
            db_command_update_fighter_stats(
                fighter_stat_list=fighter_stat_list
            ))
        self.connection.commit()


    def career_history_create_table(self, table_name):
        """Create fighter's career history table."""

        self.connection.cursor().execute(
            db_command_create_fighter_career_history_table(
                table_name=table_name
            ))
        self.connection.commit()


    def career_history_add_fights(self, table_name, fighter_career_history):
        """Add rows (fights) to fighter's career history table."""

        for index, fight in enumerate(fighter_career_history):
            index+=1
            self.connection.cursor().execute(
                db_command_add_career_history_fight(
                    table_name=table_name, fight=fight, index=index
                ))
            self.connection.commit()


    def career_history_remove_fights(self, table_name):
        """Remove all rows (fights) from fighter's career history table."""

        self.connection.cursor().execute(f"DELETE from {table_name}")
        self.connection.commit()


    ###### RETURNING DB RECORD METHODS
    def return_certain_fighter_list(self, condition):
        """Return certain fighter list based on selected option."""

        # construct entire db condition
        db_full_command = f"{db_command_preface} {condition}"

        # grab from db proper data
        fighters_list = self.connection.cursor().execute(db_full_command).fetchall()

        if 'LAST_STREAK' not in condition:
            return fighters_list
        return self.sort_fighters_by_their_last_streak(fighters_list)


    def return_fighter_urls(self):
        """Return fighter urls in order to update theirs stats."""

        return self.connection.cursor().execute(
            "SELECT FIGHTER_URL FROM fighters_table").fetchall()


    def return_fighter_names(self):
        """Return fighter list in order to fulfill the GUI db one."""

        try:
            fighter_list = self.connection.cursor().execute(
                db_command_preface).fetchall()
        except OperationalError:
            print('No such table')
            fighter_list = []

        return fighter_list


    def return_fighter_info(self, fighter_name):
        """Return fighter stats in order to display them in the search_page.py."""

        return self.connection.cursor().execute(
            f"SELECT * FROM fighters_table WHERE NAME ='{fighter_name}'"
        ).fetchone()


    def return_fighter_career_history(self, fighter_name):
        """Return fighter fights in order to display them in the search_page.py."""

        fighter_first_name = fighter_name.split()[0]
        fighter_surname = fighter_name.split()[1]

        # fighter's career_history table is made by his first & last name
        return self.connection.cursor().execute(
            f"""SELECT * FROM {fighter_first_name}_{fighter_surname}"""
        ).fetchall()


    def return_fighter_stats_for_comparing(self, fighter_name):
        """Return fighter stats in order to display them in the compare_page.py."""

        return self.connection.cursor().execute(
            db_command_return_fighter_stats_for_comparing(
                fighter_name)).fetchone()


    def return_fighter_stats_for_comparing_graph(self, fighter_name):
        """Return fighter stats in order to create
        a compare graph in the compare_page.py"""

        return self.connection.cursor().execute(
            db_command_return_fighter_stats_for_comparing_graph(
                fighter_name)).fetchone()


    # ASSISTANT METHODS
    @staticmethod
    def sort_fighters_by_their_last_streak(fighters_list):
        return sorted(
            fighters_list, key=lambda info: int(info[2].split()[0]), reverse=True,
        )



def multiprocessing_update_fighter(url):
    """Used in home_page.py to update fighters.
    Multiprocessing in order to work properly requires an
    explicit call & handover arguments. That's why this funcion exists."""

    return DatabaseManager().update_fighter(url)
