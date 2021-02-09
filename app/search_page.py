
##### search_page.py
#####   This module contains the GUI Search Page window, which
##### allows us to find any MMA fighter that we want to,
##### and to look for his specific stats.

import time
import random

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from threading import Thread
from matplotlib import pyplot as plt

from .utilities import utilities
from .constants import constants_search_page as constants
from .constants.constants_db import DB_COMMAND_CONDITIONS_DICT
from .database.db_functions import DatabaseManager
from .selenium import selenium_functions


class SearchPage(Toplevel):
    def __init__(self, parent_self):
        Toplevel.__init__(self)
        self.parent_self = parent_self


    ###############  WINDOW  ###############
        width, height = utilities.center_window(
            screen_width=self.winfo_screenwidth(),
            screen_height=self.winfo_screenheight(),
            tk_window_width=1500, tk_window_height=650
        )
        self.geometry(f"1500x650+{width}+{height}")
        self.title("Fighter Researcher - Search Page")
        self.iconbitmap("app/static/project_photos/red-fist-icon.ico")
        self.resizable(False, False)


    ###############  FRAMES  ###############
        self.left_frame = Frame(
            master=self, bg='chocolate',
            borderwidth=5, relief=RIDGE,
        )
        self.left_frame.pack(side=LEFT, fill=Y)

        self.right_frame = Frame(
            master=self, bg='bisque',
            borderwidth=2, relief=SUNKEN, width=1090,
        )
        self.right_frame.pack(side=RIGHT, fill=Y)


    ###############  LEFT SEARCH BOX  ###############
        self.search_box = LabelFrame(
            master=self.left_frame, bg='chocolate',
            font='arial 16 bold', pady=15, width=250,
            text=constants.LEFT_SEARCH_BOX_TITLE,
        )
        self.search_box.pack(pady=(30,20))

        ##### ENTRY FOR FIGHTER NAME
        self.name_entry = Entry(
            master=self.search_box, width=31,
            font='times 12 bold', bd=5,
        )
        self.name_entry.pack()

        ##### SEARCH BUTTON
        self.name_button = Button(
            master=self.search_box, bg='grey',
            text='Search', font='arial 10 bold', width=15,
            command=self.find_fighter
        )
        self.name_button.pack()


    ###############  LEFT DATABASE BOX ###############
        self.database_box = LabelFrame(
            master=self.left_frame, bg='chocolate',
            font='arial 16 bold', pady=15,
            text=constants.LEFT_DB_BOX_TITLE,
        )
        self.database_box.pack()

        ##### FIGHTERS LIST
        self.fighters_list = Listbox(
            master=self.database_box,
            font='cambria 11', width=50, height=8
        )
        self.fighters_list.pack()

        ##### SCROLLBAR
        self.fighters_list_sb = Scrollbar(
            master=self.fighters_list, orient=VERTICAL,
            command=self.fighters_list.yview,
        )
        self.fighters_list.config(
            yscrollcommand=self.fighters_list_sb.set
        )
        self.fighters_list_sb.pack(
            padx=(379, 0), ipady=46
        )

        ###### ADDING FIGHTERS TO FIGHTERS LIST
        fighters_base = DatabaseManager().return_fighter_names()
        self.number = 0
        for fighter, alias, _ in fighters_base:
           self.number += 1
           alias = f" - {alias}" if alias else ''
           self.fighters_list.insert(
               self.number, f'{self.number}. {fighter}{alias}'
           )

        ###### DISPLAY BUTTON
        self.display_button = Button(
            master=self.database_box, bg='grey',
            text='Display', font='arial 10 bold', width=15,
            command=self.display_fighter_stats
        )
        self.display_button.pack()


    ###############  LEFT SORT BY BOX  ###############
        self.sort_box = LabelFrame(
            master=self.left_frame, bg='chocolate',
            font='arial 16 bold', pady=15,
            text=constants.LEFT_SORT_BOX_TITLE,
        )
        self.sort_box.pack(pady=10)

        ##### VARIANTS LIST
        self.sort_box_variants_list = Listbox(
            master=self.sort_box, font='cambria 11', width=50
        )
        self.sort_box_variants_list.pack()

        ##### SCROLLBAR
        self.sort_box_variants_list_sb = Scrollbar(
            master=self.sort_box_variants_list, orient=VERTICAL,
            command=self.sort_box_variants_list.yview
        )
        self.sort_box_variants_list.config(
            yscrollcommand=self.sort_box_variants_list_sb.set
        )
        self.sort_box_variants_list_sb.pack(padx=(379, 0), ipady=30)

        ##### SORT BY BUTTON
        self.sort_box_button = Button(
            master=self.sort_box, bg='grey',
            text='Sort by', font='arial 10 bold', width=15,
            command=self.sort_fighters
        )
        self.sort_box_button.pack()

        ##### ADDING VARIANTS TO VARIANTS LIST
        for index, variant in enumerate(constants.SORT_BOX_VARIANTS):
            index += 1
            self.sort_box_variants_list.insert(index, variant)


    ###############  FIGHTER PHOTO  ###############
        self.fighter_photo = PhotoImage(
            file=f'app/static/project_photos/{random.choice(("paladin", "mage_khajiit"))}.png'
        )
        self.fighter_photo_label = Label(
            master=self.right_frame, image=self.fighter_photo
        )
        self.fighter_photo_label.photo = self.fighter_photo
        self.fighter_photo_label.place(x=380, y=60)


    ###############  FIGHTER FLAG  ###############
        self.fighter_flag = PhotoImage()
        self.fighter_flag_label = Label(
            master=self.right_frame, image=self.fighter_flag
        )
        self.fighter_flag_label.flag = self.fighter_flag
        self.fighter_flag_label.place(x=380, y=25)


    ###############  BACK BUTTON  ###############
        self.back_button_img = PhotoImage(
            file="app/static/project_photos/back_button.png"
        )
        self.back_button = Button(
            master=self.right_frame, bg='white',
            text="Get Back  ", font='arial 12 bold', width=120,
            image=self.back_button_img, compound=RIGHT,
            command=self.get_back_to_home_page
        )
        self.back_button.photo = self.back_button_img
        self.back_button.place(x=960)


    ###############  TITLES  ###############
        index = 0
        for row in range(2):
           for column in range(2):
               setattr(
                   self, constants.TITLES[index],
                   Label(
                       master=self.right_frame, bg='bisque',
                       text=constants.TITLES[index],
                       font='arial 20 bold' if index != 2 else 'arial 18 bold',
                   )
               )
               getattr(self, constants.TITLES[index]).place(
                   x=10+column*590,
                   y=30+row*400
               )
               index += 1


    ###############  INFO TEXTS  ###############
        info_text_x_values = iter(constants.INFO_TEXT_X_VALUES)
        info_text_y_values = iter(constants.INFO_TEXT_Y_VALUES)
        for text in constants.INFO_TEXT_NAMES:
            setattr(
                self, text,
                Label(
                    master=self.right_frame, text=text,
                    bg='bisque', font='arial 12 bold',
                )
            )
            getattr(self, text).place(
                x=next(info_text_x_values),
                y=next(info_text_y_values),
            )


    ###############  INFO ENTRIES  ###############
        info_entry_x_values = iter(constants.INFO_ENTRY_X_VALUES)
        info_entry_y_values = iter(constants.INFO_ENTRY_Y_VALUES)
        for entry_name in constants.INFO_ENTRY_NAMES:
            setattr(
                self, entry_name,
                Entry(master=self.right_frame, width=25, font='arial 12 bold')
            )
            getattr(self, entry_name).place(
                x=next(info_entry_x_values),
                y=next(info_entry_y_values),
            )


    ###############  RIGHT STATISTIC ENTRIES  ###############
        stat_entry_x_values = iter(constants.STAT_ENTRY_X_VALUES)
        stat_entry_y_values = iter(constants.STAT_ENTRY_Y_VALUES)
        for index, entry_name in enumerate(constants.STAT_ENTRY_NAMES):
            setattr(
                self, entry_name,
                Entry(
                    master=self.right_frame, width=3 if index % 2==0 else 5,
                    font='arial 12 bold' if index % 2==0 else 'arial 10 bold'
                )
            )
            getattr(self, entry_name).place(
                x=next(stat_entry_x_values),
                y=next(stat_entry_y_values)
            )

        self.f_draws = Entry(
            master=self.right_frame, width=3, font='arial 12 bold'
        )
        self.f_draws.place(x=815, y=355)


    ###############  VIEW GRAPH BUTTON  ###############
        self.view_graph_button = Button(
            master=self.right_frame, text='View Graph',
            bg='grey', font='times 15 bold', width=12,
            command=self.view_statistic_graph
        )
        self.view_graph_button.place(x=890, y=355)


    ###############  BAR THEMES  ###############
        self.ttk_style = ttk.Style()
        self.ttk_style.theme_use('winnative')
        self.ttk_style.configure(
            "red.Horizontal.TProgressbar", background='red',
            troughcolor='gray90'
        )
        self.ttk_style.configure(
            "green.Horizontal.TProgressbar", background='green',
            troughcolor='gray90'
        )


    ###############  BARS  ###############
        y=0
        for bar_name in constants.BAR_NAMES:
            if bar_name == 'f_l_ko_bar':
                y+=29
            setattr(
                self, bar_name,
                ttk.Progressbar(
                    master=self.right_frame,
                    orient=HORIZONTAL, length=150, maximum=100, value=0,
                    style="green.Horizontal.TProgressbar" if y <= 66
                    else "red.Horizontal.TProgressbar",
                )
            )
            getattr(self, bar_name).place(x=850, y=180+y)
            y+=22


    ###############  UPCOMING FIGHTS  ###############
        self.upcoming_fights = Text(
            master=self.right_frame, height=10, width=40,
            font='cambria 11 bold', wrap=WORD
        )
        self.upcoming_fights.place(x=0, y=481)


    ###############  CAREER HISTORY  ###############
        self.career_history = Listbox(
            master=self.right_frame, height=9, width=88, font='cambria 11'
        )
        self.career_history.place(x=380, y=480)

        self.career_history_sb = Scrollbar(
            master=self.career_history, orient=VERTICAL,
            command=self.career_history.yview
        )
        self.career_history.config(
            yscrollcommand=self.career_history_sb.set
        )
        self.career_history_sb.pack(padx=(685, 0), ipady=56)


    ###############  THEMES  ###############
        self.themes_var = StringVar()
        self.themes_list = ttk.Combobox(
            master=self.right_frame, textvariable=self.themes_var,
            font='arial 12 bold', state='readonly', width=10,
            values=['Default', 'Dracula', 'Navy', 'Dark grey'],
        )
        self.themes_list.current(0)
        self.themes_list.place(x=817)
        self.themes_list.bind("<<ComboboxSelected>>", self.change_theme)
        self.themes_lbl = Label(
            master=self.right_frame, text='Theme:',
            font='arial 14 bold', bg='bisque', fg='black'
        )
        self.themes_lbl.place(x=740)


    #########################################
    ###############  METHODS  ###############

    def get_back_to_home_page(self):
        """Get back to Home Page by deiconifying
        it and destroying the actual one."""

        self.parent_self.master.deiconify()
        self.destroy()


    def change_theme(self, *args):
        """Change Search Page theme based on selected option."""

        text_list = [
            *constants.TITLES, *constants.INFO_TEXT_NAMES, 'themes_lbl',
        ]
        entry_list = [
            *constants.INFO_ENTRY_NAMES, *constants.STAT_ENTRY_NAMES,'f_draws',
        ]
        left_boxes = [
            self.search_box, self.database_box, self.sort_box
        ]

        colors_dict = utilities.colors_dict(theme=self.themes_list.get(), file='SEARCH_PAGE')

        for text in text_list:
            getattr(self, text).configure(
                bg=colors_dict['lbl_bg_color'],
                fg=colors_dict['lbl_fg_color'],
            )

        for entry in entry_list:
            getattr(self, entry).configure(
                bg=colors_dict['entry_bg_color'],
                fg=colors_dict['entry_fg_color'],
            )

        for box in left_boxes:
            box.configure(
                bg=colors_dict['left_frame'],
                fg=colors_dict['lbl_fg_color'],
            )

        self.right_frame.configure(bg=colors_dict['right_frame'])
        self.left_frame.configure(bg=colors_dict['left_frame'])
        self.upcoming_fights.configure(
            bg=colors_dict['entry_bg_color'],
            fg=colors_dict['entry_fg_color'],
        )


    def find_fighter(self):
        """Main function that dispose next steps in searching for a fighter.
           If we've got him in the base - return information about it.
           If not - ask the user if he wants to start searching for him."""

        fighter = self.name_entry.get().upper()
        search = True
        if not fighter:
            messagebox.showerror(title="Error!", message="Field can't be empty!")
        elif len(fighter) <= 3:
            messagebox.showerror(title="Error!", message="Name is too short!")
        elif fighter:
            for fighter_name in self.fighters_list.get(0, END):
                if fighter in fighter_name:
                    fighter_index = fighter_name.split('.')[0]
                    messagebox.showinfo(
                        title="Success!",
                        message=f"Fighter has been successfully found in our\n"
                                f"database on {fighter_index} position!"
                    )
                    search = False
                    break

            if search:
                mbox = messagebox.askquestion(
                    title="Search",
                    message="Fighter hasn't been found in our database.\n"
                            "Would You like to search him?\n"
                            "(it may take at most 30 seconds)")
                if mbox == 'yes':
                    # global start_time
                    # start_time = time.perf_counter()
                    # # we have to spawn a new process, otherwise Tkinter will get a crash
                    # background_finding_process = Thread(
                    #     target=self.add_fighter, args=[fighter]
                    # )
                    # background_finding_process.start()

                    # -------------------------------------------------------------
                    # created in case of github
                    messagebox.showinfo(
                        title='Info',
                        message="Due to the site's rights, I cannot share the "
                                "full searching algorithm. Instead, I encourage "
                                "You guys to have a look on a video & photos to "
                                "see how it is working in a real time (presentation dir).")


    def add_fighter(self, fighter_name):
        """Run selenium background task in order to
        grab fighter's informations & add them to the database."""

        try:
            # db create table if not exists
            DatabaseManager().create_main_db_table()

            # find fighter in a web
            selenium_functions.run_driver(fighter_name=fighter_name, headless=True)

            # grab his stats
            stat_list, career_history = selenium_functions.grab_fighter_info()

            # add to db
            DatabaseManager().add_fighter(stat_list, career_history)

            # insert to GUI list
            data = DatabaseManager().return_fighter_names()
            added_fighter = list(data)[-1]
            name = added_fighter[0]
            alias = f" - {added_fighter[1]}" if added_fighter[1] else ''
            self.number += 1
            self.fighters_list.insert(
                self.number,
                f"{self.number}. {name}{alias}"
            )

            # inform user about successful completion
            end_time = round(time.perf_counter()-start_time)
            messagebox.showinfo(
                title="Success!",
                message=f"Fighter has been successfully found and added to "
                        f"database in {end_time} seconds!",
            )
        except Exception as e:
            selenium_functions.close_driver()
            messagebox.showerror(
                title="Failed!",
                message="Sir, we've got a temporary error!"
            )
            print(e)


    def display_fighter_stats(self):
        """Fill entries & change photo based on selected fighter."""

        ######### check if any fighter has been selected
        selected_option = self.fighters_list.curselection()
        if not selected_option:
            messagebox.showerror(
                title='Display',
                message='You have to choose a fighter in order to do that!'
            )
            return

        ######### get fighter name from db
        person = self.fighters_list.get(selected_option)
        person_in_base = f"{person.split()[1]} {person.split()[2]}"

        for fighter in DatabaseManager().return_fighter_names():
            if person_in_base in fighter[0]:
                person_in_base = fighter[0]
                break

        ######### grab his stats
        data = DatabaseManager(
            ).return_fighter_info(fighter_name=person_in_base)


        ######### PHOTO & FLAG
        self.fighter_photo.configure(
            file=f'app/static/fighters_photos/{person_in_base}(photo).png'
        )
        self.fighter_flag.configure(
            file=f'app/static/fighters_photos/{person_in_base}(flag).png'
        )

        ######### INFO & STAT ENTRIES
        entries_name_list = [
            *constants.INFO_ENTRY_NAMES,
            *constants.STAT_ENTRY_NAMES,
            'f_draws',
        ]
        entry_abbreviations = iter(constants.ENTRY_ABBREVIATIONS)
        for index, entry_name in enumerate(entries_name_list):
            entry = getattr(self, entry_name)
            entry.configure(state='normal')
            entry.delete(0, END)
            entry.insert(0, f"{data[index]}{next(entry_abbreviations)}")

        ######### BARS
        index = 15
        for bar_name in constants.BAR_NAMES:
            bar = getattr(self, bar_name)
            bar.configure(value=data[index])
            index += 2

        ######### UPCOMING FIGHTS
        self.upcoming_fights.configure(state='normal')
        self.upcoming_fights.delete(0.0, 'end-1c')

        if data[-5] == '<<  No fight signed up at the moment  >>':
            self.upcoming_fights.insert(INSERT, data[-5])
        else:
            self.upcoming_fights.insert(
                INSERT, f"{10*'*'}    {data[-5]}    {10*'*'}\n\n")
            self.upcoming_fights.insert(
                INSERT, f"-->    {data[-4]}\n")
            self.upcoming_fights.insert(
                INSERT, f"-->    {data[-3]}\n\nFIGTERS:\n")
            self.upcoming_fights.insert(
                INSERT, f"\t{data[-2].split('VS')[0].strip()}      VS\n")
            self.upcoming_fights.insert(
                INSERT, f"\t{data[-2].split('VS')[1].strip()}")

        self.upcoming_fights.configure(state='disabled')

        ######### CAREER HISTORY
        fight_list = DatabaseManager(
            ).return_fighter_career_history(fighter_name=person_in_base)

        self.career_history.delete(0, END)
        for index, fight in enumerate(fight_list):
            result = fight[1]
            opponent = fight[2]
            event = fight[3].split('-')[0].strip()
            date = fight[4].replace(' / ', '-')
            how = fight[5].replace(' (', '-').replace(')', '')
            round_time = f"ROUND {fight[6]}({fight[7]})"
            row = \
                f"{index + 1}. {result}  VS  {opponent}, " \
                f"{event}({date}), {how},  {round_time}"
            self.career_history.insert(index, row)

            if result == 'WIN':
                row_color = 'green'
            elif result == 'LOSS':
                row_color = 'red'
            elif result == 'DRAW' or result == 'NC':
                row_color = 'orange'

            self.career_history.itemconfigure(index=index, bg=row_color)


    def sort_fighters(self):
        """Sort fighters based on selected option."""

        try:
            # grab selected option
            selected_option = self.sort_box_variants_list.get(
                self.sort_box_variants_list.curselection())

            # every option has its db command condition
            selected_db_command_condition = DB_COMMAND_CONDITIONS_DICT[
                selected_option
            ]

            # sort fighters based on selected option's command
            sorted_fighters = DatabaseManager().return_certain_fighter_list(
                condition=selected_db_command_condition
            )

            # replace GUI fighters list with the new one
            self.fighters_list.delete(0, END)
            for index, fighter in enumerate(sorted_fighters):
                index +=1
                fighter_name = fighter[0]
                fighter_alias = f" - {fighter[1]}" if fighter[1] else ''
                self.fighters_list.insert(
                    index, f"{index}. {fighter_name}{fighter_alias}")

        except Exception as e:
            print(e)
            messagebox.showerror(
               title="Error!",
               message="Select an option!"
            )


    def view_statistic_graph(self):
        """Show diagram representing dependency between
        fighter's age and amount of fights that he fought."""

        ######### check if any fighter has been selected
        selected_option = self.fighters_list.curselection()
        if not selected_option:
            messagebox.showerror(
                title="Graph",
                message="You have to choose a fighter in order to do that!"
            )
            return


        ######### get his name from db & grab his info
        person = self.fighters_list.get(selected_option)
        person_in_base = f"{person.split()[1]} {person.split()[2]}"

        for fighter in DatabaseManager().return_fighter_names():
            if person_in_base in fighter[0]:
                person_in_base = fighter[0]
                break

        fighter_info = DatabaseManager(
            ).return_fighter_info(fighter_name=person_in_base)
        fighter_career_history = DatabaseManager(
            ).return_fighter_career_history(fighter_name=person_in_base)


        ######### create x and y coordinates for graph
        born_in_year = int(fighter_info[7].split('-')[0])
        age_and_amount_of_fights = dict()

        for amount_of_fights, fight in enumerate(reversed(fighter_career_history)):
            amount_of_fights += 1

            fight_in_year = int(fight[4].split('/')[2])
            age_at_this_fight = fight_in_year - born_in_year

            # dict = age at actual fight (key) : amount of fights (value)
            age_and_amount_of_fights[age_at_this_fight] = amount_of_fights


        ######### create and adjust graph
        style_based_on_actual_theme = utilities.colors_dict(
            theme=self.themes_list.get(), file='SEARCH_PAGE')['graph']
        plt.style.use(style_based_on_actual_theme)

        plt.figure(figsize=(9, 5))
        plt.plot(
            age_and_amount_of_fights.keys(),            # age
            age_and_amount_of_fights.values(),          # amount of fights
            color='#0077ff', marker='s', markersize=7,
        )
        plt.title(
            label=person_in_base, y=1.04,
            font='Arial', fontsize='20', fontweight='bold',
        )
        plt.xlabel("Age", fontsize='14')
        plt.ylabel("Amount Of Fights", fontsize='14', labelpad=17)
        plt.tick_params(labelsize=13)
        plt.show()
