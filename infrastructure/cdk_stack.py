'''
    - Defines resources
        - A AWS Lambda function pointing to ambda_src/pdf_data_generator
        - A Scheduled Event Bridge Daily
        - References to Parameter Store Parameters

'''

# infrastructure/cdk_stack.py

from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_events as events,
    aws_events_targets as targets,
    aws_ssm as ssm,
    aws_iam as iam,
)
from constructs import Construct
import aws_cdk as cdk

class PdfDataGeneratorStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # SSM Parameters (assuming they already exist)
        no_of_patients_range = ssm.StringParameter.from_string_parameter_attributes(
            self, "NoOfPatientsRangeParam",
            parameter_name="/pre_auth_forms/No_Of_Patients_Range"
        )
        output_s3_bucket_name = ssm.StringParameter.from_string_parameter_attributes(
            self, "OutputS3BucketParam",
            parameter_name="/pre_auth_forms/Output_S3_Bucket_Name"
        )

        # Create Lambda function
        lambda_fn = _lambda.Function(
            self,
            "PdfDataGeneratorLambda",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="main.lambda_handler",  # main.py's function
            code=_lambda.Code.from_asset("lambda_src/pdf_data_generator"),
            environment={
                "PARAM_PATIENT_RANGE": no_of_patients_range.parameter_name,
                "PARAM_S3_BUCKET": output_s3_bucket_name.parameter_name,
            }
        )

        # Give Lambda permission to read the parameters
        no_of_patients_range.grant_read(lambda_fn)
        output_s3_bucket_name.grant_read(lambda_fn)

        # If the Lambda needs to upload to S3, you can attach relevant permissions:
        # Replace <bucket-arn> with the actual ARN if you want to restrict to a single bucket.
        # lambda_fn.add_to_role_policy(iam.PolicyStatement(
        #     actions=["s3:PutObject", "s3:GetObject"],
        #     resources=["arn:aws:s3:::my-output-bucket/*"]
        # ))

        # Create EventBridge rule to trigger daily
        rule = events.Rule(
            self,
            "DailyPdfGenRule",
            schedule=events.Schedule.rate(cdk.Duration.days(1))
        )
        rule.add_target(targets.LambdaFunction(lambda_fn))
