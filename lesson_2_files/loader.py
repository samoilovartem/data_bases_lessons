import csv
import time
from db import db_session
from models import Salary

# This option is good to use when we get data one by one,
# so we save it into database one by one, but it`s slow :(


def read_csv(filename):
    with open(filename, 'r', encoding='UTF-8') as file:
        fields = ['name', 'city', 'street', 'company', 'job', 'phone_number',
                  'email', 'date_of_birth', 'salary']
        reader = csv.DictReader(file, fields, delimiter=';')
        for row in reader:
            save_salary_data(row)


def save_salary_data(row):
    salary = Salary(name=row['name'], city=row['city'], address=row['street'],
                    company=row['company'], job=row['job'],
                    phone_number=row['phone_number'], email=row['email'],
                    date_of_birth=row['date_of_birth'], salary=row['salary'])
    db_session.add(salary)
    db_session.commit()


# This option is good to use when we already have all data and we just need to upload it
# into database. It`s much faster :)


def read_csv2(filename):
    with open(filename, 'r', encoding='UTF-8') as file:
        fields = ['name', 'city', 'address', 'company', 'job', 'phone_number',
                  'email', 'date_of_birth', 'salary']
        reader = csv.DictReader(file, fields, delimiter=';')
        salary_data = []
        for row in reader:
            salary_data.append(row)
        save_salary_data2(salary_data)


def save_salary_data2(data):
    db_session.bulk_insert_mappings(Salary, data)
    db_session.commit()


if __name__ == '__main__':
    # start = time.time()
    # read_csv('payments.csv')
    # print(f'Uploading took {time.time() - start} seconds')

    start = time.time()
    read_csv2('salary.csv')
    print(f'Uploading took {time.time() - start} seconds')
