# Uber Data Engineering Project

This project demonstrates an end-to-end data engineering pipeline using Google Cloud Platform (GCP) services, Mage AI for ETL processes, and Looker Studio for data visualization. The pipeline processes and analyzes Uber trip data.

![Architecture Diagram](architecture.jpg)

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [ETL Process](#etl-process)
- [Data Visualization](#data-visualization)
- [Implementation Steps](#implementation-steps)

## Prerequisites
- Google Cloud Platform account
- Basic understanding of Python, SQL, and data engineering concepts

## Setup
1. Clone this repository:
   ```
   git clone https://github.com/your-username/uber-data-engineering-project.git
   cd uber-data-engineering-project
   ```

2. Set up your Google Cloud environment (detailed steps in the [Implementation Steps](#implementation-steps) section).


## ETL Process
1. **Extract**: Data is loaded from Google Cloud Storage using Mage AI's data loader.
2. **Transform**: Raw data is transformed into a star schema model using custom Python transformers in Mage AI.
3. **Load**: Processed data is loaded into Google BigQuery using Mage AI's data exporter.

For detailed code, refer to the following files:
- [Data Loader](mage files/uda_loader.py)
- [Transformer](mage files/uda_transformer.py)
- [Data Exporter](mage files/uda_export.py)

## Data Visualization
The processed data in BigQuery is visualized using Looker Studio. You can view the dashboard [here](https://lookerstudio.google.com/reporting/01481c8e-f8df-4310-936d-7e11163a4067).

## Implementation Steps

1. **Set up Google Cloud Platform**:
   - Create a new GCP project
   - Enable necessary APIs (Compute Engine, Cloud Storage, BigQuery)

2. **Prepare the data**:
   - Create a Cloud Storage bucket
   - Upload the Uber data CSV file to the bucket
   - Set appropriate access permissions

3. **Set up Compute Engine VM**:
   - Create a new VM instance
   - Configure HTTP and HTTPS access
   - Connect via SSH

4. **Install dependencies on VM**:
   ```bash
   sudo apt-get update -y
   sudo apt-get install python3-distutils python3-apt wget -y
   wget https://bootstrap.pypa.io/get-pip.py
   sudo python3 get-pip.py
   ```

5. **Set up Python environment and Mage AI**:
   ```bash
   python3 -m venv uber_env
   source uber_env/bin/activate
   pip install mage-ai
   ```

6. **Start Mage AI project**:
   ```bash
   mage start uber_data_analysis
   ```

7. **Configure VM firewall**:
   - Allow access to port 6789 for Mage AI web interface

8. **Implement ETL pipeline in Mage AI**:
   - Create a new pipeline
   - Implement data loader, transformer, and exporter steps
   - Test and run the pipeline

9. **Set up BigQuery**:
   - Create a new dataset
   - Configure service account and download JSON key

10. **Update Mage AI configuration**:
    - Edit `io_config.yaml` with BigQuery credentials

11. **Run the complete pipeline and verify data in BigQuery**

12. **Create Looker Studio dashboard**:
    - Connect to BigQuery dataset
    - Design and publish the dashboard
