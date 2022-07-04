import time
from db import db_session
from models import Company, Employee


"""The task: we need to find a company by its name and show all its employees.
There are 3 methods we are going to use for that"""


def get_employees_by_company(company_name):
    """Better to use ".first" instead of ".one"
    since in this case we will not receive an exception if there is no item"""
    company = Company.query.filter(Company.name == company_name).first()
    employees_list = []
    if company:
        for employee in Employee.query.filter(Employee.company_id == company.id):
            employees_list.append(f'{company.name} - {employee.name}')
    return employees_list
    # It took 18.6 second to process 100 queries with the method above


def get_employees_by_company_join(company_name):
    query = db_session.query(Employee, Company).join(
        Company, Employee.company_id == Company.id
    ).filter(Company.name == company_name)
    employees_list = []
    for employee, company in query:
        employees_list.append(f'{company.name} - {employee.name}')
    return employees_list
    # It took 6.16 second to process 100 queries with the method above


def get_employees_by_company_relation(company_name):
    company = Company.query.filter(Company.name == company_name).first()
    employees_list = []
    if company:
        for employee in company.employees:
            employees_list.append(f'{company.name} - {employee.name}')
    return employees_list
    # It took 15.5 second to process 100 queries with the method above without "lazy='joined'"
    # It took 6.85 second to process 100 queries with the method above with "lazy='joined'" which is
    # approximately same as 2nd method (join), but the query is simpler


if __name__ == '__main__':
    # start = time.perf_counter()
    # for _ in range(100):
    #     get_employees_by_company('Massey-Colon')
    # print(f'get_employees_by_company: {time.perf_counter() - start}')

    # start = time.perf_counter()
    # for _ in range(100):
    #     get_employees_by_company_join('Massey-Colon')
    # print(f'get_employees_by_company_join: {time.perf_counter() - start}')

    start = time.perf_counter()
    for _ in range(100):
        get_employees_by_company_relation('Massey-Colon')
    print(f'get_employees_by_company_relation: {time.perf_counter() - start}')



