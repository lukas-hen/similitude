import click
from connectors import BqTable
from comparison_engine import compare_schemas


@click.command()
@click.argument("table_1", type=click.STRING)
@click.argument("table_2", type=click.STRING)
def cli(table_1, table_2):
    compare_schemas(BqTable(table_1), BqTable(table_2))


"""
Mainly for debugging if you want to run the python script directly.
"""
if __name__ == "__main__":
    cli()
