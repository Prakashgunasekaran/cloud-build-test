import subprocess
import sys

process=subprocess.run(["gcloud","composer","environments","run", "my-environment", "--location", "us-central1", "dags", "list", "--", "--subdir", "/home/airflow/gcs/data/test/"],stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

output=process.stdout

if "Error" in output:
	print("The following dags failed to parse\n")
	list_failed_dags=subprocess.run(["gcloud","composer","environments","run", "my-environment", "--location", "us-central1", "dags", "list-import-errors", "--", "--subdir", "/home/airflow/gcs/data/test/"],stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
	print(list_failed_dags.stdout)
	sys.exit(1)
else:
	print("No Dag parsing errors")