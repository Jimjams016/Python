import re
import time
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk


import Backend




class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Tournament")

        container = ttk.Frame(self)
        container.grid(padx=10, pady=10, sticky="EW")

        self.frames = dict()

        for FrameClass in (MainMenu, Competitors, Events, Leaderboards, Activities, Admin, Pointscoring):
            frame = FrameClass(container, self)
            self.frames[FrameClass] = frame
            frame.grid(row=0, column=0, sticky="NESW")

        self.show_frame(MainMenu)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()






class MainMenu(ttk.Frame, App):

    def __init__(self, container, controller):
        super().__init__(container)

        self.LeftFrame = ttk.Frame(self, padding=(20, 10))
        self.LeftFrame.grid(row=0, column=0, sticky="EW")
        self.LeftFrame.columnconfigure(0, weight=1)

        self.CentreFrame = ttk.Frame(self, padding=(20, 10))
        self.CentreFrame.grid(row=0, column=1, sticky="EW")
        self.CentreFrame.columnconfigure(0, weight=1)

        self.RightFrame = ttk.Frame(self, padding=(20, 10))
        self.RightFrame.grid(row=0, column=2, sticky="EW")
        self.RightFrame.columnconfigure(0, weight=1)

        self.BottomFrame = ttk.Frame(self, padding=(0, 0))
        self.BottomFrame.grid(row=1, column=0, columnspan=3, sticky="EW")
        self.BottomFrame.columnconfigure(0, weight=1)

        self.Sport = ImageTk.PhotoImage(file='Sports1.png')
        tk.Label(self.LeftFrame, image=self.Sport, anchor='w').grid(row=1, column=0, sticky='w')

        self.Academic = ImageTk.PhotoImage(file='Academic image1.jpg')
        tk.Label(self.LeftFrame, image=self.Academic, anchor='w').grid(row=1, column=1, sticky='w')

        TitleLabel = ttk.Label(self.LeftFrame, text="Main Menu", background="black", foreground="white",
                                   font=("Montserrat", 28))
        TitleLabel.grid(row=0, column=0, sticky="EW")

        btnCompetitors = ttk.Button(self.BottomFrame, text="All Competitors", command=lambda: controller.show_frame(Competitors))
        btnCompetitors.grid(row=0, column=0, sticky="EW")

        btnEvents = ttk.Button(self.BottomFrame, text="All Events", command=lambda: controller.show_frame(Events))
        btnEvents.grid(row=0, column=1, sticky="EW")

        btnLeaderBoards = ttk.Button(self.BottomFrame, text="Leader Boards", command=lambda: controller.show_frame(Leaderboards))
        btnLeaderBoards.grid(row=0, column=2, sticky="EW")

        btnActivities = ttk.Button(self.BottomFrame, text="All Activities", command=lambda: controller.show_frame(Activities))
        btnActivities.grid(row=1, column=0, sticky="EW")

        btnAdmin = ttk.Button(self.BottomFrame, text="Admin", command=lambda: controller.show_frame(Admin))
        btnAdmin.grid(row=1, column=1, sticky="EW")

        btnPointScoring = ttk.Button(self.BottomFrame, text="Point Scoring", command=lambda: controller.show_frame(Pointscoring))
        btnPointScoring.grid(row=1, column=2, sticky="EW")

        btnExit = ttk.Button(self.BottomFrame, text="Exit", command=self.master.destroy)
        btnExit.grid(row=3, column=3, sticky="EW")





class Competitors(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)

        self.forenametext = tk.StringVar()
        self.surnametext = tk.StringVar()
        self.teamnametext = tk.StringVar()
        self.CompetitorIDtext = tk.StringVar()
        self.competitortypetext = tk.StringVar()


        lblTitle = ttk.Label(self, text='Competitors', font=("montserrat", 22, 'bold'), foreground="blue")
        lblTitle.grid(row=0, column=0, sticky="w")

        self.LeftFrame = ttk.Frame(self, padding=(20, 10))
        self.LeftFrame.grid(row=0, column=0, sticky="EW")
        self.LeftFrame.columnconfigure(0, weight=1)

        self.CentreFrame = ttk.Frame(self, padding=(20, 10))
        self.CentreFrame.grid(row=0, column=1, sticky="EW")
        self.CentreFrame.columnconfigure(0, weight=1)

        self.RightFrame = ttk.Frame(self, padding=(20, 10))
        self.RightFrame.grid(row=0, column=2, sticky="EW")
        self.RightFrame.columnconfigure(0, weight=1)

        self.BottomFrame = ttk.Frame(self, padding=(0, 0))
        self.BottomFrame.grid(row=1, column=0, columnspan=3, sticky="EW")
        self.BottomFrame.columnconfigure(0, weight=1)

        CompetitorsLabel = ttk.Label(self.LeftFrame, text="All competitors", background="black", foreground="white",font=("Montserrat", 28))
        CompetitorsLabel.grid(row=0, column=0, sticky="EW")

        lblForename = ttk.Label(self.LeftFrame, text="Forename: ")
        lblForename.grid(row=2, column=0, sticky="EW")

        lblSurname = ttk.Label(self.LeftFrame, text="Surname: ")
        lblSurname.grid(row=3, column=0, sticky="EW")

        lblTeamName = ttk.Label(self.LeftFrame, text="Team Name: ")
        lblTeamName.grid(row=4, column=0, sticky="EW")

        lblCompetitorID = ttk.Label(self.LeftFrame, text="CompetitorID: ")
        lblCompetitorID.grid(row=1, column=0, sticky="EW")

        lblCompetitorType = ttk.Label(self.LeftFrame, text="Competitor Type: ")
        lblCompetitorType.grid(row=5, column=0, sticky="EW")

        btnView = ttk.Button(self.BottomFrame, text="View All Competitors", command=self.view_all_command)
        btnView.grid(row=0, column=0, sticky="EW")

        btnSearch = ttk.Button(self.BottomFrame, text="Search Competitors", command=self.competitor_search_command)
        btnSearch.grid(row=0, column=1, sticky="EW")

        btnAdd = ttk.Button(self.BottomFrame, text="Add Competitors", command=self.Add_command)
        btnAdd.grid(row=1, column=0, sticky="EW")

        btnUpdate = ttk.Button(self.BottomFrame, text="Update selected", command=self.update_competitor_command)
        btnUpdate.grid(row=1, column=1, sticky="EW")

        btnDelete = ttk.Button(self.BottomFrame, text="Delete selected", command=self.delete_command)
        btnDelete.grid(row=1, column=2, sticky="EW")

        btnExit = ttk.Button(self.BottomFrame, text="Main Menu", command=lambda: controller.show_frame(MainMenu))
        btnExit.grid(row=2, column=3, sticky="EW")

        self.lstResults = tk.Listbox(self.RightFrame, width=60)
        self.lstResults.grid(row=0, column=0, padx=5, pady=5)

        self.scb_lstResults = ttk.Scrollbar(self.RightFrame)
        self.scb_lstResults.grid(row=0, column=1, sticky="NS")

        self.lstResults.configure(yscrollcommand=self.scb_lstResults.set)
        self.scb_lstResults.configure(command=self.lstResults.yview)

        self.lstResults.bind('<<ListboxSelect>>', self.get_selected_row)


        self.entryforename = ttk.Entry(self.LeftFrame, textvariable=self.forenametext, width=15)
        self.entryforename.grid(row=2, column=1, padx=5, pady=5)
        self.entrysurname = ttk.Entry(self.LeftFrame, textvariable=self.surnametext, width=15)
        self.entrysurname.grid(row=3, column=1, padx=5, pady=5)
        self.entryteamname = ttk.Entry(self.LeftFrame, textvariable=self.teamnametext, width=15)
        self.entryteamname.grid(row=4, column=1, padx=5, pady=5)
        self.entrycompetitorid = ttk.Entry(self.LeftFrame, textvariable=self.CompetitorIDtext, width=15)
        self.entrycompetitorid.grid(row=1, column=1, padx=5, pady=5)
        self.entrycompetitortype = ttk.Entry(self.LeftFrame, textvariable=self.competitortypetext, width=15)
        self.entrycompetitortype.grid(row=5, column=1, padx=5, pady=5)



    def get_selected_row(self, event):
        try:
            global selected_tuple
            index = self.lstResults.curselection()[0]
            selected_tuple = self.lstResults.get(index)
            self.entryforename.delete(0, 'end')
            self.entryforename.insert('end', selected_tuple[1])
            self.entrysurname.delete(0, 'end')
            self.entrysurname.insert('end', selected_tuple[2])
            self.entryteamname.delete(0, 'end')
            self.entryteamname.insert('end', selected_tuple[3])
            self.entrycompetitortype.delete(0, 'end')
            self.entrycompetitortype.insert('end', selected_tuple[4])
            self.entrycompetitorid.delete(0, 'end')
            self.entrycompetitorid.insert('end', selected_tuple[0])
        except IndexError:
            pass

    def validate(self):
        name = self.entryteamname.get()
        msg = ''

        if len(name) == 0:
            msg = 'name can\'t be empty'
        else:
            try:
                if any(ch.isdigit() for ch in name):
                    msg = 'Team name can\'t have numbers'
                else:
                    msg = 'Success!'
            except Exception as ep:
                    messagebox.showerror('error', ep)


            messagebox.showinfo('message', msg)


    def Add_command(self):

        validate = self.validate()

        if validate is True:

            Backend.insert_competitor(int(self.CompetitorIDtext.get()), self.forenametext.get(),
                                                          self.surnametext.get(), self.teamnametext.get(),
                                                          self.competitortypetext.get())
            self.lstResults.delete(0, 'end')
            self.lstResults.insert('end', (self.CompetitorIDtext.get(), self.forenametext.get(),
                                                       self.surnametext.get(), self.teamnametext.get(),
                                                       self.competitortypetext.get()))


            print("Hello")






        Backend.insert_competitor(int(self.CompetitorIDtext.get()), self.forenametext.get(), self.surnametext.get(), self.teamnametext.get(),
                                      self.competitortypetext.get())
        self.lstResults.delete(0, 'end')
        self.lstResults.insert('end', (self.CompetitorIDtext.get(), self.forenametext.get(),
                                   self.surnametext.get(), self.teamnametext.get(), self.competitortypetext.get()))

    def competitor_search_command(self):
         self.lstResults.delete(0, 'end')
         for row in Backend.competitor_search(self. forenametext.get(), self.surnametext.get(), self.teamnametext.get(), self.CompetitorIDtext.get(), self.competitortypetext.get()):
            self.lstResults.insert('end', row)

    def view_all_command(self):

        self.lstResults.delete(0, 'end')
        for row in Backend.ViewAllCompetitors():
            self.lstResults.insert('end', row)

    def update_competitor_command(self):
        Backend.update_competitor(selected_tuple[0], self.forenametext.get(), self.surnametext.get(),
                                  self.teamnametext.get(), self.competitortypetext.get())

    def delete_command(self):
        Backend.delete_competitor(selected_tuple[0])
        self.lstResults.delete(0, 'end')
        for row in Backend.ViewAllCompetitors():
            self.lstResults.insert('end', row)

class Events(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)

        self.EventIDtext = tk.StringVar()
        self.CompetitorIDtext = tk.StringVar()
        self.ActivityIDtext = tk.StringVar()
        self.RankIDtext = tk.StringVar()
        self.EventTypeIDtext = tk.StringVar()
        self.Datetext = tk.StringVar()


        self.LeftFrame = ttk.Frame(self, padding=(20, 10))
        self.LeftFrame.grid(row=0, column=0, sticky="EW")
        self.LeftFrame.columnconfigure(0, weight=1)

        self.CentreFrame = ttk.Frame(self, padding=(20, 10))
        self.CentreFrame.grid(row=0, column=1, sticky="EW")
        self.CentreFrame.columnconfigure(0, weight=1)

        self.RightFrame = ttk.Frame(self, padding=(20, 10))
        self.RightFrame.grid(row=0, column=2, sticky="EW")
        self.RightFrame.columnconfigure(0, weight=1)

        self.BottomFrame = ttk.Frame(self, padding=(0, 0))
        self.BottomFrame.grid(row=1, column=0, columnspan=3, sticky="EW")
        self.BottomFrame.columnconfigure(0, weight=1)

        EventsLabel = ttk.Label(self.LeftFrame, text="All Events", background="black", foreground="white",
                                     font=("Montserrat", 28))
        EventsLabel.grid(row=0, column=0, sticky="EW")

        lblEventID = ttk.Label(self.LeftFrame, text="EventID: ")
        lblEventID.grid(row=1, column=0, sticky="EW")

        lblCompetitorID = ttk.Label(self.LeftFrame, text="CompetitorID: ")
        lblCompetitorID.grid(row=2, column=0, sticky="EW")

        lblActivityID = ttk.Label(self.LeftFrame, text="ActivityID: ")
        lblActivityID.grid(row=3, column=0, sticky="EW")

        lblRankID = ttk.Label(self.LeftFrame, text="RankID: ")
        lblRankID.grid(row=4, column=0, sticky="EW")

        lblEventTypeID = ttk.Label(self.LeftFrame, text="Event TypeID: ")
        lblEventTypeID.grid(row=5, column=0, sticky="EW")

        lblDate = ttk.Label(self.LeftFrame, text="Date: ")
        lblDate.grid(row=6, column=0, sticky="EW")


        btnView = ttk.Button(self.BottomFrame, text="View All Events", command=self.view_all_command)
        btnView.grid(row=0, column=0, sticky="EW")

        btnView1 = ttk.Button(self.BottomFrame, text="View All Events on 15-05-22", command=self.view_all_command150522)
        btnView1.grid(row=1, column=2, sticky="EW")

        btnView2 = ttk.Button(self.BottomFrame, text="View All Events on 16-05-22", command=self.view_all_command160522)
        btnView2.grid(row=2, column=0, sticky="EW")

        btnView3 = ttk.Button(self.BottomFrame, text="View All Events on 17-05-22", command=self.view_all_command170522)
        btnView3.grid(row=2, column=1, sticky="EW")

        btnSearch = ttk.Button(self.BottomFrame, text="Search Events", command=self.Event_search_command)
        btnSearch.grid(row=0, column=1, sticky="EW")

        btnAdd = ttk.Button(self.BottomFrame, text="Add Events", command=self.Add_command)
        btnAdd.grid(row=1, column=0, sticky="EW")

        btnUpdate = ttk.Button(self.BottomFrame, text="Update selected", command=self.update_event_command)
        btnUpdate.grid(row=1, column=1, sticky="EW")

        btnDelete = ttk.Button(self.BottomFrame, text="Delete selected", command=self.delete_command)
        btnDelete.grid(row=0, column=2, sticky="EW")

        btnExit = ttk.Button(self.BottomFrame, text="Main Menu", command=lambda: controller.show_frame(MainMenu))
        btnExit.grid(row=2, column=3, sticky="EW")

        self.lstResults = tk.Listbox(self.RightFrame, width=60)
        self.lstResults.grid(row=0, column=0, padx=5, pady=5)

        self.scb_lstResults = ttk.Scrollbar(self.RightFrame)
        self.scb_lstResults.grid(row=0, column=1, sticky="NS")

        self.lstResults.configure(yscrollcommand=self.scb_lstResults.set)
        self.scb_lstResults.configure(command=self.lstResults.yview)

        self.lstResults.bind('<<ListboxSelect>>', self.get_selected_row)

        self.entryEventID = ttk.Entry(self.LeftFrame, textvariable=self.EventIDtext, width=15)
        self.entryEventID.grid(row=1, column=1, padx=5, pady=5)
        self.entryCompetitorID = ttk.Entry(self.LeftFrame, textvariable=self.CompetitorIDtext, width=15)
        self.entryCompetitorID.grid(row=2, column=1, padx=5, pady=5)
        self.entryActivityID = ttk.Entry(self.LeftFrame, textvariable=self.ActivityIDtext, width=15)
        self.entryActivityID.grid(row=3, column=1, padx=5, pady=5)
        self.entryRankID = ttk.Entry(self.LeftFrame, textvariable=self.RankIDtext, width=15)
        self.entryRankID.grid(row=4, column=1, padx=5, pady=5)
        self.entryEventTypeID = ttk.Entry(self.LeftFrame, textvariable=self.EventTypeIDtext, width=15)
        self.entryEventTypeID.grid(row=5, column=1, padx=5, pady=5)
        self.entryDate = ttk.Entry(self.LeftFrame, textvariable=self.Datetext, width=15)
        self.entryDate.grid(row=6, column=1, padx=5, pady=5)

    def get_selected_row(self, event):
        try:
            global selected_tuple
            index = self.lstResults.curselection()[0]
            selected_tuple = self.lstResults.get(index)
            self.entryEventID.delete(0, 'end')
            self.entryEventID.insert('end', selected_tuple[0])
            self.entryCompetitorID.delete(0, 'end')
            self.entryCompetitorID.insert('end', selected_tuple[1])
            self.entryActivityID.delete(0, 'end')
            self.entryActivityID.insert('end', selected_tuple[2])
            self.entryRankID.delete(0, 'end')
            self.entryRankID.insert('end', selected_tuple[3])
            self.entryEventTypeID.delete(0, 'end')
            self.entryEventTypeID.insert('end', selected_tuple[4])
            self.entryDate.delete(0, 'end')
            self.entryDate.insert('end', selected_tuple[5])
        except IndexError:
            pass

    def Add_command(self):

        Backend.insert_events(int(self.EventIDtext.get()), int(self.CompetitorIDtext.get()), self.ActivityIDtext.get(),
                              int(self.RankIDtext.get()), self.EventTypeIDtext.get(), self.Datetext.get())
        self.lstResults.delete(0, 'end')
        self.lstResults.insert('end', (self.EventIDtext.get(), int(self.CompetitorIDtext.get()),
                                       self.ActivityIDtext.get(), int(self.RankIDtext.get()), self.EventTypeIDtext.get(),
                                       self.Datetext.get()))

    def Event_search_command(self):
        self.lstResults.delete(0, 'end')
        for row in Backend.Event_search(self.EventIDtext.get(), int(self.CompetitorIDtext.get()),
                                        self.ActivityIDtext.get(), self.RankIDtext.get(), self.EventTypeIDtext.get(),
                                        self.Datetext.get()):

            self.lstResults.insert('end', row)


    def view_all_command(self):

        self.lstResults.delete(0, 'end')
        for row in Backend.ViewAllEvents():
            self.lstResults.insert('end', row)

    def view_all_command150522(self):

        self.lstResults.delete(0, 'end')
        for row in Backend.ViewAllEventsOn150522():
            self.lstResults.insert('end', row)

    def view_all_command160522(self):

        self.lstResults.delete(0, 'end')
        for row in Backend.ViewAllEventsOn160522():
            self.lstResults.insert('end', row)

    def view_all_command170522(self):

        self.lstResults.delete(0, 'end')
        for row in Backend.ViewAllEventsOn170522():
            self.lstResults.insert('end', row)


    def update_event_command(self):
         Backend.update_event(selected_tuple[0], int(self.ActivityIDtext.get()), int(self.CompetitorIDtext.get()),
                                   int(self.RankIDtext.get()), int(self.EventTypeIDtext.get()), self.Datetext.get())

         print(selected_tuple[0], self.EventIDtext.get(), self.ActivityIDtext.get(), int(self.CompetitorIDtext.get()),
               self.RankIDtext.get(), self.EventTypeIDtext.get(), self.Datetext.get())

    def delete_command(self):
        self.lstResults.delete(0, 'end')
        for row in Backend.delete_events(selected_tuple[0]):
            self.lstResults.insert('end', row)





class Leaderboards(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)

        self.EventIDtext = tk.StringVar()
        self.CompetitorIDtext = tk.StringVar()
        self.ActivityIDtext = tk.StringVar()
        self.RankIDtext = tk.StringVar()
        self.EventTypeIDtext = tk.StringVar()
        self.Datetext = tk.StringVar()

        self.LeftFrame = ttk.Frame(self, padding=(20, 10))
        self.LeftFrame.grid(row=0, column=0, sticky="EW")
        self.LeftFrame.columnconfigure(0, weight=1)

        self.CentreFrame = ttk.Frame(self, padding=(20, 10))
        self.CentreFrame.grid(row=0, column=1, sticky="EW")
        self.CentreFrame.columnconfigure(0, weight=1)

        self.RightFrame = ttk.Frame(self, padding=(20, 10))
        self.RightFrame.grid(row=0, column=2, sticky="EW")
        self.RightFrame.columnconfigure(0, weight=1)

        self.BottomFrame = ttk.Frame(self, padding=(0, 0))
        self.BottomFrame.grid(row=1, column=0, columnspan=3, sticky="EW")
        self.BottomFrame.columnconfigure(0, weight=1)

        LeaderboardsLabel = ttk.Label(self.LeftFrame, text="All Leaderboards", background="black", foreground="white",
                                font=("Montserrat", 28))
        LeaderboardsLabel.grid(row=0, column=0, sticky="EW")

        self.lstResults = tk.Listbox(self.RightFrame, width=70)
        self.lstResults.grid(row=0, column=0, padx=5, pady=5)

        self.scb_lstResults = ttk.Scrollbar(self.RightFrame)
        self.scb_lstResults.grid(row=0, column=1, sticky="NS")

        self.lstResults.configure(yscrollcommand=self.scb_lstResults.set)
        self.scb_lstResults.configure(command=self.lstResults.yview)

        self.lstResults.bind('<<ListboxSelect>>', self.get_selected_row)

        IndEventbtn = ttk.Button(self.LeftFrame, text='Individual Events', width=25,
                                       command=self.IndividualCommand)
        IndEventbtn.grid(row=1, column=0, padx=5, pady=10, sticky="n")

        IndSingleEventbtn = ttk.Button(self.LeftFrame, text='Individual Single Events', width=25,
                                       command=self.IndividualSingleCommand)
        IndSingleEventbtn.grid(row=2, column=0, padx=5, pady=10, sticky="n")

        IndMultiEventbtn = ttk.Button(self.LeftFrame, text='Individual Multiple Events', width=25,
                                       command=self.IndividualMultiCommand)
        IndMultiEventbtn.grid(row=3, column=0, padx=5, pady=10, sticky="n")

        TeamSingEventbtn = ttk.Button(self.LeftFrame, text='Team Single Events', width=25,
                                      command=self.TeamSingleCommand)
        TeamSingEventbtn.grid(row=4, column=0, padx=5, pady=10, sticky="n")

        TeamMultiEventbtn = ttk.Button(self.LeftFrame, text='Team Multiple Events', width=25,
                                      command=self.TeamMultiCommand)
        TeamMultiEventbtn.grid(row=5, column=0, padx=5, pady=10, sticky="n")

        btnExit = ttk.Button(self.BottomFrame, text="Main Menu", command=lambda: controller.show_frame(MainMenu))
        btnExit.grid(row=2, column=3, sticky="EW")


    def IndividualSingleCommand(self):
        self.lstResults.delete(0, 'end')
        for row in Backend.RankSingleEventCompetitors():
            self.lstResults.insert('end', row)
        print("Individuals Single Leaderboards")

    def IndividualCommand(self):
        self.lstResults.delete(0, 'end')
        for row in Backend.RankIndividualCompetitors():
            self.lstResults.insert('end', row)
        print("Individuals Leaderboards")

    def IndividualMultiCommand(self):
        self.lstResults.delete(0, 'end')
        for row in Backend.RankIndividualMultipleEventCompetitors():
            self.lstResults.insert('end', row)
        print("Individuals multi Leaderboards")

    def TeamSingleCommand(self):
            self.lstResults.delete(0, 'end')
            for row in Backend.RankTeamSingleEventCompetitors():
                self.lstResults.insert('end', row)
            print("team single Leaderboards")

    def TeamMultiCommand(self):
            self.lstResults.delete(0, 'end')
            for row in Backend.RankTeamMultipleEventCompetitors():
                self.lstResults.insert('end', row)
    print("team single Leaderboards")


    def get_selected_row(self, event):
        try:
            global selected_tuple
            index = self.lstResults.curselection()[0]
            selected_tuple = self.lstResults.get(index)
        except IndexError:
            pass

class Activities(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)

        self.ActivtyIDtext = tk.StringVar()
        self.Descriptiontext = tk.StringVar()

        self.LeftFrame = ttk.Frame(self, padding=(20, 10))
        self.LeftFrame.grid(row=0, column=0, sticky="EW")
        self.LeftFrame.columnconfigure(0, weight=1)

        self.CentreFrame = ttk.Frame(self, padding=(20, 10))
        self.CentreFrame.grid(row=0, column=1, sticky="EW")
        self.CentreFrame.columnconfigure(0, weight=1)

        self.RightFrame = ttk.Frame(self, padding=(20, 10))
        self.RightFrame.grid(row=0, column=2, sticky="EW")
        self.RightFrame.columnconfigure(0, weight=1)

        self.BottomFrame = ttk.Frame(self, padding=(0, 0))
        self.BottomFrame.grid(row=1, column=0, columnspan=3, sticky="EW")
        self.BottomFrame.columnconfigure(0, weight=1)

        ActivitiesLabel = ttk.Label(self.LeftFrame, text="All Activities", background="black", foreground="white",
                                font=("Montserrat", 28))
        ActivitiesLabel.grid(row=0, column=0, sticky="EW")

        lblActivityID = ttk.Label(self.LeftFrame, text="ActivityID: ")
        lblActivityID.grid(row=1, column=0, sticky="EW")

        lblDescription = ttk.Label(self.LeftFrame, text="Description: ")
        lblDescription.grid(row=2, column=0, sticky="EW")

        btnView = ttk.Button(self.BottomFrame, text="View All Activities", command=self.view_all_command)
        btnView.grid(row=0, column=0, sticky="EW")

        btnSearch = ttk.Button(self.BottomFrame, text="Search Activities", command=self.Activities_search_command)
        btnSearch.grid(row=0, column=1, sticky="EW")

        btnAdd = ttk.Button(self.BottomFrame, text="Add Activities", command=self.Add_command)
        btnAdd.grid(row=1, column=0, sticky="EW")

        btnUpdate = ttk.Button(self.BottomFrame, text="Update selected", command=self.update_Activity_command)
        btnUpdate.grid(row=1, column=1, sticky="EW")

        btnDelete = ttk.Button(self.BottomFrame, text="Delete selected", command=self.delete_command)
        btnDelete.grid(row=0, column=2, sticky="EW")

        btnExit = ttk.Button(self.BottomFrame, text="Main Menu", command=lambda: controller.show_frame(MainMenu))
        btnExit.grid(row=2, column=3, sticky="EW")

        self.lstResults = tk.Listbox(self.RightFrame, width=60)
        self.lstResults.grid(row=0, column=0, padx=5, pady=5)

        self.scb_lstResults = ttk.Scrollbar(self.RightFrame)
        self.scb_lstResults.grid(row=0, column=1, sticky="NS")

        self.lstResults.configure(yscrollcommand=self.scb_lstResults.set)
        self.scb_lstResults.configure(command=self.lstResults.yview)

        self.lstResults.bind('<<ListboxSelect>>', self.get_selected_row)

        self.entryActivityID = ttk.Entry(self.LeftFrame, textvariable=self.ActivtyIDtext, width=15)
        self.entryActivityID.grid(row=1, column=1, padx=5, pady=5)
        self.entryDescription = ttk.Entry(self.LeftFrame, textvariable=self.Descriptiontext, width=15)
        self.entryDescription.grid(row=2, column=1, padx=5, pady=5)


    def get_selected_row(self, event):
        try:
            global selected_tuple
            index = self.lstResults.curselection()[0]
            selected_tuple = self.lstResults.get(index)
            self.entryActivityID.delete(0, 'end')
            self.entryActivityID.insert('end', selected_tuple[0])
            self.entryDescription.delete(0, 'end')
            self.entryDescription.insert('end', selected_tuple[1])

        except IndexError:
            pass

    def Add_command(self):

        Backend.insert_activities(self.ActivtyIDtext.get(), self.Descriptiontext.get())
        self.lstResults.delete(0, 'end')
        self.lstResults.insert('end', (self.ActivtyIDtext.get(), self.Descriptiontext.get()))

    def Activities_search_command(self):
        self.lstResults.delete(0, 'end')
        for row in Backend.Activities_search(self.ActivtyIDtext.get(), self.Descriptiontext.get()):
            self.lstResults.insert('end', row)

    def view_all_command(self):

        self.lstResults.delete(0, 'end')
        for row in Backend.ViewActivities():
            self.lstResults.insert('end', row)

    def update_Activity_command(self):
        Backend.update_Activity(int(self.ActivtyIDtext.get()), self.Descriptiontext.get())

        print(int(self.ActivtyIDtext.get()), self.Descriptiontext.get())

    def delete_command(self):
        self.lstResults.delete(0, 'end')
        for row in Backend.delete_Activities(selected_tuple[0]):
            self.lstResults.insert('end', row)


class Admin(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)

        self.LeftFrame = ttk.Frame(self, padding=(20, 10))
        self.LeftFrame.grid(row=0, column=0, sticky="EW")
        self.LeftFrame.columnconfigure(0, weight=1)

        self.CentreFrame = ttk.Frame(self, padding=(20, 10))
        self.CentreFrame.grid(row=0, column=1, sticky="EW")
        self.CentreFrame.columnconfigure(0, weight=1)

        self.RightFrame = ttk.Frame(self, padding=(20, 10))
        self.RightFrame.grid(row=0, column=2, sticky="EW")
        self.RightFrame.columnconfigure(0, weight=1)

        self.BottomFrame = ttk.Frame(self, padding=(0, 0))
        self.BottomFrame.grid(row=1, column=0, columnspan=3, sticky="EW")
        self.BottomFrame.columnconfigure(0, weight=1)

        AdminLabel = ttk.Label(self.LeftFrame, text="Admin", background="black", foreground="white",
                               font=("Montserrat", 28))
        AdminLabel.grid(row=0, column=0, sticky="EW")

        self.Cogs = ImageTk.PhotoImage(file='Cogs.jpg')
        tk.Label(self.LeftFrame, image=self.Cogs, anchor='w').grid(row=1, column=0, sticky='w')

        btnBackup = ttk.Button(self.RightFrame, text="Back Up DB", command=self.BackUpDatabseCommand)
        btnBackup.grid(row=3, column=3, sticky="EW")

        btnDelete = ttk.Button(self.RightFrame, text="Delete Tables", command=self.DeleteTablesCommand)
        btnDelete.grid(row=4, column=3, sticky="EW")

        btnExit = ttk.Button(self.BottomFrame, text="Main Menu", command=lambda: controller.show_frame(MainMenu))
        btnExit.grid(row=3, column=3, sticky="EW")

    def BackUpDatabseCommand(self):
        Backend.BackUpDatabase(self)


    def DeleteTablesCommand(self):
        Backend.DropTables(self)


class Pointscoring(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)

        self.PointsAwardedtext = tk.StringVar()
        self.RankIDtext = tk.StringVar()

        self.LeftFrame = ttk.Frame(self, padding=(20, 10))
        self.LeftFrame.grid(row=0, column=0, sticky="EW")
        self.LeftFrame.columnconfigure(0, weight=1)

        self.CentreFrame = ttk.Frame(self, padding=(20, 10))
        self.CentreFrame.grid(row=0, column=1, sticky="EW")
        self.CentreFrame.columnconfigure(0, weight=1)

        self.RightFrame = ttk.Frame(self, padding=(20, 10))
        self.RightFrame.grid(row=0, column=2, sticky="EW")
        self.RightFrame.columnconfigure(0, weight=1)

        self.BottomFrame = ttk.Frame(self, padding=(0, 0))
        self.BottomFrame.grid(row=1, column=0, columnspan=3, sticky="EW")
        self.BottomFrame.columnconfigure(0, weight=1)

        PointscoringLabel = ttk.Label(self.LeftFrame, text="Point Scoring", background="black", foreground="white",
                                    font=("Montserrat", 28))
        PointscoringLabel.grid(row=0, column=0, sticky="EW")

        lblRankID = ttk.Label(self.LeftFrame, text="RankID: ")
        lblRankID.grid(row=1, column=0, sticky="EW")

        lblPointsAwarded = ttk.Label(self.LeftFrame, text="Points Awarded: ")
        lblPointsAwarded.grid(row=2, column=0, sticky="EW")

        btnView = ttk.Button(self.BottomFrame, text="View All Points", command=self.view_all_command)
        btnView.grid(row=0, column=0, sticky="EW")

        btnAdd = ttk.Button(self.BottomFrame, text="Add Points", command=self.Add_command)
        btnAdd.grid(row=1, column=0, sticky="EW")

        btnUpdate = ttk.Button(self.BottomFrame, text="Update selected", command=self.update_Points_command)
        btnUpdate.grid(row=1, column=1, sticky="EW")

        btnDelete = ttk.Button(self.BottomFrame, text="Delete selected", command=self.delete_command)
        btnDelete.grid(row=0, column=1, sticky="EW")

        btnExit = ttk.Button(self.BottomFrame, text="Main Menu", command=lambda: controller.show_frame(MainMenu))
        btnExit.grid(row=2, column=3, sticky="EW")

        self.lstResults = tk.Listbox(self.RightFrame, width=60)
        self.lstResults.grid(row=0, column=0, padx=5, pady=5)

        self.scb_lstResults = ttk.Scrollbar(self.RightFrame)
        self.scb_lstResults.grid(row=0, column=1, sticky="NS")

        self.lstResults.configure(yscrollcommand=self.scb_lstResults.set)
        self.scb_lstResults.configure(command=self.lstResults.yview)

        self.lstResults.bind('<<ListboxSelect>>', self.get_selected_row)

        self.entryRankID = ttk.Entry(self.LeftFrame, textvariable=self.RankIDtext, width=15)
        self.entryRankID.grid(row=1, column=1, padx=5, pady=5)
        self.entryPointsAwarded = ttk.Entry(self.LeftFrame, textvariable=self.PointsAwardedtext, width=15)
        self.entryPointsAwarded.grid(row=2, column=1, padx=5, pady=5)

    def get_selected_row(self, event):
        try:
            global selected_tuple
            index = self.lstResults.curselection()[0]
            selected_tuple = self.lstResults.get(index)
            self.entryRankID.delete(0, 'end')
            self.entryRankID.insert('end', selected_tuple[0])
            self.entryPointsAwarded.delete(0, 'end')
            self.entryPointsAwarded.insert('end', selected_tuple[1])

        except IndexError:
            pass

    def Add_command(self):

        Backend.insert_points(self.RankIDtext.get(), self.PointsAwardedtext.get())
        self.lstResults.delete(0, 'end')
        self.lstResults.insert('end', (self.RankIDtext.get(), self.PointsAwardedtext.get()))

    def view_all_command(self):

        self.lstResults.delete(0, 'end')
        for row in Backend.ViewPoints():
            self.lstResults.insert('end', row)

    def update_Points_command(self):
        Backend.update_Points(int(self.RankIDtext.get()), self.PointsAwardedtext.get())

        print(int(self.RankIDtext.get()), self.PointsAwardedtext.get())

    def delete_command(self):
        self.lstResults.delete(0, 'end')
        for row in Backend.delete_Points(selected_tuple[0]):
            self.lstResults.insert('end', row)

app = App()
app.mainloop()