from google.cloud import bigquery

import click
import comparison
import connectors
import spinner


@click.command()
@click.argument("table_1", type=str)
@click.argument("table_2", type=str)
@click.option("--limit", "-l", type=int, default=-1, required=False, help="Limits the amount of rows evaluated")
@click.option("--key", "-k", type=str, multiple=True, required=False, help="Key for column-wise comparisons. If not provided only schema checks will be performed.")
def cli(table_1, table_2, limit, key):

    """ Singleton Client """
    bq_client = bigquery.Client()

    with spinner.Spinner(msg="Fetching table schemas..."):
        t1 = connectors.get_table(table_1, bq_client)
        t2 = connectors.get_table(table_2, bq_client)
        schema_comparison_res = comparison.schemas(t1, t2)
    schema_comparison_res()


"""
Mainly for debugging if you want to run the python script directly.
"""
if __name__ == "__main__":
    cli()
