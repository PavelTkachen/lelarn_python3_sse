from datetime import datetime
import random
import datetime
from faker import Faker
fake = Faker()

def get_data():
    data = list()
    for _ in range(10):
        data.append({'id': random.randrange(1, 10000), 'name': fake.name() , 'date': datetime.datetime.now()})
    return data