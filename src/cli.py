import click
from connectors import BqTable

"""
Need to group commands under cli to use as an entrypoint for setup.py.
"""

"""sandbox-334614.etl_raw.waifu_raw"""


@click.command()
@click.argument("table_1", type=click.STRING)
@click.argument("table_2", type=click.STRING)
def cli(table_1, table_2):
    a = BqTable(table_1)
    #b = BqTable(table_2)
    print(a.get_schema())


"""
Mainly for debugging if you want to run the python script directly.
"""
if __name__ == "__main__":
    cli()
