from google.cloud import bigquery

import models


source_prefixes = (
    "bq://",
    "psql://",
)

""" Singleton ish (not enforced) """
client = bigquery.Client()


def get_table(table_path: str) -> models.Table:
    """
    Fetches a table object.

    Finds the db specific implementation by prefix.
    """

    if not table_path.startswith(source_prefixes):
        raise ValueError(f"Invalid table prefix: `{table_path}`")
    elif table_path.startswith(source_prefixes[0]):
        table_without_prefix = table_path.lstrip(source_prefixes[0])
        return BqTable(table_without_prefix, client)


class BqTable(models.Table):

    def __init__(self, table_path: str, bq_client: bigquery.Client):
        self.table_path = table_path
        self._bq_client = bq_client
        self.schema = self._get_schema()

    def __repr__(self):
        return f"table:'{self.table_path}'"

    def _get_schema(self):
        """
        Returns table schema as a list of pydantic Column models.
        """

        table = self._bq_client.get_table(self.table_path)
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


