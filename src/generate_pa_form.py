import json
import os
import random
import boto3
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def load_config():
    """Load configuration from config.json."""
    with open("config.json", "r") as file:
        return json.load(file)

def load_template_spec():
    """Load template specifications from template_spec.json."""
    with open("template_spec.json", "r") as file:
        return json.load(file)

def generate_random_patient_data(patient_id, template_id):
    """Generate random patient data based on template specifications."""
    first_names = ["John", "Jane", "Michael", "Emily", "Chris", "Olivia"]
    last_names = ["Doe", "Smith", "Johnson", "Williams", "Brown"]
    specialties = ["Cardiology", "Neurology", "Orthopedics", "Oncology"]
    services = ["MRI Scan", "CT Scan", "Physical Therapy", "Chemotherapy"]
    medications = ["Atorvastatin", "Metformin", "Lisinopril", "Amlodipine"]
    
    patient = {
        "patient_id": patient_id,
        "name": {
            "first": random.choice(first_names),
            "middle": "A",
            "last": random.choice(last_names)
        },
        "date_of_birth": f"{random.randint(1950, 2010)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}",
        "insurance": {
            "provider": "XYZ Health Plan",
            "policy_number": f"ABC-{random.randint(100000000, 999999999)}"
        },
        "provider": {
            "name": f"Dr. {random.choice(first_names)} {random.choice(last_names)}",
            "specialty": random.choice(specialties),
            "npi": f"{random.randint(1000000000, 9999999999)}",
            "contact": {
                "phone": f"555-{random.randint(1000, 9999)}",
                "fax": f"555-{random.randint(1000, 9999)}",
                "address": "123 Medical St, Suite 200, City, State, 12345"
            }
        },
        "prior_authorization": {
            "type": template_id,
            "service_requested": random.choice(services + medications),
            "cpt_code": f"{random.randint(10000, 99999)}",
            "icd_10": f"R{random.randint(0,99)}.{random.randint(0,9)}",
            "justification": "Medical necessity for the requested service."
        }
    }
    return patient

def generate_pa_form(patient_data, output_folder, template_spec):
    """Generate a Prior Authorization form as a PDF using patient data."""
    template_id = patient_data['prior_authorization']['type']
    template_info = next(t for t in template_spec['templates'] if t['template_id'] == template_id)
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    pdf_filename = os.path.join(output_folder, f"PA_Form_{patient_data['patient_id']}_T{template_id}.pdf")
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    width, height = letter
    
    c.setFont("Helvetica-Bold", 14)
    c.drawString(200, height - 50, template_info['fields']['header']['title'])
    
    # Add missing sections dynamically
    y_position = height - 80
    for section, fields in template_info['fields'].items():
        if isinstance(fields, dict):
            c.setFont("Helvetica-Bold", 12)
            c.drawString(50, y_position, section.replace('_', ' ').title())
            y_position -= 20
            c.setFont("Helvetica", 10)
            for key, value in fields.items():
                if isinstance(value, bool) and value:
                    c.drawString(50, y_position, f"{key.replace('_', ' ').title()}: {patient_data.get(key, 'N/A')}")
                    y_position -= 20
    
    # Save PDF
    c.save()
    print(f"Generated: {pdf_filename}")
    return pdf_filename

def main():
    config = load_config()
    template_spec = load_template_spec()
    output_folder = config["output_folder"]
    num_forms = random.randint(config["form_count_range"][0], config["form_count_range"][1])
    
    for i in range(num_forms):
        template_id = random.choice([1, 2, 3])
        patient_data = generate_random_patient_data(f"PAT{i+1}", template_id)
        generate_pa_form(patient_data, output_folder, template_spec)

if __name__ == "__main__":
    main()
