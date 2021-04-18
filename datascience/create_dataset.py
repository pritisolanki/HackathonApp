from faker import Faker
import json
from faker.providers import BaseProvider
import random 
import pprint
from random import randrange
import csv

fake = Faker()
#Set the dataset fields
csv_columns = ['name','age','lat','lng','disable','outdoor','preparation', 'community', 'local_support', 'environment', 'asset_protection','acts']

preparation = ['Prepare your emergency kit for flood diaster', 'Prepare your emergency kit for fire diaster','Create educational material to show impact of disaster impact',
'Register at flood warning service/ and bureau of meteorology warning service','Check if the house is at risk by looking at the flood map',
'Make an emergency package']

community = ['Contribute to local communities','Deliver grocery or medications to neighbours','Attend  community service','Donate books ,movies and newspaper to library',
'Try 5-min meditation','Talk to elderly','Invitee community member to your celebrations','Bike, walk or take public transport','Introduce your self to your neighbours',
'Take a test to check your wellbeing after disaster','Donate what you don’t use.']

local_support = ['Support local produce','Go to framer market','Buy  handmade products','Buy from "nothing group" facebook group','Help someone with your skills',
'Support startups ideas','Donate local hospitals and well being centres online','Volunteer to a Cause']

environment = ['Plant native plants to support wildlife','Adopt pet/Wildlife','Create wildlife habitats','Donate plants/tree to school or community'
'support local meetup group','Help in your neighbors garden','Place a bird feeder','Prune branches from overhanging trees.']

asset_protection = ['Donate to local leader group online', 'Write to local authorities to help the local groups', 'Back up important data for company/ yourself/ community',
'Mark "places" as vital for the community online','Digitalise important photos for your family/ community']

#custom provider for problem specific needs - Hobby
class CategoryOutdoorProvider(BaseProvider):
    def categoryoutdoor(self):
        categoriesoutdoor = ['preparation', 'local_support', 'asset_protection']
        categoriesoutdoor = random.sample(categoriesoutdoor,3)
        categories_string = ','.join(categoriesoutdoor)
        return categories_string
fake.add_provider(CategoryOutdoorProvider)


class CategoryProvider(BaseProvider):
    def category(self):
        categories = ['preparation', 'community', 'local_support', 'environment', 'asset_protection']
        categories = random.sample(categories,3)
        categories_string = ','.join(categories)
        return categories_string
fake.add_provider(CategoryProvider)

#custom provider for problem specific needs - Age
class AgeProvider(BaseProvider):
    def age(self):
        age = randrange(12,90)
        return age
fake.add_provider(AgeProvider)

def getpreparation():
    return ','.join(random.sample(preparation,2))   

def getcommunity():
    return ','.join(random.sample(community,2))

def getlocal_support():
    return ','.join(random.sample(local_support,2))

def getenvironment():
    return ','.join(random.sample(environment,2))

def getasset_protection():
    return ','.join(random.sample(asset_protection,2))

def getcategories(outdoor):
    if(outdoor) :
        return fake.categoryoutdoor()
    else:
        return fake.category()
        
#get the actions
def getacts(categories):
    catArr = categories.split(',')
    acts = {}
    preparation = ''
    community = ''
    local_support = ''
    environment = ''
    asset_protection = ''
    for category in catArr:
        if(category == 'preparation'):
            preparation = getpreparation()
            
        if(category == 'community' ):
            community = getcommunity()

        if(category == 'local_support'):
            local_support = getlocal_support()

        if(category == 'environment' ):
            environment = getenvironment()

        if(category == 'asset_protection'):
            asset_protection = getasset_protection()

        acts={preparation,community,local_support,environment,asset_protection}
    return ','.join(acts)

#create dataset
def create_dataset(x):
        customer_data = {}
        for i in range(0, x):
            outdoor = fake.boolean(chance_of_getting_true=35)
            categories = getcategories(outdoor)        
            acts = getacts(categories)
            preparation = 0
            community = 0
            local_support = 0
            environment = 0
            asset_protection = 0

            if 'preparation' in categories:
               preparation = 1

            if 'community' in categories:
               community = 1

            if 'local_support' in categories:
               local_support = 1

            if 'environment' in categories:
               environment = 1
               
            if 'asset_protection' in categories:
               asset_protection = 1

            au_latlng = fake.local_latlng(country_code='AU', coords_only=True)
            lat = au_latlng[0]
            lng = au_latlng[1]

            customer_data[i]={ 
                                'name': fake.name(), 
                                'age': fake.age(),
                                'lat': lat,
                                'lng' : lng,
                                'disable' : fake.boolean(chance_of_getting_true=25),
                                'outdoor' : outdoor,
                                'preparation': preparation,
                                'community':community,
                                'local_support':local_support,
                                'environment':environment,
                                'asset_protection':asset_protection,                                
                                'acts' : acts[1:]
                            }        
        return customer_data
 
user_data = create_dataset(30000)
#pprint.pprint(user_data)
#generate csv
csv_file = "fake_dataset.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in user_data:
            writer.writerow(user_data[data])
except IOError:
    print("I/O error")s