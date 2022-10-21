from flask import Flask
from flask import request
import json
from config import config
from postgre_conn_all import connect
import random, string
import psycopg2
from flask_cors import CORS, cross_origin


app = Flask(__name__)

cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'
app.config['CORS_ALLOW_ALL_ORIGINS'] = True
app.config['CORS_ORIGIN_WHITELIST'] = ('http://localhost:3000', 'http://localhost:3002','localhost:3002','http://127.0.0.1:3002')
@cross_origin()

@app.route("/service/create",  methods = ['POST'])
def createService():
    json_text=request.get_json()
    service_id=json_text['service_id']
    service_name=json_text['service_name']
    service_description=json_text['service_description']
    service_start_date=json_text['service_start_date']
    service_end_date=json_text['service_end_date']
    service_active_flag=json_text['service_active_flag']
    params_all=config()
    main_conn=connect(params_all)
    postgres_insert_query = """ INSERT INTO kvx_db_prod.kvx_services (service_id,service_name,service_description,service_start_date,service_end_date,service_active_flag) VALUES (%s,%s,%s,%s,%s,%s)"""
    record_to_insert = (service_id,service_name,service_description,service_start_date,service_end_date,service_active_flag)
    main_conn.do_insert(postgres_insert_query,record_to_insert)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

@app.route("/service/paymentDetails",  methods = ['POST'])
def createService():
    json_text=request.get_json()
    payment_id=json_text['payment_id']
    payment_type=json_text['payment_type']
    order_id=json_text['order_id']
    cust_id=json_text['cust_id']
    service_id=json_text['service_id']
    sp_id=json_text['sp_id']
    payment_auth_flag=json_text['payment_auth_flag']
    payment_date_time=json_text['payment_date_time']
    payment_gateway=json_text['payment_gateway']
    payment_version=json_text['payment_version']
    payment_ref_no=json_text['payment_ref_no']
    external_payment_ref_no=json_text['external_payment_ref_no']
    payment_amount=json_text['payment_amount']
    
    params_all=config()
    main_conn=connect(params_all)
    postgres_insert_query = """ INSERT INTO kvx_db_prod.kvx_cust_payment_details (payment_id, payment_type, order_id, cust_id, service_id, sp_id, payment_auth_flag, payment_date_time, payment_gateway, payment_version, payment_ref_no, external_payment_ref_no, payment_amount) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    record_to_insert = (payment_id, payment_type, order_id, cust_id, service_id, sp_id, payment_auth_flag, payment_date_time, payment_gateway, payment_version, payment_ref_no, external_payment_ref_no, payment_amount)
    try:
        main_conn.do_insert(postgres_insert_query,record_to_insert)
    except Exception as e:
        data:dict={'Error in DB:':e}
        return json.dumps(data,indent=4, sort_keys=True, default=str), 200, {'ContentType':'application/json'}    
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

if __name__ == "__main__":
    app.run(debug=True, port=5000)
