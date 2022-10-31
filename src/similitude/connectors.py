from google.cloud import bigquery
from src.similitude import models


source_prefixes = (
    "bq://",
    "psql://",
)

""" Singleton Client """
bq_client = bigquery.Client()


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

    def __init__(self, table_path: str):
        self.table_path = table_path
        self.schema = self._get_schema()

    def __repr__(self):
        return self.table_path

    def _get_schema(self):
        """
        Returns table schema as a list of pydantic Field models.
        """

        table = bq_client.get_table(self.table_path)
        schema = table.schema

        fields = [
            models.Field(
                name=field.name,
                field_type=field.field_type,
                is_nullable=field.is_nullable,
            )
            for field in schema
        ]

        return fields


