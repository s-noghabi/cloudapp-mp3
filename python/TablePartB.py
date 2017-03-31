import happybase as hb

conn = hb.Connection()

# TODO #

print('Found tables:')
print(conn.tables())

########

conn.close()
