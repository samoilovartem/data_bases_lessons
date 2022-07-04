from models import Salary
from sqlalchemy.sql import func
from sqlalchemy import desc
from db import db_session


def top_salary(num_rows):
    top_salary = Salary.query.order_by(Salary.salary.desc()).limit(num_rows)

    for s in top_salary:
        print(f'Salary: {s.salary}')


def salary_by_city(city):
    top_salary = Salary.query.filter(Salary.city == city).order_by(Salary.salary.desc())

    print(city)
    for s in top_salary:
        print(f'Salary: {s.salary}')


def salary_by_email_domain(domain, num_rows):
    top_salary = Salary.query.filter(Salary.email.ilike(f'%{domain}')).order_by(Salary.salary.desc())\
                .limit(num_rows)

    print(domain)
    for s in top_salary:
        print(f'Salary: {s.salary}')


def average_salary():
    avg_salary = db_session.query(func.avg(Salary.salary)).scalar()
    print(f'Average salary is {avg_salary:.2f}')


def count_distinct_cities():
    count_cities = db_session.query(Salary.city).group_by(Salary.city).count()
    print(f'Total amount of cities is {count_cities}')


def top_avg_salary_by_city(num_rows):
    top_salary = db_session.query(
        Salary.city,
        func.avg(Salary.salary).label('avg_salary')
    ).group_by(Salary.city).order_by(desc('avg_salary')).limit(num_rows)

    for city, salary in top_salary:
        print(f'In {city} average salary is {salary:.2f}')


if __name__ == '__main__':
    # top_salary(10)
    # salary_by_city('Rickybury')
    # salary_by_email_domain('@gmail.com', 10)
    # average_salary()
    # count_distinct_cities()
    top_avg_salary_by_city(5)