from src.similitude.models import SchemaComparison


OKGREEN = "\033[92m"
FAIL = "\033[91m"
ENDC = "\033[0m"
CHECK = "\u2713"
CROSS = "\u2717"
INDENT_SIZE = 3


def print_fail(string: str, indent: bool = False) -> None:
    conditional_indent = "\t" if indent else ""
    print(f"{conditional_indent}{FAIL}{CROSS} {string}{ENDC}")


def print_ok(string: str, indent: bool = False) -> None:
    conditional_indent = "\t" if indent else ""
    print(f"{conditional_indent}{OKGREEN}{CHECK} {string}{ENDC}")


def print_list_fail(strings: list[str], indent: bool = False) -> None:
    for s in strings:
        print_fail(string=s, indent=indent)


def print_list_ok(strings: list[str], indent: bool = False) -> None:
    for s in strings:
        print_ok(string=s, indent=indent)


def schema_comparison(
    s: SchemaComparison, t1_id: str = "table_1", t2_id: str = "table_2"
):
    if len(s.table_1_unique) == 0 and len(s.table_2_unique) == 0:
        print_ok("Full schema match!")
        return

    if len(s.table_1_unique) > 0:
        print(f"Unique fields in {t1_id}:")
        print_list_fail(s.table_1_unique, indent=True)

    if len(s.table_2_unique) > 0:
        print(f"Unique fields in {t2_id}")
        print_list_fail(s.table_2_unique, indent=True)

    if len(s.intersection) > 0:
        print(f"Fields in both tables: ")
        print_list_ok(s.intersection, indent=True)
