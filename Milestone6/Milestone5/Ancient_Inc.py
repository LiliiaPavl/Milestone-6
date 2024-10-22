import csv
from faker import Faker

fake = Faker()

num_employees = 43
employee_data = [{
    'Name': fake.name(),
    'Hiring Date': fake.date_this_decade(),
    'Department': fake.job(),
    'Birthday': fake.date_of_birth(minimum_age=20, maximum_age=60)
} for _ in range(num_employees)]

with open('database.csv', mode='w') as file:
    writer = csv.DictWriter(file, fieldnames=employee_data[0].keys())
    writer.writeheader()
    writer.writerows(employee_data)

print(f" {num_employees} employee records in 'database.csv'.")
     