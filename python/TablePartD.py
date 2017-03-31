import happybase as hb
import csv

conn = hb.Connection()

# tuples of rows and the corresponding columns to read
to_read = [
    (b'row1', (b'hero', b'power', b'name', b'xp', b'color')),
    (b'row4', (b'hero', b'color')),
    (b'row12', (b'power', b'name', b'color')),
    (b'row1', (b'hero', b'name', b'color')),
    (b'row8', (b'hero', b'power')),
    (b'row19', (b'name', b'color'))
]

# TODO #

convert = {
    b'hero': b'personal:hero',
    b'power': b'personal:power',
    b'name': b'professional:name',
    b'xp': b'professional:xp',
    b'color': b'custome:color'
}

table = conn.table('powers')

for row, cols in to_read:
    row = table.row(row)
    printlist = []

    for column in cols:
        printlist.append(column + ':' + row[convert[column]])

    print(','.join(printlist))

########

conn.close()
