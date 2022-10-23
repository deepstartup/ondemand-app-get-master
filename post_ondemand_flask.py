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
def paymentDetails():
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

@app.route("/service/serviceProvider",  methods = ['POST'])
def serviceProvider():
    json_text=request.get_json()
    service_provider_id=json_text['service_provider_id']
    service_provider_type=json_text['service_provider_type']
    service_provider_location_id=json_text['service_provider_location_id']
    service_provider_creation_date=json_text['service_provider_creation_date']
    service_provider_activation_flag=json_text['service_provider_activation_flag']
    service_id=json_text['service_id']
    service_provider_document_id=json_text['service_provider_document_id']
    service_charge=json_text['service_charge']
    params_all=config()
    main_conn=connect(params_all)
    postgres_insert_query = """ INSERT INTO kvx_db_prod.kvx_service_provider(service_provider_id, service_provider_type, service_provider_location_id, service_provider_creation_date, service_provider_activation_flag, service_id, service_provider_document_id, service_charge) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
    record_to_insert = (service_provider_id, service_provider_type, service_provider_location_id, service_provider_creation_date, service_provider_activation_flag, service_id, service_provider_document_id, service_charge)
    try:
        main_conn.do_insert(postgres_insert_query,record_to_insert)
    except Exception as e:
        data:dict={'Error in DB:':e}
        return json.dumps(data,indent=4, sort_keys=True, default=str), 200, {'ContentType':'application/json'}    
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

@app.route("/service/customerMaster",  methods = ['POST'])
def customerMaster(): 
    json_text=request.get_json()
    cust_id=json_text['cust_id']
    cust_first_name=json_text['cust_first_name']
    cust_last_name=json_text['cust_last_name']
    cust_gender=json_text['cust_gender']
    cust_dob=json_text['cust_dob']
    cust_primary_contact_type=json_text['cust_primary_contact_type']
    cust_primary_mobile_no=json_text['cust_primary_mobile_no']
    cust_secondary_mobile_no=json_text['cust_secondary_mobile_no']
    cust_primary_email_id=json_text['cust_primary_email_id']
    cust_secondary_email_id=json_text['cust_secondary_email_id']
    cust_location_type=json_text['cust_location_type']
    cust_location_lat=json_text['cust_location_lat']
    cust_location_long=json_text['cust_location_long']
    cust_location_street_add1=json_text['cust_location_street_add1']
    cust_location_street_add2=json_text['cust_location_street_add2']
    cust_location_city=json_text['cust_location_city']
    cust_location_state=json_text['cust_location_state']
    cust_location_country=json_text['cust_location_country']
    cust_location_zip_code=json_text['cust_location_zip_code']
    cust_activation_flag=json_text['cust_activation_flag']
    
    params_all=config()
    main_conn=connect(params_all)
    postgres_insert_query = """ INSERT INTO kvx_db_prod.kvx_customer_master (cust_id, cust_first_name, cust_last_name, cust_gender, cust_dob, cust_primary_contact_type, cust_primary_mobile_no, cust_secondary_mobile_no, cust_primary_email_id, cust_secondary_email_id, cust_location_type, cust_location_lat, cust_location_long, cust_location_street_add1, cust_location_street_add2, cust_location_city, cust_location_state, cust_location_country, cust_location_zip_code, cust_activation_flag) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    record_to_insert = (cust_id, cust_first_name, cust_last_name, cust_gender, cust_dob, cust_primary_contact_type, cust_primary_mobile_no, cust_secondary_mobile_no, cust_primary_email_id, cust_secondary_email_id, cust_location_type, cust_location_lat, cust_location_long, cust_location_street_add1, cust_location_street_add2, cust_location_city, cust_location_state, cust_location_country, cust_location_zip_code, cust_activation_flag)
    try:
        main_conn.do_insert(postgres_insert_query,record_to_insert)
    except Exception as e:
        data:dict={'Error in DB:':e}
        return json.dumps(data,indent=4, sort_keys=True, default=str), 200, {'ContentType':'application/json'}    
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

@app.route("/service/orderDetails",  methods = ['POST'])
def orderDetails(): 
    json_text=request.get_json()
    order_id=json_text['order_id']
    cust_id=json_text['cust_id']
    service_id=json_text['service_id']
    service_provider_id=json_text['service_provider_id']
    order_date=json_text['order_date']
    order_status=json_text['order_status']
    order_type=json_text['order_type']
    order_qty=json_text['order_qty']
    payment_id=json_text['payment_id']
    favourite_details=json_text['favourite_details']
    
    params_all=config()
    main_conn=connect(params_all)
    postgres_insert_query = """ INSERT INTO kvx_db_prod.kvx_order_details (order_id, cust_id, service_id, service_provider_id, order_date, order_status, order_type, order_qty, payment_id, favourite_details) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    record_to_insert = (order_id, cust_id, service_id, service_provider_id, order_date, order_status, order_type, order_qty, payment_id, favourite_details)
    try:
        main_conn.do_insert(postgres_insert_query,record_to_insert)
    except Exception as e:
        data:dict={'Error in DB:':e}
        return json.dumps(data,indent=4, sort_keys=True, default=str), 200, {'ContentType':'application/json'}    
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

@app.route("/service/customerReview",  methods = ['POST'])
def customerReview(): 
    json_text=request.get_json()
    order_id=json_text['order_id']
    rating=json_text['rating']
    reviewer_name=json_text['reviewer_name']
    reviewer_type=json_text['reviewer_type']
    review_timestamp=json_text['review_timestamp']
    review_comments=json_text['review_comments']
    
    params_all=config()
    main_conn=connect(params_all)
    postgres_insert_query = """ INSERT INTO kvx_db_prod.kvx_customer_review (order_id, rating, reviewer_name, reviewer_type, review_timestamp, review_comments) VALUES (%s,%s,%s,%s,%s,%s)"""
    record_to_insert = (order_id, rating, reviewer_name, reviewer_type, review_timestamp, review_comments)
    try:
        main_conn.do_insert(postgres_insert_query,record_to_insert)
    except Exception as e:
        data:dict={'Error in DB:':e}
        return json.dumps(data,indent=4, sort_keys=True, default=str), 200, {'ContentType':'application/json'}    
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

@app.route("/service/serviceProviderEnterprise",  methods = ['POST'])
def serviceProviderEnterprise(): 
    json_text=request.get_json()
    
    sp_enterprice_id=json_text['sp_enterprice_id']
    sp_enterprice_name=json_text['sp_enterprice_name']
    sp_enterprice_owner=json_text['sp_enterprice_owner']
    sp_service_provider_id=json_text['sp_service_provider_id']
    sp_primary_contact_type=json_text['sp_primary_contact_type']
    sp_primary_mobile_no=json_text['sp_primary_mobile_no']
    sp_secondary_mobile_no=json_text['sp_secondary_mobile_no']
    sp_primary_email_id=json_text['sp_primary_email_id']
    sp_secondary_email_id=json_text['sp_secondary_email_id']
    sp_id_type=json_text['sp_id_type']
    sp_id_number=json_text['sp_id_number']
    activation_flag=json_text['activation_flag']
    params_all=config()
    main_conn=connect(params_all)
    postgres_insert_query = """INSERT INTO kvx_db_prod.kvx_sp_enterprise (sp_enterprice_id, sp_enterprice_name, sp_enterprice_owner, sp_service_provider_id, sp_primary_contact_type, sp_primary_mobile_no, sp_secondary_mobile_no, sp_primary_email_id, sp_secondary_email_id, sp_id_type, sp_id_number, activation_flag) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    record_to_insert = (sp_enterprice_id, sp_enterprice_name, sp_enterprice_owner, sp_service_provider_id, sp_primary_contact_type, sp_primary_mobile_no, sp_secondary_mobile_no, sp_primary_email_id, sp_secondary_email_id, sp_id_type, sp_id_number, activation_flag)
    try:
        main_conn.do_insert(postgres_insert_query,record_to_insert)
    except Exception as e:
        data:dict={'Error in DB:':e}
        return json.dumps(data,indent=4, sort_keys=True, default=str), 200, {'ContentType':'application/json'}    
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

@app.route("/service/serviceProviderIndividual",  methods = ['POST'])
def serviceProviderIndividual(): 
    json_text=request.get_json()
    sp_individual_id=json_text['sp_individual_id']
    sp_enterprise_id=json_text['sp_enterprise_id']
    sp_service_provider_id=json_text['sp_service_provider_id']
    sp_first_name=json_text['sp_first_name']
    sp_last_name=json_text['sp_last_name']
    sp_gender=json_text['sp_gender']
    sp_dob=json_text['sp_dob']
    sp_primary_contact_type=json_text['sp_primary_contact_type']
    sp_primary_mobile_no=json_text['sp_primary_mobile_no']
    sp_secondary_mobile_no=json_text['sp_secondary_mobile_no']
    sp_primary_email_id=json_text['sp_primary_email_id']
    sp_secondary_email_id=json_text['sp_secondary_email_id']
    sp_primary_id_type=json_text['sp_primary_id_type']
    sp_primary_id_number=json_text['sp_primary_id_number']
    sp_secondary_id_type=json_text['sp_secondary_id_type']
    sp_secondary_id_number=json_text['sp_secondary_id_number']
    activation_flag=json_text['activation_flag']
    params_all=config()
    main_conn=connect(params_all)
    postgres_insert_query = """INSERT INTO kvx_db_prod.kvx_sp_individual (sp_individual_id, sp_enterprise_id, sp_service_provider_id, sp_first_name, sp_last_name, sp_gender, sp_dob, sp_primary_contact_type, sp_primary_mobile_no, sp_secondary_mobile_no, sp_primary_email_id, sp_secondary_email_id, sp_primary_id_type, sp_primary_id_number, sp_secondary_id_type, sp_secondary_id_number, activation_flag) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    record_to_insert = (sp_individual_id, sp_enterprise_id, sp_service_provider_id, sp_first_name, sp_last_name, sp_gender, sp_dob, sp_primary_contact_type, sp_primary_mobile_no, sp_secondary_mobile_no, sp_primary_email_id, sp_secondary_email_id, sp_primary_id_type, sp_primary_id_number, sp_secondary_id_type, sp_secondary_id_number, activation_flag)
    try:
        main_conn.do_insert(postgres_insert_query,record_to_insert)
    except Exception as e:
        data:dict={'Error in DB:':e}
        return json.dumps(data,indent=4, sort_keys=True, default=str), 200, {'ContentType':'application/json'}    
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

if __name__ == "__main__":
    app.run(debug=True, port=5000)
