import happybase as hb
import csv

conn = hb.Connection()

# TODO #

table = conn.table('powers')

for key, data in table.scan(include_timestamp=True):
    print('Found: {}, {}'.format(key, data))

########

conn.close()
