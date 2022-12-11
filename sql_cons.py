import sqlite3
conn = sqlite3.connect('users.sqlite')
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS Users(
TG_ID INTEGER ,
Telefon INTEGER ,
Ism STRING,
Familiya STRING,
SizKimsiz STRING,
Murojatid INTEGER,
Stage INTEGER,
Lang INTEGER

)
""")
first_insert = """
INSERT INTO Users VALUES ("{}" ," ", " ", " ", " ", "{}","{}", " ")
"""
get_id = """
SELECT TG_ID 
FROM Users
Where TG_ID = "{}"
"""

upd_Telefon = """
UPDATE Users 
SET Telefon = "{}" 
WHERE TG_ID = "{}"
"""
select_Telefon = """
SELECT Telefon 
From Users
WHERE TG_ID = "{}"
"""


upd_Ism = """
UPDATE Users 
SET Ism = "{}" 
WHERE TG_ID = "{}"
"""
select_Ism = """
SELECT Ism 
From Users
WHERE TG_ID = "{}"
"""


upd_Familiya = """
UPDATE Users 
SET Familiya = "{}" 
WHERE TG_ID = "{}"
"""
select_Familiya = """
SELECT Familiya 
From Users
WHERE TG_ID = "{}"
"""


upd_SizKimsiz = """
UPDATE Users 
SET SizKimsiz = "{}" 
WHERE TG_ID = "{}"
"""
select_SizKimsiz= """
SELECT  SizKimsiz
From Users
WHERE TG_ID = "{}"
"""


upd_MijozTuri = """
UPDATE Users 
SET MijozTuri = "{}" 
WHERE TG_ID = "{}"
"""
select_MijozTuri = """
SELECT  MijozTuri
From Users
WHERE TG_ID = "{}"
"""


upd_FarzandSoni = """
UPDATE Users 
SET FarzandSoni = "{}" 
WHERE TG_ID = "{}"
"""
select_FarzandSoni = """
SELECT FarzandSoni 
From Users
WHERE TG_ID = "{}"
"""

upd_Stage = """
UPDATE Users 
SET Stage = "{}" 
WHERE TG_ID = "{}"
"""
select_Stage = """
SELECT Stage 
From Users
WHERE TG_ID = "{}"
"""

upd_Lang = """
UPDATE Users 
SET Lang = "{}" 
WHERE TG_ID = "{}"
"""
select_Lang = """
SELECT  Lang
From Users
WHERE TG_ID = "{}"
"""

upd_mid= """
UPDATE Users 
SET Murojatid = "{}" 
WHERE TG_ID = "{}"
"""
select_mid = """
SELECT  Murojatid
From Users
WHERE TG_ID = "{}"
"""
conn.commit()

