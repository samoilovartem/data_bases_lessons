import csv
import random
from models import Company
from datetime import date, timedelta


def get_project_name():
    projects = ['Rebranding', 'CRM development', '1С maintenance', 'Website development',
                'Customer survey', 'Call center launching', 'Wifi network modernization',
                'Researching', 'Website design', 'Mobile app development',
                'Booklet design', 'Information security audit',
                'Staff training']

    return random.choice(projects)


def make_projects_for_employee(company_id, employee_id):
    projects = []
    for month in range(1, 13):
        start_date = date(2021, month, random.randint(1, 10))
        end_date = start_date + timedelta(days=random.randint(5, 20))
        project = [get_project_name(), company_id, employee_id, start_date, end_date]
        projects.append(project)
    return projects


def make_fake_projects():
    data = []
    companies = Company.query.all()
    for company in companies:
        for employee in company.employees:
            data += make_projects_for_employee(company.id, employee.id)
    return data


def generate_data(data, filename):
    with open(filename, 'w', encoding='UTF-8') as file:
        writer = csv.writer(file, delimiter=';')
        for row in data:
            writer.writerow(row)


if __name__ == '__main__':
    generate_data(make_fake_projects(), 'projects.csv')
