import happybase as hb
import csv

conn = hb.Connection()

# TODO #

table = conn.table('powers')
header_lines = 2

with open('input.csv', 'rb') as f:
    reader = csv.reader(f)
    # skip 2 lines
    reader.next()
    reader.next()

    for row in reader:
        data = {}

        data[b'personal:hero'] = row[1]
        data[b'personal:power'] = row[2]
        data[b'professional:name'] = row[3]
        data[b'professional:xp'] = row[4]
        data[b'custome:color'] = row[5]

        table.put(row[0], data)

print('Inserted data')

########

conn.close()
