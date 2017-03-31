import happybase as hb

conn = hb.Connection()

# TODO #

powers_cf = {
    'personal': dict(),
    'professional': dict(),
    'custome': dict()
}

food_cf = {
    'nutrition': dict()
}

conn.create_table('powers', powers_cf)
print('Created table powers')

conn.create_table('food', food_cf)
print('Created table food')

########

conn.close()
