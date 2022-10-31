import models
import typing

OKGREEN = "\033[92m"
FAIL = "\033[91m"
ENDC = "\033[0m"
CHECK = "\u2713"
CROSS = "\u2717"
INDENT_SIZE = 3


def schemas(table_1: models.Table, table_2: models.Table) -> typing.Callable:
    """
    Compares two schemas to see if all fields exists in both tables and are of the same type/constraints.
    """

    names_1 = set([col for col in table_1.schema])
    names_2 = set([col for col in table_2.schema])
    table_1_unique = names_1 - names_2
    table_2_unique = names_2 - names_1
    intersection = names_1 & names_2

    def results():
        if len(table_1_unique) == 0 and len(table_2_unique) == 0:
            _print_ok("Full schema match!")
            return

        if len(table_1_unique) > 0:
            print(f"Unique columns in {table_1.table_path}:")
            for c in _set_to_sorted_list(table_1_unique):
                _print_fail(c, indent=True)

        if len(table_2_unique) > 0:
            print(f"Unique columns in {table_2.table_path}")
            for c in _set_to_sorted_list(table_2_unique):
                _print_fail(c, indent=True)

        if len(intersection) > 0:
            print(f"Columns in both tables: ")
            for c in _set_to_sorted_list(intersection):
                _print_ok(c, indent=True)

    return results


def _print_fail(string, indent=False):
    conditional_indent = "\t" if indent else ""
    print(f"{conditional_indent}{FAIL}{CROSS} {string}{ENDC}")


def _print_ok(string, indent=False):
    conditional_indent = "\t" if indent else ""
    print(f"{conditional_indent}{OKGREEN}{CHECK} {string}{ENDC}")


def _set_to_sorted_list(s):
    return sorted(list(s), key=lambda x: x.name)
