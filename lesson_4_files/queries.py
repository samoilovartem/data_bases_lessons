from sqlalchemy import func

from models import Project, Company, ProjectEmployee, Employee
from db import db_session


def get_company_projects_employees(company_name):
    query = Project.query.join(
        Project.company, Project.employees
    ).filter(Company.name == company_name)

    for project in query:
        print('-' * 20)
        print(project.name)
        for project_employee in project.employees:
            delta = (project_employee.date_end - project_employee.date_start).days
            print(f'{project_employee.employee.name} -- {delta}')


def project_time_total(company_name):
    query = db_session.query(
        Project.name,
        func.sum(ProjectEmployee.date_end - ProjectEmployee.date_start)
    ).join(
        Project.company, Project.employees
    ).filter(
        Company.name == company_name
    ).group_by(Project.name)

    for project_name, delta in query:
        print(f'{project_name} -- {delta}')


def project_employees_time_total(company_name):
    query = db_session.query(
        Project.name,
        Employee.name,
        func.sum(ProjectEmployee.date_end - ProjectEmployee.date_start)
    ).join(
        Project.company, Project.employees, ProjectEmployee.employee
    ).filter(
        Company.name == company_name
    ).group_by(Project.name, Employee.name)

    for project_name, employee_name, delta in query:
        print(f'{project_name} -- {employee_name} -- {delta}')


if __name__ == '__main__':
    # get_company_projects_employees('Edwards-Dillon')
    # project_time_total('Edwards-Dillon')
    project_employees_time_total('Edwards-Dillon')