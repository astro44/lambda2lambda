
import sys, os
import boto3
import multiprocessing.dummy as mp
import json



def execLambda( num ):
    pload ={'defined':{'sweet': num}}
    print pload
    region = 'us-east-1'
    session = boto3.session.Session()
    client = session.client('lambda', region)
    response = client.invoke(
            FunctionName= "lam2lam-test",
            InvocationType = "RequestResponse",
            Payload        = json.dumps(pload)
        )
    minionData =response['Payload'].read()
    print ' minion outgoing:',pload['defined'].keys()[0]
    return minionData

def lambda_handler(event, context):
    region = 'us-east-1'
    if event.has_key('defined') or 'sweet' in event:
        print '...NEW...MINION here',event['defined']['sweet']
        #print event
        return {'message':'Hola from minion lambda %s'%(event['defined']['sweet']), 'id':event['defined']['sweet']}
    print '...main here'
    pload = {'defined':{'sweet':'abc123'}}
    pool = mp.Pool(12)
    results = pool.map(execLambda, (1,2,3,4,5,6,7,8,9,10,11,12))
    pool.close()
    pool.join()
    for result in results:
        rjson =json.loads(result)
        print rjson
    return results
    
