- When you run cdk synth or cdk deploy, the CDK CLI will execute the  command based on the cdk.json, which calls the  infrastructure/app.py.

## app:

- Tells the CDK CLI how to run your application. In this case, it calls Python, instructing it to run the infrastructure/app.py module.
Make sure the infrastructure/app.py path corresponds to where your code actually resides.
## context (Optional but recommended):

- You can store CDK context keys that change features or versioning behaviors. For example:
@aws-cdk/core:newStyleStackSynthesis enables the modern (v2) style synthesis.
aws-cdk:enableDiffNoFail means that if there’s a difference in cdk diff, it won’t fail automatically.
## Other keys 
- may be added based on your project’s needs. For instance, you might include custom context to parameterize environment variables or references used by your CDK code.