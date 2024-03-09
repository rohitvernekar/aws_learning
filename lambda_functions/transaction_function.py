import json
import pandas as pd
import pymysql

rds_endpoint = ''
rds_username = ''
rds_password = ''
db_name = 'test'

print("connection started")
conn = pymysql.connect(host=rds_endpoint,
                       user=rds_username,
                       password=rds_password,
                       database=db_name)

cur = conn.cursor()

print("cursor created")


def lambda_handler(event, context):
    print("insert method called")
    result = get_data()
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }


def insert_data():
    sql = """insert into `LambdaTest` (name, email)
         values (%s, %s) 
    """
    cur.execute(sql, ('testinglamdafunc', 'testlambda@test.com'))
    conn.commit()


def get_data():
    sql = """select name, email from `LambdaTest`"""
    cur.execute(sql)
    res = cur.fetchone()
    return res
