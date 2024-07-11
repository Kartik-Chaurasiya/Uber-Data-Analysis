from mage_ai.settings.repo import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_big_query(data, **kwargs) -> None:
    """
    Template for exporting data to a BigQuery warehouse.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#bigquery
    """
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    # Define the table names in the order they appear in the transformer output
    table_names = ['datetime_dim', 'passenger_count_dim', 'trip_distance_dim', 
                   'rate_code_dim', 'pickup_location_dim', 'dropoff_location_dim', 
                   'payment_type_dim', 'fact_table']

    for table_name, df in zip(table_names, data):
        table_id = f'copy_id_of_table_created_in_BigQuery.{table_name}'
        BigQuery.with_config(ConfigFileLoader(config_path, config_profile)).export(
            DataFrame(df),
            table_id,
            if_exists='replace',  # Specify resolution policy if table name already exists
        )