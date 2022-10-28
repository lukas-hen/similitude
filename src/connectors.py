from google import cloud
import models


source_prefixes = (
    "bq://",
    "psql://",
)


def get_table(table_path: str) -> models.Table:
    """
    Fetches a table object.

    Finds the db specific implementation by prefix.
    """

    if not table_path.startswith(source_prefixes):
        raise ValueError(f"Invalid table prefix: `{table_path}`")
    elif table_path.startswith(source_prefixes[0]):
        table_without_prefix = table_path.lstrip(source_prefixes[0])
        return BqTable(table_without_prefix)


class BqTable(models.Table):

    def __init__(self, table_path):
        self.table_path = table_path

    def __repr__(self):
        return f"table:'{self.table_path}'"

    def get_schema(self):
        """
        Returns table schema as a list of pydantic Column models.
        """

        # Construct a BigQuery client object.
        client = cloud.bigquery.Client()

        table = client.get_table(self.table_path)
        schema = table.schema

        columns = [
            models.Column(
                name=column.name,
                column_type=column.field_type,
                is_nullable=column.is_nullable,
            )
            for column in schema
        ]

        return columns


