from google.cloud import bigquery
from models import Column

source_prefixes = (
    "bq://",
    "psql://",
)


class Table:
    """
    Abstraction of a table object.

    Acts as an interface to table interaction.
    Should not have to be aware of the underlying table connection/implementation details.
    What underlying connector is used is determined by the table string prefix.
    E.g 'bq://' for bigquery tables, or psql:// for a postgres database.
    """

    def __init__(self, table_path):
        self.table_path = table_path

        """ Evaluate prefix validity """
        self._assert_table_prefix()

    def get_schema(self):
        pass

    def __repr__(self):
        return f"table:'{self.table_path}'"

    def _assert_table_prefix(self):
        try:
            assert self.table_path.startswith(source_prefixes)
        except AssertionError:
            raise AssertionError(
                "Invalid table prefix. Make sure your table is prefixed with any of the valid data sources. ({source_prefixes})"
            )


class BqTable(Table):
    def __init__(self, table_path):
        super().__init__(table_path)
        self.prefix_stripped_table_path = self.table_path.lstrip(
            "bq://"
        )  # might be worth removing prefix in Table class to not hardcode the strip.

    def get_schema(self):
        """
        Returns table schema as a list of pydantic Column models.
        """

        # Construct a BigQuery client object.
        client = bigquery.Client()

        table = client.get_table(self.prefix_stripped_table_path)
        schema = table.schema

        columns = [
            Column(
                name=column.name,
                column_type=column.field_type,
                is_nullable=column.is_nullable,
            )
            for column in schema
        ]

        return columns
