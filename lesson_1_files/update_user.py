from lesson_2_files.db import db_session
from models import User


user = User.query.first()
user.salary = 5000
db_session.commit()