

# lambda_src/pdf_data_generator/main.py
import os
import json
import boto3
import random
from .pdf_filler import fill_pdf
from .random_data import generate_patient_data

ssm = boto3.client("ssm")
s3 = boto3.client("s3")

def lambda_handler(event, context):
    # 1. Fetch parameter names from environment variables
    param_patient_range = os.environ.get("PARAM_PATIENT_RANGE")
    param_s3_bucket = os.environ.get("PARAM_S3_BUCKET")

    # 2. Retrieve actual values from SSM
    patient_range_val = ssm.get_parameter(Name=param_patient_range)["Parameter"]["Value"]  # e.g. "5-10"
    output_bucket_param = ssm.get_parameter(Name=param_s3_bucket)["Parameter"]["Value"]   # e.g. "my-output-bucket"

    # 3. Parse the patient range
    min_patients, max_patients = map(int, patient_range_val.split('-'))
    num_patients = random.randint(min_patients, max_patients)

    # 4. For each patient, generate data, fill PDF, and upload
    for i in range(num_patients):
        patient_data = generate_patient_data()  # from random_data.py

        # Path to the bundled PDF in 'assets/'
        pdf_template_path = os.path.join(os.path.dirname(__file__), 'assets', 'Drug-Prior-Authorization-Form.pdf')

        # Fill PDF in memory (returns bytes)
        filled_pdf_bytes = fill_pdf(pdf_template_path, patient_data)

        # Upload to S3
        pdf_filename = f"patient_{i+1}.pdf"
        s3.put_object(
            Bucket=output_bucket_param,
            Key=pdf_filename,
            Body=filled_pdf_bytes
        )

    return {
        "statusCode": 200,
        "body": json.dumps(f"Generated {num_patients} PDF(s) and uploaded to {output_bucket_param}")
    }
