import csv
import json
import os
import requests
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import boto3
from aws_requests_auth.aws_auth import AWSRequestsAuth
import datetime
import pytz

host = 'search-testcapital-zekiodzquu4fawrsu7pi6z5hfy.us-west-1.es.amazonaws.com'
path = 'testcapital'
region = 'us-west-1'

service = 'es'
session = boto3.session.Session()
credentials = session.get_credentials().get_frozen_credentials()
print(credentials.token)
print(credentials.access_key)
print(credentials.secret_key)
print(session.region_name)
# awsauth = AWS4Auth(credentials.access_key, 
# credentials.secret_key,  
# region, 
# service,
# session_token=credentials.token)
awsauth = AWSRequestsAuth(
    aws_access_key=credentials.access_key,
    aws_secret_access_key=credentials.secret_key,
    aws_token=credentials.token,
    aws_host=host,
    aws_region=session.region_name,
    aws_service=service
)
es = Elasticsearch(
    hosts=[{'host': host, 'port': 443}],
    http_auth = awsauth,
    use_ssl = True,
    verify_certs = True,
    connection_class = RequestsHttpConnection
)

count = 1
csvfile = open('/Users/rs186125/Downloads/F_5500_2017_Latest/f_5500_2017_latest.csv', 'r')
url = 'https://search-testcapital-zekiodzquu4fawrsu7pi6z5hfy.us-west-1.es.amazonaws.com/testcapital/_doc/'

fieldnames = ("ACK_ID","FORM_PLAN_YEAR_BEGIN_DATE","FORM_TAX_PRD","TYPE_PLAN_ENTITY_CD","TYPE_DFE_PLAN_ENTITY_CD","INITIAL_FILING_IND","AMENDED_IND","FINAL_FILING_IND","SHORT_PLAN_YR_IND","COLLECTIVE_BARGAIN_IND","F5558_APPLICATION_FILED_IND","EXT_AUTOMATIC_IND","DFVC_PROGRAM_IND","EXT_SPECIAL_IND","EXT_SPECIAL_TEXT","PLAN_NAME","SPONS_DFE_PN","PLAN_EFF_DATE","SPONSOR_DFE_NAME","SPONS_DFE_DBA_NAME","SPONS_DFE_CARE_OF_NAME","SPONS_DFE_MAIL_US_ADDRESS1","SPONS_DFE_MAIL_US_ADDRESS2","SPONS_DFE_MAIL_US_CITY","SPONS_DFE_MAIL_US_STATE","SPONS_DFE_MAIL_US_ZIP","SPONS_DFE_MAIL_FOREIGN_ADDR1","SPONS_DFE_MAIL_FOREIGN_ADDR2","SPONS_DFE_MAIL_FOREIGN_CITY","SPONS_DFE_MAIL_FORGN_PROV_ST","SPONS_DFE_MAIL_FOREIGN_CNTRY","SPONS_DFE_MAIL_FORGN_POSTAL_CD","SPONS_DFE_LOC_US_ADDRESS1","SPONS_DFE_LOC_US_ADDRESS2","SPONS_DFE_LOC_US_CITY","SPONS_DFE_LOC_US_STATE","SPONS_DFE_LOC_US_ZIP","SPONS_DFE_LOC_FOREIGN_ADDRESS1","SPONS_DFE_LOC_FOREIGN_ADDRESS2","SPONS_DFE_LOC_FOREIGN_CITY","SPONS_DFE_LOC_FORGN_PROV_ST","SPONS_DFE_LOC_FOREIGN_CNTRY","SPONS_DFE_LOC_FORGN_POSTAL_CD","SPONS_DFE_EIN","SPONS_DFE_PHONE_NUM","BUSINESS_CODE","ADMIN_NAME","ADMIN_CARE_OF_NAME","ADMIN_US_ADDRESS1","ADMIN_US_ADDRESS2","ADMIN_US_CITY","ADMIN_US_STATE","ADMIN_US_ZIP","ADMIN_FOREIGN_ADDRESS1","ADMIN_FOREIGN_ADDRESS2","ADMIN_FOREIGN_CITY","ADMIN_FOREIGN_PROV_STATE","ADMIN_FOREIGN_CNTRY","ADMIN_FOREIGN_POSTAL_CD","ADMIN_EIN","ADMIN_PHONE_NUM","LAST_RPT_SPONS_NAME","LAST_RPT_SPONS_EIN","LAST_RPT_PLAN_NUM","ADMIN_SIGNED_DATE","ADMIN_SIGNED_NAME","SPONS_SIGNED_DATE","SPONS_SIGNED_NAME","DFE_SIGNED_DATE","DFE_SIGNED_NAME","TOT_PARTCP_BOY_CNT","TOT_ACTIVE_PARTCP_CNT","RTD_SEP_PARTCP_RCVG_CNT","RTD_SEP_PARTCP_FUT_CNT","SUBTL_ACT_RTD_SEP_CNT","BENEF_RCVG_BNFT_CNT","TOT_ACT_RTD_SEP_BENEF_CNT","PARTCP_ACCOUNT_BAL_CNT","SEP_PARTCP_PARTL_VSTD_CNT","CONTRIB_EMPLRS_CNT","TYPE_PENSION_BNFT_CODE","TYPE_WELFARE_BNFT_CODE","FUNDING_INSURANCE_IND","FUNDING_SEC412_IND","FUNDING_TRUST_IND","FUNDING_GEN_ASSET_IND","BENEFIT_INSURANCE_IND","BENEFIT_SEC412_IND","BENEFIT_TRUST_IND","BENEFIT_GEN_ASSET_IND","SCH_R_ATTACHED_IND","SCH_MB_ATTACHED_IND","SCH_SB_ATTACHED_IND","SCH_H_ATTACHED_IND","SCH_I_ATTACHED_IND","SCH_A_ATTACHED_IND","NUM_SCH_A_ATTACHED_CNT","SCH_C_ATTACHED_IND","SCH_D_ATTACHED_IND","SCH_G_ATTACHED_IND","FILING_STATUS","DATE_RECEIVED","VALID_ADMIN_SIGNATURE","VALID_DFE_SIGNATURE","VALID_SPONSOR_SIGNATURE","ADMIN_PHONE_NUM_FOREIGN","SPONS_DFE_PHONE_NUM_FOREIGN","ADMIN_NAME_SAME_SPON_IND","ADMIN_ADDRESS_SAME_SPON_IND","PREPARER_NAME","PREPARER_FIRM_NAME","PREPARER_US_ADDRESS1","PREPARER_US_ADDRESS2","PREPARER_US_CITY","PREPARER_US_STATE","PREPARER_US_ZIP","PREPARER_FOREIGN_ADDRESS1","PREPARER_FOREIGN_ADDRESS2","PREPARER_FOREIGN_CITY","PREPARER_FOREIGN_PROV_STATE","PREPARER_FOREIGN_CNTRY","PREPARER_FOREIGN_POSTAL_CD","PREPARER_PHONE_NUM","PREPARER_PHONE_NUM_FOREIGN","TOT_ACT_PARTCP_BOY_CNT","SUBJ_M1_FILING_REQ_IND","COMPLIANCE_M1_FILING_REQ_IND","M1_RECEIPT_CONFIRMATION_CODE","ADMIN_MANUAL_SIGNED_DATE","ADMIN_MANUAL_SIGNED_NAME","LAST_RPT_PLAN_NAME","SPONS_MANUAL_SIGNED_DATE","SPONS_MANUAL_SIGNED_NAME","DFE_MANUAL_SIGNED_DATE","DFE_MANUAL_SIGNED_NAME")
csvfile.next()
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    adminsigneddate = row["ADMIN_SIGNED_DATE"]
    print(adminsigneddate)
    if not row["ADMIN_SIGNED_DATE"]:
        utc_now = pytz.utc.localize(datetime.datetime.utcnow())
        row["ADMIN_SIGNED_DATE"] = utc_now.isoformat()
        print(row["ADMIN_SIGNED_DATE"])
    if not row['PLAN_EFF_DATE']:
        utc_now = pytz.utc.localize(datetime.datetime.utcnow())
        row["PLAN_EFF_DATE"] = utc_now.isoformat()
    data = json.dumps(row)
    requesturl = url + str(count)
    print('url is ' + requesturl)
    es.index(index="testcapital", doc_type="_doc", id=count, body=data)

        # with open('/Users/rs186125/Downloads/F_5500_2017_Latest/f_5500_2017_latest' + str(count) + '.json') as json_file:
        #     data = json.load(json_file)
        #     response = requests.post(url, data)
        # filename = '/Users/rs186125/Downloads/F_5500_2017_Latest/f_5500_2017_latest' + str(count) + '.json'
        # a = open(filename)
        # data = json.load(a)
        # print(data)
        # print('indexing data... ' + str(count))
        # requesturl = url + str(count)
        # print('url is ' + requesturl)
        # response = requests.put(requesturl, auth=awsauth, json=data)
        # if response.status_code == 200:
        #     print('indexed data... ' + str(count))        
    count = count + 1