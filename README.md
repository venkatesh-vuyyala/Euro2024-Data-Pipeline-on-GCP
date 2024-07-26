# Euro2024-Data-Pipeline-on-GCP

## Introduction
In the world of data engineering, the journey from data retrieval to insightful visualization is an adventure filled with challenges and rewards. In this guide, we’ll walk through the intricate steps of constructing a comprehensive Euro 2024 statistics pipeline using Google Cloud services. From retrieving data via the Euro2024 API to crafting a dynamic Looker Studio dashboard, each phase contributes to the seamless flow of data for analysis and visualization.

## Architecture
![Architecture-2](https://github.com/user-attachments/assets/a9d83b93-9a7f-42f2-bbc3-a562c14235db)

## Data Retrieval with Python and Euro API
- Our project harnesses Python's capabilities to efficiently retrieve player statistics from the Euro 2024 API. By leveraging Python's robust libraries, we streamline data collection, ensuring accurate and timely access to essential statistics for effective analysis and reporting.

## Storing Data in Google Cloud Storage (GCS)

- Once the data is obtained, our next step involves preserving it securely in the cloud. We’ll explore how to store this data in a CSV format within Google Cloud Storage (GCS), ensuring accessibility and scalability for future processing.

## Creating a Cloud Function Trigger
- With our data safely stored, we proceed to set up a Cloud Function that acts as the catalyst for our pipeline. This function triggers upon file upload to the GCS bucket, serving as the initiator for our subsequent data processing steps.

## Execution of the Cloud Function
- Within the Cloud Function, intricate code is crafted to precisely trigger a Dataflow job. We’ll meticulously handle triggers and pass the requisite parameters to seamlessly initiate the Dataflow job, ensuring a smooth flow of data processing.

## Dataflow Job for BigQuery
- The core of our pipeline lies in the Dataflow job. Triggered by the Cloud Function, this job orchestrates the transfer of data from the CSV file in GCS to BigQuery. We’ll meticulously configure the job settings to ensure optimal performance and accurate data ingestion into BigQuery.
  
<img width="1189" alt="Data Flow" src="https://github.com/user-attachments/assets/5013c1b1-5475-450f-87cc-d480651e7ad0">

## Workflow Orchestration with Apache Airflow
We utilized Apache Airflow to streamline and manage our data workflows. Airflow's robust DAGs enable us to define, schedule, and monitor complex workflows, ensuring each step of our pipeline runs reliably and efficiently.

<img width="1189" alt="Data Flow" src="https://github.com/user-attachments/assets/c416b533-6e81-4d81-83c1-6b1339431bde">

## Looker Dashboard Creation

Finally, we’ll explore the potential of BigQuery as a data source for Looker Studio. Configuring Looker to connect with BigQuery, we’ll create a visually compelling dashboard. This dashboard will serve as the visualization hub, enabling insightful analysis based on the data loaded from our cricket statistics pipeline.

<img width="1205" alt="Screenshot 2024-07-25 at 4 58 29 PM" src="https://github.com/user-attachments/assets/1cd9ffd9-6c04-4610-906e-bbe21e9e8e4a">

