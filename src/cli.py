import click
import comparison
import connectors


@click.command()
@click.argument("table_1", type=click.STRING)
@click.argument("table_2", type=click.STRING)
def cli(table_1, table_2):
    t1 = connectors.get_table(table_1)
    t2 = connectors.get_table(table_2)
    comparison.schemas(t1, t2)


"""
Mainly for debugging if you want to run the python script directly.
"""
if __name__ == "__main__":
    cli()
