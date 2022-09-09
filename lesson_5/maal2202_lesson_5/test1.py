# Lektion 5 - Övning 1

firstname = "john"
lastname = "smith"
tele = "00468123456789"

# 1
print (f'Firstname: {firstname}, Lastname: {lastname}, Phonenumber: {tele}')

# 2
fullname = firstname + str(" ") + lastname
print(fullname)

# 3
fullname = (f'{firstname} {lastname}')
print(fullname)

# 4
print(f' len() of fullname + firstname + lastname: {len(fullname) + len(firstname) + len(lastname)}')

# 5
print (f'Firstname: {firstname}, Lastname: {lastname}\nPhonenumber: {tele}')

# 6
print(str("Fullname: ") + fullname + str(", Phonenumber: ") + tele) # 6:1
print(f'Fullname: {fullname}, Phonenumber: {tele}') # 6:2
print("Fullname: {name}, Phonenumber: {phonenumber}".format(name=fullname, phonenumber=tele)) # 6:3
print("Fullname: %s, Phonenumber: %s" % (fullname, tele)) # 6:4