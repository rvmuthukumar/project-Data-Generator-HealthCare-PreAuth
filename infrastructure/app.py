# infrastructure/app.py
'''
    Entry point for the CDK app 

'''
import aws_cdk as cdk
from .cdk_stack import PdfDataGeneratorStack

app = cdk.App()
PdfDataGeneratorStack(app, "PdfDataGeneratorStack")

app.synth()
