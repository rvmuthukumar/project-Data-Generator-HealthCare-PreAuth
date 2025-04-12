

# lambda_src/pdf_data_generator/random_data.py
from faker import Faker
import random

fake = Faker()

def generate_patient_data():
    """
    Return a dictionary mapping PDF field names to random data.
    Adjust field keys to match the actual PDF form field names.
    """
    data = {
        "First Name": fake.first_name(),
        "Last Name": fake.last_name(),
        "MI": fake.random_letter().upper(),
        "Phone Number": fake.phone_number(),
        "Address": fake.street_address(),
        "City": fake.city(),
        "State": fake.state_abbr(),
        "Zip Code": fake.zipcode(),
        "Date of Birth": fake.date_of_birth(minimum_age=18, maximum_age=90).strftime("%m/%d/%Y"),
        "Plan/Medical Group Name": fake.company(),
        "Plan/Medical Group Phone": fake.phone_number(),
        "Plan/Medical Group Fax": fake.phone_number(),
        # ... etc. for all PDF fields you want.
        "Medication Name": random.choice(["Amoxicillin", "Lisinopril", "Atorvastatin", "Metformin", "Acetaminophen" ,  "Ibuprofen" , 
                                            "Aspirin"  , "Albuterol" ,   "Amlodipine" , "Levothyroxine"   ,  "Omeprazole"  ,
                                            "Losartan"  ,"Hydrochlorothiazide"  ,"Gabapentin"  ,"Metoprolol"  , "Prednisone"  ,
                                            "Montelukast"  , "Furosemide"  , "Sertraline"  ,"Simvastatin"  ]),


        "Primary Insurance Name": fake.company(),
        "Patient ID Number": str(random.randint(100000, 999999)),
        # etc.
    }
    return data
