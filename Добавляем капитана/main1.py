from data.users import User
from data import db_session


db_session.global_init("db/users.db")


user = User()
user.surname = "Scott"
user.name = "Ridley"
user.age = 21
user.position = "captain"
user.speciality = "research engineer"
user.address = "module_1"
user.email = "scott_chief@mars.org"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()

user = User()
user.surname = "Smith"
user.name = "John"
user.age = 25
user.position = "employeer"
user.speciality = "research engineer"
user.address = "module_2"
user.email = "johnsmth@mars.org"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()

user = User()
user.surname = "Johnson"
user.name = "Thomas"
user.age = 20
user.position = "employeer"
user.speciality = "research engineer"
user.address = "module_2"
user.email = "thomasjson@mars.org"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()

user = User()
user.surname = "Brown"
user.name = "James"
user.age = 28
user.position = "employeer"
user.speciality = "research engineer"
user.address = "module_3"
user.email = "jambron@mars.org"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()
