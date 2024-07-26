from googleapiclient.discovery import build


def trigger_df_job(cloud_event,environment):   
 
    service = build('dataflow', 'v1b3')
    project = "storied-program-429401-a3"

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
        "jobName": "euro2024_datadlow",  # Provide a unique name for the job
        "parameters": {
        "javascriptTextTransformGcsPath": "gs://euro_dataflow_metadata/udf.js",
        "JSONPath": "gs://euro_dataflow_metadata/bq.json",
        "javascriptTextTransformFunctionName": "transform",
        "outputTable": "storied-program-429401-a3:Euro2024_dataset.Topscorer_Euro2024",
        "inputFilePattern": "gs://player_ranking_data/Topscorer.csv",
        "bigQueryLoadingTemporaryDirectory": "gs://euro_dataflow_metadata",
        }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)