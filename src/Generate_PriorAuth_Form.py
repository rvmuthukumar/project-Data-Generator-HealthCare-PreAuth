import json

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.acroform import AcroForm


def create_comprehensive_prior_auth_form(output_path,data):
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter
    form = AcroForm(c)

    # Title
    c.setFont("Helvetica-Bold", 14)
    c.drawString(160, height - 30, "Comprehensive Prior Authorization Request Form")
    
    c.setFont("Helvetica", 8)
    c.setFillColorRGB(1, 0, 0)
    c.drawString(230, height - 40, "IMPORTANT: Incomplete forms will NOT be processed.")
    c.setFillColorRGB(0, 0, 0)

    # Patient Information Section
    c.setFont("Helvetica-Bold", 10)
    c.drawString(50, height - 70, "Patient Information")
    c.setFont("Helvetica", 10)

    patient_fields = [
        ("First Name", data["first_name"], 50, height - 90, 200),
        ("Last Name", data["last_name"], 300, height - 90, 200),
        ("Middle Initial", data["middle_initial"], 50, height - 120, 50),
        ("Member ID", data["member_id"], 120, height - 120, 200),
        ("Birth Date", data["birth_date"], 350, height - 120, 150),
        ("Phone Number", data["phone_number"], 50, height - 150, 200),
        ("Home Address", data["home_address"], 50, height - 180, 500),
        ("City", data["city"], 50, height - 210, 200),
        ("State", data["state"], 270, height - 210, 50),
        ("ZIP Code", data["zip_code"], 350, height - 210, 100),
    ]

    for label, value, x, y, field_width in patient_fields:
        form.textfield(name=label, x=x, y=y - 20, width=field_width, height=15, value=value, tooltip=label)

    # Provider Information
    c.setFont("Helvetica-Bold", 10)
    c.drawString(50, height - 250, "Provider Information")
    c.setFont("Helvetica", 10)

    provider_fields = [
        ("Requesting Provider Name", data["requesting_provider_name"], 50, height - 270, 300),
        ("Provider Phone", data["provider_phone"], 50, height - 300, 200),
        ("Provider Fax", data["provider_fax"], 300, height - 300, 200),
        ("Provider NPI", data["provider_npi"], 50, height - 330, 200),
        ("Provider Tax ID", data["provider_tax_id"], 300, height - 330, 200),
        ("Provider Address", data["provider_address"], 50, height - 360, 500),
        ("Facility Name", data["facility_name"], 50, height - 390, 300),
        ("Facility Address", data["facility_address"], 50, height - 420, 500),
    ]

    for label, value, x, y, field_width in provider_fields:
        form.textfield(name=label, x=x, y=y - 20, width=field_width, height=15, value=value, tooltip=label)

    # Diagnosis & Procedures
    c.setFont("Helvetica-Bold", 10)
    c.drawString(50, height - 460, "Diagnosis & Procedures")
    c.setFont("Helvetica", 10)
    diagnosis_y = height - 480
    for i in range(5):
        form.textfield(name=f"Diagnosis {i+1} ICD-10", x=50, y=diagnosis_y - 20, width=250, height=15, value=data['diagnoses'][i]['ICD-10'])
        form.textfield(name=f"Procedure {i+1} CPT", x=320, y=diagnosis_y - 20, width=250, height=15, value=data['procedures'][i]['CPT'])
        diagnosis_y -= 30

    # Reason for Referral
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, diagnosis_y - 20, "Reason for Referral")
    form.textfield(name="Reason for Referral", x=50, y=diagnosis_y - 55, width=500, height=30, value=data["reason_for_referral"], tooltip="Enter referral reason")

    # Patient Consent & Signature
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, diagnosis_y - 100, "Patient Consent and Signature")
    c.setFont("Helvetica", 10)
    form.textfield(name="Patient Signature", x=50, y=diagnosis_y - 130, width=250, height=20, value=data["patient_signature"], tooltip="Patient Signature")
    form.textfield(name="Date", x=320, y=diagnosis_y - 130, width=100, height=20, value=data["signature_date"], tooltip="Date")

    # Finalizing
    c.save()


# Define output path
pdf_output_folder = "../Data/PreAuthForms"

# Load patient data
patient_data_file_path = "../Data/PatientData/test_patient_data.json"

with open(patient_data_file_path, "r") as f:
    patients_data = json.load(f)

for i, patient_data in enumerate(patients_data):
    pdf_path = f"{pdf_output_folder}/PriorAuthForm_{i+1}.pdf"    
    create_comprehensive_prior_auth_form(pdf_path, patient_data)
