import sqlite3

# Create Database And Connect
db = sqlite3.connect("app.db")

# Setting Up The Cursor
cr = db.cursor()

cr.execute("update users set name = 'Abdelgwad' where user_id = 2")

cr.execute("select * from skills")

print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())


db.commit()


# ----------------------------------------------
# -- Databases => SQLite => Update and Delete --
# ----------------------------------------------

# Import SQLite Module

# Create Database And Connect
db = sqlite3.connect("app.db")

# Setting Up The Cursor
cr = db.cursor()

# Update Data
# cr.execute("update users set name = 'Mahmoud' where user_id = 1")
# cr.execute("update users set name = 'Sayed' where user_id = 2")
# cr.execute("update users set name = 'Ameer' where user_id = 3")

# Delete Data
cr.execute("delete from users where user_id = 4")

# Fetch Data
cr.execute("select * from users")

print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())

# Save (Commit) Changes
db.commit()

# Close Database
db.close()
