import csv
import time
from db import db_session
from models import Payment, Employee, Company


def read_csv(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        fields = ['company',  'city', 'address', 'phone_company', 'name', 'job',
                  'phone_person', 'email', 'date_of_birth', 'payment_date', 'amount']
        reader = csv.DictReader(f, fields, delimiter=';')
        payments_data = []
        for row in reader:
            payments_data.append(row)
        return payments_data


def save_companies(all_data):
    processed = []
    unique_companies = []
    for row in all_data:
        if row['company'] not in processed:
            company = {'name': row['company'], 'city': row['city'],
                       'address': row['address'], 'phone': row['phone_company'],
            }
            unique_companies.append(company)
            processed.append(company['name'])
    db_session.bulk_insert_mappings(Company, unique_companies, return_defaults=True)
    db_session.commit()
    return unique_companies


def save_employees(all_data, companies):
    processed = []
    unique_employees = []
    for row in all_data:
        if row['phone_person'] not in processed:
            employee = {'name': row['name'], 'job': row['job'], 'email': row['email'],
                        'phone': row['phone_person'], 'date_of_birth': row['date_of_birth'],
                        'company_id': get_company_id(row['company'], companies)}
            unique_employees.append(employee)
            processed.append(row['phone_person'])
    db_session.bulk_insert_mappings(Employee, unique_employees, return_defaults=True)
    db_session.commit()
    return unique_employees


def get_company_id(company_name, unique_companies):
    for row in unique_companies:
        if row['name'] == company_name:
            return row['id']
    return None


def save_payments(all_data, employees):
    payments = []
    for row in all_data:
        payment = {'payment_date': row['payment_date'], 'amount': row['amount'],
                   'employee_id': get_employee_id(row['phone_person'], employees)
        }
        payments.append(payment)
    db_session.bulk_insert_mappings(Payment, payments)
    db_session.commit()


def get_employee_id(phone, unique_employees):
    for row in unique_employees:
        if row['phone'] == phone:
            return row['id']
    return None


if __name__ == '__main__':
    data = read_csv('payments.csv')
    companies = save_companies(data)
    employees = save_employees(data, companies)
    save_payments(data, employees)
