from pydantic import BaseModel


class Column(BaseModel):
    """
    Simple representation of a column.
    Centralized as model to unify across different databases.
    """

    name: str
    column_type: str  # Should be checked against central enum of types.
    is_nullable: bool

    def __eq__(self, other):
        if not isinstance(other, Column):
            # don't attempt to compare against unrelated types
            return NotImplemented

        name_equal = self.name == other.name
        type_equal = self.column_type == other.column_type
        contraints_equal = self.is_nullable == other.is_nullable
        return name_equal and type_equal and contraints_equal

    def __hash__(self):
        return hash(str(self.name))
