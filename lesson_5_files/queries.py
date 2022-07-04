import time

from models import Employee


def get_employee_by_job():
    start = time.perf_counter()
    for _ in range(10):
        Employee.query.filter(Employee.job == 'Art gallery manager').all()
    print(f'{time.perf_counter() - start}')


if __name__ == '__main__':
    """This is how we can check raw SQL query"""
    query = Employee.query.filter(Employee.job == 'Art gallery manager')
    print(query.first())


