from src.similitude import models


def join_keys(keys: str) -> list[str]:
    """
    Parses join_key input string.
    Should be provided as comma separated strings.
    """
    no_space_keys = keys.replace(" ", "")
    return no_space_keys.split(",")


def bq_schema(bq_schema) -> list[models.Field]:
    fields = [
        models.Field(
            name=field.name,
            type=field.field_type,
            is_nullable=field.is_nullable,
        )
        for field in bq_schema
    ]

    return fields
