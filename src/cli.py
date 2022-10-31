from google.cloud import bigquery
from src.similitude import compare, connectors, format, spinner, parse

import click


@click.group(help="CLI tool for comparing tables.")
def cli():
    pass


@click.command()
@click.argument("table_1", type=str)
@click.argument("table_2", type=str)
def schema(table_1, table_2):
    with spinner.Spinner(msg="Fetching table schemas..."), bigquery.Client() as bq:
        schema_1 = bq.get_table(table_1).schema
        schema_2 = bq.get_table(table_2).schema
        schema_comparison = compare.schemas(
            parse.bq_schema(schema_1), parse.bq_schema(schema_2)
        )

    format.schema_comparison(schema_comparison, t1_id=table_1, t2_id=table_2)


@click.command()
@click.argument("table_1", type=str)
@click.argument("table_2", type=str)
@click.option(
    "--join-by",
    "-j",
    type=str,
    required=True,
    prompt="Enter field(s) to join by (separate with ',' if multiple)",
    help="Key for column-wise comparisons. If not provided only schema checks will be performed.",
)
def columns(table_1, table_2, join_by):
    """TODO:
    * Show what percentage was left out due to the index. Both from table_1 and table_2
    * Automatically find what columns are categorical and what are numerical.
    * Compare categorical columns with categorical. (Also include numerical columns with only 2 values since they are flags) Comparison is reasonably a % match.
    * Compare numerical columns, floats, ints, etc
    * LATER: allow for custom mappings of columns
    DELIMITATION:
    * For now we will assume that the schemas are matching between the tables compared.
    """
    join_keys = parse.join_keys(join_by)


cli.add_command(schema)
cli.add_command(columns)

"""
Mainly for debugging if you want to run the python script directly.
"""
if __name__ == "__main__":
    cli()
