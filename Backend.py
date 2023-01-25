import sqlite3
import subprocess
import time


def ViewAllCompetitors():
    db = sqlite3.connect("Tournament.db")
    cursor = db.cursor()
    print("====================")
    print("View All Competitors")
    cursor.execute("SELECT CompetitorID, Forename, Surname, TeamName, CompetitorType "
                   "FROM tblCompetitors ORDER BY CompetitorID, TeamName, Surname")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
    return rows


def RankAllCompetitors():
    db = sqlite3.connect("Tournament.db")
    cursor = db.cursor()
    print("====================")
    print("Rank All Competitors")
    cursor.execute("SELECT *,sum(PointsAwarded) AS TotalPoints "
                   "FROM tblCompetitors "
                   "INNER JOIN tblEvents ON tblCompetitors.CompetitorID = tblEvents.CompetitorID "
                   "INNER JOIN tblActivities ON tblEvents.ActivityID = tblActivities.ActivityID "
                   "INNER JOIN tblPoints ON tblEvents.RankID = tblPoints.RankID "
                   "GROUP BY tblCompetitors.CompetitorID "
                   "ORDER BY TotalPoints DESC;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    return rows


def RankIndividualCompetitors():
    db = sqlite3.connect("Tournament.db")
    cursor = db.cursor()
    print("===========================")
    print("Rank Individual Competitors")
    cursor.execute("SELECT *, "
                   "sum(PointsAwarded) AS TotalPoints "
                   "FROM tblCompetitors "
                   "INNER JOIN tblEvents ON tblCompetitors.CompetitorID = tblEvents.CompetitorID "
                   "INNER JOIN tblActivities ON tblEvents.ActivityID = tblActivities.ActivityID "
                   "INNER JOIN tblPoints ON tblEvents.RankID = tblPoints.RankID "
                   "WHERE tblCompetitors.TeamName = 'Individuals' "
                   "GROUP BY tblCompetitors.CompetitorID  ")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    return rows


def AllTeamCompetitors():
    db = sqlite3.connect("Tournament.db")
    cursor = db.cursor()
    print("====================")
    print("All Team Competitors")
    cursor.execute("SELECT TeamName, "
                   "sum(PointsAwarded) AS TotalPoints "
                   "FROM tblCompetitors "
                   "INNER JOIN tblEvents ON tblCompetitors.CompetitorID = tblEvents.CompetitorID "
                   "INNER JOIN tblActivities ON tblEvents.ActivityID = tblActivities.ActivityID "
                   "INNER JOIN tblPoints ON tblEvents.RankID = tblPoints.RankID "
                   "WHERE tblCompetitors.TeamName is NOT 'Individuals' "
                   "GROUP BY tblCompetitors.TeamName "
                   "ORDER BY TotalPoints DESC;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    return rows


def RankSingleEventCompetitors():
    db = sqlite3.connect("Tournament.db")
    cursor = db.cursor()
    print("=============================")
    print("Rank Single Event Competitors")
    cursor.execute("SELECT Forename, Surname, TeamName,sum(PointsAwarded) AS TotalPoints "
                   "FROM tblCompetitors "
                   "INNER JOIN tblEvents ON tblCompetitors.CompetitorID = tblEvents.CompetitorID "
                   "INNER JOIN tblActivities ON tblEvents.ActivityID = tblActivities.ActivityID "
                   "INNER JOIN tblPoints ON tblEvents.RankID = tblPoints.RankID "
                   "WHERE tblCompetitors.TeamName IS 'Individuals' AND tblCompetitors.CompetitorType = 'S' "
                   "GROUP BY tblCompetitors.TeamName "
                   "ORDER BY TotalPoints DESC;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
    return rows


def RankTeamSingleEventCompetitors():
    db = sqlite3.connect("Tournament.db")
    cursor = db.cursor()
    print("==================================")
    print("Rank Team Single Event Competitors")
    cursor.execute("SELECT Forename, Surname, TeamName,sum(PointsAwarded) AS TotalPoints "
                   "FROM tblCompetitors "
                   "INNER JOIN tblEvents ON tblCompetitors.CompetitorID = tblEvents.CompetitorID "
                   "INNER JOIN tblActivities ON tblEvents.ActivityID = tblActivities.ActivityID "
                   "INNER JOIN tblPoints ON tblEvents.RankID = tblPoints.RankID "
                   "WHERE tblCompetitors.TeamName IS NOT 'Individuals' AND tblCompetitors.CompetitorType = 'S' "
                   "GROUP BY tblCompetitors.TeamName "
                   "ORDER BY TotalPoints DESC;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
    return rows


def RankIndividualMultipleEventCompetitors():
    db = sqlite3.connect("Tournament.db")
    cursor = db.cursor()
    print("==========================================")
    print("Rank Individual Multiple Event Competitors")
    cursor.execute("SELECT Forename, Surname, TeamName,sum(PointsAwarded) AS TotalPoints "
                   "FROM tblCompetitors "
                   "INNER JOIN tblEvents ON tblCompetitors.CompetitorID = tblEvents.CompetitorID "
                   "INNER JOIN tblActivities ON tblEvents.ActivityID = tblActivities.ActivityID "
                   "INNER JOIN tblPoints ON tblEvents.RankID = tblPoints.RankID "
                   "WHERE tblCompetitors.TeamName IS 'Individuals' AND tblCompetitors.CompetitorType = 'M' "
                   "GROUP BY tblCompetitors.TeamName "
                   "ORDER BY TotalPoints DESC;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
    return rows


def RankTeamMultipleEventCompetitors():
    db = sqlite3.connect("Tournament.db")
    cursor = db.cursor()
    print("====================================")
    print("Rank Team Multiple Event Competitors")
    cursor.execute("SELECT Forename, Surname, TeamName,sum(PointsAwarded) AS TotalPoints "
                   "FROM tblCompetitors "
                   "INNER JOIN tblEvents ON tblCompetitors.CompetitorID = tblEvents.CompetitorID "
                   "INNER JOIN tblActivities ON tblEvents.ActivityID = tblActivities.ActivityID "
                   "INNER JOIN tblPoints ON tblEvents.RankID = tblPoints.RankID "
                   "WHERE tblCompetitors.TeamName IS NOT 'Individuals' AND tblCompetitors.CompetitorType = 'M' "
                   "GROUP BY tblCompetitors.TeamName "
                   "ORDER BY TotalPoints DESC;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
    return rows


def ViewAllEvents():
    db = sqlite3.connect("Tournament.db")
    cursor = db.cursor()
    print("===============")
    print("View All Events")
    cursor.execute("SELECT tblEvents.EventID, tblEvents.CompetitorID, tblEvents.ActivityID, tblEvents.RankID,"
                   "tblEvents.EventTypeID, tblEvents.Date, tblCompetitors.Forename, tblCompetitors.Surname,"
                   "tblCompetitors.TeamName, tblActivities.Description, TblPoints.PointsAwarded "
                   "FROM tblEvents "
                   "INNER JOIN tblCompetitors on tblEvents.CompetitorID = tblCompetitors.CompetitorID "
                   "INNER JOIN tblActivities on tblEvents.ActivityID = tblActivities.ActivityID "
                   "INNER JOIN tblPoints on tblEvents.RankID = tblPoints.RankID " 
                   "ORDER BY tblEvents.EventID, tblEvents.Date;")
    rows = cursor.fetchall()
    cursor.close()
    db.close()
    return rows


def ViewAllEventsOn150522():
    db = sqlite3.connect("Tournament.db")
    cursor = db.cursor()
    print("===========================")
    print("View All Events on 15-05-22")
    cursor.execute("SELECT * FROM tblEvents WHERE Date = '15-05-22' ORDER BY EventID;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
    return rows


def ViewAllEventsOn160522():
    db = sqlite3.connect("Tournament.db")
    cursor = db.cursor()
    print("===========================")
    print("View All Events on 16-05-22")
    cursor.execute("SELECT * FROM tblEvents WHERE Date = '16-05-22' ORDER BY EventID;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
    return rows


def ViewAllEventsOn170522():
    db = sqlite3.connect("Tournament.db")
    cursor = db.cursor()
    print("===========================")
    print("View All Events on 17-05-22")
    cursor.execute("SELECT * FROM tblEvents WHERE Date = '17-05-22' ORDER BY EventID;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
    return rows


def ViewPoints():
    db = sqlite3.connect("Tournament.db")
    cursor = db.cursor()
    print("===========")
    print("View Points")
    cursor.execute("SELECT * FROM tblPoints;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
    return rows


def ViewActivities():
    db = sqlite3.connect("Tournament.db")
    cursor = db.cursor()
    print("===============")
    print("View Activities")
    cursor.execute("SELECT * FROM tblActivities;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
    return rows


def competitor_search(Forename="", Surname="", TeamName="", CompetitorID="", CompetitorType=""):
    db = sqlite3.connect("Tournament.db")
    cursor = db.cursor()
    print("===============")
    print("Comp search")
    cursor.execute("SELECT * FROM tblCompetitors WHERE Forename like? "
                   "OR Surname like? OR TeamName like? OR CompetitorID like? OR CompetitorType like?",
                   (Forename, Surname, TeamName, CompetitorID, CompetitorType))
    rows = cursor.fetchall()
    return rows


def insert_competitor(CompetitorID, Forename, Surname, TeamName, CompetitorType):
    db = sqlite3.connect("Tournament.db")
    cursor = db.cursor()
    print("===============")
    print("Insert Comp")
    cursor.execute("INSERT INTO tblCompetitors VALUES(?,?,?,?,?)", (CompetitorID, Forename, Surname, TeamName,
                                                                    CompetitorType))

    db.commit()
    db.close()


def update_competitor(CompetitorID, Forename, Surname, TeamName, CompetitorType):
    db = sqlite3.connect("Tournament.db")
    cursor = db.cursor()
    print("===============")
    print("Update tblCompetitors")
    cursor.execute("UPDATE tblCompetitors "
                   "SET Forename=?, Surname=?, TeamName=?, CompetitorType=? WHERE CompetitorID=?",
                   (Forename, Surname, TeamName, CompetitorType, CompetitorID))
    db.commit()
    db.close()


def delete_competitor(CompetitorID):
    db = sqlite3.connect("Tournament.db")
    cursor = db.cursor()
    print("===============")
    print("Delete tblCompetitors")
    cursor.execute("DELETE FROM tblCompetitors WHERE CompetitorID=?", (CompetitorID,))
    db.commit()
    db.close()


def Event_search(EventID="", CompetitorID="", ActivityID="", RankID="", EventTypeID="", Date=""):
    db = sqlite3.connect("Tournament.db")
    cursor = db.cursor()
    print("===============")
    print("Event search")
    cursor.execute("SELECT tblEvents.EventID, tblEvents.CompetitorID, tblEvents.ActivityID, tblEvents.RankID,"
                   "tblEvents.EventTypeID, tblEvents.Date, tblCompetitors.Forename, tblCompetitors.Surname,"
                   "tblCompetitors.TeamName, tblActivities.Description, TblPoints.PointsAwarded "
                   "FROM tblEvents "
                   "INNER JOIN tblCompetitors on tblEvents.CompetitorID = tblCompetitors.CompetitorID "
                   "INNER JOIN tblActivities on tblEvents.ActivityID = tblActivities.ActivityID "
                   "INNER JOIN tblPoints on tblEvents.RankID = tblPoints.RankID "
                   "WHERE tblEvents.EventID like? OR tblActivities.ActivityID like? OR tblEvents.CompetitorID like? "
                   "OR tblEvents.RankID like? OR tblEvents.Date like? OR tblEvents.EventTypeID like? "
                   "ORDER BY tblEvents.Date;",
                   (EventID, CompetitorID, ActivityID, RankID, EventTypeID, Date,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    db.close()
    return rows




def insert_events(EventID, CompetitorID, ActivityID, RankID, EventTypeID, Date):
    db = sqlite3.connect("Tournament.db")
    cursor = db.cursor()
    print("===============")
    print("Insert Comp")
    cursor.execute("INSERT INTO tblEvents VALUES(?,?,?,?,?,?)", (EventID, CompetitorID, ActivityID, RankID,
                                                                 EventTypeID, Date))

    db.commit()
    db.close()

def update_event(EventID, CompetitorID, ActivityID, RankID, EventTypeID, Date):
    db = sqlite3.connect("Tournament.db")
    cursor = db.cursor()
    print("===============")
    print("Update tblEvents")
    cursor.execute("UPDATE tblEvents SET CompetitorID=?, ActivityID=?, RankID=?, EventTypeID=?, Date=? WHERE EventID=?",
                   (CompetitorID, ActivityID, RankID, EventTypeID, Date, EventID, ))
    db.commit()
    db.close()


def delete_events(EventID):
    db = sqlite3.connect("Tournament.db")
    cursor = db.cursor()
    print("===============")
    print("Delete tblCompetitors")
    cursor.execute("DELETE FROM tblEvents WHERE EventID=?", (EventID,))
    db.commit()
    db.close()

def insert_activities(ActivityID, Description):
    db = sqlite3.connect("Tournament.db")
    cursor = db.cursor()
    print("===============")
    print("Insert Comp")
    cursor.execute("INSERT INTO tblActivities VALUES(?,?)", (ActivityID, Description,))

    db.commit()
    db.close()

def Activities_search(ActivityID="", Description=""):
    db = sqlite3.connect("Tournament.db")
    cursor = db.cursor()
    print("===============")
    print("Activity search")
    cursor.execute("SELECT * FROM tblActivities WHERE ActivityID like? "
                   "OR Description like?",
                   (ActivityID, Description))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    db.close()
    return rows

def delete_Activities(ActivityID):
    db = sqlite3.connect("Tournament.db")
    cursor = db.cursor()
    print("===============")
    print("Delete tblActivities")
    cursor.execute("DELETE FROM tblActivities WHERE ActivityID=?", (ActivityID,))
    db.commit()
    db.close()

def update_Activity(ActivityID, Description):
    db = sqlite3.connect("Tournament.db")
    cursor = db.cursor()
    print("===============")
    print("Update tblCompetitors")
    cursor.execute("UPDATE tblActivities "
                   "SET Description=? WHERE ActivityID=?",
                   (Description, ActivityID))
    db.commit()
    db.close()


def insert_points(RankID, PointsAwarded):
    db = sqlite3.connect("Tournament.db")
    cursor = db.cursor()
    print("===============")
    print("Insert Comp")
    cursor.execute("INSERT INTO tblActivities VALUES(?,?)", (RankID, PointsAwarded,))

    db.commit()
    db.close()


def delete_Points(RankID):
    db = sqlite3.connect("Tournament.db")
    cursor = db.cursor()
    print("===============")
    print("Delete tblActivities")
    cursor.execute("DELETE FROM tblPoints WHERE RankID=?", (RankID,))
    db.commit()
    db.close()


def update_Points(RankID, PointsAwarded):
    db = sqlite3.connect("Tournament.db")
    cursor = db.cursor()
    print("===============")
    print("Update tblCompetitors")
    cursor.execute("UPDATE tblPoints "
                   "SET PointsAwarded=? WHERE RankID=?",
                   (PointsAwarded, RankID))

    db.commit()
    db.close()


def BackUpDatabase(self):
    filename = "Tournament_Backup"+time.strftime("%y%m%d-%H%M")+".db"
    sqlite_cmd = ".backup"
    print(sqlite_cmd + " " + filename)
    subprocess.call(["sqlite3", "Tournament.db", sqlite_cmd+ " " + filename])

def DropTables(self):
    db = sqlite3.connect("Tournament.db")
    cursor = db.cursor()
    cursor.execute("DROP TABLE tblActivities")
    cursor.execute("DROP TABLE tblCompetitors")
    cursor.execute("DROP TABLE tblEvents")
    cursor.execute("DROP TABLE tblEventType")
    cursor.execute("DROP TABLE tblPoints")

# ViewAllCompetitors()
# RankAllCompetitors()
# RankIndividualCompetitors()
# AllTeamCompetitors()
# RankSingleEventCompetitors()
# RankTeamSingleEventCompetitors()
# RankIndividualMultipleEventCompetitors()
# RankTeamMultipleEventCompetitors()
# ViewAllEvents()
# ViewAllEventsOn150522()
# ViewAllEventsOn160522()
# ViewAllEventsOn170522()
# ViewPoints()
# ViewActivities()

