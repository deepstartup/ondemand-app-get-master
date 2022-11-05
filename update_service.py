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

@app.route("/service/updateService",  methods = ['POST'])
def updateService():
    json_text=request.get_json()
    service_id=json_text['service_id']
    service_name=json_text['service_name']
    service_description=json_text['service_description']
    service_start_date=json_text['service_start_date']
    service_end_date=json_text['service_end_date']
    service_active_flag=json_text['service_active_flag']
    params_all=config()
    updated_rows = 0
    conn = psycopg2.connect(**params_all)
    cur = conn.cursor()
    postgres_update_query = """ UPDATE kvx_db_prod.kvx_services set service_name=%s,service_description=%s,service_start_date=%s,service_end_date=%s,service_active_flag=%s where service_id=%s"""
    record_to_update = (service_name,service_description,service_start_date,service_end_date,service_active_flag,service_id)
    cur.execute(postgres_update_query,record_to_update)
    updated_rows = cur.rowcount
    conn.commit()
    cur.close()
    return json.dumps({'success':True,'No_Rows_Updated':updated_rows}), 200, {'ContentType':'application/json'}
@app.route("/service/updateserviceProvider",  methods = ['POST'])
def updateserviceProvider():
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
    updated_rows = 0
    conn = psycopg2.connect(**params_all)
    cur = conn.cursor()
    postgres_update_query = """ UPDATE kvx_db_prod.kvx_service_provider set service_provider_type=%s,service_provider_location_id=%s,service_provider_creation_date=%s,service_provider_activation_flag=%s,service_id=%s,service_provider_document_id=%s,service_charge=%s where service_provider_id=%s"""
    record_to_update = (service_provider_type,service_provider_location_id,service_provider_creation_date,service_provider_activation_flag,service_id,service_provider_document_id,service_charge,service_provider_id)
    cur.execute(postgres_update_query,record_to_update)
    updated_rows = cur.rowcount
    conn.commit()
    cur.close()
    return json.dumps({'success':True,'No_Rows_Updated':updated_rows}), 200, {'ContentType':'application/json'}

@app.route("/service/updatecustomerMaster",  methods = ['POST'])
def updatecustomerMaster():
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
    updated_rows = 0
    conn = psycopg2.connect(**params_all)
    cur = conn.cursor()
    postgres_update_query = """ UPDATE kvx_db_prod.kvx_customer_master  set cust_first_name=%s, cust_last_name=%s, cust_gender=%s, cust_dob=%s, cust_primary_contact_type=%s, cust_primary_mobile_no=%s, cust_secondary_mobile_no=%s, cust_primary_email_id=%s, cust_secondary_email_id=%s, cust_location_type=%s, cust_location_lat=%s, cust_location_long=%s, cust_location_street_add1=%s, cust_location_street_add2=%s, cust_location_city=%s, cust_location_state=%s, cust_location_country=%s, cust_location_zip_code=%s,cust_activation_flag=%s where cust_id=%s"""
    record_to_update = (cust_first_name, cust_last_name, cust_gender, cust_dob, cust_primary_contact_type, cust_primary_mobile_no, cust_secondary_mobile_no, cust_primary_email_id, cust_secondary_email_id, cust_location_type, cust_location_lat, cust_location_long, cust_location_street_add1, cust_location_street_add2, cust_location_city, cust_location_state, cust_location_country, cust_location_zip_code, cust_activation_flag,cust_id)
    cur.execute(postgres_update_query,record_to_update)
    updated_rows = cur.rowcount
    conn.commit()
    cur.close()
    return json.dumps({'success':True,'No_Rows_Updated':updated_rows}), 200, {'ContentType':'application/json'}
@app.route("/service/updateserviceProviderEnterprise",  methods = ['POST'])
def updateserviceProviderEnterprise(): 
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
    updated_rows = 0
    conn = psycopg2.connect(**params_all)
    cur = conn.cursor()
    postgres_update_query = """UPDATE kvx_db_prod.kvx_sp_enterprise   set sp_enterprice_name=%s, sp_enterprice_owner=%s, sp_service_provider_id=%s, sp_primary_contact_type=%s, sp_primary_mobile_no=%s, sp_secondary_mobile_no=%s, sp_primary_email_id=%s, sp_secondary_email_id=%s, sp_id_type=%s, sp_id_number=%s, activation_flag=%s where sp_enterprice_id=%s"""
    record_to_update =(sp_enterprice_name, sp_enterprice_owner, sp_service_provider_id, sp_primary_contact_type, sp_primary_mobile_no, sp_secondary_mobile_no, sp_primary_email_id, sp_secondary_email_id, sp_id_type, sp_id_number, activation_flag,sp_enterprice_id)
    updated_rows = cur.rowcount
    conn.commit()
    cur.close()
    return json.dumps({'success':True,'No_Rows_Updated':updated_rows}), 200, {'ContentType':'application/json'}

@app.route("/service/updateserviceProviderIndividual",  methods = ['POST'])
def updateserviceProviderIndividual(): 
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
    updated_rows = 0
    conn = psycopg2.connect(**params_all)
    cur = conn.cursor()
    postgres_update_query = """UPDATE kvx_db_prod.kvx_sp_individual set sp_enterprise_id=%s, sp_service_provider_id=%s, sp_first_name=%s, sp_last_name=%s, sp_gender=%s, sp_dob=%s, sp_primary_contact_type=%s, sp_primary_mobile_no=%s, sp_secondary_mobile_no=%s, sp_primary_email_id=%s, sp_secondary_email_id=%s, sp_primary_id_type=%s, sp_primary_id_number=%s, sp_secondary_id_type=%s, sp_secondary_id_number=%s, activation_flag=%s where sp_individual_id=%s"""
    record_to_update =(sp_enterprise_id, sp_service_provider_id, sp_first_name, sp_last_name, sp_gender, sp_dob, sp_primary_contact_type, sp_primary_mobile_no, sp_secondary_mobile_no, sp_primary_email_id, sp_secondary_email_id, sp_primary_id_type, sp_primary_id_number, sp_secondary_id_type, sp_secondary_id_number, activation_flag,sp_individual_id)
    updated_rows = cur.rowcount
    conn.commit()
    cur.close()
    return json.dumps({'success':True,'No_Rows_Updated':updated_rows}), 200, {'ContentType':'application/json'}
@app.route("/service/updateserviceProviderLocation",  methods = ['POST'])
def updateserviceProviderLocation(): 
    json_text=request.get_json()
    sp_location_id=json_text['sp_location_id']
    service_provider_id=json_text['service_provider_id']
    sp_location_type=json_text['sp_location_type']
    sp_location_lat=json_text['sp_location_lat']
    sp_location_long=json_text['sp_location_long']
    sp_location_street_add1=json_text['sp_location_street_add1']
    sp_location_street_add2=json_text['sp_location_street_add2']
    sp_location_city=json_text['sp_location_city']
    sp_location_state=json_text['sp_location_state']
    sp_location_country=json_text['sp_location_country']
    sp_location_zip_code=json_text['sp_location_zip_code']
    sp_location_creation_date=json_text['sp_location_creation_date']
    sp_location_indicator=json_text['sp_location_indicator']
    params_all=config()
    updated_rows = 0
    conn = psycopg2.connect(**params_all)
    cur = conn.cursor()
    postgres_update_query = """UPDATE kvx_db_prod.kvx_sp_location set service_provider_id=%s, sp_location_type=%s, sp_location_lat=%s, sp_location_long=%s, sp_location_street_add1=%s, sp_location_street_add2=%s, sp_location_city=%s, sp_location_state=%s, sp_location_country=%s, sp_location_zip_code=%s, sp_location_creation_date=%s, sp_location_indicator=%s where sp_location_id=%s"""
    record_to_update =(service_provider_id, sp_location_type, sp_location_lat, sp_location_long, sp_location_street_add1, sp_location_street_add2, sp_location_city, sp_location_state, sp_location_country, sp_location_zip_code, sp_location_creation_date, sp_location_indicator,sp_location_id)
    updated_rows = cur.rowcount
    conn.commit()
    cur.close()
    return json.dumps({'success':True,'No_Rows_Updated':updated_rows}), 200, {'ContentType':'application/json'}
if __name__ == "__main__":
    app.run(debug=True, port=6001)
