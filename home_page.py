
##### home_page.py
#####   This file contains the main GUI page of the project.

import time
import datetime
import multiprocessing
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from search_page import SearchPage
from compare_page import ComparePage
from Code_additions import utilities
from Code_additions import constants_home_page as constants
from Database.sql_functions import (DatabaseManager,
                                    multiprocessing_update_fighter)



class HomePage:
    def __init__(self, master):
        self.master = master
        self.actual_language = 'eng'
        self.fighter_url_list = DatabaseManager().return_fighter_urls()
        self.amount_of_fighters = len(self.fighter_url_list)
        self.index = 0
        self.counter = None


    ###############  BACKGROUND IMAGE  ###############
        background_img = PhotoImage(
            file='Static/project_photos/background_image.png'
        )
        self.canvas_background = Canvas(
            master=self.master, width=626, height=915,
            borderwidth=0, highlightthickness=0
        )
        self.canvas_background.pack()
        self.canvas_background.create_image(
            0, 0, image=background_img, anchor="nw"
        )


    ###############  LANGUAGE  ###############
        english_flag_icon = PhotoImage(
            file='Static/project_photos/en_flag.png'
        )
        polish_flag_icon = PhotoImage(
            file='Static/project_photos/pl_flag.png'
        )

        self.btn_english_version = Button(
            master=self.master, bg='black', fg='white', activebackground='snow',
            text="English  ", font='times 10 bold', width=75,
            image=english_flag_icon, compound=RIGHT,
            command=lambda: self.change_language('eng')
        )
        self.btn_polish_version = Button(
            master=self.master, bg='black', fg='white', activebackground='snow',
            text="Polish    ", font='times 10 bold', width=75,
            image=polish_flag_icon, compound=RIGHT,
            command=lambda: self.change_language('pl')
        )

        self.btn_english_version.image = english_flag_icon
        self.btn_polish_version.image = polish_flag_icon

        self.btn_english_version.place(x=10, y=10)
        self.btn_polish_version.place(x=10, y=34)


    ###############  DATE  ###############
        self.todays_date = str(datetime.date.today())
        self.todays_date_text = self.canvas_background.create_text(
            468, 24, font='arial 12', fill="white", text=f"Today's date:",
        )
        self.todays_date_number = self.canvas_background.create_text(
            570, 25, font='arial 12', fill="white", text=self.todays_date,
        )


    ###############  PREFACE TEXT  ###############
        self.preface_text1 = self.canvas_background.create_text(
            315, 115, font='times 18 bold', fill="white",
            text="This application was developed by programmer"
        )
        self.preface_text2 = self.canvas_background.create_text(
            315, 160, font='times 26 bold', fill="white",
            text="Adam Mańk",
        )


    ###############  BUTTON SEARCH  ###############
        btn_search_image = PhotoImage(
            file='Static/project_photos/red_fist.png'
        )
        self.btn_search = Button(
            master=self.master, bg='black', fg='white', activebackground='snow',
            text="  Search for Fighter   ", font='arial 13 bold',
            image=btn_search_image, compound=LEFT,
            command=lambda: self.open_new_page('search_page')
        )
        self.btn_search.image = btn_search_image
        self.btn_search.place(x=8, y=380)


    ###############  BUTTON COMPARE  ###############
        btn_compare_image = PhotoImage(
            file='Static/project_photos/compare_icon.png'
        )
        self.btn_compare = Button(
            master=self.master, bg='black', fg='white', activebackground='snow',
            text=" Compare Fighters   ", font='arial 13 bold',
            image=btn_compare_image, compound=RIGHT,
            command=lambda: self.open_new_page('compare_page')
        )
        self.btn_compare.image = btn_compare_image
        self.btn_compare.place(x=395, y=380)


    ###############  LAST UPDATE NOTE  ###############
        with open(file="Static/Last_update.txt", mode='r') as f:
            date_of_last_update = f.readline()
            f.close()
        self.last_update_text = self.canvas_background.create_text(
            315, 595, font='times 20 bold', fill="white", text="Last update",
        )
        self.last_update_date = self.canvas_background.create_text(
            315, 635, font='times 14 bold', fill="white", text=date_of_last_update,
        )


    ###############  UPDATE BUTTON  ###############
        btn_update_image = PhotoImage(
            file="Static/project_photos/update_icon.png"
        )
        self.btn_update = Button(
            master=self.master, bg='black', fg='white', activebackground='snow',
            text="Update Fighters stats", font='arial 12 bold', width=24,
            command=self.update_fighters_btn_command
        )
        self.btn_update.image = btn_update_image
        self.btn_update.place(x=195, y=670)


    ###############  UPDATE BAR THEME  ###############
        self.ttk_style = ttk.Style()
        self.ttk_style.theme_use('winnative')
        self.ttk_style.configure(
            "green.Horizontal.TProgressbar", background='green',
            troughcolor='gray90'
        )
        # ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')

    ###############  UPDATE BAR & TEXT  ###############
        self.update_process_bar = ttk.Progressbar(
            master=self.master, orient=HORIZONTAL,
            length=500, maximum=self.amount_of_fighters,
            style="green.Horizontal.TProgressbar"
        )
        self.update_process_text = self.canvas_background.create_text(
            315, 810, font='times 20 bold', fill="green",
            text=f"",
        )


    ###############  RUN APP  ###############
        self.master.mainloop()


    #########################################
    ###############  METHODS  ###############

    def change_language(self, language):
        """Change Home Page elements language."""

        # Control
        if self.actual_language == language:
            return

        # Set actual language
        self.actual_language = language

        # Set proper data based on choosed language
        tk_obj_values_dict = constants.eng_tk_obj_values_dict if \
            language == 'eng' else constants.pl_tk_obj_values_dict
        canv_obj_values_dict = constants.eng_canv_obj_values_dict if \
            language == 'eng' else constants.pl_canv_obj_values_dict

        # Translate Tkinter elements
        for obj in tk_obj_values_dict.items():
            obj_name = obj[0]
            obj_trans_text = obj[1][0]
            obj_width_attr = obj[1][1]
            obj_x_coordinate = obj[1][2]
            obj_y_coordinate = obj[1][3]

            getattr(self, obj_name).configure(
                text=obj_trans_text, width=obj_width_attr,
            )
            getattr(self, obj_name).place(
                x=obj_x_coordinate, y=obj_y_coordinate
            )

        # Translate Canvas elements
        for obj in canv_obj_values_dict.items():
            obj_name = obj[0]
            obj_trans_text = obj[1]

            canvas_obj = getattr(self, obj_name)

            self.canvas_background.itemconfigure(
                tagOrId=canvas_obj, text=obj_trans_text,
            )


    def open_new_page(self, page_name):
        """Open Search or Compare Page based on passed
        argument (clicked button) and minimize the actual one."""

        # minimize actual window
        self.master.iconify()

        # open the new chosen one
        SearchPage(parent_self=self) if page_name == 'search_page' \
            else ComparePage(parent_self=self)


    def update_fighters_btn_command(self):
        """Ask user a question if he wants to update fighter stats.
        If yes - show update process elements & run update_fighters method """

        # ask user a question
        mbox = messagebox.askquestion(
            title="Update Fighters",
            message="Are You sure You want to update fighter stats?\n"
                    "It will take at most 2 minutes.\n"
                    "Of course You will be informed about all the process :).")

        if mbox == 'yes':

            # run time counter
            # self.counter = time.perf_counter()

            # show update bar
            self.update_process_bar.place(x=63, y=770)

            # show update text
            self.canvas_background.itemconfigure(
                tagOrId=self.update_process_text,
                text=f"0/{self.amount_of_fighters}")

            # change last update info
            self.canvas_background.itemconfigure(
                tagOrId=self.last_update_date,
                text=self.todays_date
            )

            # save the new date of an update
            with open(file="Static/last_update.txt", mode='w+') as f:
                f.write(self.todays_date)
                f.close()

            # run updating method
            # self.update_fighters(fighter_url_list=self.fighter_url_list)

            #-------------------------------------------------------------
            # created in case of github
            messagebox.showinfo(
                title='Info',
                message="Due to the site's rights, I cannot share the "
                        "full searching algorithm. Instead, I encourage "
                        "You guys to have a look on a video & photos to "
                        "see how it is working in a real time (Presentation dir)."
                        "\nHave a nice day!")
            self.canvas_background.itemconfigure(
                tagOrId=self.update_process_text,
                text=f"{self.amount_of_fighters}/{self.amount_of_fighters}")
            self.update_process_bar.configure(value=self.amount_of_fighters)


    def update_fighters(self, fighter_url_list):
        """Use  multiprocessing.Process  in a for loop
        to update every fighter at the same time."""

        for fighter_url in fighter_url_list:
            url = fighter_url[0]

            # we have to spawn a new process, otherwise Tkinter will get a crash
            update_fighter_process = multiprocessing.Process(
                target=multiprocessing_update_fighter, args=[url])

            # start a process
            update_fighter_process.start()

            # check process status
            self.check_process(update_fighter_process)


    def check_process(self, process):
        """Update Home Page GUI window (load a bar),
        whenever a fighter has been successfully updated."""

        if not process.is_alive():                    # Process is done. Update GUI.
            print(
                "we're done with one sir  =  ", process.name
            )

            # join process, increase index
            process.join()
            self.index += 1

            # update GUI bar
            self.update_process_bar.configure(value=self.index)

            # update GUI text
            self.canvas_background.itemconfigure(
                tagOrId=self.update_process_text,
                text=f"{self.index}/{self.amount_of_fighters}")

            # if all the processes have ended
            if self.index == self.amount_of_fighters:
                total_update_time = round(
                    time.perf_counter() - self.counter
                )
                messagebox.showinfo(
                    title='Success!!!',
                    message="All fighters have successfully went through the update process in "
                            f"{total_update_time} seconds!")
                self.index = 0
                self.counter = None

        else:                                         # Not done yet. Check again later.
            self.master.after(
                5000, self.check_process, process
            )



def base():
    window = Tk()
    width, height = utilities.center_window(
        screen_width=window.winfo_screenwidth(),
        screen_height=window.winfo_screenheight(),
        tk_window_width=626, tk_window_height=915,
    )
    window.geometry(f"626x900+{width}+{height}")
    window.title("Fighter Researcher - Home Page")
    window.iconbitmap("Static/project_photos/red-fist-icon.ico")
    window.resizable(False, False)
    HomePage(window)


if __name__ == '__main__':
    base()
