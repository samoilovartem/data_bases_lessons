import csv
import random
from faker import Faker

fake = Faker()


def get_fake_row():
    return [fake.name(), fake.city(), fake.street_address(),
            fake.company(),
            fake.job(), fake.phone_number(), fake.free_email(),
            fake.date_of_birth(minimum_age=18, maximum_age=70),
            random.randint(20000, 200000)]


def generate_data(num_rows=100):
    with open('salary.csv', 'w', encoding='UTF-8') as file:
        writer = csv.writer(file, delimiter=';')
        for _ in range(num_rows):
            writer.writerow(get_fake_row())


if __name__ == '__main__':
    generate_data()
