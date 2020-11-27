
##### compare_page.py
##### This module contains the GUI Compare Page window, which allows us to
#####      compare any two available in database fighters.

import numpy as np
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from matplotlib import pyplot as plt

from Code_additions import utilities
from Code_additions import constants_compare_page as constants
from Database.sql_functions import DatabaseManager
from Database.sql_constants import db_command_conditions_dict


class ComparePage(Toplevel):
    def __init__(self, parent_self):
        Toplevel.__init__(self)
        self.parent_self = parent_self


    ###############  WINDOW  ###############
        width, height = utilities.center_window(
            screen_width=self.winfo_screenwidth(),
            screen_height=self.winfo_screenheight(),
            tk_window_width=1500, tk_window_height=700
        )
        self.geometry(f"1500x700+{width}+{height}")
        self.title("Fighter Researcher - Compare Page")
        self.iconbitmap("Static/project_photos/red-fist-icon.ico")
        self.resizable(False, False)


    ###############  FRAMES  ###############
        self.left_frame = Frame(
            master=self, bg='bisque',
            borderwidth=3, relief=SUNKEN, width=1096)
        self.left_frame.pack(side=LEFT, fill=Y)

        self.right_frame = Frame(
            master=self, bg='chocolate',
            borderwidth=5, relief=RIDGE)
        self.right_frame.pack(side=RIGHT, fill=Y)


    ###############  RIGHT DATABASE BOX  ###############
        self.database_box = LabelFrame(
            master=self.right_frame, bg='chocolate',
            font='arial 16 bold', pady=15,
            text=constants.right_db_box_title,
        )
        self.database_box.pack(pady=(60, 0))

        ##### FIGHTERS LIST
        self.fighters_list = Listbox(
            master=self.database_box,
            font='cambria 11', width=48, height=9,
        )
        self.fighters_list.grid(row=0, column=0, padx=(2, 0))

        ##### SCROLLBAR
        self.fighters_list_sb = Scrollbar(
            master=self.fighters_list, orient=VERTICAL,
            command=self.fighters_list.yview,
        )
        self.fighters_list.config(
            yscrollcommand=self.fighters_list_sb.set
        )
        self.fighters_list_sb.pack(
            padx=(370, 0), ipady=55
        )

        ###### ADDING FIGHTERS TO FIGHTERS LIST
        fighters_base = DatabaseManager().return_fighter_names()
        self.number = 0
        for name, alias, _ in fighters_base:
            self.number += 1
            alias = f"  -  {alias}" if alias else ''
            self.fighters_list.insert(
                self.number, f'{self.number}. {name}{alias}'
            )

        ###### DISPLAY BUTTONS
        self.first_fighter_choose_btn = Button(
            master=self.database_box, width=20, bg='grey',
            font='arial 10 bold', text='Choose First Fighter',
            command=lambda: self.display_fighter('first')
        )
        self.first_fighter_choose_btn.grid(row=1, pady=(15, 0))

        self.second_fighter_choose_btn = Button(
            master=self.database_box, width=20, bg='grey',
            font='arial 10 bold', text='Choose Second Fighter',
            command=lambda: self.display_fighter('second')
        )
        self.second_fighter_choose_btn.grid(row=3, pady=(15, 0))

        ###### ENTRIES
        for entry_name in constants.right_fighter_name_entries:
            setattr(
                self, entry_name,
                Entry(
                    master=self.database_box, font='cambria 12', width=41
                )
            )
            getattr(self, entry_name).grid(
                row=2 if 'first' in entry_name else 4,
                ipady=2, pady=(5,0))


    ###############  RIGHT SORT BY BOX  ###############
        self.sort_box = LabelFrame(
            master=self.right_frame, bg='chocolate',
            font='arial 16 bold', pady=15,
            text=constants.right_sort_box_title,
        )
        self.sort_box.pack(pady=(30, 0))

        ##### VARIANTS LIST
        self.sort_box_variants_list = Listbox(
            master=self.sort_box, font='cambria 11', width=49, height=6)
        self.sort_box_variants_list.grid(row=0, column=0)

        ##### SCROLLBAR
        self.sort_box_variants_list_sb = Scrollbar(
            master=self.sort_box_variants_list, orient=VERTICAL,
            command=self.sort_box_variants_list.yview
        )
        self.sort_box_variants_list.config(
            yscrollcommand=self.sort_box_variants_list_sb.set
        )
        self.sort_box_variants_list_sb.pack(padx=(370, 0), ipady=30)

        ##### SORT BY BUTTON
        self.sort_box_button = Button(
            master=self.sort_box, bg='grey', width=15,
            text='Sort by', font='arial 10 bold',
            command=self.sort_fighters
        )
        self.sort_box_button.grid(row=1, column=0)

        ##### ADDING VARIANTS TO VARIANTS LIST
        for index, variant in enumerate(constants.sort_box_variants):
            index += 1
            self.sort_box_variants_list.insert(index, variant)


     ###############  BACK BUTTON   ###############
        self.back_button_img = PhotoImage(
            file="Static/project_photos/back_button.png"
        )
        self.back_button = Button(
            master=self, bg='grey',
            text="Get Back  ", font='arial 12 bold', width=120,
            image=self.back_button_img, compound=RIGHT,
            command=self.get_back_to_home_page
        )
        self.back_button.photo = self.back_button_img
        self.back_button.place(x=1366, y=6)


    ###############  THEMES   ###############
        self.themes_var = StringVar()
        self.themes_list = ttk.Combobox(
            master=self.right_frame, textvariable=self.themes_var,
            font='arial 12 bold', state='readonly', width=10,
            values=['Default', 'Dracula', 'Navy', 'Dark grey'],
        )
        self.themes_list.current(0)
        self.themes_list.place(x=80)
        self.themes_list.bind("<<ComboboxSelected>>", self.change_theme)
        self.themes_lbl = Label(
            master=self.right_frame, text='Theme:',
            font='arial 14 bold', bg='chocolate', fg='black'
        )
        self.themes_lbl.place(x=0)


    ############### FIRST FIGHTER  ###############
        ##### NAME
        self.first_name = Entry(
            master=self.left_frame, width=25, font='arial 20 bold'
        )
        self.first_name.place(x=10, y=30)
        self.first_name.insert(
            0,
            utilities.compare_page_center_name_or_stat(
                obj='Force Khajiit', stat_or_name='name'
            )
        )

        ##### PHOTO
        self.first_photo = PhotoImage(
            file='Static/project_photos/mage_khajiit.png'
        )
        self.first_photo_label = Label(
            master=self.left_frame, image=self.first_photo
        )
        self.first_photo_label.photo = self.first_photo
        self.first_photo_label.place(x=10, y=85)

        ##### FLAG
        self.first_flag = PhotoImage()
        self.first_flag_label = Label(
            master=self.left_frame, image=self.first_flag
        )
        self.first_flag_label.photo = self.first_flag
        self.first_flag_label.place(x=390, y=29)


    ############### SECOND FIGHTER  ###############
        ##### NAME
        self.second_name = Entry(
            master=self.left_frame, width=25, font='arial 20 bold'
        )
        self.second_name.place(x=700, y=30)
        self.second_name.insert(
            0,
            utilities.compare_page_center_name_or_stat(
                obj="Light Paladin", stat_or_name='name',
            )
        )

        ##### PHOTO
        self.second_photo = PhotoImage(
            file='Static/project_photos/paladin.png'
        )
        self.second_photo_label = Label(
            master=self.left_frame, image=self.second_photo
        )
        self.second_photo_label.photo = self.second_photo
        self.second_photo_label.place(x=870, y=85)

        ##### FLAG
        self.second_flag = PhotoImage()
        self.second_flag_label = Label(
            master=self.left_frame, image=self.second_flag
        )
        self.second_flag_label.photo = self.second_flag
        self.second_flag_label.place(x=650, y=29)


    ###############  VS LABEL  ###############
        self.vs_label = Label(
            master=self.left_frame, text='VS', font='arial 40 bold', bg='bisque'
        )
        self.vs_label.place(x=500, y=20)


    ###############  INFO LABELS  ###############
        y = 0
        for text in constants.info_text_names:
            setattr(
                self, text,
                Label(
                    master=self.left_frame, text=text,
                    bg='bisque', font='arial 14 bold'
                )
            )
            getattr(self, text).place(x=430, y=110 + y)
            y += 40


    ###############  INFO ENTRIES  ###############
        info_entry_names_x_values = iter(constants.info_entry_names_x_values)
        info_entry_names_y_values = iter(constants.info_entry_names_y_values)
        for entry_name in constants.info_entry_names:
            setattr(
                self, entry_name,
                Entry(
                    master=self.left_frame,
                    width=20, font='arial 14 bold'
                )
            )
            getattr(self, entry_name).place(
                x=next(info_entry_names_x_values),
                y=next(info_entry_names_y_values),
            )


    ###############  STAT TITLE LABELS  ###############
        stat_title_text_x_values = iter(constants.stat_title_text_x_values)
        for text in constants.stat_title_text_names:
            setattr(
                self, text,
                Label(
                    master=self.left_frame, text=text,
                    font='arial 18 bold', bg='bisque',
                )
            )
            getattr(self, text).place(
                x=next(stat_title_text_x_values), y=395
            )


    ###############  STAT LABELS  ###############
        stat_text_x_values = iter(constants.stat_text_x_values)
        for label_name, label_text in constants.stat_text_names.items():
            setattr(
                self, label_name,
                Label(
                    master=self.left_frame, text=label_text,
                    font='arial 12 bold', bg='bisque'
                )
            )
            getattr(self, label_name).place(
                x=next(stat_text_x_values),
                y=440
            )


    ###############  STAT ENTRIES  ###############
        stat_entry_names_x_values = iter(constants.stat_entry_names_x_values)
        stat_entry_names_y_values = iter(constants.stat_entry_names_y_values)
        for index, entry_name in enumerate(constants.stat_entry_names):
            setattr(
                self, entry_name,
                Entry(
                    master=self.left_frame,
                    width=4 if index <=11 else 5,
                    font='arial 12 bold' if index <=11 else 'arial 10 bold'
                )
            )
            getattr(self, entry_name).place(
                x=next(stat_entry_names_x_values),
                y=next(stat_entry_names_y_values)
            )


    ###############  BAR COLORS  ###############
        self.ttk_style = ttk.Style()
        self.ttk_style.theme_use('winnative')
        self.ttk_style.configure(
            "red.Vertical.TProgressbar", background='red', troughcolor='gray90'
)
        self.ttk_style.configure(
            "green.Vertical.TProgressbar", background='green', troughcolor='gray90'
        )


    ###############  BARS  ###############
        bar_x_values = iter(constants.bar_x_values)
        for index, bar_name in enumerate(constants.bar_list):
            setattr(
                self, bar_name,
                ttk.Progressbar(
                    master=self.left_frame, orient=VERTICAL,
                    length=150, maximum=100, value=0,
                    style="red.Vertical.TProgressbar" if '_l_' in bar_name
                    else "green.Vertical.TProgressbar")
            )
            getattr(self, bar_name).place(
                x=next(bar_x_values), y=495
            )


    ###############  VIEW GRAPH BUTTON  ###############
        self.view_graph_button = Button(
            master=self.left_frame, text='VIEW\nGRAPH',
            bg='grey', font='Times 18 bold', width=10,
            command=self.view_statistic_graph,
        )
        self.view_graph_button.place(x=475, y=480)


    #########################################
    ###############  METHODS  ###############

    def get_back_to_home_page(self):
        """Get back to Home Page by deiconifying
        it and destroying the actual one."""

        self.parent_self.master.deiconify()
        self.destroy()


    def change_theme(self, *args):
        """Change Compare Page theme based on selected option."""

        text_list = [
            *constants.info_text_names,
            *constants.stat_title_text_names,
            *constants.stat_text_names.keys(),
            'vs_label', 'themes_lbl'
        ]
        entry_list = constants.info_entry_names
        right_boxes = [self.database_box, self.sort_box, self.themes_lbl]

        colors_dict = constants.compare_colors_dict(self.themes_list.get())

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

        for box in right_boxes:
            box.configure(
                bg=colors_dict['right_frame'],
                fg=colors_dict['lbl_fg_color'],
            )

        self.right_frame.configure(bg=colors_dict['right_frame'])
        self.left_frame.configure(bg=colors_dict['left_frame'])


    def display_fighter(self, which):
        """Based on passed argument, fill entries with
        proper values & changes photos for first or second fighter."""

    ##########  CONTROL  ##########
        display = False
        selected_fighter = self.fighters_list.curselection()

        fighter_name_from_entry = self.first_fighter_choose_entry.get() \
            if which == 'first' else self.second_fighter_choose_entry.get()
        fighter_name_from_entry = fighter_name_from_entry.upper()

        ### NO SELECT  &  NO WRITE
        if not selected_fighter and not fighter_name_from_entry:
            messagebox.showerror(
                title='Error!',
                message="Choose fighter from database or write his name!!!"
            )

        ### NO SELECT  &  WRITE <= 3
        elif not selected_fighter and len(fighter_name_from_entry) <= 3:
            messagebox.showerror(
                title="Error!",
                message="Can't match any fighter with a few letters!!!"
            )

        ### NO SELECT  &  WRITE > 3
        elif not selected_fighter and fighter_name_from_entry:
            error = True
            for fighter_name_from_list in self.fighters_list.get(0, END):
                if fighter_name_from_entry in fighter_name_from_list:
                    person = fighter_name_from_list
                    error = False
                    display = True
                    break
            if error:
                messagebox.showerror(
                    title='Error!',
                    message="Fighter has not been found in our database!\n"
                            "Maybe You've done some misspelling?"
                )

        ### SELECT
        elif selected_fighter:
            person = self.fighters_list.get(selected_fighter)
            display = True

        ### FINAL CONTROL
        if not display:
            return


    ##########  CONTROL PASSED, LET'S START WITH DISPLAYING  ##########
        ### RIGHT BOX ENTRY
        if which == 'first':
            self.first_fighter_choose_entry.delete(0, END)
            self.first_fighter_choose_entry.insert(
                0, person.split(maxsplit=1)[1])
        elif which == 'second':
            self.second_fighter_choose_entry.delete(0, END)
            self.second_fighter_choose_entry.insert(
                0, person.split(maxsplit=1)[1])


        ### GRAB FIGHTER INFOS
        person_in_base = f"{person.split()[1]} {person.split()[2]}"
        for fighter in DatabaseManager().return_fighter_names():
            if person_in_base in fighter[0]:
                person_in_base = fighter[0]
                break

        fighter_stats = DatabaseManager().return_fighter_stats_for_comparing(
            fighter_name=person_in_base
        )


        ### PHOTO, FLAG, TITLE
        if which == 'first':
            self.first_photo.configure(
                file=f'Static/fighters_photos/{person_in_base}(photo).png')
            self.first_flag.configure(
                file=f'Static/fighters_photos/{person_in_base}(flag).png')

            self.first_name.delete(0, END)
            self.first_name.insert(
                index=0, string=utilities.compare_page_center_name_or_stat(
                    obj=fighter_stats[0], stat_or_name='name')
            )
        elif which == 'second':
            self.second_photo.configure(
                file=f'Static/fighters_photos/{person_in_base}(photo).png')
            self.second_flag.configure(
                file=f'Static/fighters_photos/{person_in_base}(flag).png')

            self.second_name.delete(0, END)
            self.second_name.insert(
                index=0, string=utilities.compare_page_center_name_or_stat(
                    obj=fighter_stats[0], stat_or_name='name'))


        ### ENTRIES
        entry_list = constants.first_fighter_entry_names_for_displaying if \
            which == 'first' else constants.second_fighter_entry_names_for_displaying

        entry_abbreviations = iter(constants.entry_abbreviations)
        fighter_stats = list(fighter_stats)
        fighter_stats[3] = f"{fighter_stats[3]}KG / {fighter_stats[4]}CM"
        del fighter_stats[4]

        for index, entry_name in enumerate(entry_list):
            index += 1
            entry = getattr(self, entry_name)
            entry.delete(0, END)

            entry.insert(
                    0, utilities.compare_page_center_name_or_stat(
                        obj=str(fighter_stats[index]) + next(entry_abbreviations),
                        stat_or_name='stat' if index > 7 else None,
                    )
                )

        ### BARS
        fighter_bar_list = [*constants.bar_list[6:12], *constants.bar_list[:6]] \
            if which == 'first' else constants.bar_list[12:]
        index = 9
        for control, bar_name in enumerate(fighter_bar_list):
            if control != 0 and control % 2 == 0:
                index += 2
            getattr(self, bar_name).configure(value=fighter_stats[index])


    def sort_fighters(self):
        """Based on selected option, group and order
        fighters in a certain schedule in GUI database."""

        try:
            # grab selected option from list
            selected_option = self.sort_box_variants_list.get(
                self.sort_box_variants_list.curselection())

            # grab proper db command based on selected option
            selected_db_command_condition = db_command_conditions_dict[
                selected_option
            ]

            # grab appropriate fighters
            sorted_fighters = DatabaseManager().return_certain_fighter_list(
                condition=selected_db_command_condition
            )

            # add them to gui list
            self.fighters_list.delete(0, END)
            for index, fighter in enumerate(sorted_fighters):
                index += 1
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
        """Show daiagram representing dependency of
        fighter's age and amount of fights that he has fought."""

        ######### check if any fighter has been selected
        first_fighter = self.first_fighter_choose_entry.get().strip()
        second_fighter = self.second_fighter_choose_entry.get().strip()

        if not all([first_fighter, second_fighter]):
            messagebox.showerror(
                title="Graph",
                message="You have to choose 2 fighters in order to do that!"
            )
            return

        ######### get their names from db & grab their stats
        first_fighter_in_db = f"{first_fighter.split()[0]} {first_fighter.split()[1]}"
        second_fighter_in_db = f"{second_fighter.split()[0]} {second_fighter.split()[1]}"

        for fighter in DatabaseManager().return_fighter_names():

            if first_fighter_in_db in fighter[0]:
                first_fighter_in_db = fighter[0]
            if second_fighter_in_db in fighter[0]:
                second_fighter_in_db = fighter[0]

        first_fighter_stats = DatabaseManager(
            ).return_fighter_stats_for_comparing_graph(
            fighter_name=first_fighter_in_db
        )
        second_fighter_stats = DatabaseManager(
            ).return_fighter_stats_for_comparing_graph(
            fighter_name=second_fighter_in_db
        )

        ######### create and adjust graph
        style_based_on_actual_theme = constants.compare_colors_dict(
            self.themes_list.get())['graph']
        plt.style.use(style_based_on_actual_theme)
        plt.figure(figsize=(10, 5))

        x_indexes = np.arange(len(constants.graph_x_values))
        bar_width = 0.3

        plt.bar(
            x_indexes - bar_width/2,
            first_fighter_stats,
            width=bar_width,
            label=first_fighter_in_db
        )
        plt.bar(
            x_indexes + bar_width/2,
            second_fighter_stats,
            width=bar_width,
            label=second_fighter_in_db
        )
        plt.title(
            label=f"Warrior Fights Comparison",
            y=1.04, font='Arial', fontsize='20', fontweight='bold',
        )
        plt.xticks(ticks=x_indexes, labels=constants.graph_x_values)
        plt.xlabel("Fight Results", fontsize=15, labelpad=8)
        plt.ylabel("Amount Of Fights", fontsize=15, labelpad=10)
        plt.tick_params(labelsize=10)
        plt.legend()
        plt.grid()
        plt.tight_layout()
        plt.show()
