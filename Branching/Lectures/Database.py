# ------------------------
# -- Databases => Intro --
# ------------------------
# - Database Is A Place Where We Can Store Data
# - Database Organized Into Tables (Users, Categories)
# - Tables Has Columns (ID, Username, Password)
# - There's Many Types Of Databases (MongoDB, MySQL, SQLite)
# - SQL Stand For Structured Query Language
# - SQLite => Can Run in Memory or in A Single File
# - You Can Browse File With https://sqlitebrowser.org/
# - Data Inside Database Has Types (Text, Integer, Date)
# ------------------------------------------------------

# --------------------------------------------------------
# -- Databases => SQLite => Create Database And Connect --
# --------------------------------------------------------
# - Connect
# - Execute
# - Close
# --------------------------------------------------

# Import SQLite Module
import sqlite3

# Create Database And Connect
db = sqlite3.connect("app.db")

cr = db.cursor()

# Create The Tables and Fields
db.execute(
    "create table if not exists skills (name TEXT, progress Integer, user_id Integer)")

cr.execute("create table if not exists users (user_id, name TEXT)")

cr.execute("insert into users(user_id, name) values(1, 'ahmed')")
cr.execute("insert into users(user_id, name) values(2, 'abdo')")

db.commit()

# Close Database
db.close()
