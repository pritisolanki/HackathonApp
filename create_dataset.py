from faker import Faker
import json
from faker.providers import BaseProvider
import random 
import pprint
from random import randrange
import csv

fake = Faker()
csv_columns = ['name','country','age','disable','outdoor','hobbies',]

#custom provider
class HobbyProvider(BaseProvider):
    def hobby(self):
        hobbies = ['Writing', 'Blogging', 'Gardening', 'Craft', 'Cooking', 'Outdoor Activities', 'Volunteering']
        hobby_choices = random.sample(hobbies,5)
        hobby_string = ','.join(hobby_choices)
        return hobby_string
fake.add_provider(HobbyProvider)

class AgeProvider(BaseProvider):
    def age(self):
        age = randrange(12,90)
        return age
fake.add_provider(AgeProvider)

#create dataset
def create_dataset(x):
        customer_data = {}
        for i in range(0, x):
            customer_data[i]={ 
                                'name': fake.name(), 
                                'country' : fake.country(), 
                                'age': fake.age(),
                                'disable' : fake.boolean(chance_of_getting_true=25),
                                'outdoor' : fake.boolean(chance_of_getting_true=35),
                                'hobbies' : fake.hobby()
                            }        
        return customer_data
    
user_data = create_dataset(100)

#generate csv
csv_file = "fake_dataset.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in user_data:
            writer.writerow(user_data[data])
except IOError:
    print("I/O error")