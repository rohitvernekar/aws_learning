import json

def lambda_handler(event, context):
    print(event)
    api_key=event['authorizationToken']
    if api_key == "test123":
        auth="Allow"
    else:
        auth="Deny"
    authResponse = {}
    authResponse['principalId'] = "test1"
    policyDocument = {}
    policyDocument['Version'] = '2012-10-17'
    policyDocument['Statement'] = []
    statementOne = {}
    statementOne['Action'] = 'execute-api:Invoke'
    statementOne['Effect'] = auth
    statementOne['Resource'] = ["arn:aws:execute-api:us-east-1:237541920932:loya092ah7/*/*"]
    policyDocument['Statement'] = [statementOne]
    authResponse['policyDocument'] = policyDocument
    return authResponse
