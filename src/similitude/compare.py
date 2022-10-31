from src.similitude import models
import typing


def schemas(schema_1: list[models.Field], schema_2: list[models.Field]) -> dict:
    """
    Compares two schemas to see if all fields exists in both tables and are of the same type/constraints.
    """

    names_1 = set([field for field in schema_1])
    names_2 = set([field for field in schema_2])
    table_1_unique = names_1 - names_2
    table_2_unique = names_2 - names_1
    intersection = names_1 & names_2

    return models.SchemaComparison(
        table_1_unique=_field_set_to_sorted_list(table_1_unique),
        table_2_unique=_field_set_to_sorted_list(table_2_unique),
        intersection=_field_set_to_sorted_list(intersection),
    )


def _field_set_to_sorted_list(s):
    return sorted(list(s), key=lambda x: x.name)
