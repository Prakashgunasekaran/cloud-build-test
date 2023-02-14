#!/bin//bash

environment=$1
location=$2
ERROR_STR="Error"
output=$(gcloud composer environments run ${environment} --location ${location} dags list -- --subdir /home/airflow/gcs/data/test/)

if [[ "$output" =~ "$ERROR_STR".* ]]; then 

	gcloud composer environments run ${environment} --location ${location} dags list-import-errors -- --subdir /home/airflow/gcs/data/test/
	exit 1
fi
