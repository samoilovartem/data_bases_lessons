import csv
import random
from faker import Faker
from datetime import date


fake = Faker()


def generate_fake_companies(num_rows=10):
    companies = []
    for _ in range(num_rows):
        companies.append(
            [fake.company(), fake.city(),
             fake.street_address(), fake.phone_number()]
        )
    return companies


def generate_fake_employees(companies, num_rows=10):
    employees = []
    for company in companies:
        for _ in range(num_rows):
            employee = [fake.name(), fake.job(), fake.phone_number(),
                        fake.free_email(), fake.date_of_birth(minimum_age=18, maximum_age=70)]
            employees.append(company + employee)
    return employees


def generate_fake_payments(employees):
    payments = []
    for employee in employees:
        for month in range(1, 13):
            payment_date = date(2021, month, random.randint(10, 28))
            amount = random.randint(20000, 200000)
            payment = [payment_date, amount]
            payments.append(employee + payment)
    return payments


def generate_data(payments):
    with open('payments.csv', 'w', encoding='UTF-8') as file:
        writer = csv.writer(file, delimiter=';')
        for payment in payments:
            writer.writerow(payment)


if __name__ == '__main__':
    companies = generate_fake_companies()
    employees = generate_fake_employees(companies)
    payments = generate_fake_payments(employees)
    generate_data(payments)
