from basic import db, Puppy

# CREATES ALL THE TABLES
# Converts our model class to DB table
db.create_all()

### CREATE ###
sammy = Puppy('Sammy', 3)
frankie = Puppy('Frankie', 4)
db.session.add_all([sammy, frankie])
db.session.commit()

rufus = Puppy('Rufus', 5)
db.session.add(rufus)
db.session.commit()

### READ ###
print("### READ ###")
all_puppies = Puppy.query.all() # List of puppies objects in the table!
print(all_puppies)

# SELECT BY ID
print("# SELECT BY ID")
# puppy_one = Puppy.query.get(1)
puppy_one = db.session.get(Puppy, 1)
print(puppy_one.name)

# FILTERS
# PRODUCE SOME SQL CODE!
print("# FILTERS")
puppy_frankie = Puppy.query.filter_by(name='Frankie')
print(puppy_frankie.all())

### UPDATE ###
print("### UPDATE ###")
# first_puppy = Puppy.query.get(1)
first_puppy = db.session.get(Puppy, 1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

### DELETE ###
print("### DELETE ###")
# second_puppy = Puppy.query.get(2)
second_puppy = db.session.get(Puppy, 2)
db.session.delete(second_puppy)
db.session.commit()

#
print("### PRINT ###")
all_puppies = Puppy.query.all()
print(all_puppies)