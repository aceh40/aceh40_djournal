import os
import sqlite3

from aceh40_djournal import settings

dir = settings.BASE_DIR

conn = sqlite3.connect(os.path.join(dir,'db.sqlite3'))
c = conn.cursor()

weight_history_file = open(r'C:\Users\assen_bankov\PycharmProjects\aceh40_djournal\wip_code\weight_history.csv', 'r')
file_content = weight_history_file.read()
file_content_rows = file_content.split('\n')
for row in file_content_rows:
    row = row.split(',')
    print (row)
    c.execute("INSERT INTO journal_weightentry (created_date, weight, note, user_id) VALUES ('{}', {}, '{}', 2)".format(
        row[0], row[1], row[2]
    ))


# c.execute("")

conn.commit()