# testcapital

Test project to invoke AWS ElastticSearch through API gateway and Lambda

## Build

To build the project

```./gradlew clean build shadowJar --refresh-dependencies```

## Loading the test data to Elastic search

The test data is provided in CSV format. 
Since elastic search requires the data to be in Json format execute testcapital.py located in src/main/scripts folder
The python script will parse the CSV file into json and create requests to send to AWS elastic search env

## API Gateway

Create a AWS lambda function and using testcapital-all.jar
Expose the lambda function using api gateway
Send the request as following url
http://<API_GATEWAY_URL>?sponsorName="xyz"&sponsorState="AK"&planName="abc"
