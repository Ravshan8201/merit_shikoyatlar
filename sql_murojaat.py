import sqlite3
conn = sqlite3.connect('users.sqlite')
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS Murojaat(
TG_ID INTEGER ,
MurojaatID INTEGER,
MijozTuri STRING,
FarzandSoni STRING,
MurojaatTuri STRING,
Filial STRING,
Soha STRING,
Matn STRING,
Status STRING,
Javobgar STRING,
OxirgiMuddat STRING,
MijozBahosi STRING,
QoshganShaxs STRING,
QoshilganVaqt STRING,
OxirgiOzgarishVaqti STRING,
OxirgiOzgartirganShaxs STRING

)
""")
first_insert_murojat = """
INSERT INTO Murojaat VALUES ("{}" ,"{}", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ")
"""


upd_MurojaatID = """
UPDATE Murojaat 
SET MurojaatID = "{}" 
WHERE TG_ID = "{}"
"""
select_MurojaatID = """
SELECT  MurojaatID
From Murojaat
WHERE TG_ID = "{}"
"""


upd_MijozTuri = """
UPDATE Murojaat 
SET MijozTuri = "{}" 
WHERE TG_ID = "{}"
"""
select_MijozTuri = """
SELECT  MijozTuri
From Murojaat
WHERE TG_ID = "{}"
"""


upd_FarzandSoni = """
UPDATE Murojaat 
SET FarzandSoni = "{}" 
WHERE TG_ID = "{}"
"""
select_FarzandSoni = """
SELECT FarzandSoni 
From Murojaat
WHERE TG_ID = "{}"
"""


upd_MurojaatTuri = """
UPDATE Murojaat 
SET MurojaatTuri = "{}" 
WHERE TG_ID = "{}"
"""
select_MurojaatTuri = """
SELECT  MurojaatTuri
From Murojaat
WHERE TG_ID = "{}"
"""


upd_Filial = """
UPDATE Murojaat 
SET Filial = "{}" 
WHERE TG_ID = "{}"
"""
select_Filial= """
SELECT  Filial
From Murojaat
WHERE TG_ID = "{}"
"""


upd_Soha = """
UPDATE Murojaat 
SET Soha = "{}" 
WHERE TG_ID = "{}"
"""
select_Soha = """
SELECT Soha 
From Murojaat
WHERE TG_ID = "{}"
"""

upd_Matn = """
UPDATE Murojaat 
SET Matn = "{}" 
WHERE TG_ID = "{}"
"""
select_Matn = """
SELECT  Matn
From Murojaat
WHERE TG_ID = "{}"
"""

upd_Status = """
UPDATE Murojaat 
SET Status  = "{}" 
WHERE TG_ID = "{}"
"""
select_Status = """
SELECT  Status
From Murojaat
WHERE TG_ID = "{}"
"""

upd_Javobgar = """
UPDATE Murojaat 
SET JavobgarJavobgar = "{}" 
WHERE TG_ID = "{}"
"""
select_Javobgar = """
SELECT  Javobgar
From Murojaat
WHERE TG_ID = "{}"
"""

upd_OxirgiMuddat = """
UPDATE Murojaat 
SET OxirgiMuddat = "{}" 
WHERE TG_ID = "{}"
"""
select_OxirgiMuddat = """
SELECT  OxirgiMuddat
From Murojaat
WHERE TG_ID = "{}"
"""

upd_MijozBahosi = """
UPDATE Murojaat 
SET MijozBahosi = "{}" 
WHERE TG_ID = "{}"
"""
select_MijozBahosi = """
SELECT  MijozBahosi
From Murojaat
WHERE TG_ID = "{}"
"""

upd_QoshganShaxs = """
UPDATE Murojaat 
SET QoshganShaxs = "{}" 
WHERE TG_ID = "{}"
"""
select_QoshganShaxs = """
SELECT QoshganShaxs 
From Murojaat
WHERE TG_ID = "{}"
"""

upd_QoshilganVaqt = """
UPDATE Murojaat 
SET QoshilganVaqt = "{}" 
WHERE TG_ID = "{}"
"""
select_QoshilganVaqt = """
SELECT QoshilganVaqt 
From Murojaat
WHERE TG_ID = "{}"
"""
