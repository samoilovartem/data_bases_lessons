from models import User


user = User.query.first()
print(f"""
Name: {user.name},
Salary: {user.salary}
Email: {user.email}
""")