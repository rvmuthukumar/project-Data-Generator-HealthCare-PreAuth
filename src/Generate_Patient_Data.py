import json
import random

def generate_test_data(num_records, output_path):
    first_names = ["John", "Jane", "Alice", "Robert", "Michael", "Emily", "Sophia", "Daniel"]
    last_names = ["Doe", "Smith", "Brown", "Williams", "Johnson", "Davis", "Martinez", "Wilson"]
    states = ["NY", "CA", "TX", "FL", "IL", "PA", "OH", "MI"]
    cities = {
        "NY": "New York",
        "CA": "Los Angeles",
        "TX": "Houston",
        "FL": "Miami",
        "IL": "Chicago",
        "PA": "Philadelphia",
        "OH": "Columbus",
        "MI": "Detroit"
    }

    records = []
    for _ in range(num_records):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        state = random.choice(states)

        record = {
            "first_name": first_name,
            "last_name": last_name,
            "middle_initial": random.choice(["A", "B", "C", "D", "E"]),
            "member_id": str(random.randint(100000000, 999999999)),
            "birth_date": f"{random.randint(1, 12):02d}/{random.randint(1, 28):02d}/{random.randint(1950, 2005)}",
            "phone_number": f"555-{random.randint(100, 999)}-{random.randint(1000, 9999)}",
            "home_address": f"{random.randint(100, 9999)} {random.choice(['Main St', 'Broadway', 'Elm St', 'Maple Ave'])}",
            "city": cities[state],
            "state": state,
            "zip_code": f"{random.randint(10000, 99999)}",
            "requesting_provider_name": f"Dr. {random.choice(['Adams', 'Baker', 'Clark', 'Davis'])}",
            "provider_phone": f"555-{random.randint(100, 999)}-{random.randint(1000, 9999)}",
            "provider_fax": f"555-{random.randint(100, 999)}-{random.randint(1000, 9999)}",
            "provider_npi": str(random.randint(1000000000, 9999999999)),
            "provider_tax_id": str(random.randint(100000000, 999999999)),
            "provider_address": f"{random.randint(100, 9999)} {random.choice(['Medical Center', 'Health Plaza', 'Clinic'])+", " + cities[state] +", "+ state}",
            "facility_name": f"{random.choice(['City Hospital', 'Wellness Clinic', 'Medical Center'])}",
            "facility_address": f"{random.randint(100, 9999)} {random.choice(['Health St', 'Wellness Blvd', 'Clinic Ave'])+", " + cities[state] +", "+ state}",
            "diagnoses": [{"ICD-10": f"{random.randint(100, 999)}.{random.randint(0, 9)}"} for _ in range(5)],
            "procedures": [{"CPT": f"{random.randint(10000, 99999)}"} for _ in range(5)],
            "reason_for_referral": random.choice([
                "Patient requires specialized treatment for chronic illness.",
                "Referral for advanced diagnostic testing and evaluation.",
                "Patient requires pre-operative clearance and consultation.",
                "Patient requires specialized treatment for chronic illness & diabetes management.",
                "Referral for advanced diagnostic imaging, including MRI and CT scan evaluation.",
                "Patient requires pre-operative clearance and specialist consultation before surgery.",
                "Request for durable medical equipment (DME) due to mobility impairment.",
                "Authorization for physical therapy sessions following post-surgical rehabilitation.",
                "Referral to a cardiologist for abnormal ECG results and further evaluation.",
                "Patient requires long-term home healthcare services for ongoing chronic conditions.",
                "Request for outpatient behavioral therapy for anxiety and depression management.",
                "Patient needs an oncology consultation due to recent abnormal biopsy results.",
                "Authorization for inpatient hospitalization for acute medical condition management."


            ]),
            "patient_signature": f"{first_name} {last_name}",
            "signature_date": f"{random.randint(1, 12):02d}/{random.randint(1, 28):02d}/{2024}"
        }
        records.append(record)
    
    with open(output_path, "w") as f:
        json.dump(records, f, indent=4)



patient_data_file_path = "../Data/PatientData/test_patient_data.json"

# Example usage:
generate_test_data(10, patient_data_file_path)
