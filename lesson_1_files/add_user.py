from lesson_2_files.db import db_session
from models import User


user = User(name='Artem Samoilov', salary=5000, email='samoylov@somedomain.com')
db_session.add(user)
db_session.commit()